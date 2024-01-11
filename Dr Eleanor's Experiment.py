'''
The challenge is to calculate the average and standard deviation of radiation levels for multiple locations.
Organise data into a suitable structure.
Calculate the average of multiple data observations.
Calculate standard deviation, giving insights to variability.
Add functionality so the user can input new radiation levels.
'''
import math

# function for entering new radiation levels into an existing location
def enter_data(new_data_location):
    # Create loop to enter radiation levels and check for errors.
    while True:
        try:
            new_data = input("Enter the new radiation level you would like to enter: (if multiple, separate with comma) ")
            # if just one value entered, convert this value to float and append to the dictionary
            if len(new_data) == 1:
                new_data = float(new_data)
                radiation_levels[new_data_location].append(new_data)
            # if more than one value was entered, get rid of spaces and split by the commas
            else:
                new_data = new_data.replace(" ", "")
                new_data = new_data.split(",")
                # convert the values to floats and add to dictionary
                for data in new_data:
                    data = float(data)
                    radiation_levels[new_data_location].append(data)
        # consider errors when converting to float
        except ValueError:
            print("The radiation levels must be numeric and positive. Please try again.")
        except Exception as e:
            print("e")
        else:
            break
    
    print(f'''
Your data has been added in.
Here are the radiation levels for {new_data_location}:
{radiation_levels[new_data_location]}
''')

# create function to add new location to dictionary
def add_new_location():
    new_location = input("Enter the name of the new location: ").lower()
    new_location = new_location.strip()
    radiation_levels[new_location] = []
    # ask user if they would like to enter data for this new location, if yes use enter_data function 
    while True:
        new_data_q = input("Would you like to add a radiation level to the new location? (Y/N) ").upper()
        if new_data_q != "N" and new_data_q != "Y":
            print("Your answer wasn't recognised. Please try again.")
        elif new_data_q == "Y":
            enter_data(new_location)
            break
        elif new_data_q == "N":
            break
        else:
            print("Your answer wasn't recognised. Please try again.")

# create function calculating the average for a location
def average(average_location):
    total = sum(radiation_levels[average_location])
    amount_of_levels = len(radiation_levels[average_location])
    # create error if no data for this location (otherwise will be trying to divide by 0)
    if amount_of_levels == 0:
        print(" This can't be calculated as you have no values for this location.")
    else:
        return total/amount_of_levels

# creat function calculating the standard deviation for a location
def standard_deviation(sd_location):
    copy_levels = radiation_levels[sd_location]
    levels_len = len(copy_levels)
    # create error if no data for this location (otherwise will be trying to divide by 0)
    if levels_len == 0:
        print("This can't be calculated as you have no values for this location.")
    else:
        av = average(sd_location)
        sum_sq_diff = 0
        for level in copy_levels:
            sq_diff = (level - av)**2
            sum_sq_diff += sq_diff
        variance = sum_sq_diff / len(copy_levels)
        sd = math.sqrt(variance)
    return sd

# create variable with existing location and radiation levels
radiation_levels = {
    "city center" : [22.0, 19.0, 20.0, 31.0, 28.0],
    "industrial zone" : [35.0, 32.0, 30.0, 37.0, 40.0],
    "residential district" : [15.0, 12.0, 18.0, 20.0, 14.0],
    "rural outskirts" : [9.0, 13.0, 16.0, 14.0, 7.0],
    "downtown" : [25.0, 18.0, 22.0, 21.0, 26.0]
                    }

# print current radiation levels
print("Here are the current radiation levels stored: ")
for key in radiation_levels:
    print(key.capitalize())
    print(radiation_levels[key])
print("\n")

# ask user if they would like to enter more data to existing location
while True:
    add_data = input("Would you like to enter more data to an existing location? (Y/N) ").upper()
    if add_data != "Y" and add_data != "N":
        print("This wasn't recognised. Please try again.")
        continue
    else:
        break
if add_data == "Y":
    while True:
        # Create loop to enter location and check this exists in dictionary
        new_data_location = input("Which location would you like to add data to? : ").lower()
        if new_data_location in radiation_levels:
            break
        else:
            print("This location was not recognised. Please try again.")
    enter_data(new_data_location)

# create loop asking user if they would like to enter a new location to the dictionary
while True:
    new_location_q = input("Would you like to add a new location? (Y/N) ").upper()
    if new_location_q == "N":
        break
    # if user would like to add a new location, call the add_new_location function
    elif new_location_q == "Y":
        add_new_location()
    else:
        print("Your answer wasn't recognised, please try again.")

# ask user which location they would like to calculate the average of
average_location = input("Which area would you like to calculate the average radiation of? (Enter 'all' for all locations) ").lower()
average_location = average_location.strip()
# if user would like the averages of all locations, loop through locations and calculate average for each
if average_location == "all":
    print("The average radiation across all locations: ")
    for location in radiation_levels.keys():
        print(f"{location}: {average(location)}")
else:
    print(f"The average radiation in {average_location} is {average(average_location)}")

# ask user which location they would like to calculate the standard deviation of
sd_location = input("Which area would you like to calculate the standard deviation of the radiation levels? (Enter 'all' for all locations) ").lower()
sd_location = sd_location.strip()
# if user would like the standard deviation of all locations, loop through locations and calculate standard deviation for each
if sd_location == "all":
    print("Standard deviation of radiation across all locations: ")
    for location in radiation_levels.keys():
        print(f"{location}: {standard_deviation(location)}")
else:
    print(f"The standard deviation of radiation in {sd_location} is {standard_deviation(sd_location)}")