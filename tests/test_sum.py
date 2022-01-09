from py_sonarcloud.sum import sum


def test_sum():
    assert sum(5, 10) == 15
