import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
   def test_add(self):
      self.assertEqual(add(2, 3), 5)
      self.assertEqual(add(-1, 1), 0)
      self.assertEqual(add(-1, -1), -2) 
   def test_subtract(self):
      self.assertEqual(subtract(5, 3), 2)
      self.assertEqual(subtract(5, 6), -1)
      self.assertEqual(subtract(-1, 1), -2)
   def test_divide(self):
      self.assertEqual(divide(6, 3), 2)
      self.assertEqual(divide(16, -2), -8)
      self.assertEqual(divide(3, 0), 0)
if __name__ == '__main__':
   unittest.main()
