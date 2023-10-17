from models import BloodType


def read_blood_type(prompt: str) -> BloodType:
    while True:
        try:
            raw_value = input(prompt).replace('0', 'O').upper()
            return BloodType(raw_value)
        except Exception as ex:
            print(ex)
