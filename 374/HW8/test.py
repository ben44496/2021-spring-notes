import json

class Test():

    def __init__(self, test, map):
        self.test = test
        self.map = map

    def print(self):
        print("Name:", self.test)
        print("Map:", self.map)

def load_tests(file_path="racetrack.json"):
    tests = []
    with open(file_path, 'r') as file:
        data = json.load(file)['tests']
    for k in data:
        tests.append(Test(**k))
    return tests

if __name__ == '__main__':
    data = load_tests()
    print(data[-1].arr)