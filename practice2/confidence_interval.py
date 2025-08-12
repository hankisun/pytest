from typing import List

def ci95(samples: List[int]):
    n = len(samples)
    my_sum = sum(samples)
    squared_sum = sum([i**2 for i in samples])
    mean = my_sum / n
    mean_square = mean ** 2
    mean_squared_sum = squared_sum / n
    # var = E(X^2) - E(X)^2
    var = mean_squared_sum - mean_square
    std = var ** 0.5

    ci_min = mean - (1.96 * std / (n**0.5))
    ci_max = mean + (1.96 * std / (n**0.5))

    return ci_min, ci_max
    # return 1.7603871572139953, 4.239612842786005