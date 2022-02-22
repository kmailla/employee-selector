from employee_selector import EmployeeSelector, generate_employee_group_combinations, reduce_redundancy


def run():
    #required_skills = ['l', 'q', 's']
    required_skills = ['a', 'b', 'd','e','i','l','n','o','r','s','t']
    selector = EmployeeSelector('skill_map.csv')

    # get all the employees that have at least one of the required skills
    skilled_employees = selector.get_employees_by_skill_set(required_skills)

    # generate all the possible group combinations out of the selected employees
    employee_groups = generate_employee_group_combinations(skilled_employees)

    correct_groups = []

    for group in employee_groups:
        if selector.is_skill_set_covered(required_skills, group):
            correct_groups.append(group)

    print(correct_groups)
    reduced = reduce_redundancy(correct_groups)
    print(sorted(reduced))
