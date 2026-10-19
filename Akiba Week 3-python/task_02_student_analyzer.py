def validate_score(score):
    return score >= 0 and score <= 100

def validate_students(students):
    for student in students:
        if not validate_score(student["score"]):
            return False

    return True

def calculate_grade(score):
    if not validate_score(score):
        return "Invalid score"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def find_highest(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def find_lowest(scores):
    lowest = scores[0]

    for score in scores:
        if score < lowest:
            lowest = score 
    return lowest


def count_pass(scores):
    passed = 0
    for score in scores:
        if score >= 50:
            passed += 1
    return passed


def count_fail(scores):
    failed = 0
    for score in scores:
        if score < 50:
            failed += 1
    return failed



def get_scores(students):
    scores=[]
    for student in students:
        scores.append(student["score"])

    return scores


def students_above_average(students):
    scores = get_scores(students)
    average = calculate_average(scores)
    above_average = []
    for student in students:
        if student["score"] > average:
            above_average.append(student)

    return above_average


def generate_report(students):
    if not students:
        return "Error: No students provided"

    if not validate_students(students):
        return "Error: Invalid student score"

    scores = get_scores(students)
    average = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)
    passed = count_pass(scores)
    failed = count_fail(scores)
    above_average = students_above_average(students)

    return {
        "scores": scores,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "above_average": above_average
    }

students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

report = generate_report(students)

if isinstance(report, dict):

    print("Student Grades:")

    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        print(f"{name}: Score {score}, Grade {grade}")

    print("\nClass Report:")

    for key, value in report.items():
        if key == "above_average":
            print("Above-average students:")
            for student in value:
                print(f"  {student['name']}: {student['score']}")
        else:
            print(f"{key}: {value}")