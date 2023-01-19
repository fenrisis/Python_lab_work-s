# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]


# Function to be passed to the map() function.
def mod(employee_list):
    return_val = employee_list['name'] + "_" + employee_list["department"]
    return return_val

# This function Modifies the employee list of dictionaries into list of employee-department strings
def to_mod_list(employee_list):
    return_list = []
    map_employee_list = map(mod, employee_list)
    for x in map_employee_list:
        return_list.append(x)
    return return_list



# This function Generates a list of usernames
def generate_usernames(mod_list):
    return_list = [x.replace(" ", "_") for x in mod_list]
    return return_list



# This function Maps employee id to first initial
def map_id_to_initial(employee_list):
    first_init = {employee["name"][0] : employee["id"] for employee in employee_list}
    return first_init


# This function prints final result of our mapping
def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()
