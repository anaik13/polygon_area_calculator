import unittest2
# import polygon_area_calculator.app
# import app
import app
import prepare_data.square.gen_randint


class TestApp(unittest2.TestCase):
    square1 = app.Square(3)

    def test_generate_data_square(self):
        self.assertGreaterEqual(prepare_data.square.gen_randint.generate_data_1(), 1)
        self.assertLessEqual(prepare_data.square.gen_randint.generate_data_1(), 10)

    def test_area(self):
        self.assertEqual(self.square1.calculate_area(), 9)
        # self.assertEqual(self.square1.print_perimeter(), 12)


if __name__ == '__main__':
    unittest2.main()
