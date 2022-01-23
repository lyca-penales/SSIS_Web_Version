import cloudinary
import cloudinary.uploader

from flask import Blueprint, render_template, redirect, url_for, flash, request

from extensions import db

#from .. forms import *
from .. manage import *

main = Blueprint('main', __name__)

#----------For Students----------#

@main.route('/')
def students():
    data = all_students()
    course_codes = all_course_code()
    return render_template('students.html', student=data, courses=course_codes)

@main.route('/add_student', methods=['POST', 'GET'])
def add_student():
    conn = db.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        Student_Id = request.form['Student_Id']
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        Gender = request.form['Gender']
        Year_Level = request.form['Year_Level']
        Course_Code = request.form['Course_Code']
        if Student_Id == "":
            flash('Error. Student Id must not be empty.')
            return redirect('/')
        elif Firstname == "":
            flash('Error. Firstname must not be empty.')
            return redirect('/')
        elif Lastname == "":
            flash('Error. Lastname must not be empty.')
            return redirect('/')
        elif Gender == "":
            flash('Error. Gender must not be empty.')
            return redirect('/')
        elif Year_Level == "":
            flash('Error. Year_Level must not be empty.')
            return redirect('/')
        elif Course_Code == "":
            flash('Error. Course_Code must not be empty.')
            return redirect('/')
        else:
            try:
                photo = request.files['photo']
                result = cloudinary.uploader.upload(photo)
                url = result.get('url')
                cursor.execute('''INSERT INTO student
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''', (Student_Id, url, Firstname, Lastname, Gender, Year_Level, Course_Code))
                cursor.close()
                conn.commit()
                conn.close()
                flash('Student Added Successfully!')
                return redirect('/')
            except:
                url = 'https://res.cloudinary.com/dccav3ldg/image/upload/v1642721953/SSIS/user-icon-placeholder_lzfbmn.png'
                conn = db.connect()
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO student
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''', (Student_Id, url, Firstname, Lastname, Gender, Year_Level, Course_Code))
                cursor.close()
                conn.commit()
                conn.close()
                flash('Student Added Successfully!')
                return redirect('/')
        
@main.route('/edit/student/<Student_Id>', methods=['POST', 'GET'])
def get_student(Student_Id):
    data = get_student_id(Student_Id)
    course_codes = all_course_code()
    print(data[0])
    return render_template('edit_student.html', student=data[0], courses=course_codes)

@main.route('/update/student/<Student_Id>', methods=['POST'])
def update_student(Student_Id):
    conn = db.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        Gender = request.form['Gender']
        Year_Level = request.form['Year_Level']
        Course_Code = request.form['Course_Code']
        if Firstname == "":
            flash('Error. Firstname must not be empty.')
            return redirect('/')
        elif Lastname == "":
            flash('Error. Lastname must not be empty.')
            return redirect('/')
        elif Gender == "":
            flash('Error. Gender must not be empty.')
            return redirect('/')
        elif Year_Level == "":
            flash('Error. Year Level must not be empty.')
            return redirect('/')
        elif Course_Code == "":
            flash('Error. Course Code must not be empty.')
            return redirect('/')
        else:
            try:
                photo = request.files['photo']
                result = cloudinary.uploader.upload(photo)
                url = result.get('url')
                cursor.execute("""
                            UPDATE student
                            SET Firstname = %s,
                                Photo_Link = %s,
                                Lastname = %s,
                                Gender = %s,
                                Year_Level = %s,
                                Course_Code = %s
                            WHERE Student_Id = %s
                            """, (Firstname, url, Lastname, Gender, Year_Level, Course_Code, Student_Id))
                cursor.close()
                conn.commit()
                conn.close()
                flash('Student Updated Successfully!')
                return redirect('/')
            except:
                conn = db.connect()
                cursor = conn.cursor()
                cursor.execute("""
                            UPDATE student
                            SET Firstname = %s,
                                Lastname = %s,
                                Gender = %s,
                                Year_Level = %s,
                                Course_Code = %s
                            WHERE Student_Id = %s
                            """, (Firstname, Lastname, Gender, Year_Level, Course_Code, Student_Id))
                flash('Student Updated Successfully!')
                cursor.close()
                conn.commit()
                conn.close()
                return redirect('/')

@main.route('/delete/student/<Student_Id>', methods=['POST', 'GET'])
def delete_student(Student_Id):
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM student WHERE Student_Id = %s', (Student_Id))  
    cursor.close()
    conn.commit()
    conn.close()
    flash('Student Removed Successfully!')
    return redirect('/')

@main.route('/student/search', methods=['GET', 'POST'])
def search_student():
    if request.method == 'POST':
        u_input = request.form.get('u_search')
        field = request.form.get('search_select')

        if field == 'student_id':
            data = select_student_id(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        elif field == 'firstname':
            data = select_firstname(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        elif field == 'lastname':
            data = select_lastname(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        elif field == 'gender':
            data = select_gender(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        elif field == 'year_level':
            data = select_year_level(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        elif field == 'course_code':
            data = select_Scourse_code(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')
        else:
            data = select_student_all(u_input)
            for u_input in data:
                return render_template('students.html', student = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/')

#----------For Courses----------#

@main.route('/ssis-courses')
def courses():
    data = all_courses()
    college_codes = all_college_code()
    return render_template('courses.html', courses = data, college = college_codes)

@main.route('/add_course', methods=['POST'])
def add_course():
    conn = db.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        Course_Code = request.form['Course_Code']
        Course_Name = request.form['Course_Name']  
        College_Code = request.form['College_Code']
        if Course_Code == "":
            flash('Error. Course code must not be empty.')
            return redirect('/ssis-courses')
        elif Course_Name == "":
            flash('Error. Course name must not be empty.')
            return redirect('/ssis-courses')
        elif College_Code == "":
            flash('Error. College code must not be empty.')
            return redirect('/ssis-courses')
        else:
            try:
                cursor.execute('''INSERT INTO courses 
                        VALUES (%s, %s, %s)''', (Course_Code, Course_Name, College_Code))
                cursor.close()
                conn.commit()
                conn.close()
                flash('Course Added Successfully!')
                return redirect('/ssis-courses')
            except:
                flash('Error. Course code already exist.')
                return redirect('/ssis-courses')
            
@main.route('/delete/course/<Course_Code>', methods=['POST', 'GET'])
def delete_course(Course_Code):
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM courses WHERE Course_Code = %s', (Course_Code))  
        cursor.close()
        conn.commit()
        conn.close()
        flash('Course Removed Successfully!')
        return redirect('/ssis-courses')
    except:
        flash('Warning. Course information that has enrolled students cannot be deleted')
        return redirect('/ssis-courses')

@main.route('/edit/course/<Course_Code>', methods=['POST', 'GET'])
def get_course(Course_Code):
    college_codes = all_college_code()
    data = get_course_code(Course_Code)
    print(data[0])
    return render_template('edit_course.html', courses=data[0], college=college_codes)

@main.route('/update/course/<Course_Code>', methods=['POST'])
def update_course(Course_Code):
    conn = db.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        Course_Name = request.form['Course_Name']
        College_Code = request.form['College_Code']
        if Course_Name == "":
            flash('Error. Course name must not be empty.')
            return redirect('/ssis-courses')
        elif College_Code == "":
            flash('Error. College code must not be empty.')
            return redirect('/ssis-courses')
        else:
            cursor.execute("""
                        UPDATE courses
                        SET Course_Name = %s,
                            College_Code = %s
                        WHERE Course_Code = %s
                        """, (Course_Name, College_Code, Course_Code))
            flash('Course Updated Successfully!')
            cursor.close()
            conn.commit()
            conn.close()
            return redirect('/ssis-courses')

@main.route('/course/search', methods=['GET', 'POST'])
def search_course():
    if request.method == 'POST':
        u_input = request.form.get('u_search')
        field = request.form.get('search_select')

        if field == 'course_code':
            data = select_course_code(u_input)
            for u_input in data:
                return render_template('courses.html', courses = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-courses')
        elif field == 'course_name':
            data = select_course_name(u_input)
            for u_input in data:
                return render_template('courses.html', courses = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-courses')
        elif field == 'college_code':
            data = select_Ccollege_code(u_input)
            for u_input in data:
                return render_template('courses.html', courses = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-courses')
        else:
            data = select_course_all(u_input)
            for u_input in data:
                return render_template('courses.html', courses = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-courses')

#----------For Colleges----------#

@main.route('/ssis-colleges')
def colleges():
    data = all_colleges()
    return render_template('colleges.html', college = data)

@main.route('/add_college', methods=['POST'])
def add_college():
    conn = db.connect()
    cursor = conn.cursor()
    if request.method == 'POST':
        College_Code = request.form['college_code']
        College_Name = request.form['college_name']
        if College_Code == "":
            flash('Error. College code must not be empty.')
            return redirect('/ssis-colleges')
        elif College_Name == "":
            flash('Error. College name must not be empty.')
            return redirect('/ssis-colleges')
        else:
            try:
                cursor.execute('''INSERT INTO college VALUES (%s, %s)''', (College_Code, College_Name))
                cursor.close()
                conn.commit()
                conn.close()
                flash('College Added Successfully!')
                return redirect('/ssis-colleges')
            except:
                flash('Error. College code already exist.')
                return redirect('/ssis-colleges')

@main.route('/delete/college/<College_Code>', methods=['POST', 'GET'])
def delete_college(College_Code):
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM college WHERE College_Code = %s', (College_Code))  
        cursor.close()
        conn.commit()
        conn.close()
        flash('College Removed Successfully!')
        return redirect('/ssis-colleges')
    except:
        flash('Warning. College information that has courses cannot be deleted.')
        return redirect('/ssis-colleges')

@main.route('/edit/college/<College_Code>', methods=['POST', 'GET'])
def get_college(College_Code):
    data = get_college_code(College_Code)
    print(data[0])
    return render_template('edit_college.html', college=data[0])

@main.route('/update/college/<College_Code>', methods=['POST'])
def update_college(College_Code):
    conn = db.connect()
    cursor = conn.cursor() 
    if request.method == 'POST':
        College_Name = request.form['College_Name']
        if College_Name == "":
            flash('Error. College name must not be empty.')
            return redirect('/ssis-colleges')
        else:
            cursor.execute("""
                        UPDATE college
                        SET College_Name = %s
                        WHERE College_Code = %s
                        """, (College_Name, College_Code))
            flash('College Updated Successfully!')
            cursor.close()
            conn.commit()
            conn.close()
            return redirect('/ssis-colleges')

@main.route('/college/search', methods=['GET', 'POST'])
def search_college():
    if request.method == 'POST':
        u_input = request.form.get('u_search')
        field = request.form.get('search_select')

        if field == 'college_code':
            data = select_college_code(u_input)
            for u_input in data:
                return render_template('colleges.html', college = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-colleges')
        elif field == 'college_name':
            data = select_college_name(u_input)
            for u_input in data:
                return render_template('colleges.html', college = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-colleges')
        else:
            data = select_college_all(u_input)
            for u_input in data:
                return render_template('colleges.html', college = data)
            else:
                flash('Sorry, no data found. Please try again.')
                return redirect('/ssis-colleges')