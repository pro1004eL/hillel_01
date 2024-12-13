from sqlalchemy import create_engine, Column, Integer, String, func, update, delete, select
from sqlalchemy.ext.declarative import declarative_base
from all_lessons.lesson_22.db_sqlalhemy.tables.course_table import Course, Base
from all_lessons.lesson_22.db_sqlalhemy.tables.student_table import Student
from sqlalchemy.orm import sessionmaker
from faker import Faker
from random import choice, randint



PG_URL = "postgresql://anton:anton@localhost:5432/orm_db"

local_faker = Faker()

engine = create_engine(PG_URL)


Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)




