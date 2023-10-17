from experta import Fact, Field
from models import BloodType


class BloodTypeFact(Fact):
    type = Field(BloodType, mandatory=True)


class BloodRecipientFact(BloodTypeFact):
    pass


class BloodDonorFact(BloodTypeFact):
    pass


class BloodTransfusionFact(Fact):
    is_allowed = Field(bool, mandatory=True)
