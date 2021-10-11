import json


if __name__ == "__main__":


    with open('midterm.json') as f:
        data = json.load(f)

    print(data[0])