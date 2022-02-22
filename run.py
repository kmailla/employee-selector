from argparse import ArgumentParser
from employee_selector import EmployeeSelector, get_ideal_groups


def list_groups(groups):
    print(''.join([' '.join(group)+'\n' for group in groups]))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('skills', nargs='*', type=str, help='skill are symbolized by characters between a-z')

    args = parser.parse_args()

    # read the given skills from the command line
    required_skills = args.skills

    selector = EmployeeSelector()
    ideal_groups = get_ideal_groups(required_skills, selector)
    list_groups(ideal_groups)
