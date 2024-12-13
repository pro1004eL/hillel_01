
from sql_alchemy_connection import session, Course


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

        print('Courses added to the database.')
    else:
        print('Courses already exist in the database.')

#create_courses()