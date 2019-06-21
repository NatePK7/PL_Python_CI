import unittest
import app

class Mytest(unittest.TestCase):
	def test_my_function(self):
		self.assertEqual(app.my_function(1,1), 2)
		self.assertEqual(app.my_function(1,-1), 0)
		self.assertEqual(app.my_function(-1,-1), -2)
		self.assertEqual(app.my_function(1.1,1), 2.1)

if __name__ == '__main__':
	unittest.main()
