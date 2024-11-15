def filter_by_state(list_of_operations: list, state_wanted: str = "EXECUTED") -> list:
    """Function takes a list of bank operations and returns the list of ops with wanted state"""
    if not isinstance(list_of_operations, list):
        print("Invalid input(data type)")
        return []
    list_of_wanted_operations = []
    for operation in list_of_operations:
        if "state" not in operation.keys():
            print("Invalid input(no state)")
            return []
    for operation in list_of_operations:
        if operation["state"] and operation["state"] == state_wanted:
            list_of_wanted_operations.append(operation)
    return list_of_wanted_operations


def sort_by_date(list_of_operations: list, descending: bool = True) -> list:
    """Function takes list of bank operations and returns the list sorted by date (descending by default)"""
    if not isinstance(list_of_operations, list):
        print("Invalid input(data type)")
        return []
    for operation in list_of_operations:
        if "date" not in operation.keys():
            print("Invalid input(no date)")
            return []
    operations_sorted_by_date = sorted(
        list_of_operations, key=lambda operation: operation.get("date"), reverse=descending
    )
    return operations_sorted_by_date
