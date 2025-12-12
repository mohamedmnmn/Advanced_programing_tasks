import pymysql
conn = pymysql.connect(host='localhost', user='root', password='', database='school')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INT, name VARCHAR(100), grade FLOAT)')
cursor.executemany('REPLACE INTO students VALUES (%s, %s, %s)', [(1, 'Ali', 85.5), (2, 'Sara', 92.0), (3, 'Mohamed', 78.3)])
conn.commit()
for row in cursor.execute('SELECT * FROM students'):
    print(row)
conn.close()
# ------------------------------------
conn = pymysql.connect(host='localhost',user='root',password='',database='school')
cursor = conn.cursor()
name = input("Enter name: ")
grade = float(input("Enter grade: "))
cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", (name, grade))
conn.commit()
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
# --------------------------------------
conn = pymysql.connect(host='localhost', user='root', password='your_password', database='school')
cursor = conn.cursor()
try:
    conn.begin() 
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", ('Ahmed', 90.0))
    cursor.execute("INSERT INTO students (name, grade) VALUES (%s, %s)", ('Nour', 95.5))
    x = 10 / 0
    conn.commit()
except:
    conn.rollback()
    print("Error! Changes undone.")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)
conn.close()
# -------------------------------------
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    def __repr__(self): return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"
engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
session.add_all([Book(title='Python Basics', author='Guido'), Book(title='AI with Python', author='Mohamed')])
session.commit()
for book in session.query(Book).all():
    print(book)
session.close()