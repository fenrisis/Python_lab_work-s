



def create_dict(name, id, department):

    # Return's a dictionary that maps "first_name" to name, "age" to age, and "title" to title
    return {"first_name": str(name), "id": int(id), "department": str(department)}


def write_json_to_file(json_obj, output_file):

    # This function writes json string to file
    newfile = open(output_file, 'w')
    newfile.write(str(json_obj))
    newfile.close()
    return newfile


def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(name, id, department)
    print("employee_dict: " + str(employee_dict))

# dump stuf
    json_object = json.dumps(employee_dict)
    print("json_object: " + json_object)

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")


if __name__ == "__main__":
    main()
