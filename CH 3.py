# Math
import math
signal_power = 1
noise_power = 1.1102
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)
print(height,decibels)

# Defining functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics()

## Exercises

def right_justify(to_justify):
    white_space = 70-len(to_justify);
    justified = white_space*' ' + to_justify
    print(justified);

right_justify('test');
right_justify('testing a lot more');

## Printer

def print_this_many(func, arg,value):
    count = 0
    while count < arg :
        func(value)
        count += 1

print_this_many(print,3, 'TEST')

# Print a cube up to 100 characters

cube_value = int(input())


def print_cube(length):
    if length%2==0:
        print('TEST')
    else:
        print('Enter an odd number')
        new_value = int(input())
        print_cube(new_value)

print_cube(cube_value)