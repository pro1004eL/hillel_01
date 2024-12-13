from sql_alchemy_connection import session, Student


# delete a student by id
def delete_student(student_id):

    student = session.query(Student).filter_by(id=student_id).first()

    if student:
        session.delete(student)

        session.commit()

        print(f'Student {student} deleted successfully')
    else:
        print(f'Student with id: {student_id} not found')

delete_student(student_id=24)


# delete students by condition
def delete_students_by_condition(condition):

    students_to_delete = session.query(Student).filter(condition).all()

    if students_to_delete:

        for student in students_to_delete:
            # Remove references in the association table
            student.courses.clear()

        session.query(Student).filter(condition).delete(synchronize_session='fetch')

        session.commit()

        print('All matching students deleted.')
    else:
        print('No students matched the condition.')

#delete_students_by_condition(Student.age > 40)