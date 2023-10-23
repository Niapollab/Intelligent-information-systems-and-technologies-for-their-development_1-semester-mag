from enum import Enum


class BloodType(Enum):
    O = 'O'  # noqa: E741
    A = 'A'
    B = 'B'
    AB = 'AB'


class TransfusionResult(Enum):
    ALLOWED = 'Allowed'
    NOT_ALLOWED = 'Not allowed'
    UNDEFINED = 'Undefined'
