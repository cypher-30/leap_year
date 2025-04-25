import math

def show_history() -> None:
    print("\n == Brief History of Python == ")
    print("\n == Created in 1991 == ")
    print("\n == Python 3 released in 2008 == ")
    print("\n Program that computes average scores of students.")

def prompt_names_and_scores() -> tuple[list[str], list[float]]:
    while True:

        try:
            count = int(input("Input the number of students to grade: "))

            if count <= 0:
                print("Input a number greater than zero.")
                continue
            break

        except ValueError:

            print("Invalid input. Please enter a whole number.")

    names = []

    scores = []

    print("\nEnter student names and their scores:")

    for i in range(count):

        name = input(f"Student {i + 1} name: ").strip()

        if not name:
            name = f"Student{i + 1}"

        names.append(name)

        while True:
            try:
                score = float(input(f"Enter score for {name}: "))

                if 0 <= score <= 100:

                    scores.append(score)

                    break
                else:

                    print("Score must be between 0 and 100.")

            except ValueError:

                print("Invalid input. Please enter a number.")

    return names, scores


def match_grade(score: float) -> str:
    match True:

        case _ if score >= 70:
            return "A"

        case _ if score >= 60:
            return "B"

        case _ if score >= 50:
            return "C"

        case _ if score >= 40:
            return "D"

        case _:
            return "F"


def compute_avg(scores: list[float]) -> float:
    return round(sum(scores) / len(scores), 2)


def generate_results_table(names: list[str], scores: list[float]) -> None:
    print("\n=== Student Results ===")

    print(f"{'Name':<15} {'Score':<10} {'Grade'}")

    print("-" * 30)

    for i in range(len(names)):
        name = names[i]

        score = scores[i]

        grade = match_grade(score)

        print(f"{name:<15} {score:<10.2f} {grade}")

    average_score = compute_avg(scores)

    print("\nClass Average:", average_score)

    print("Rounded Up:", math.ceil(average_score))

    print("Rounded Down:", math.floor(average_score))


def main():
    print("=== Grading System ===")

    course = "Data Structures and Algorithms"

    print(f"Course: {course}")

    while True:

        names, scores = prompt_names_and_scores()

        generate_results_table(names, scores)

        looper = input("\nGrade another class? (input yes/no): ").strip().lower()

        if looper != "yes":
            print("Thankyou for using Python grading system!")

            break


if __name__ == "__main__":
    main()