from unittest import TestCase

from solver import add, square_equation_solver

class TestAddCase(TestCase):
    def test_ok(self):
        res = add(1, 2)
        self.assertEqual(res, 3)


class TestSquareEduationSolver(TestCase):
    def test_raises_type_errar(self):
        with self.assertRaises(TypeError):
            square_equation_solver("", 1, 1.5)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 0)
        self.assertIsInstance(res, tuple)

    def test_no_results(self):
        res = square_equation_solver(0, 0, 1)
        self.assertEqual(res, (None, None))

