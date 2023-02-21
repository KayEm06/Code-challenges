def main():
    value = float(input("Enter the value you would like to convert: "))
    unit_to = input("Enter the unit you would like to convert to: ")
    unit_from = input("Enter the unit you would like to convert from: ")

    conversion(value, unit_to, unit_from)

def conversion(value, unit_from, unit_to):
    units = {
        'miles': {
            'kilometres': 1.60934,
            'metres': 1609.34,
            'centimetres': 160934,
        },
        'kilometres': {
            'metres': 1000,
            'centimetres': 100000,
            'miles': 0.621371,
        },
        'metres': {
            'kilometres': 0.001,
            'centimetres': 100,
            'miles': 0.000621371,
        },
        'centimetres': {
            'kilometres': 0.00001,
            'metres': 0.01,
            'miles': 0.00000621371,
        },
        'kilograms': {
            'pounds': 2.20462,
        },
        'pounds': {
            'kilograms': 0.453592,
        }
    }

    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if (unit_to not in units) or (unit_from not in units):
        print("There is no direct conversion between those two units.")
    else:
        converted = units.get(unit_from,).get(unit_to)
        print(f"{value} {unit_from} is equal to {round(value * converted, 3)} {unit_to}")

main()

