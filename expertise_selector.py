import numpy as np
import pandas as pd


# expects a-z, returns 0-26
def letter_to_int(letter):
    return ord(letter)-97


# expects 0-7, return A-H
def index_to_employee(idx):
    return chr(int(idx)+65)


# the map to read in has each employee is a new line
def load_skill_mapper(file_path):
    lower_bound = letter_to_int('a')
    upper_bound = letter_to_int('z')

    # the columns will be the employee's names and each expertise
    #expertise_df = pd.DataFrame(columns=['name'] + [str(i) for i in range(lower_bound, upper_bound)])

    with open(file_path, 'r', encoding='utf-8') as f:
        raw_lines = f.read().split('\n')

        # the expertise array is the number of different skills time the number of employees
        skill_array = np.zeros((len(raw_lines), upper_bound-lower_bound+1))
        print(skill_array)

        for i, line in enumerate(raw_lines):
            letters = line.split(',')[1:]
            for char in letters:
                skill_array[i][letter_to_int(char)] = 1

    return skill_array


# expects the skill char
def get_employees_by_skill(skill, skill_mapper):
    employees = []
    skill_idx = letter_to_int(skill)
    intersection_array = skill_mapper[:, skill_idx]

    for i, num in enumerate(intersection_array):
        if num == 1:
            employees.append(index_to_employee(i))

    return employees


def get_employees_by_skill_set(skill_set, skill_mapper):
    employees = set()

    for skill in skill_set:
        employees.update(get_employees_by_skill(skill, skill_mapper))

    return employees


skillmap = load_skill_mapper('expertise_map.csv')

print(get_employees_by_skill_set(['l', 'q', 's'], skillmap))