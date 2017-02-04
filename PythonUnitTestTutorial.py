class PythonUnitTestTutorial:

  def squareroot(self,x):

      return x*x

  def sum(self,a,b):

      return a+b


if __name__ == "__main__":
   pytest = PythonUnitTestTutorial()
   print pytest.squareroot(4)
   print pytest.sum(2,3)
