from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from all_lessons.lesson_22.db_sqlalhemy.tables.student_courses_relation_table import student_courses


Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)

    # Relationship to students
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __str__(self):
        return f'Course(title={self.title})'