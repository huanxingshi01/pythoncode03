import yaml

from Business.Calculator import Calculator
import pytest


class TestCal:
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("C:\\Users\\90619\\PycharmProjects\\pythoncode03"
                                                               "\\testing\\data\\cal.yaml")))
    def test_add(self, a, b, result):
        cal = Calculator()
        assert result == cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("C:\\Users\\90619\\PycharmProjects\\pythoncode03"
                                                                  "\\testing\\data\\cal01.yaml")))
    def test_less(self, a, b, result):
        cal = Calculator()
        assert result == cal.less(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("C:\\Users\\90619\\PycharmProjects\\pythoncode03"
                                                               "\\testing\\data\\cal02.yaml")))
    def test_multiply(self, a, b, result):
        cal = Calculator()
        assert result == cal.multiply(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("C:\\Users\\90619\\PycharmProjects\\pythoncode03"
                                                               "\\testing\\data\\cal03.yaml")))
    def test_div(self, a, b, result):
        cal = Calculator()
        assert result == cal.div(a, b)
