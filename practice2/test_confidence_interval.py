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
import pytest
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

@pytest.mark.parametrize("samples, expected_min, expected_max", [
    ([1,2,3,4,5], 1.76, 4.24),
    ([6,7,8,9,10], 6.76, 9.24),
    ([11,12,13,14,15], 11.76, 14.24),
    ([1,3,5,7,9,11,13], 4.037, 9.963)
])
def test_ci95_round(samples, expected_min, expected_max):
    # given

    # when
    actual_min, actual_max = ci.ci95_round(samples,3)
    # then
    assert actual_min == expected_min
    assert actual_max == expected_max

def test_ci99():
    # given (preparing)
    samples = [1,2,3,4,5]
    mean = 3
    std = 2 ** 0.5
    n = len(samples)

    expected_ci_min = mean - (2.57 * (std / (n**0.5)))
    expected_ci_max = mean + (2.57 * (std / (n**0.5)))

    # when
    actual_ci_min, actual_ci_max = ci.ci99(samples)

    # then
    assert expected_ci_min == actual_ci_min
    assert expected_ci_max == actual_ci_max
