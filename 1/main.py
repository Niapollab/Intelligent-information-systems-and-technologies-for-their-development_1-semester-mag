from cli import read_blood_type
from engines import BloodTransfusionEngine


def main() -> None:
    engine = BloodTransfusionEngine.build(
        read_blood_type('Input donor blood type: '),
        read_blood_type('Input recipient blood type: ')
    )
    engine.run()

    print('Transfusion:', engine.result.value)


if __name__ == '__main__':
    main()
