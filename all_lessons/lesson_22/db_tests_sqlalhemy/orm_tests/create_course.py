
from sql_alchemy_connection import session
from all_lessons.lesson_22.db_sqlalhemy.tables.course_students_tables import Course


def create_courses():

    existing_courses = session.query(Course).all()

    if not existing_courses:
        courses = [
            Course(title='Python'),
            Course(title='Java Script'),
            Course(title='Java'),
            Course(title='C++'),
            Course(title='Stalker')
        ]

        session.add_all(courses)
        session.commit()

        print('Courses added to the database.')
    else:
        print('Courses already exist in the database.')

#create_courses()


def add_new_course(title):

    existing_course = session.query(Course).filter_by(title=title).first() # Check if a course with the same title already exists

    if existing_course:
        print(f"The course '{title}' already exists.")
        return

    new_course = Course(title=title)

    session.add(new_course)
    session.commit()

    print(f"Course '{title}' added successfully.")

add_new_course('Charles')
