def main():
    with open('input.txt') as f:
        read_data = f.read().splitlines()

    print(calculateFirstPuzzle(read_data))
    print(calculateSecondPuzzle(read_data))


def calculateFuelRequired(mass):
    return int(int(mass) / 3) - 2

def calculateFirstPuzzle(module_masses):
    totalFuel = 0
    for mass in module_masses:
        totalFuel += calculateFuelRequired(mass)

    return totalFuel

def calculateSecondPuzzle(module_masses):
    totalFuel = 0

    for mass in module_masses:
        moduleFuelRequired = calculateFuelRequired(mass)
        while moduleFuelRequired > 0:
            totalFuel += moduleFuelRequired
            moduleFuelRequired = calculateFuelRequired(moduleFuelRequired)


    return totalFuel

main()