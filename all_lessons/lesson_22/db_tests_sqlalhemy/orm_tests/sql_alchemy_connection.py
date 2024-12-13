
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from all_lessons.lesson_22.db_sqlalhemy.tables.course_table import Course
from all_lessons.lesson_22.db_sqlalhemy.tables.student_table import Student



PG_URL = "postgresql://anton:anton@localhost:5432/orm_db"


engine = create_engine(PG_URL)

Base = declarative_base()

# table with student_courses relations
student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()





Base.metadata.create_all(engine)

