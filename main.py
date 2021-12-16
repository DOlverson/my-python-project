from helper import validate_and_call, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    for days_and_unit in set(user_input.split(", "))
    #days_and_units_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_call(days_and_units_dictionary)
