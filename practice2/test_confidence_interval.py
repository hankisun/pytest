"""
신뢰수준 90 95 99
z-score     1.96 2.57

samples = [1,2,3,4,5]
E(X) = 3
E(X^2) = 55/5 = 11
E(X)^2 = 9
std = root(var)
var = E(X^2) - E(X)^2 = 11 - 9 = 2
std = root(2) = 1.414
n = 5

mean +- z-score * std / root(n)
ci_max, ci_min
"""
import confidence_interval as ci

def test_ci95():
    # given (preparing)
    samples = [1,2,3,4,5]
    mean = 3
    std = 2 ** 0.5
    n = len(samples)

    expected_ci_min = mean - (1.96 * (std / (n**0.5)))
    expected_ci_max = mean + (1.96 * (std / (n**0.5)))

    # when
    actual_ci_min, actual_ci_max = ci.ci95(samples)

    # then
    assert expected_ci_min == actual_ci_min
    assert expected_ci_max == actual_ci_max

