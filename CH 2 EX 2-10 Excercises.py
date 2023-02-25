#2.10 - testing double assignment (it works)
x = y = 1
## Does a semicolon still work? (Yes)
print (x,y);
# No semicolon works too
print (x,y)

# Variable multiplication as below does not work.
# xy

# Ex 2.2
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# Convert hours to minutes
start_time = (6*60) + 52
first_run = 8 + (15/60)
second_run = 3 * (7 + (12/60))
third_run = first_run
return_time = start_time + first_run + second_run + third_run
# Convert to hours by flooring using the 60 minute division (of an hour)
# Add the hours using a string format to the remainder of diving the minutes by 60 and floor by 1 to limit to full minutes
return_time_str = str(return_time//60) + ' hours and ' + str(return_time%60//1) + ' minutes'
print (return_time_str)

