from sql_alchemy_connection import session, Student



def student_id_and_enrolled_courses(student_id=None):

    if student_id:
        student = session.query(Student).filter_by(id=student_id).first()

        if student:
            print(f'Student: {student.name}')

            if student.courses:
                for course in student.courses:
                    print(f' - Course: {course.title}')
            else:
                print(' - No courses enrolled')
        else:
            print(f'No student found with ID {student_id}')

student_id_and_enrolled_courses(student_id=1)



def student_name_and_enrolled_courses(student_name=None):

    student_name = session.query(Student).filter_by(name=student_name).first()

    if student_name:
        print(f'Student: {student_name.name}')

        if student_name.courses:

            for course in student_name.courses:
                print(f' - Course: {course.title}')

        else:
            print(' - Not enrolled in any courses')
    else:
        print(f'Student {student_name} not found')

student_name_and_enrolled_courses('Thomas Preston')



def all_students_and_their_courses():

    students = session.query(Student).all()

    for student in students:
        print(f'Student: {student.name}, Age: {student.age}')

        if student.courses:

            for course in student.courses:
                print(f' - Course: {course.title}')

        else:
            print(' - Not enrolled in any courses')

all_students_and_their_courses()