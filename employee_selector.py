from itertools import combinations
import numpy as np
from utils import employee_to_index, index_to_employee, skill_to_int


class EmployeeSelector:
    """
    A class representing the employee-skill matrix in a numerical format as well as including methods that are
    part of the employee group selection algorithm
    """
    skill_matrix = None

    def __init__(self, skill_mapper_file_path='data/skill_matrix.csv'):
        """
        Initializes an instance of an EmployeeSelector class
        :skill_mapper_file_path: the file path to the employee-skill matrix
        """

        # hardcoding these values as this is now the expected format
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

    def get_employees_by_skill(self, skill):
        """
        Collects employees that have the given skill
        :param skill: a skill (a-z)
        :returns: a list of employees
        """
        skill_idx = skill_to_int(skill)
        intersection_array = self.skill_matrix[:, skill_idx]

        employees = []
        for i, num in enumerate(intersection_array):
            if num == 1:
                employees.append(index_to_employee(i))

        return employees

    def get_employees_by_skill_set(self, skill_set):
        """
        Collects employees that have at least one of the given skills
        :param skill_set: a list or set of skills (a-z)
        :returns: a sorted set of employees
        """
        # using a set to prevent redundancy
        employees = set()
        for skill in skill_set:
            employees.update(self.get_employees_by_skill(skill))

        return sorted(employees)

    @classmethod
    def generate_employee_group_combinations(cls, employees):
        """
        Returns a list of tuples containing group combinations
        :param employees: a (non-redundant) list or set of employees (A-H)
        :returns: a list of all the possible group combinations of the given employees with the following characteristics:
        1. an employee is either part or not part of a group
        2. there is at least one person in each group
        3. the employees' order does not matter
        """
        employee_combinations = []
        for i in range(1, len(employees) + 1):
            employee_combinations.extend(list(combinations(employees, i)))

        return employee_combinations

    def is_skill_set_covered(self, skill_set, employees):
        """
        Checks if the given employees cover the given skills in terms of knowledge
        :param skill_set: a list or set of skills (a-z)
        :param employees: a list or set of employees (A-H)
        :returns: true or false based on whether the skills are covered
        """
        employee_rows = self.skill_matrix[[employee_to_index(e) for e in employees], :]
        skill_intersection = np.sum(employee_rows[:, [skill_to_int(s) for s in skill_set]], axis=0)

        return np.all(skill_intersection >= 1)

    @classmethod
    def reduce_redundancy(cls, employee_groups):
        """
        Returns a list or set of employee groups without keeping ones where someone's skills are covered
        by the others already
        :param employee_groups: a list or set of groups consisting of employees (A-H)
        :returns: a sorted list of employee groups without redundant skilled employees
        """
        for i in range(0, len(employee_groups)):
            for k in range(1, len(employee_groups) - i):
                if set(employee_groups[i]).issubset(set(employee_groups[i + k])):
                    # erase the group that is a subset of another existing one
                    employee_groups[i + k] = [-1]

        # filter out erased groups
        nonredundant_groups = list(filter(lambda x: x != [-1], employee_groups))

        return sorted(nonredundant_groups)

    def get_ideal_groups(self, required_skills):
        """
        Returns the ideal project groups required by the company
        :param required_skills: a list or set of skills (a-z)
        :returns: a list of non-redundant employee groups that cover the required skills
        """
        # get all the employees that have at least one of the required skills
        skilled_employees = self.get_employees_by_skill_set(required_skills)

        # generate all the possible group combinations out of the selected employees
        employee_groups = self.generate_employee_group_combinations(skilled_employees)

        skilled_groups = []

        # only keep groups from the generated ones that actually cover the skills
        for group in employee_groups:
            if self.is_skill_set_covered(required_skills, group):
                skilled_groups.append(list(group))

        # get rid of redundant groups as the last step
        final_employee_groups = self.reduce_redundancy(skilled_groups)

        return final_employee_groups
