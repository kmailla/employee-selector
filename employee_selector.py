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


# the map to read in has each employee is a new line
def load_skill_mapper(file_path):
    lower_bound = skill_to_int('a')
    upper_bound = skill_to_int('z')

    with open(file_path, 'r', encoding='utf-8') as f:
        raw_lines = f.read().split('\n')

        # the skill array  = (number of employees) * (the number of different skills)
        skill_array = np.zeros((len(raw_lines), upper_bound-lower_bound+1))

        for i, line in enumerate(raw_lines):
            letters = line.split(',')[1:]
            for char in letters:
                skill_array[i][skill_to_int(char)] = 1

    return skill_array


# expects the skill char
def get_employees_by_skill(skill, skill_mapper):
    employees = []
    skill_idx = skill_to_int(skill)
    intersection_array = skill_mapper[:, skill_idx]

    for i, num in enumerate(intersection_array):
        if num == 1:
            employees.append(index_to_employee(i))

    return employees


def get_employees_by_skill_set(skill_set, skill_mapper):
    # using a set to prevent redundancy
    employees = set()
    for skill in skill_set:
        employees.update(get_employees_by_skill(skill, skill_mapper))

    return sorted(employees)


# returning one employee skill vector if the other is a subset of that one
def reduce_redundancy(employee_sets):
    for i in range(0, len(employee_sets)):
        for k in range(1, len(employee_sets)-i):
            if set(employee_sets[i]).issubset(set(employee_sets[i+k])):
                employee_sets[i+k] = [-1]

    reduced_employee_sets = list(filter(lambda x: x != [-1], employee_sets))

    return reduced_employee_sets


# returning all possible combinations of given employees
def generate_employee_combinations(employees):
    employee_combinations = []
    for i in range(1, len(employees)+1):
        employee_combinations.extend(set(list(combinations(employees, i))))

    return employee_combinations


def is_skill_set_covered(skill_set, employees, skill_mapper):
    employee_rows = skill_mapper[[employee_to_index(e) for e in employees], :]
    skill_intersection = np.sum(employee_rows[:, [skill_to_int(s) for s in skill_set]], axis=0)

    if np.all(skill_intersection >= 1):
        return True
    else:
        return False

