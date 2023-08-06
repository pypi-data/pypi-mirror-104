from dataclasses import dataclass
import datetime
from typing import Optional


@dataclass
class VaccinationByDayRow:
    """Represents on row of vaccinations by day table"""

    date: datetime.datetime
    first_dose: int
    second_dose: int = 0


@dataclass
class VaccinationByAgeRow:
    age_group: str
    count_first: int
    count_second: int
    share_first: float
    share_second: float


@dataclass
class VaccineSupplyUsage:
    date: datetime.datetime
    supplied: int
    used: int


@dataclass
class VaccinationByRegionRow:
    region: str
    count_first: int
    count_second: int
    share_first: float
    share_second: float


@dataclass
class VaccinationByManufacturerRow:
    date: datetime.datetime
    pfizer: Optional[int]
    moderna: Optional[int]
    az: Optional[int]
    janssen: Optional[int]


@dataclass
class VaccinationDose:
    date: datetime.datetime
    dose: int


@dataclass
class VaccinationByAgeRange:
    dose1: "list[VaccinationDose]"
    dose2: "list[VaccinationDose]"


@dataclass
class VaccinationMunShare:
    name: str
    dose1: int
    share1: float
    dose2: int
    share2: float
    population: int