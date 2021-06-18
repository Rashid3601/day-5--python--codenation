# loops revision, for loops run for a limited amount of time
# while loops will run until a condition is met
# activity 1

celsius = 25

def temperature_formula():
    farenheit = 1.8 * celsius + 32
    print("Today's temperature {} degrees celsius, which is {} degrees farenheit!".format(
        celsius, farenheit))
    kelvin = 273.15 + celsius
    print("However...! For all you scientists out there.")
    kelvin = 273.15 + celsius
    print("Today's temperature {} degrees celsius, which is {} degrees kelvin!".format(
        celsius, kelvin))
temperature_formula()

# activity 2
rows = 5
rows1 = 4
for i in (range(1, rows + 1)):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
for i in reversed(range(1, rows1 + 1)):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')

rows = 6
rows1 = 5
for i in (range(0, rows)):
    for j in range(0, i):
        print("*", end=" ")
    print('')
for i in reversed(range(0, rows1)):
    for j in range(0, i):
        print("*", end=" ")
    print('')



