from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import declarative_base

# Basic class
Base = declarative_base()


# table with student_courses relations
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

