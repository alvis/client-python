from polygon.rest.models import (
    StockFinancial,
    Financials,
    DataPoint,
    CashFlowStatement,
    ExchangeGainsLosses,
    NetCashFlow,
    NetCashFlowFromFinancingActivities,
    ComprehensiveIncome,
    ComprehensiveIncomeLoss,
    ComprehensiveIncomeLossAttributableToParent,
    OtherComprehensiveIncomeLoss,
    IncomeStatement,
    BasicEarningsPerShare,
    CostOfRevenue,
    GrossProfit,
    OperatingExpenses,
    Revenues,
)
from base import BaseTest


class FinancialsTest(BaseTest):
    def test_list_stock_financials(self):
        financials = [f for f in self.c.vx.list_stock_financials()]
        expected = [
            StockFinancial(
                cik="0001413447",
                company_name="NXP Semiconductors N.V.",
                end_date="2022-04-03",
                filing_date="2022-05-03",
                financials=[
                    Financials(
                        balance_sheet={
                            "equity_attributable_to_noncontrolling_interest": DataPoint(
                                formula=None,
                                label="Equity Attributable To Noncontrolling Interest",
                                order=1500,
                                unit="USD",
                                value=251000000.0,
                                xpath=None,
                            ),
                            "liabilities": DataPoint(
                                formula=None,
                                label="Liabilities",
                                order=600,
                                unit="USD",
                                value=14561000000.0,
                                xpath=None,
                            ),
                            "equity_attributable_to_parent": DataPoint(
                                formula=None,
                                label="Equity Attributable To Parent",
                                order=1600,
                                unit="USD",
                                value=6509000000.0,
                                xpath=None,
                            ),
                            "noncurrent_assets": DataPoint(
                                formula=None,
                                label="Noncurrent Assets",
                                order=300,
                                unit="USD",
                                value=16046000000.0,
                                xpath=None,
                            ),
                            "liabilities_and_equity": DataPoint(
                                formula=None,
                                label="Liabilities And Equity",
                                order=1900,
                                unit="USD",
                                value=21321000000.0,
                                xpath=None,
                            ),
                            "assets": DataPoint(
                                formula=None,
                                label="Assets",
                                order=100,
                                unit="USD",
                                value=21321000000.0,
                                xpath=None,
                            ),
                            "fixed_assets": DataPoint(
                                formula=None,
                                label="Fixed Assets",
                                order=400,
                                unit="USD",
                                value=2814000000.0,
                                xpath=None,
                            ),
                            "other_than_fixed_noncurrent_assets": DataPoint(
                                formula=None,
                                label="Other Than Fixed Noncurrent Assets",
                                order=500,
                                unit="USD",
                                value=16046000000.0,
                                xpath=None,
                            ),
                            "noncurrent_liabilities": DataPoint(
                                formula=None,
                                label="Noncurrent Liabilities",
                                order=800,
                                unit="USD",
                                value=11716000000.0,
                                xpath=None,
                            ),
                            "current_assets": DataPoint(
                                formula=None,
                                label="Current Assets",
                                order=200,
                                unit="USD",
                                value=5275000000.0,
                                xpath=None,
                            ),
                            "equity": DataPoint(
                                formula=None,
                                label="Equity",
                                order=1400,
                                unit="USD",
                                value=6760000000.0,
                                xpath=None,
                            ),
                            "current_liabilities": DataPoint(
                                formula=None,
                                label="Current Liabilities",
                                order=700,
                                unit="USD",
                                value=2845000000.0,
                                xpath=None,
                            ),
                        },
                        cash_flow_statement=[
                            CashFlowStatement(
                                exchange_gains_losses=[
                                    ExchangeGainsLosses(
                                        formula=None,
                                        label="Exchange Gains/Losses",
                                        order=1000,
                                        unit="USD",
                                        value=0,
                                        xpath=None,
                                    )
                                ],
                                net_cash_flow=[
                                    NetCashFlow(
                                        formula=None,
                                        label="Net Cash Flow",
                                        order=1100,
                                        unit="USD",
                                        value=-147000000.0,
                                        xpath=None,
                                    )
                                ],
                                net_cash_flow_from_financing_activities=[
                                    NetCashFlowFromFinancingActivities(
                                        formula=None,
                                        label="Net Cash Flow From Financing Activities",
                                        order=700,
                                        unit="USD",
                                        value=-674000000.0,
                                        xpath=None,
                                    )
                                ],
                            )
                        ],
                        comprehensive_income=[
                            ComprehensiveIncome(
                                comprehensive_income_loss=[
                                    ComprehensiveIncomeLoss(
                                        formula=None,
                                        label="Comprehensive Income/Loss",
                                        order=100,
                                        unit="USD",
                                        value=644000000.0,
                                        xpath=None,
                                    )
                                ],
                                comprehensive_income_loss_attributable_to_parent=[
                                    ComprehensiveIncomeLossAttributableToParent(
                                        formula=None,
                                        label="Comprehensive Income/Loss Attributable To Parent",
                                        order=300,
                                        unit="USD",
                                        value=635000000.0,
                                        xpath=None,
                                    )
                                ],
                                other_comprehensive_income_loss=[
                                    OtherComprehensiveIncomeLoss(
                                        formula=None,
                                        label="Other Comprehensive Income/Loss",
                                        order=400,
                                        unit="USD",
                                        value=-22000000.0,
                                        xpath=None,
                                    )
                                ],
                            )
                        ],
                        income_statement=[
                            IncomeStatement(
                                basic_earnings_per_share=[
                                    BasicEarningsPerShare(
                                        formula=None,
                                        label="Basic Earnings Per Share",
                                        order=4200,
                                        unit="USD / shares",
                                        value=2.5,
                                        xpath=None,
                                    )
                                ],
                                cost_of_revenue=[
                                    CostOfRevenue(
                                        formula=None,
                                        label="Cost Of Revenue",
                                        order=300,
                                        unit="USD",
                                        value=1359000000.0,
                                        xpath=None,
                                    )
                                ],
                                gross_profit=[
                                    GrossProfit(
                                        formula=None,
                                        label="Gross Profit",
                                        order=800,
                                        unit="USD",
                                        value=1777000000.0,
                                        xpath=None,
                                    )
                                ],
                                operating_expenses=[
                                    OperatingExpenses(
                                        formula=None,
                                        label="Operating Expenses",
                                        order=1000,
                                        unit="USD",
                                        value=904000000.0,
                                        xpath=None,
                                    )
                                ],
                                revenues=[
                                    Revenues(
                                        formula=None,
                                        label="Revenues",
                                        order=100,
                                        unit="USD",
                                        value=3136000000.0,
                                        xpath=None,
                                    )
                                ],
                            )
                        ],
                    )
                ],
                fiscal_period="Q1",
                fiscal_year="2022",
                source_filing_file_url="https://api.polygon.io/v1/reference/sec/filings/0001413447-22-000014/files/nxpi-20220403_htm.xml",
                source_filing_url="https://api.polygon.io/v1/reference/sec/filings/0001413447-22-000014",
                start_date="2022-01-01",
            )
        ]
        self.assertEqual(financials, expected)