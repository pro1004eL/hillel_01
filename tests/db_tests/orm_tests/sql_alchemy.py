from sqlalchemy import create_engine, Column, Integer, String, func, update, delete, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.db.orm_lesson.tables.user_table import Student, Course, Base
from faker import Faker
from random import choice, randint
from sqlalchemy.sql import and_

# З'єднання з базою даних PostgreSQL
PG_URL = "postgresql://anton:anton@localhost:5432/orm_db"

local_faker = Faker()

engine = create_engine(PG_URL)


# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def create_courses():

    existing_courses = session.query(Course).all()

    if not existing_courses:
        courses = [
            Course(title='Mathematics'),
            Course(title='English'),
            Course(title='History'),
            Course(title='Philosophy'),
            Course(title='Computer Science')
        ]

        session.add_all(courses)
        session.commit()

        print("Courses added to the database.")
    else:
        print("Courses already exist in the database.")

#create_courses()

# Create 20 random students and randomly assign courses[1-3]
def add_new_students(num):

    courses = session.query(Course).all()

    for k in range(num):
        student = Student(
            name=local_faker.name(),
            age=local_faker.random_int(18, 33)
        )

        # Randomly assign 1-3 courses to each student
        student.courses = [choice(courses) for _ in range(randint(1, 3))]

        session.add(student)

    session.commit()
    print("Students created successfully!")

#add_new_students(2)


# Create one student and assign courses manually
def add_new_student(name, age, course_ids=None):

    student = Student(name=name, age=age)

    if course_ids:
        selected_courses = session.query(Course).filter(Course.id.in_(course_ids)).all()

        if not selected_courses:
            print("No matching courses found for the provided IDs.")
            return
        student.courses = selected_courses  # Assign selected courses

    session.add(student)

    session.commit()

    print(f"Student {student.name} created successfully with courses: {[course.title for course in student.courses]}")

#add_new_student('Tom Cruse', 19, course_ids=[2, 5])



# todo Queries:

# course by id and enrolled students
def course_id_and_their_enrolled_students(course_id=None):

    if course_id:
        course = session.query(Course).filter_by(id=course_id).first()

        if course:
            print(f"Course: {course.title}")

            if course.students:
                for student in course.students:
                    print(f"  - Student: {student.name}, Age: {student.age}")
            else:
                print("  - No students enrolled")
        else:
            print(f"No course found with ID {course_id}.")

#course_and_their_enrolled_students(course_id=2)


# course by title and enrolled students
def course_title_and_their_enrolled_students(course_title=None):

    specific_course = session.query(Course).filter_by(title=course_title).first()

    if specific_course:
        print(f"Students registered for {specific_course.title}:")

        if specific_course.students:

            for student in specific_course.students:
                print(f"  - {student.name}, Age: {student.age}")

        else:
            print("  - No students registered")
    else:
        print("Course not found")

#course_title_and_their_enrolled_students('History')


# all courses and their enrolled students
def all_courses_and_their_enrolled_students():

    courses = session.query(Course).all()

    for course in courses:
        print(f"Course: {course.title}")

        if not course.students:
            print("  - No students enrolled")

        else:
            for student in course.students:
                print(f"  - Student: {student.name}, Age: {student.age}")

#all_courses_and_their_enrolled_students()


# student by id and his enrolled courses
def student_id_and_enrolled_courses(student_id=None):

    if student_id:
        student = session.query(Student).filter_by(id=student_id).first()

        if student:
            print(f"Student: {student.name}")

            if student.courses:
                for course in student.courses:
                    print(f"  - Course: {course.title}")
            else:
                print("  - No courses enrolled")
        else:
            print(f"No student found with ID {student_id}.")

#student_id_and_enrolled_courses(student_id=18)


# student by name and his enrolled courses
def student_name_and_enrolled_courses(student_name=None):

    student_name = session.query(Student).filter_by(name=student_name).first()

    if student_name:
        print(f"Student: {student_name.name}")

        if student_name.courses:

            for course in student_name.courses:
                print(f"  - Course: {course.title}")

        else:
            print("  - Not enrolled in any courses")
    else:
        print(f"Student {student_name} not found")

#student_name_and_enrolled_courses('Margaret')


# List of all students and their enrolled courses
def all_students_and_their_courses():

    students = session.query(Student).all()

    for student in students:
        print(f"Student: {student.name}, Age: {student.age}")

        if student.courses:

            for course in student.courses:
                print(f'  - Course: {course.title}')

        else:
            print('  - Not enrolled in any courses')

#all_students_and_their_courses()


#todo Update and Delete

# Update a student's name and/or age
def update_student(student_id, new_name=None, new_age=None):

    student = session.query(Student).filter_by(id=student_id).first()

    if student:
        if new_name:
            student.name = new_name

        if new_age:
            student.age = new_age

        session.commit()

        print(f'Updated student: {student}')
    else:
        print(f'Student with id: {student_id} not found')

#update_student(student_id=15, new_name="Lara Croft", new_age=26)


# Update a course's title
def update_course(course_id, new_title):

    course = session.query(Course).filter_by(id=course_id).first()

    if course:
        course.title = new_title

        session.commit()

        print(f"Updated course: {course}")
    else:
        print(f'Course with id: {course_id} not found')

#update_course(course_id=4, new_title="Advanced Mathematics")


# delete a student by id
def delete_student(student_id):

    student = session.query(Student).filter_by(id=student_id).first()

    if student:
        session.delete(student)

        session.commit()

        print(f"Student {student} deleted successfully")
    else:
        print(f'Student with id: {student_id} not found')

#delete_student(student_id=35)


# delete students by condition
def delete_students_by_condition(condition):

    students_to_delete = session.query(Student).filter(condition).all()

    if students_to_delete:

        for student in students_to_delete:
            # Remove references in the association table
            student.courses.clear()

        session.query(Student).filter(condition).delete(synchronize_session='fetch')

        session.commit()

        print("All matching students deleted.")
    else:
        print("No students matched the condition.")

#delete_students_by_condition(Student.name == 'Tom Cruse')



# delete a course by id
def delete_course(course_id):

    course = session.query(Course).filter_by(id=course_id).first()

    if course:
        session.delete(course)

        session.commit()

        print(f"Deleted course: {course}")
    else:
        print(f'Course with id: {course_id} not found')

#delete_course(course_id=26)



