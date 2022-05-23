def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{number_of_days} days are {number_of_days * 24 * 60 * 60} seconds"
    else:
        return "Unsupported Unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_units_dictionary["Unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, Please enter a valid number.")
        else:
            print("Your input is invalid. Please enter a whole number.")
    except ValueError:
        print("Your input is invalid. Please enter a whole number.")


user_input = ""
while user_input != "exit":
    user_input = input("Enter the number of days and conversion unit I.E 10:hours.Type exit to end program.\n")
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "Unit": days_and_units[1]}
    validate_and_execute()
