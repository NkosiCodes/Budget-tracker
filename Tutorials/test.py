from calculator import choice
import calculator as cl
import unittest

class TestChoice(unittest.TestCase):

    # def test_choice(self):
    #     self.assertEqual(choice, 1)
    #     self.assertEqual(choice, 2)
    #     self.assertEqual(choice, 3)
    #     self.assertEqual(choice, 4)

    def test_num(self):
        self.assertEqual(False, "-" in str(cl.num_1))
        self.assertEqual(False, "-" in str(cl.num_2))

if __name__ == "__main__":
    unittest.main()
