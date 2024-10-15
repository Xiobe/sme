from enum import Enum

BELGIAN_AWU_TRESHOLD_SME_ENTERPRISE = 50
BELGIAN_AWU_TRESHOLD_LARGE_ENTERPRISE = 250
BELGIAN_TURNOVER_TRESHOLD_SME_ENTERPRISE = 10000000
BELGIAN_TURNOVER_TRESHOLD_LARGE_ENTERPRISE = 50000000
BELGIAN_BALANCESHEET_TRESHOLD_SME_ENTERPRISE = 10000000
BELGIAN_BALANCESHEET_TRESHOLD_LARGE_ENTERPRISE = 43000000

class SizeCap(Enum):
    """The SizeCap represents the size of the Company based on the annual workload units"""

    small = "small"
    medium = "medium"
    large = "large"

class SmallMediumEnterprise():

    def __init__(self, annual_workload_units: int, annual_turnover: float, annual_balance_sheet_total: float) -> None:
        """Enterprise initializer"""
        self._awu = annual_workload_units
        self._turnover = annual_turnover
        self._balancesheet = annual_balance_sheet_total

    def get_category(self):
        """Analyzes the category of enterprise based on the company capsizes"""
        if self.get_awu_sizecap() == SizeCap.small:

            if self.get_turnover_sizecap() == SizeCap.large and self.get_balancesheet_sizecap() == SizeCap.large:
                return SizeCap.large

            elif self.get_turnover_sizecap() == SizeCap.large and self.get_balancesheet_sizecap() == SizeCap.medium:
                return SizeCap.medium

            elif self.get_turnover_sizecap() == SizeCap.medium and self.get_balancesheet_sizecap() == SizeCap.medium:
                return SizeCap.medium

            elif self.get_turnover_sizecap() == SizeCap.medium and self.get_balancesheet_sizecap() == SizeCap.large:
                return SizeCap.medium

            else:
                return SizeCap.small

        elif self.get_awu_sizecap() == SizeCap.medium:

            if self.get_turnover_sizecap() == SizeCap.large and self.get_balancesheet_sizecap() == SizeCap.large:
                return SizeCap.large
            else:
                return SizeCap.medium

        elif self.get_awu_sizecap() == SizeCap.large:
            return SizeCap.large


    def get_awu_sizecap(self) -> SizeCap:
        """Returns the sizecap of the enterprise based on the annual workload units (also called full time equivalents)"""
        if self.annual_workload_units < BELGIAN_AWU_TRESHOLD_SME_ENTERPRISE:
            return SizeCap.small
        elif self.annual_workload_units > BELGIAN_AWU_TRESHOLD_LARGE_ENTERPRISE:
            return SizeCap.large
        else:
            return SizeCap.medium

    def get_turnover_sizecap(self) -> SizeCap:
        """Returns the sizecap of the enterprise based on its annual turnover"""
        if self.annual_turnover < BELGIAN_TURNOVER_TRESHOLD_SME_ENTERPRISE:
            return SizeCap.small
        elif self.annual_turnover > BELGIAN_TURNOVER_TRESHOLD_SME_ENTERPRISE:
            return SizeCap.large
        else:
            return SizeCap.medium

    def get_balancesheet_sizecap(self) -> SizeCap:
        """Returns the sizecap of the enterpise based on its annual balance sheet"""
        if self.annual_balance_sheet_total < BELGIAN_BALANCESHEET_TRESHOLD_SME_ENTERPRISE:
            return SizeCap.small
        elif self.annual_balance_sheet_total > BELGIAN_BALANCESHEET_TRESHOLD_LARGE_ENTERPRISE:
            return SizeCap.large
        else:
            return SizeCap.medium

    @property
    def annual_turnover(self) -> float:
        """Returns the annual turnover for the company"""
        return self._turnover

    @annual_turnover.setter
    def annual_turnover(self, annual_turnover) -> None:
        """Sets the annual turnover for the company"""
        self._turnover = float(annual_turnover)

    @property
    def annual_workload_units(self) -> int:
        """Returns the annual work load (also known as Full Time Equivalents) for the company"""
        return self._awu

    @annual_workload_units.setter
    def annual_workload_units(self, annual_workload_units) -> None:
        """Sets the annual work load (also known as Full Time Equivalents) for the company"""
        self._awu = int(annual_workload_units)

    @property
    def annual_balance_sheet_total(self) -> float:
        """Returns the annual balance sheet for the company"""
        return self._balancesheet

    @annual_balance_sheet_total.setter
    def annual_balance_sheet_total(self, annual_balance_sheet_total) -> None:
        """Sets the annual balance sheet value of the company"""
        self._balancesheet = float(annual_balance_sheet_total)

    def __repr__(self) -> str:
        """Returns the printable format of the object"""

        return f"annual workload units: {self.annual_workload_units}\nannual turnover: {self.annual_turnover}\nannual balance sheet: {self.annual_balance_sheet_total}\ncategory: {self.get_category().value}"

    def __eq__(cls, object) -> bool:
        """Equalty compares the category type for both SME's."""
        if cls.get_category() == object.get_category():
            return True
        else:
            return False
