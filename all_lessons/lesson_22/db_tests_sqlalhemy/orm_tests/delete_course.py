from sql_alchemy_connection import session, Course



def delete_course(course_id):

    course = session.query(Course).filter_by(id=course_id).first()

    if course:
        session.delete(course)

        session.commit()

        print(f"Deleted course: {course}")
    else:
        print(f'Course with id: {course_id} not found')

delete_course(course_id=5)