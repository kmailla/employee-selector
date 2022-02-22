from itertools import combinations
import numpy as np


def employee_to_index(employee):
    return ord(employee) - 65


# expects a-z, returns 0-26
def skill_to_int(letter):
    return ord(letter) - 97


# expects 0-7, return A-H
def index_to_employee(idx):
    return chr(int(idx) + 65)


# returning one employee skill vector if the other is a subset of that one
def reduce_redundancy(employee_sets):
    for i in range(0, len(employee_sets)):
        for k in range(1, len(employee_sets) - i):
            if set(employee_sets[i]).issubset(set(employee_sets[i + k])):
                employee_sets[i + k] = [-1]

    reduced_employee_sets = list(filter(lambda x: x != [-1], employee_sets))

    return sorted(reduced_employee_sets)


# returning all possible combinations of given employees
def generate_employee_group_combinations(employees):
    employee_combinations = []
    for i in range(1, len(employees) + 1):
        employee_combinations.extend(list(combinations(employees, i)))

    return employee_combinations


def get_ideal_groups(required_skills, employee_selector):
    # get all the employees that have at least one of the required skills
    skilled_employees = employee_selector.get_employees_by_skill_set(required_skills)

    # generate all the possible group combinations out of the selected employees
    employee_groups = generate_employee_group_combinations(skilled_employees)

    skilled_groups = []

    for group in employee_groups:
        if employee_selector.is_skill_set_covered(required_skills, group):
            skilled_groups.append(list(group))

    print(skilled_groups)

    final_employee_groups = reduce_redundancy(skilled_groups)

    print(final_employee_groups)

    return final_employee_groups


class EmployeeSelector:
    skill_matrix = None

    def __init__(self, skill_mapper_file_path='skill_matrix.csv'):
        lower_bound = skill_to_int('a')
        upper_bound = skill_to_int('z')

        with open(skill_mapper_file_path, 'r', encoding='utf-8') as f:
            raw_lines = f.read().split('\n')

            # the skill array  = (number of employees) * (the number of different skills)
            self.skill_matrix = np.zeros((len(raw_lines), upper_bound - lower_bound + 1))

            for i, line in enumerate(raw_lines):
                letters = line.split(',')[1:]
                for char in letters:
                    self.skill_matrix[i][skill_to_int(char)] = 1

    # expects the skill char
    def get_employees_by_skill(self, skill):
        employees = []
        skill_idx = skill_to_int(skill)
        intersection_array = self.skill_matrix[:, skill_idx]

        for i, num in enumerate(intersection_array):
            if num == 1:
                employees.append(index_to_employee(i))

        return employees

    def get_employees_by_skill_set(self, skill_set):
        # using a set to prevent redundancy
        employees = set()
        for skill in skill_set:
            employees.update(self.get_employees_by_skill(skill))

        return sorted(employees)

    def is_skill_set_covered(self, skill_set, employees):
        employee_rows = self.skill_matrix[[employee_to_index(e) for e in employees], :]
        skill_intersection = np.sum(employee_rows[:, [skill_to_int(s) for s in skill_set]], axis=0)

        if np.all(skill_intersection >= 1):
            return True
        else:
            return False
