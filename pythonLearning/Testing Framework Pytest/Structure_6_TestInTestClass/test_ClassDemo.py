# pip3 install pytest-html
# pytest -v -s test_ClassDemo.py --browser chrome --html=htmlReport.html
import pytest
from Structure_6_TestInTestClass.class_to_test import Class_to_test


# We can pass the names of fixture inside usefixture function to use to fixture
@pytest.mark.usefixtures("moduleSetUp")

class TestDemo():

    # because of autouse keyword we don't need to pass (classSet)  fixture to test method
    @pytest.fixture(autouse = True)
    def classSet(self):
        self.abc = Class_to_test(self.num)

    def test_methodA(self):
        result = self.abc.sumNumbers(2, 8)
        assert result == 20
        print("running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running methodB")



