import yaml
import pytest_assume
from Business.Calculator import Calculator
import pytest


class TestCal:

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("data/cal01.yaml")))
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["check_add"])
    def check_less(self, a, b, result):
        cal = Calculator()
        assert result == cal.less(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("data/cal.yaml")),
                             ids=['整数', '负数', '浮点数', '正负数'])
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    def check_add(self, a, b, result):
        cal = Calculator()
        assert result == cal.add(a, b)
        # pytest.assume(result == cal.add(a, b))

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("data/cal03.yaml")))
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["check_multiply"])
    def check_div(self, a, b, result):
        cal = Calculator()
        assert result == cal.div(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open("data/cal02.yaml")))
    @pytest.mark.run(order=3)
    @pytest.mark.dependency()
    def check_multiply(self, a, b, result):
        cal = Calculator()
        assert result == cal.multiply(a, b)
