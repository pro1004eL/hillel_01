from sql_alchemy_connection import session, Course



def course_id_and_their_enrolled_students(course_id=None):

    if course_id:
        course = session.query(Course).filter_by(id=course_id).first()

        if course:
            print(f'Course: {course.title}')

            if course.students:

                for student in course.students:
                    print(f' - Student: {student.name}, Age: {student.age}')
            else:
                print(' - No students enrolled')
        else:
            print(f'No course found with ID: {course_id}.')

course_id_and_their_enrolled_students(course_id=2)



def course_title_and_their_enrolled_students(course_title=None):

    specific_course = session.query(Course).filter_by(title=course_title).first()

    if specific_course:
        print(f'Students registered for {specific_course.title}:')

        if specific_course.students:

            for student in specific_course.students:
                print(f' - {student.name}, Age: {student.age}')

        else:
            print(' - No students registered')
    else:
        print('Course not found')

course_title_and_their_enrolled_students('Python')



def all_courses_and_their_enrolled_students():

    courses = session.query(Course).all()

    for course in courses:
        print(f"Course: {course.title}")

        if not course.students:
            print(" - No students enrolled")

        else:
            for student in course.students:
                print(f" - Student: {student.name}, Age: {student.age}")

all_courses_and_their_enrolled_students()


