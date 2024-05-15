from GameField import GameField
from task import Optimizer
import json
import time

FIELD_FILENAME = "field.csv"


def main():
    field = GameField()
    field.fill(FIELD_FILENAME)
    TIMEOUT_SECONDS = 100

    try:
        start_time = time.time()
        best_chromosome = Optimizer.optimize(field)
        result = field.testAnt(best_chromosome)
        print(f"Your result is {result}")
        print("Max is 89")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        # if elapsed_time > TIMEOUT_SECONDS:
        #     raise Exception("Test exceeded time limit.")
        max_answer = field.get_max_answer()
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

    except Exception as e:
        print(f"Error during optimization: {e}")
        grade = str(e)

    with open("grade.json", "w") as jsonFile:
        data = {'grade': grade}
        json.dump(data, jsonFile)


if __name__ == "__main__":
    main()
