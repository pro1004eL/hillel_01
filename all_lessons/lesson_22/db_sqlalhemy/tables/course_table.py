from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from all_lessons.lesson_22.db_sqlalhemy.tables.student_courses_relation_table import student_courses

# Basic class
Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)

    # Relationship to students
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __str__(self):
        return f'Course(title={self.title})'