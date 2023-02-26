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

# Print a square up to 71 characters wide
def print_square(length):

    # Set height to 0 (first line)
    height = 0

    # If the number given for the length is even then prompt for an odd number


    if length.isnumeric() != True:
        print('Enter a number')
        print_square(input())
        return

    length = int(length) 
    if length%2==0:
        print('Enter an odd number')
        print_square(input())

    else:
        # Anything greater than 71 will get ceiled to 71
        if length > 71:
            length = 71

       # Identify middle of square function
        def middle():
            return math.ceil((length - 1)/ 2)
        
        # Draw the edge or middle line when called
        def pointed_line():
            # Draw first point
            string = '+'
            width = 1

            # While still drawing
            while width < (length -1):

                # Check if the middle of the line was reached
                if width == middle():
                    string += ' +'
                    width += 1

                # Continue to draw if the middle is not reached
                else:
                    string += ' -'
                    width += 1

            # Draw the final point in the line
            string += " +"
            print(string)

        # If first line
        if height == 0:
            
            # Draw edge
            pointed_line()
            height += 1
        
            # While height not complete
            while height < (length -1):

                # Check if height is the middle and if so, draw 'edge line'
                if height ==  middle():
                    pointed_line()
                    height += 1
                
                # Draw the non-edge line
                else:
                    width = 1
                    string = '|'

                    while width < (length -1):
                    
                        # Add middle line
                        if width ==  middle() :
                            string += ' |'
                            width += 1

                        # Add spaces
                        else:
                            string +='  '
                            width += 1
                    
                    # Finish
                    string += " |"
                    print(string)
                    
                    height += 1

            # After height is complete, draw the last edge
            pointed_line()
            height += 1

# Print a square with prompted input
print_square(input())