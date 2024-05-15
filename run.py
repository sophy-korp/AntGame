from GameField import GameField
from task import Optimizer
import json

FIELD_FILENAME = "field.csv"


def main():
    field = GameField()
    field.fill(FIELD_FILENAME)
    best_chromosome = Optimizer.optimize(field)
    result = field.testAnt(best_chromosome)
    max_answer = field.get_max_answer()
    print(f"Your result is {result}")
    print(f"Max is {max_answer}")
    grade = 0
    percent = result * 100 / max_answer

    if percent >= 90:
        grade = 5
    elif percent >= 85:
        grade = 4
    elif percent >= 80:
        grade = 3
    elif percent >= 65:
        grade = 2
    elif percent >= 55:
        grade = 1

    # if 50 <= result < 60:
    #     grade = 1
    # elif 80 > result >= 60:
    #     grade = 2
    # elif 82 > result >= 80:
    #     grade = 3
    # elif 84 > result >= 82:
    #     grade = 4
    # elif result >= 84:
    #     grade = 5

    with open('grade.json') as fp:
        dictObj = json.load(fp)

    with open('grade.json', 'r+') as file:
        dictObj['grade'].append(grade)
        file.write(json.dumps(dictObj))
        file.close()


if __name__ == "__main__":
    main()
