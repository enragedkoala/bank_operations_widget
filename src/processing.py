def filter_by_state(list_of_operations: list, state_wanted: str = "EXECUTED") -> list:
    """Function takes a list of operations and returns the list of ops with wanted state"""
    list_of_wanted_operations = []
    for operation in list_of_operations:
        if "state" not in operation.keys():
            print("invalid input")
            quit()
    for operation in list_of_operations:
        if operation["state"] and operation["state"] == state_wanted:
            list_of_wanted_operations.append(operation)
    return list_of_wanted_operations
