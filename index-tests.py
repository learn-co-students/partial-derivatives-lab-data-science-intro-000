import unittest
from ipynb.fs.full.index import (three_x_y_at_one, three_x_y_at_three, three_x_y_at_six,
 three_x_y_at_nine, y_values_for_at_one, y_values_for_at_three, y_values_for_at_six, y_values_for_at_nine,
 df_dx_when_y_equals_one, df_dx_when_y_equals_three, df_dx_when_y_equals_six, df_dx_when_y_equals_nine,
 df_dx_3xy)

class DerivativeRules(unittest.TestCase):
    def test_three_x_y_at_one(self):
        self.assertEqual(three_x_y_at_one(3), 9)

    def test_three_x_y_at_three(self):
        self.assertEqual(three_x_y_at_three(3), 27)

    def test_three_x_y_at_six(self):
        self.assertEqual(three_x_y_at_six(1), 18)

    def test_three_x_y_at_nine(self):
        self.assertEqual(three_x_y_at_nine(2), 54)

    def test_y_values_for_at_one(self):
        zero_to_ten = list(range(0, 11))
        zero_to_four = list(range(0, 5))
        self.assertEqual(y_values_for_at_one(zero_to_ten), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_y_values_for_at_three(self):
        zero_to_ten = list(range(0, 11))
        zero_to_four = list(range(0, 5))
        self.assertEqual(y_values_for_at_three(zero_to_four), [0, 9, 18, 27, 36])
        self.assertEqual(y_values_for_at_three(zero_to_ten), [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90])

    def test_y_values_for_at_six(self):
        zero_to_ten = list(range(0, 11))
        zero_to_four = list(range(0, 5))
        self.assertEqual(y_values_for_at_six(zero_to_four), [0, 18, 36, 54, 72])
        self.assertEqual(y_values_for_at_six(zero_to_ten), [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180])

    def test_y_values_for_at_nine(self):
        zero_to_ten = list(range(0, 11))
        zero_to_four = list(range(0, 5))
        self.assertEqual(y_values_for_at_nine(zero_to_four), [0, 27, 54, 81, 108])
        self.assertEqual(y_values_for_at_nine(zero_to_ten), [0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270])

    def test_df_dx_when_y_equals_one(self):
        self.assertEqual(df_dx_when_y_equals_one(), 3)

    def test_df_dx_when_y_equals_three(self):
        self.assertEqual(df_dx_when_y_equals_three(), 9)

    def test_df_dx_when_y_equals_six(self):
        self.assertEqual(df_dx_when_y_equals_six(), 18)

    def test_df_dx_when_y_equals_nine(self):
        self.assertEqual(df_dx_when_y_equals_nine(), 27)

    def test_df_dx_3xy(self):
        self.assertEqual(df_dx_3xy(2, 1), 3)
        self.assertEqual(df_dx_3xy(2, 2), 6)
        self.assertEqual(df_dx_3xy(5, 2), 6)
