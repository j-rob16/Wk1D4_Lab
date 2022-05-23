def select_option():
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option


def select_description():
    description = input("Enter task description to search for: ")
    return description


def select_duration():
    duration = int(input("Enter task duration: "))
    return duration