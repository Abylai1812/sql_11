from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

postgres_database = "postgresql://postgres:Ashkon.30102002@localhost:5432/lms"
engine = create_engine(postgres_database)

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    students = relationship("Student", back_populates="course")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="students")

Base.metadata.create_all(bind=engine)

session = Session(engine)

python_course = Course(name="Python")
java_course = Course(name="Java")

student_1 = Student(name="Abilkaiyr", course=python_course)
student_2 = Student(name="Altynai", course=java_course)

session.add_all([python_course, java_course, student_1, student_2])
session.commit()