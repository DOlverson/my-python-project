def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return print(f"There are {num_of_days * 24} hours in {num_of_days} days.")
    elif conversion_unit == "minutes":
        return print(f"There are {num_of_days * 24 * 60} minutes in {num_of_days} days.")
    else:
        print("Unsupported unit.")

def validate_and_call(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
            days_to_units(user_input_number, days_and_units_dictionary["unit"])
        elif user_input_number == 0:
            print("The number must be greater than 0.\n")
        else:
            print("No negative numbers please.\n")
    except ValueError:
        print("This must be a positive number.\n")

user_input_message = "Enter the number of days and a conversion unit?"