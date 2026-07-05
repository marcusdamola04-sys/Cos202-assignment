# PERSONAL POCKET CGPA CALCULATOR

print("""
========== PERSONAL POCKET CGPA CALCULATOR ==========
""")

name = input("Enter Your Name: ")
matric = input("Enter Your Matric Number: ")

semester_count = int(input("Enter the Number of Semesters: "))

all_courses = []
semester_gpas = []
semester_units = []
semester_points = []

semester = 1

while semester <= semester_count:
    print(f"\n---------- SEMESTER {semester} ----------")

    num_courses = int(input("Enter Number of Courses: "))

    courses = []

    total_units = 0
    total_quality_points = 0

    course = 1

    while course <= num_courses:
        print(f"\nCourse {course}")

        code = input("Course Code: ")
        score = int(input("Course Score: "))
        unit = int(input("Course Unit: "))

        if score >= 70:
            grade = "A"
            point = 5
        elif score >= 60:
            grade = "B"
            point = 4
        elif score >= 50:
            grade = "C"
            point = 3
        elif score >= 45:
            grade = "D"
            point = 2
        elif score >= 40:
            grade = "E"
            point = 1
        else:
            grade = "F"
            point = 0

        quality_point = point * unit

        total_units += unit
        total_quality_points += quality_point

        course_info = {
            "code": code,
            "score": score,
            "unit": unit,
            "grade": grade,
            "point": point
        }

        courses.append(course_info)

        course += 1

    gpa = round(total_quality_points / total_units, 2)

    all_courses.append(courses)
    semester_gpas.append(gpa)
    semester_units.append(total_units)
    semester_points.append(total_quality_points)

    semester += 1

print("\n=========================================")
print("STUDENT RESULT")
print("=========================================")

print(f"Name: {name}")
print(f"Matric Number: {matric}")

i = 0

while i < len(all_courses):

    print(f"\nSEMESTER {i + 1}")

    j = 0

    while j < len(all_courses[i]):
        print(
            f"{all_courses[i][j]['code']}\t"
            f"Score: {all_courses[i][j]['score']}\t"
            f"Unit: {all_courses[i][j]['unit']}\t"
            f"Grade: {all_courses[i][j]['grade']}"
        )
        j += 1

    print(f"Total Units: {semester_units[i]}")
    print(f"GPA: {semester_gpas[i]}")

    i += 1

total_units = 0
total_quality_points = 0

i = 0

while i < len(semester_units):
    total_units += semester_units[i]
    total_quality_points += semester_points[i]
    i += 1

cgpa = round(total_quality_points / total_units, 2)

print("\n=========================================")
print(f"FINAL CGPA = {cgpa}")
print("=========================================")