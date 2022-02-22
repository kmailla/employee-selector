# expects A-H, returns 0-7
def employee_to_index(employee):
    employee_index = ord(employee) - 65
    if employee_index < 0 or employee_index > 7:
        raise ValueError('Expected input: A-H. Got {} instead.'.format(employee_index))
    else:
        return employee_index


# expects 0-7, returns A-H
def index_to_employee(idx):
    if idx < 0 or idx > 7:
        raise ValueError('Expected input: 0-7. Got {} instead.'.format(idx))
    else:
        return chr(int(idx) + 65)


# expects a-z, returns 0-25
def skill_to_int(letter):
    skill_int = ord(letter) - 97
    if skill_int < 0 or skill_int > 25:
        raise ValueError('Expected input: a-z. Got {} instead.'.format(letter))
    else:
        return skill_int
