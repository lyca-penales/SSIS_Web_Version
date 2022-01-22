import pymysql

from extensions import db

#----------For Students----------#
def all_students():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
                SELECT s.Student_Id, s.Photo_Link, s.Firstname, s.Lastname, s.Gender, s.Year_Level, s.Course_Code
                FROM student s
                JOIN courses c ON s.Course_Code = c.Course_Code
                ORDER BY s.Student_Id DESC
                """)
    all_students = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_students

def get_student_id(Student_Id):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Student_Id = %s', (Student_Id))
    get_student_id = cursor.fetchall()
    cursor.close()
    conn.close()
    return get_student_id

def select_student_id(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Student_Id = %s', (u_input))
    select_student_id = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_student_id

def select_firstname(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Firstname = %s', (u_input))
    select_firstname = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_firstname

def select_lastname(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Lastname = %s', (u_input))
    select_lastname = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_lastname

def select_gender(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Gender = %s', (u_input))
    select_gender = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_gender

def select_year_level(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Year_Level = %s', (u_input))
    select_year_level = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_year_level

def select_Scourse_code(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM student WHERE Course_Code = %s', (u_input))
    select_Scourse_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_Scourse_code

def select_student_all(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('''SELECT * FROM student 
                        WHERE  Student_Id = %s OR 
                               Firstname = %s OR
                               Lastname = %s OR
                               Gender = %s OR
                               Year_Level = %s OR  
                               Course_Code = %s''', (u_input, u_input, u_input, u_input, u_input, u_input))
    select_student_all = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_student_all

#----------For Courses----------#
def all_courses():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
                SELECT a.Course_Code, a.Course_Name, a.College_Code
                FROM courses a
                JOIN college c ON a.College_Code = c.College_Code
                ORDER BY a.Course_Code DESC 
                """)
    all_courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_courses

def get_course_code(Course_Code):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM courses WHERE Course_Code = %s', (Course_Code))
    get_course_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return get_course_code

def select_course_code(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM courses WHERE Course_Code = %s', (u_input))
    select_course_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_course_code

def select_course_name(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM courses WHERE Course_Name = %s', (u_input))
    select_course_name = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_course_name

def select_Ccollege_code(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM courses WHERE College_Code = %s', (u_input))
    select_Ccollege_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_Ccollege_code

def select_course_all(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM courses WHERE Course_Code = %s OR Course_Name = %s OR  College_Code = %s', (u_input, u_input, u_input))
    select_course_all = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_course_all

#----------For Colleges----------#
def all_colleges():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM college')
    all_colleges = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_colleges

def all_college_code():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT College_Code FROM college')
    all_college_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_college_code

def get_college_code(College_Code):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM college WHERE College_Code = %s', (College_Code))
    get_college_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return get_college_code

def select_college_code(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM college WHERE College_Code = %s', (u_input))
    select_college_code = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_college_code

def select_college_name(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM college WHERE College_Name = %s', (u_input))
    select_college_name = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_college_name

def select_college_all(u_input):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM college WHERE College_Code = %s OR College_Name = %s', (u_input, u_input))
    select_college_all = cursor.fetchall()
    cursor.close()
    conn.close()
    return select_college_all
