from typing import Optional, List, Dict, Union, Tuple

import numpy as np
import pandas as pd
import scipy.stats
from matplotlib import pyplot as plt

from .assets import AssetList
from .common.helpers import Frame, Rebalance, Float, Date
from .common.validators import validate_integer, validate_real
from .settings import PeriodLength, _MONTHS_PER_YEAR


class Portfolio:
    """
    Implementation of investment portfolio.
    Arguments are similar to AssetList (weights are added), but different behavior.
    Works with monthly end of day historical rate of return data.
    """
    # TODO: rebalance_period should be an attribute
    # TODO: add withdrawals as an attribute: frequency (monthly/annual), amount (nominal, percentage), inflation_adjusted

    def __init__(
        self,
        symbols: Optional[List[str]] = None,
        *,
        first_date: Optional[str] = None,
        last_date: Optional[str] = None,
        ccy: str = "USD",
        inflation: bool = True,
        weights: Optional[List[float]] = None,
    ):
        self._list: AssetList = AssetList(
            symbols=symbols,
            first_date=first_date,
            last_date=last_date,
            ccy=ccy,
            inflation=inflation,
        )
        self.currency = self._list.currency.name
        self._ror = self._list.ror
        self.symbols = self._list.symbols
        self.tickers = [x.split(".", 1)[0] for x in self.symbols]
        self.names = self._list.names
        self._weights = None
        self.weights = weights
        self.assets_weights = dict(zip(self.symbols, self.weights))
        self.assets_first_dates = self._list.assets_first_dates
        self.assets_last_dates = self._list.assets_last_dates
        self.first_date = self._list.first_date
        self.last_date = self._list.last_date
        self.period_length = self._list.period_length
        self.pl = PeriodLength(
            self.get_returns_ts().shape[0] // _MONTHS_PER_YEAR,
            self.get_returns_ts().shape[0] % _MONTHS_PER_YEAR,
        )
        self._pl_txt = f"{self.pl.years} years, {self.pl.months} months"
        if inflation:
            self.inflation = self._list.inflation
            self.inflation_ts: pd.Series = self._list.inflation_ts

    def __repr__(self):
        dic = {
            "symbols": self.symbols,
            "weights": self.weights,
            "currency": self.currency,
            "first date": self.first_date.strftime("%Y-%m"),
            "last_date": self.last_date.strftime("%Y-%m"),
            "period length": self._pl_txt,
        }
        return repr(pd.Series(dic))

    def __len__(self):
        return len(self.symbols)

    def _add_inflation(self):
        if hasattr(self, "inflation"):
            return pd.concat(
                [self.get_returns_ts(), self.inflation_ts], axis=1, join="inner", copy="false"
            )
        else:
            return self.get_returns_ts()

    def _validate_period(self, period):
        validate_integer("period", period, min_value=0, inclusive=False)
        if period > self.pl.years:
            raise ValueError(
                f"'period' ({period}) is beyond historical data range ({self.period_length})."
            )

    @property
    def weights(self) -> Union[list, tuple]:
        """
        Get or set assets weights in portfolio.

        If not defined equal weights are used for each asset.

        Weights must be a list (or tuple) of float values.

        Returns
        -------
            Values for the weights of assets in portfolio.

        Examples
        --------
        >>> x = ok.Portfolio(['SPY.US', 'BND.US'])
        >>> x.weights
        [0.5, 0.5]
        """
        return self._weights

    @weights.setter
    def weights(self, weights: Optional[List[float]]):
        if weights is None:
            # Equally weighted portfolio
            n = len(self.symbols)  # number of assets
            weights = list(np.repeat(1 / n, n))
        else:
            [validate_real("weight", weight) for weight in weights]
            Frame.weights_sum_is_one(weights)
            if len(weights) != len(self.symbols):
                raise ValueError(
                    f"Number of tickers ({len(self.symbols)}) should be equal "
                    f"to the weights number ({len(weights)})"
                )
        self._weights = weights

    def get_returns_ts(self, rebalancing_period: str = "month") -> pd.Series:
        """
        Calculate rate of return time series for portfolio given a rebalancing period.

        The rebalancing is the action of bringing the portfolio that has deviated away
        from original target asset allocation back into line. After rebalancing the portfolio assets
        have weights set with Portfolio(weights=[...]).
        Different rebalancing periods are allowed for portfolio: 'month' (default), 'year' or 'none'.

        Parameters
        ----------
        rebalancing_period : {"month", "year", "none"}, default "month"
            Portfolio rebalancing periods. 'none' is for not rebalanced portfolio.

        Returns
        -------
            Monthly rate of return time series for portfolio.
        """
        if rebalancing_period == 'month':
            s = Frame.get_portfolio_return_ts(self.weights, self._ror)
            s.rename("portfolio", inplace=True)
        elif rebalancing_period in ['year', 'none']:
            s = Rebalance.rebalanced_portfolio_return_ts(
                self.weights, self._ror, period=rebalancing_period
            )
        else:
            raise ValueError('rebalancing_period must be "year", "month" or None')
        return s

    @property
    def wealth_index(self) -> pd.DataFrame:
        """
        Calculate wealth index time series for the portfolio and accumulated inflation.

        Wealth index (Cumulative Wealth Index) is a time series that presents the value of portfolio over
        historical time period. Accumulated inflation time series is added if `inflation=True` in the Portfolio.

        Wealth index is obtained from the accumulated return multiplicated by the initial investments.
        That is: 1000 * (Acc_Return + 1)
        Initial investments are taken as 1000 units of the Portfolio base currency.

        Returns
        -------
            Time series of wealth index values for portfolio and accumulated inflation.

        Examples
        --------
        >>> x = ok.Portfolio(['SPY.US', 'BND.US'])
        >>> x.wealth_index
                    portfolio     USD.INFL
        2007-05  1000.000000  1000.000000
        2007-06  1004.034950  1008.011590
        2007-07   992.940364  1007.709187
        2007-08  1006.642941  1005.895310
                      ...          ...
        2020-12  2561.882476  1260.242835
        2021-01  2537.800781  1265.661880
        2021-02  2553.408256  1272.623020
        2021-03  2595.156481  1281.658643
        [167 rows x 2 columns]
        """
        df = self._add_inflation()
        df = Frame.get_wealth_indexes(df)
        if isinstance(df, pd.Series):  # should always return a DataFrame
            df = df.to_frame()
            df.rename({1: "portfolio"}, axis="columns", inplace=True)
        return df

    @property
    def wealth_index_with_assets(self) -> pd.DataFrame:
        """
        Calculate wealth index time series for the portfolio, all assets and accumulated inflation.

        Wealth index (Cumulative Wealth Index) is a time series that presents the value of portfolio over
        historical time period. Accumulated inflation time series is added if `inflation=True` in the Portfolio.

        Wealth index is obtained from the accumulated return multiplicated by the initial investments.
        That is: 1000 * (Acc_Return + 1)
        Initial investments are taken as 1000 units of the Portfolio base currency.

        Returns
        -------
        DataFrame
            Time series of wealth index values for portfolio, each asset and accumulated inflation.

        Examples
        --------
        >>> pf = ok.Portfolio(['VOO.US', 'GLD.US'], weights=[0.8, 0.2])
        >>> pf.wealth_index_with_assets
                   portfolio       VOO.US       GLD.US     USD.INFL
        2010-10  1000.000000  1000.000000  1000.000000  1000.000000
        2010-11  1041.065584  1036.658420  1058.676480  1001.600480
        2010-12  1103.779375  1108.395183  1084.508186  1003.303201
        2011-01  1109.298272  1133.001556  1015.316564  1008.119056
                      ...          ...          ...          ...
        2020-12  3381.729677  4043.276231  1394.513920  1192.576493
        2021-01  3332.356424  4002.034813  1349.610572  1197.704572
        2021-02  3364.480340  4112.891178  1265.124950  1204.291947
        2021-03  3480.083884  4301.261594  1250.702526  1212.842420
        """
        if hasattr(self, "inflation"):
            df = pd.concat(
                [self.get_returns_ts(), self._ror, self.inflation_ts],
                axis=1,
                join="inner",
                copy="false",
            )
        else:
            df = pd.concat(
                [self.get_returns_ts(), self._ror], axis=1, join="inner", copy="false"
            )
        return Frame.get_wealth_indexes(df)

    @property
    def mean_return_monthly(self) -> float:
        return Frame.get_portfolio_mean_return(self.weights, self._ror)

    @property
    def mean_return_annual(self) -> float:
        return Float.annualize_return(self.mean_return_monthly)

    def get_cagr(self, period: Optional[int] = None, real: bool = False) -> pd.Series:
        """
        Calculate Compound Annual Growth Rate (CAGR) for a given period.
        """
        df = self._add_inflation()
        dt0 = self.last_date
        if period is None:
            dt = self.first_date
        else:
            self._validate_period(period)
            dt = Date.subtract_years(dt0, period)
        cagr = Frame.get_cagr(df[dt:])
        if real:
            if not hasattr(self, "inflation"):
                raise Exception(
                    "Real CAGR is not defined. Set inflation=True in Portfolio to calculate it."
                )
            mean_inflation = Frame.get_cagr(self.inflation_ts[dt:])
            cagr = (1. + cagr) / (1. + mean_inflation) - 1.
            cagr.drop(self.inflation, inplace=True)
        return cagr

    def get_cumulative_return(self, period: Union[str, int, None] = None, real: bool = False) -> pd.Series:
        """
        Calculate cumulative return of return for MONTHLY rebalanced portfolio.

        Parameters
        ----------
        period: str, int or None, default None
            Trailing period in years.
            None - full time cumulative return.
            'YTD' - (Year To Date) period of time beginning the first day of the calendar year up to the last month.
        real: bool, default False
            Cumulative return is adjusted for inflation (real cumulative return) if True.
            Portfolio should be initiated with `Inflation=True` for real cumulative return.

        Returns
        -------
        Series

        Examples
        --------
        >>> x = ok.Portfolio(['BTC-USD.CC', 'LTC-USD.CC'], weights=[.8, .2], last_date='2021-03')
        >>> x.get_cumulative_return(period=2)
        portfolio    8.589341
        USD.INFL     0.040569
        dtype: float64

        To get inflation adjusted return (real annualized return) add `real=True` option:
        >>> x.get_cumulative_return(period=2, real=True)
        portfolio    8.215476
        dtype: float64
        """
        df = self._add_inflation()
        dt0 = self.last_date

        if period is None:
            dt = self.first_date
        elif str(period).lower() == "ytd":
            year = dt0.year
            dt = str(year)
        else:
            self._validate_period(period)
            dt = Date.subtract_years(dt0, period)

        cr = Frame.get_cumulative_return(df[dt:])
        if real:
            if not hasattr(self, "inflation"):
                raise Exception(
                    "Real cumulative return is not defined (no inflation information is available)."
                    "Set inflation=True in Portfolio to calculate it."
                )
            cumulative_inflation = Frame.get_cumulative_return(self.inflation_ts[dt:])
            cr = (1. + cr) / (1. + cumulative_inflation) - 1.
            cr.drop(self.inflation, inplace=True)
        return cr

    def get_rolling_cumulative_return(self, window: int = 12) -> pd.DataFrame:
        """
        Calculate rolling cumulative return.

        Parameters
        ----------
        window : int, default 12
            Window size in months.

        Returns
        -------
            DataFrame
            Time series of rolling cumulative return.
        """
        return Frame.get_rolling_fn(
            self.get_returns_ts(),
            window=window,
            fn=Frame.get_cumulative_return,
            window_below_year=True,
        )

    @property
    def annual_return_ts(self) -> pd.DataFrame:
        return Frame.get_annual_return_ts_from_monthly(self.get_returns_ts())

    @property
    def dividend_yield(self) -> pd.DataFrame:
        """
        Calculates dividend yield time series in all base currencies of portfolio assets.
        For every currency dividend yield is a weighted sum of the assets dividend yields.
        Portfolio asset allocation (weights) is a constant (monthly rebalanced portfolios).
        TODO: calculate for not rebalance portfolios (and arbitrary reb period).
        """
        div_yield_assets = self._list.dividend_yield
        currencies_dict = self._list.currencies
        if "asset list" in currencies_dict:
            del currencies_dict["asset list"]
        currencies_list = list(set(currencies_dict.values()))
        div_yield_df = pd.DataFrame(dtype=float)
        for currency in currencies_list:
            assets_with_the_same_currency = [
                x for x in currencies_dict if currencies_dict[x] == currency
            ]
            df = div_yield_assets[assets_with_the_same_currency]
            # for monthly rebalanced portfolio
            weights = [
                self.assets_weights[k]
                for k in self.assets_weights
                if k in assets_with_the_same_currency
            ]
            weighted_weights = np.asarray(weights) / np.asarray(weights).sum()
            div_yield_series = Frame.get_portfolio_return_ts(weighted_weights, df)
            div_yield_series.rename(currency, inplace=True)
            div_yield_df = pd.concat([div_yield_df, div_yield_series], axis=1)
        return div_yield_df

    @property
    def real_mean_return(self) -> float:
        if not hasattr(self, "inflation"):
            raise Exception(
                "Real Return is not defined. Set inflation=True to calculate."
            )
        infl_mean = Float.annualize_return(self.inflation_ts.mean())
        ror_mean = Float.annualize_return(self.get_returns_ts().mean())
        return (1.0 + ror_mean) / (1.0 + infl_mean) - 1.0

    @property
    def risk_monthly(self) -> float:
        return Frame.get_portfolio_risk(self.weights, self._ror)

    @property
    def risk_annual(self) -> float:
        return Float.annualize_risk(self.risk_monthly, self.mean_return_monthly)

    @property
    def semideviation_monthly(self) -> float:
        return Frame.get_semideviation(self.get_returns_ts())

    @property
    def semideviation_annual(self) -> float:
        return Frame.get_semideviation(self.get_returns_ts()) * 12 ** 0.5

    def get_var_historic(self, time_frame: int = 12, level=5) -> float:
        """
        Calculate historic Value at Risk (VaR) for the portfolio.

        The VaR calculates the potential loss of an investment with a given time frame and confidence level.
        Loss is a positive number (expressed in cumulative return).
        If VaR is negative there are gains at this confidence level.

        Parameters
        ----------
        time_frame : int, default 12 (12 months)
        level : int, default 5 (5% quantile)

        Returns
        -------
        Float

        Examples
        --------
        >>> x = ok.Portfolio(['SP500TR.INDX', 'SP500BDT.INDX'], last_date='2021-01')
        >>> x.get_var_historic(time_frame=12, level=1)
        0.24030006476701732
        """
        rolling = self.get_rolling_cumulative_return(window=time_frame)
        return Frame.get_var_historic(rolling, level)

    def get_cvar_historic(self, time_frame: int = 12, level=5) -> float:
        """
        Calculate historic Conditional Value at Risk (CVAR, expected shortfall) for the portfolio.

        CVaR is the average loss over a specified time period of unlikely scenarios beyond the confidence level.
        Loss is a positive number (expressed in cumulative return).
        If CVaR is negative there are gains at this confidence level.

        Parameters
        ----------
        time_frame : int, default 12 (12 months)
        level : int, default 5 (5% quantile)

        Returns
        -------
        Float

        Examples
        --------
        >>> x = ok.Portfolio(['USDEUR.FX', 'BTC-USD.CC'], last_date='2021-01')
        >>> x.get_cvar_historic(time_frame=2, level=1)
        0.3566909250442616
        """
        rolling = self.get_rolling_cumulative_return(window=time_frame)
        return Frame.get_cvar_historic(rolling, level)

    @property
    def drawdowns(self) -> pd.Series:
        """
        Calculate drawdowns time series for the portfolio.

        The drawdown is the percent decline from a previous peak in wealth index.
        """
        return Frame.get_drawdowns(self.get_returns_ts())

    def describe(self, years: Tuple[int] = (1, 5, 10)) -> pd.DataFrame:
        """
        Generate descriptive statistics for the portfolio.

        Statistics includes:
        - YTD (Year To date) compound return
        - CAGR for a given list of periods
        - Dividend yield - yield for last 12 months (LTM)

        Risk metrics (full available period):
        - risk (standard deviation)
        - CVAR
        - max drawdowns (and dates)

        Parameters
        ----------
        years : tuple of (int,), default (1, 5, 10)
            List of periods for CAGR.

        Returns
        -------
            DataFrame

        See Also
        --------
            get_cumulative_return : Calculate cumulative return.
            get_cagr : Calculate assets Compound Annual Growth Rate (CAGR).
            dividend_yield : Calculate dividend yield (LTM).
            risk_annual : Return annualized risks (standard deviation).
            get_cvar : Calculate historic Conditional Value at Risk (CVAR, expected shortfall).
            drawdowns : Calculate drawdowns.
        """
        description = pd.DataFrame()
        dt0 = self.last_date
        df = self._add_inflation()
        # YTD return
        year = dt0.year
        ts = Rebalance.rebalanced_portfolio_return_ts(
            self.weights, self._ror[str(year):], period="none"
        )
        value = Frame.get_cumulative_return(ts)
        if hasattr(self, "inflation"):
            ts = df[str(year):].loc[:, self.inflation]
            inflation = Frame.get_cumulative_return(ts)
            row = {"portfolio": value, self.inflation: inflation}
        else:
            row = {"portfolio": value}
        row.update(period="YTD", rebalancing="1 year", property="compound return")
        description = description.append(row, ignore_index=True)
        # CAGR for a list of periods (rebalanced 1 year)
        if self.pl.years >= 1:
            for i in years:
                dt = Date.subtract_years(dt0, i)
                if dt >= self.first_date:
                    ts = Rebalance.rebalanced_portfolio_return_ts(
                        self.weights, self._ror[dt:], period="year"
                    )
                    value = Frame.get_cagr(ts)
                    if hasattr(self, "inflation"):
                        ts = df[dt:].loc[:, self.inflation]
                        inflation = Frame.get_cagr(ts)
                        row = {"portfolio": value, self.inflation: inflation}
                    else:
                        row = {"portfolio": value}
                else:
                    row = (
                        {x: None for x in df.columns}
                        if hasattr(self, "inflation")
                        else {"portfolio": None}
                    )
                row.update(period=f"{i} years", rebalancing="1 year", property="CAGR")
                description = description.append(row, ignore_index=True)
            # CAGR for full period (rebalanced 1 year)
            ts = self.get_returns_ts(rebalancing_period="year")
            value = Frame.get_cagr(ts)
            if hasattr(self, "inflation"):
                ts = df.loc[:, self.inflation]
                full_inflation = Frame.get_cagr(
                    ts
                )  # full period inflation is required for following calc
                row = {"portfolio": value, self.inflation: full_inflation}
            else:
                row = {"portfolio": value}
            row.update(
                period=f"{self.period_length} years",
                rebalancing="1 year",
                property="CAGR",
            )
            description = description.append(row, ignore_index=True)
            # CAGR rebalanced 1 month
            value = self.get_cagr()
            if hasattr(self, "inflation"):
                row = value.to_dict()
                full_inflation = value.loc[
                    self.inflation
                ]  # full period inflation is required for following calc
            else:
                row = {"portfolio": value}
            row.update(
                period=f"{self.period_length} years",
                rebalancing="1 month",
                property="CAGR",
            )
            description = description.append(row, ignore_index=True)
            # CAGR not rebalanced
            value = Frame.get_cagr(
                self.get_returns_ts(rebalancing_period="none")
            )
            if hasattr(self, "inflation"):
                row = {"portfolio": value, self.inflation: full_inflation}
            else:
                row = {"portfolio": value}
            row.update(
                period=f"{self.period_length} years",
                rebalancing="Not rebalanced",
                property="CAGR",
            )
            description = description.append(row, ignore_index=True)
            # Dividend Yield
            dy = self.dividend_yield
            for i, ccy in enumerate(dy):
                value = self.dividend_yield.iloc[-1, i]
                row = {"portfolio": value}
                row.update(
                    period="LTM",
                    rebalancing="1 month",
                    property=f"Dividend yield ({ccy})",
                )
                description = description.append(row, ignore_index=True)
        # risk (rebalanced 1 month)
        row = {"portfolio": self.risk_annual}
        row.update(
            period=f"{self.period_length} years", rebalancing="1 month", property="Risk"
        )
        description = description.append(row, ignore_index=True)
        # CVAR (rebalanced 1 month)
        if self.pl.years >= 1:
            row = {"portfolio": self.get_cvar_historic()}
            row.update(
                period=f"{self.period_length} years",
                rebalancing="1 month",
                property="CVAR",
            )
            description = description.append(row, ignore_index=True)
        # max drawdowns (rebalanced 1 month)
        row = {"portfolio": self.drawdowns.min()}
        row.update(
            period=f"{self.period_length} years",
            rebalancing="1 month",
            property="Max drawdown",
        )
        description = description.append(row, ignore_index=True)
        # max drawdowns dates
        row = {"portfolio": self.drawdowns.idxmin()}
        row.update(
            period=f"{self.period_length} years",
            rebalancing="1 month",
            property="Max drawdown date",
        )
        description = description.append(row, ignore_index=True)
        if hasattr(self, "inflation"):
            description.rename(columns={self.inflation: "inflation"}, inplace=True)
        description = Frame.change_columns_order(
            description, ["property", "rebalancing", "period", "portfolio"]
        )
        return description

    @property
    def table(self) -> pd.DataFrame:
        """
        Returns security name - ticker - weight DataFrame table.
        """
        x = pd.DataFrame(
            data={
                "asset name": list(self.names.values()),
                "ticker": list(self.names.keys()),
            }
        )
        x["weights"] = self.weights
        return x

    def get_rolling_cagr(self, years: int = 1) -> pd.Series:
        """
        Rolling portfolio CAGR (annualized rate of return) time series.
        """
        if self.pl.years < 1:
            raise ValueError(
                "Portfolio history data period length should be at least 12 months."
            )
        rolling_return = (self.get_returns_ts() + 1.0).rolling(
            _MONTHS_PER_YEAR * years
        ).apply(np.prod, raw=True) ** (1 / years) - 1.0
        rolling_return.dropna(inplace=True)
        return rolling_return

    # Forecasting

    def _test_forecast_period(self, years):
        max_period_years = round(self.period_length / 2)
        if max_period_years < 1:
            raise ValueError(
                f"Time series does not have enough history to forecast. "
                f"Period length is {self.period_length:.2f} years. At least 2 years are required."
            )
        if not isinstance(years, int) or years == 0:
            raise ValueError("years must be an integer number (not equal to zero).")
        if years > max_period_years:
            raise ValueError(
                f"Forecast period {years} years is not credible. "
                f"It should not exceed 1/2 of portfolio history period length {self.period_length / 2} years"
            )

    def percentile_inverse(
        self,
        distr: str = "norm",
        years: int = 1,
        score: float = 0,
        n: Optional[int] = None,
    ) -> float:
        """
        Compute the percentile rank of a score (CAGR value) in a given time frame.

        If percentile_inverse of, for example, 0% (CAGR value) is equal to 8% for 1 year time frame
        it means that 8% of the CAGR values in the distribution are negative in 1 year periods. Or in other words
        the probability of getting negative result after 1 year of investments is 8%.

        Args:
            distr: norm, lognorm, hist - distribution type (normal or lognormal) or hist for CAGR array from history
            years: period length when CAGR is calculated
            score: score that is compared to the elements in CAGR array.
            n: number of random time series (for 'norm' or 'lognorm' only)

        Returns:
            Percentile-position of score (0-100) relative to distr.
        """
        if distr == "hist":
            cagr_distr = self.get_rolling_cagr(years)
        elif distr in ["norm", "lognorm"]:
            if not n:
                n = 1000
            cagr_distr = self._get_monte_carlo_cagr_distribution(
                distr=distr, years=years, n=n
            )
        else:
            raise ValueError('distr should be one of "norm", "lognorm", "hist".')
        return scipy.stats.percentileofscore(cagr_distr, score, kind="rank")

    def percentile_from_history(
        self, years: int, percentiles: List[int] = [10, 50, 90]
    ) -> pd.DataFrame:
        """
        Calculate given percentiles for portfolio CAGR (annualized rolling returns) distribution from the historical data.
        Each percentile is calculated for a period range from 1 year to 'years'.

        years - max window size for rolling CAGR (limited with half history of period length).
        percentiles - list of percentiles to be calculated
        """
        self._test_forecast_period(years)
        period_range = range(1, years + 1)
        returns_dict = {}
        for percentile in percentiles:
            percentile_returns_list = [
                self.get_rolling_cagr(years).quantile(percentile / 100)
                for years in period_range
            ]
            returns_dict.update({percentile: percentile_returns_list})
        df = pd.DataFrame(returns_dict, index=list(period_range))
        df.index.rename("years", inplace=True)
        return df

    def forecast_wealth_history(
        self, years: int = 1, percentiles: List[int] = [10, 50, 90]
    ) -> pd.DataFrame:
        """
        Compute accumulated wealth for each CAGR derived by 'percentile_from_history' method.
        CAGRs are taken from the historical data.

        Initial portfolio wealth is adjusted to the last known historical value (from wealth_index). It is useful
        for a chart with historical wealth index and forecasted values.

        Args:
            years:
            percentiles:

        Returns:
            Dataframe of percentiles for period range from 1 to 'years'
        """
        first_value = self.wealth_index["portfolio"].values[-1]
        percentile_returns = self.percentile_from_history(
            years=years, percentiles=percentiles
        )
        return first_value * (percentile_returns + 1.0).pow(
            percentile_returns.index.values, axis=0
        )

    def _forecast_preparation(self, years: int):
        self._test_forecast_period(years)
        period_months = years * _MONTHS_PER_YEAR
        # make periods index where the shape is max_period
        start_period = self.last_date.to_period("M")
        end_period = self.last_date.to_period("M") + period_months - 1
        ts_index = pd.period_range(start_period, end_period, freq="M")
        return period_months, ts_index

    def forecast_monte_carlo_returns(
        self, distr: str = "norm", years: int = 1, n: int = 100
    ) -> pd.DataFrame:
        """
        Generates N random monthly returns time series with normal or lognormal distributions.
        Forecast period should not exceed 1/2 of portfolio history period length.
        """
        period_months, ts_index = self._forecast_preparation(years)
        # random returns
        if distr == "norm":
            random_returns = np.random.normal(
                self.mean_return_monthly, self.risk_monthly, (period_months, n)
            )
        elif distr == "lognorm":
            std, loc, scale = scipy.stats.lognorm.fit(self.get_returns_ts())
            random_returns = scipy.stats.lognorm(std, loc=loc, scale=scale).rvs(
                size=[period_months, n]
            )
        else:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        return pd.DataFrame(data=random_returns, index=ts_index)

    def forecast_monte_carlo_wealth_indexes(
        self, distr: str = "norm", years: int = 1, n: int = 100
    ) -> pd.DataFrame:
        """
        Generates N future random wealth indexes.
        Random distribution could be normal or lognormal.

        First value for the forecasted wealth indexes is the last historical portfolio index value. It is useful
        for a chart with historical wealth index and forecasted values.
        """
        if distr not in ["norm", "lognorm"]:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        return_ts = self.forecast_monte_carlo_returns(distr=distr, years=years, n=n)
        first_value = self.wealth_index["portfolio"].values[-1]
        return Frame.get_wealth_indexes(return_ts, first_value)

    def _get_monte_carlo_cagr_distribution(
        self, distr: str = "norm", years: int = 1, n: int = 100,
    ) -> pd.Series:
        """
        Generate random CAGR distribution.
        CAGR is calculated for each of N future random returns time series.
        Random distribution could be normal or lognormal.
        """
        if distr not in ["norm", "lognorm"]:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        return_ts = self.forecast_monte_carlo_returns(distr=distr, years=years, n=n)
        return Frame.get_cagr(return_ts)

    def forecast_monte_carlo_cagr(
        self,
        distr: str = "norm",
        years: int = 1,
        percentiles: List[int] = [10, 50, 90],
        n: int = 10000,
    ) -> pd.Series:
        """
        Calculate percentiles for forecasted CAGR distribution.
        CAGR is calculated for each of N future random returns time series.
        Random distribution could be normal or lognormal.
        """
        if distr not in ["norm", "lognorm"]:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        cagr_distr = self._get_monte_carlo_cagr_distribution(
            distr=distr, years=years, n=n
        )
        results = {}
        for percentile in percentiles:
            value = cagr_distr.quantile(percentile / 100)
            results.update({percentile: value})
        return results

    def forecast_wealth(
        self,
        distr: str = "norm",
        years: int = 1,
        percentiles: List[int] = [10, 50, 90],
        today_value: Optional[int] = None,
        n: int = 1000,
    ) -> Dict[int, float]:
        """
        Calculate percentiles of forecasted random accumulated wealth distribution.
        Random distribution could be normal lognormal or from history.

        today_value - the value of portfolio today (before forecast period). If today_value is None
        the last value of the historical wealth indexes is taken.
        """
        if distr == "hist":
            results = (
                self.forecast_wealth_history(years=years, percentiles=percentiles)
                .iloc[-1]
                .to_dict()
            )
        elif distr in ["norm", "lognorm"]:
            results = {}
            wealth_indexes = self.forecast_monte_carlo_wealth_indexes(
                distr=distr, years=years, n=n
            )
            for percentile in percentiles:
                value = wealth_indexes.iloc[-1, :].quantile(percentile / 100)
                results.update({percentile: value})
        else:
            raise ValueError('distr should be "norm", "lognorm" or "hist".')
        if today_value:
            modifier = today_value / self.wealth_index["portfolio"].values[-1]
            results.update((x, y * modifier) for x, y in results.items())
        return results

    def plot_forecast(
        self,
        distr: str = "norm",
        years: int = 5,
        percentiles: List[int] = [10, 50, 90],
        today_value: Optional[int] = None,
        n: int = 1000,
        figsize: Optional[tuple] = None,
    ):
        """
        Plots forecasted ranges of wealth indexes (lines) for a given set of percentiles.

        distr - the distribution model type:
            norm - normal distribution
            lognorm - lognormal distribution
            hist - percentiles are taken from historical data
        today_value - the value of portfolio today (before forecast period)
        n - number of random wealth time series used to calculate percentiles (not needed if distr='hist')
        """
        wealth = self.wealth_index
        x1 = self.last_date
        x2 = x1.replace(year=x1.year + years)
        y_start_value = wealth["portfolio"].iloc[-1]
        y_end_values = self.forecast_wealth(
            distr=distr, years=years, percentiles=percentiles, n=n
        )
        if today_value:
            modifier = today_value / y_start_value
            wealth *= modifier
            y_start_value = y_start_value * modifier
            y_end_values.update((x, y * modifier) for x, y in y_end_values.items())
        fig, ax = plt.subplots(figsize=figsize)
        ax.plot(
            wealth.index.to_timestamp(),
            wealth["portfolio"],
            linewidth=1,
            label="Historical data",
        )
        for percentile in percentiles:
            x, y = [x1, x2], [y_start_value, y_end_values[percentile]]
            if percentile == 50:
                ax.plot(x, y, color="blue", linestyle="-", linewidth=2, label="Median")
            else:
                ax.plot(
                    x,
                    y,
                    linestyle="dashed",
                    linewidth=1,
                    label=f"Percentile {percentile}",
                )
        ax.legend(loc="upper left")
        return ax

    def plot_forecast_monte_carlo(
        self,
        distr: str = "norm",
        years: int = 1,
        n: int = 20,
        figsize: Optional[tuple] = None,
    ):
        """
        Plots N random wealth indexes and historical wealth index.
        Forecasted indexes are generated accorded to a given distribution (Monte Carlo simulation).
        Normal and lognormal distributions could be used for Monte Carlo simulation.
        """
        s1 = self.wealth_index
        s2 = self.forecast_monte_carlo_wealth_indexes(distr=distr, years=years, n=n)
        s1["portfolio"].plot(legend=None, figsize=figsize)
        for n in s2:
            s2[n].plot(legend=None)

    # distributions
    @property
    def skewness(self):
        """
        Compute expanding skewness of the return time series.
        For normally distributed data, the skewness should be about zero.
        A skewness value greater than zero means that there is more weight in the right tail of the distribution.
        """
        return Frame.skewness(self.get_returns_ts())

    def skewness_rolling(self, window: int = 60):
        """
        Compute rolling skewness of the return time series.
        For normally distributed data, the skewness should be about zero.
        A skewness value greater than zero means that there is more weight in the right tail of the distribution.

        window - the rolling window size in months (default is 5 years).
        The window size should be at least 12 months.
        """
        return Frame.skewness_rolling(self.get_returns_ts(), window=window)

    @property
    def kurtosis(self):
        """
        Calculate expanding Fisher (normalized) kurtosis time series for portfolio returns.
        Kurtosis is the fourth central moment divided by the square of the variance.
        Kurtosis should be close to zero for normal distribution.
        """
        return Frame.kurtosis(self.get_returns_ts())

    def kurtosis_rolling(self, window: int = 60):
        """
        Calculate rolling Fisher (normalized) kurtosis time series for portfolio returns.
        Kurtosis is the fourth central moment divided by the square of the variance.
        Kurtosis should be close to zero for normal distribution.

        window - the rolling window size in months (default is 5 years).
        The window size should be at least 12 months.
        """
        return Frame.kurtosis_rolling(self.get_returns_ts(), window=window)

    @property
    def jarque_bera(self):
        """
        Performs Jarque-Bera test for normality.
        It shows whether the returns have the skewness and kurtosis matching a normal distribution.

        Returns:
            (The test statistic, The p-value for the hypothesis test)
            Low statistic numbers correspond to normal distribution.
        """
        return Frame.jarque_bera_series(self.get_returns_ts())

    def kstest(self, distr: str = "norm") -> dict:
        """
        Performs Kolmogorov-Smirnov test on portfolio returns and evaluate goodness of fit.
        Test works with normal and lognormal distributions.

        Returns:
            (The test statistic, The p-value for the hypothesis test)
        """
        return Frame.kstest_series(self.get_returns_ts(), distr=distr)

    def plot_percentiles_fit(
        self, distr: str = "norm", figsize: Optional[tuple] = None
    ):
        """
        Generates a probability plot of portfolio returns against percentiles of a specified
        theoretical distribution (the normal distribution by default).
        Works with normal and lognormal distributions.
        """
        plt.figure(figsize=figsize)
        if distr == "norm":
            scipy.stats.probplot(self.get_returns_ts(), dist=distr, plot=plt)
        elif distr == "lognorm":
            scipy.stats.probplot(
                self.get_returns_ts(),
                sparams=(scipy.stats.lognorm.fit(self.get_returns_ts())),
                dist=distr,
                plot=plt,
            )
        else:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        plt.show()

    def plot_hist_fit(self, distr: str = "norm", bins: int = None):
        """
        Plots historical distribution histogram and theoretical PDF (Probability Distribution Function).
        Lognormal and normal distributions could be used.

        normal distribution - 'norm'
        lognormal distribution - 'lognorm'
        """
        data = self.get_returns_ts()
        # Plot the histogram
        plt.hist(data, bins=bins, density=True, alpha=0.6, color="g")
        # Plot the PDF.Probability Density Function
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        if distr == "norm":  # Generate PDF
            mu, std = scipy.stats.norm.fit(data)
            p = scipy.stats.norm.pdf(x, mu, std)
        elif distr == "lognorm":
            std, loc, scale = scipy.stats.lognorm.fit(data)
            mu = np.log(scale)
            p = scipy.stats.lognorm.pdf(x, std, loc, scale)
        else:
            raise ValueError('distr should be "norm" (default) or "lognorm".')
        plt.plot(x, p, "k", linewidth=2)
        title = "Fit results: mu = %.3f,  std = %.3f" % (mu, std)
        plt.title(title)
        plt.show()
