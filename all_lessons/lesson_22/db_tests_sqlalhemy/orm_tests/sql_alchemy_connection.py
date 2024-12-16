from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from all_lessons.lesson_22.db_sqlalhemy.tables.course_students_tables import Course, Student, Base



PG_URL = "postgresql://anton:anton@localhost:5432/orm_db"


engine = create_engine(PG_URL)



Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)





