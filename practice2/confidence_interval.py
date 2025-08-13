from typing import List

def calculate_sum_and_squared_sum(samples: List[int]):
    return sum(samples), sum([i**2 for i in samples])

def _mean(total, n):
    return total / n

def _std(sum, squared_sum, n):
    # var = E(X^2) - E(X)^2
    return (_mean(squared_sum, n) - _mean(sum, n) ** 2) ** 0.5

def _get_ci_point(ci):
    if ci == 95:
        return 1.96
    if ci == 99:
        return 2.57
    raise ValueError(f"Invalid confidence interval {ci}")

def ci_min(mean, std, n, ci):
    return mean - (_get_ci_point(ci) * std / (n**0.5))

def ci_max(mean, std, n, ci):
    return mean + (_get_ci_point(ci) * std / (n**0.5))

def ci95(samples: List[int]):
    n = len(samples)
    sum, squared_sum = calculate_sum_and_squared_sum(samples)
    mean = _mean(sum, n)
    std = _std(sum, squared_sum, n)

    return ci_min(mean, std, n, ci=95), ci_max(mean, std, n, ci=95)

def ci95_round(samples: List[int], round_num:int):
    ci_min, ci_max = ci95(samples)
    return round(ci_min, round_num), round(ci_max, round_num)


def ci99(samples: List[int]):
    n = len(samples)
    sum, squared_sum = calculate_sum_and_squared_sum(samples)
    mean = _mean(sum, n)
    std = _std(sum, squared_sum, n)

    return ci_min(mean, std, n, ci=99), ci_max(mean, std, n, ci=99)
    # return 1.7603871572139953, 4.239612842786005
