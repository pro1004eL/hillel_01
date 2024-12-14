from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

# Basic class
Base = declarative_base()


# Many-to-Many association table
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer)

    # Relationship to courses
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def __str__(self):
        return f'Student(id={self.id}, name={self.name}, age={self.age})'



class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)

    # Relationship to students
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __str__(self):
        return f'Course(title={self.title})'