from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
app.secret_key = "Web-SSIS"

mysql = MySQL()

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'ssis_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cur = conn.cursor(pymysql.cursors.DictCursor)

@app.route('/ssis_home')
def ssis_home():
    return render_template('ssis_home.html')

#----------STUDENT----------#
@app.route('/students')
def students():
    cur.execute("""
                SELECT s.Student_Id, s.Firstname, s.Lastname, s.Gender, s.Year_Level, s.Course_Code
                FROM student s
                JOIN courses c ON s.Course_Code = c.Course_Code
                ORDER BY s.Student_Id DESC
                """)
    data = cur.fetchall()
    #cur.close()
    return render_template('students.html', student = data)

@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        Student_Id = request.form['Student_Id']
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        Gender = request.form['Gender']
        Year_Level = request.form['Year_Level']
        Course_Code = request.form['Course_Code']
        cur.execute('''INSERT INTO student
                    VALUES (%s, %s, %s, %s, %s, %s)''', (Student_Id, Firstname, Lastname, Gender, Year_Level, Course_Code))
        conn.commit()
        flash('Student Added Successfully')
        return redirect(url_for('students'))

#----------COURSE----------#
@app.route('/courses')
def courses():
    cur.execute("""
                SELECT a.Course_Code, a.Course_Name, a.College_Code, c.College_Name
                FROM courses a
                JOIN college c ON a.College_Code = c.College_Code
                ORDER BY a.Course_Code DESC 
                """)
    data = cur.fetchall()
    return render_template('courses.html', courses = data)

@app.route('/add_course', methods=['POST'])
def add_course():
    if request.method == 'POST':
        Course_Code = request.form['Course_Code']
        Course_Name = request.form['Course_Name']
        College_Code = request.form['College_Code']
        cur.execute('''INSERT INTO courses 
                    VALUES (%s, %s, %s)''', (Course_Code, Course_Name, College_Code))
        conn.commit()
        flash('Course Added Successfully')
        return redirect(url_for('courses'))

#----------COLLEGE----------#
@app.route('/colleges')
def colleges():
    cur.execute('SELECT * FROM college')
    data = cur.fetchall()
    #cur.close()
    return render_template('colleges.html', college = data)

@app.route('/add_college', methods=['POST'])
def add_college():
    if request.method == 'POST':
        College_Code = request.form['college_code']
        College_Name = request.form['college_name']
        cur.execute('''INSERT INTO college VALUES (%s, %s)''', (College_Code, College_Name))
        conn.commit()
        flash('College Added Successfully')
        return redirect(url_for('colleges'))

#starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)