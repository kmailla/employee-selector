from employee_selector import EmployeeSelector, get_ideal_groups
import unittest


class SelectorTestCase(unittest.TestCase):
    def test_get_ideal_groups(self):
        required_skills = ['l', 'q', 's']
        expected_ideal_groups = [['C', 'E'], ['C', 'H'], ['D', 'E'], ['D', 'F'], ['D', 'H']]

        selector = EmployeeSelector()
        ideal_groups = get_ideal_groups(required_skills, selector)

        self.assertEqual(ideal_groups, expected_ideal_groups)


if __name__ == '__main__':
    unittest.main()
