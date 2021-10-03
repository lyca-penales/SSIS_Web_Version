CREATE DATABASE ssis_db;
USE ssis_db;
CREATE TABLE college (
	College_Code VARCHAR(50) NOT NULL PRIMARY KEY,
    College_Name VARCHAR(250) NOT NULL
    );

INSERT INTO college(College_Code, College_Name)
	VALUES
		('CCS', 'College of Computer Studies'),
        ('CSM', 'College of Science and Mathematics'),
        ('COET', 'College of Engineering and Technology');
        
CREATE TABLE courses (
	Course_Code VARCHAR(50) NOT NULL PRIMARY KEY,
	Course_Name VARCHAR(250) NOT NULL,
	College_Code VARCHAR(50),
    FOREIGN KEY (College_Code) REFERENCES college (College_Code)
    );
    
INSERT INTO courses(Course_Code, Course_Name)
	VALUES
		('BSCS', 'Bachelor of Science in Computer Science'),
        ('BSM', 'Bachelor of Science in Mathematics'),
        ('BSEE', 'Bachelor of Science in Eletrical Engineering');
        
CREATE TABLE student (
	Student_Id VARCHAR(10) NOT NULL PRIMARY KEY,
    Firstname VARCHAR(250) NOT NULL,
    Lastname VARCHAR(250) NOT NULL,
    Gender VARCHAR(200) NOT NULL,
    Year_Level VARCHAR(200) NOT NULL,
    Course_Code VARCHAR(50),
    FOREIGN KEY (Course_Code) REFERENCES courses (Course_Code)
    );
    
INSERT INTO student(Student_Id, Firstname, Lastname, Gender, Year_Level)
	VALUES
		('2019-0001', 'Chris', 'Thompson', 'Male', '3rd Year'),
        ('2018-0001', 'Jane', 'Perez', 'Female', '4th Year'),
        ('2020-0001', 'Josh', 'Lopez', 'Male', '2nd Year');