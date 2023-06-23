import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name_and_Student_Id(student_id):
    try:
      connection = get_connection()
      cursor = connection.cursor()
      query = "SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Student_Id = ?"
      cursor.execute(query,(student_id,))
      record = cursor.fetchall()
      close_connection(connection)
      for row in record:
       print ("ID Студента:", row[3])
       print ("Имя Студента:", row[4])
       print ("ID школы:", row[0])
       print ("Название школы:", row[1])
    except sqlite3.Error as error:
        print ('Ошибка в получении данных ', error)


get_school_name_and_Student_Id(204)