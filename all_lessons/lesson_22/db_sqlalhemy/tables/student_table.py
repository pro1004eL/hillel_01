from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from all_lessons.lesson_22.db_sqlalhemy.tables.student_courses_relation_table import student_courses


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer)

    # Relationship to courses
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def __str__(self):
        return f'Student(id={self.id}, name={self.name}, age={self.age})'



