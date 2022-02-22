from employee_selector import EmployeeSelector
import unittest


class SelectorTestCase(unittest.TestCase):
    selector = None

    @classmethod
    def setUpClass(cls):
        cls.selector = EmployeeSelector()

    def test_get_ideal_groups(self):
        required_skills = ['l', 'q', 's']
        expected_ideal_groups = [['C', 'E'], ['C', 'H'], ['D', 'E'], ['D', 'F'], ['D', 'H']]

        ideal_groups = self.selector.get_ideal_groups(required_skills)

        self.assertEqual(ideal_groups, expected_ideal_groups)

    def test_wrong_input_skill(self):
        required_skills = ['l', 'A', 's']
        self.assertRaises(ValueError, lambda: self.selector.get_ideal_groups(required_skills))


if __name__ == '__main__':
    unittest.main()
