from cli import read_blood_type
from engines import BloodTransfusionEngine


def main() -> None:
    engine = BloodTransfusionEngine.build(
        read_blood_type('Input donor blood type: '),
        read_blood_type('Input recipient blood type: ')
    )
    engine.run()

    is_allowed = engine.facts[engine.facts.last_index - 1]['is_allowed']
    print('Transfusion:', 'Allowed' if is_allowed else 'Not allowed')


if __name__ == '__main__':
    main()
