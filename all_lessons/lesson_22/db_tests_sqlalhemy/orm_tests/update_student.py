from sql_alchemy_connection import session, Student



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

update_student(student_id=13, new_name="Steave Guttenberg", new_age=29)



