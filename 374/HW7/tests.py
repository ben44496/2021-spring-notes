import numpy as np
import pandas as pd
import json

class Test():
    def __init__(self, test, ans, arr):
        self.test = test
        self.ans = ans
        self.arr = np.array(arr)

    def print(self):
        print("Name:", self.test)
        print("Ans:", self.ans)
        print("Arr:", self.arr)


def load_tests(file_path="snails_test.json"):
    tests = []
    with open(file_path, 'r') as file:
        data = json.load(file)['tests']
    for k in data:
        tests.append(Test(**k))
    return tests

def test(func, tests):
    failed_tests = []
    for t in tests:
        actual = func(t.arr)
        expected = t.ans
        if t.ans != actual:
            failed_tests.append((t.test, expected, actual))
    return failed_tests


if __name__ == '__main__':
    # tl = Test_Loader()
    # data = tl.load_tests()
    data = load_tests()
    print(data[-1].arr)