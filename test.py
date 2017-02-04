import unittest
from PythonUnitTestTutorial import PythonUnitTestTutorial

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

    def testsquareroot(self):
        pytest = PythonUnitTestTutorial()
        self.assertEqual(pytest.squareroot(3),9)

    def testsum(self):
       pytest = PythonUnitTestTutorial()
       self.assertEqual(pytest.sum(3,4),7)

if __name__ == '__main__':
    unittest.main()
