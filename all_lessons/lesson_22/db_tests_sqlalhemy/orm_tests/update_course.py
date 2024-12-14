from sql_alchemy_connection import session, Course



def update_course(course_id, new_title):

    course = session.query(Course).filter_by(id=course_id).first()

    if course:
        course.title = new_title

        session.commit()

        print(f'Updated course: {course}')
    else:
        print(f'Course with id: {course_id} not found')

update_course(course_id=6, new_title='DBeaver')


