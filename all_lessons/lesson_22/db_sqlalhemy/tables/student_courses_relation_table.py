# from sqlalchemy import Column, Integer, String, ForeignKey, Table
# from sqlalchemy.orm import relationship, declarative_base
#
# # Basic class
# Base = declarative_base()
#
#
# # Many-to-Many association table
# student_courses = Table(
#     'student_courses', Base.metadata,
#     Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
#     Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
# )
#
