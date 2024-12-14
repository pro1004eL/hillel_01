from sql_alchemy_connection import session
from all_lessons.lesson_22.db_sqlalhemy.tables.course_students_tables import Student, Course
from random import choice, randint
from faker import Faker


local_faker = Faker()


def add_new_student(name, age, course_ids=None):

    student = Student(name=name, age=age)

    if course_ids:
        selected_courses = session.query(Course).filter(Course.id.in_(course_ids)).all()

        if not selected_courses:
            print('No matching courses found for the provided IDs.')
            return
        student.courses = selected_courses  # Assign selected courses

    session.add(student)

    session.commit()

    print(f'Student {student.name} created successfully with courses: {[course.title for course in student.courses]}')

add_new_student('Eric Lassard', 33, course_ids=[1, 3, 6])


# Create 20 random students and randomly assign courses[1-3]
def add_new_students(num):

    courses = session.query(Course).all()

    for k in range(num):
        student = Student(
            name=local_faker.name(),
            age=local_faker.random_int(16, 43)
        )

        # Randomly assign 1-3 courses to each student
        student.courses = [choice(courses) for _ in range(randint(1, 3))]

        session.add(student)

    session.commit()
    print('Students created successfully!')

add_new_students(6)