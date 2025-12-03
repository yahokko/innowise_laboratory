---------------------------------------------------------------------
-- 1. CREATE TABLES
-- Database schema for the Student Grades Manager project
---------------------------------------------------------------------

-- Table storing basic student information
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,      -- Unique student identifier
    full_name TEXT NOT NULL,                   -- Full name of the student
    birth_year INTEGER NOT NULL                -- Year of birth
    );

-- Table storing grades for each student
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,                   -- Unique grade identifier
    student_id INTEGER NOT NULL,                            -- ID of the student (foreign key)
    subject TEXT NOT NULL,                                  -- Subject name
    grade INTEGER CHECK(grade >= 1 AND grade <= 100),       -- Grade between 1 and 100
    FOREIGN KEY(student_id) REFERENCES students(id)         -- Link to students table
    );

---------------------------------------------------------------------
-- 2. INSERT SAMPLE DATA
-- Provided test dataset for students and their grades
---------------------------------------------------------------------

INSERT INTO students (full_name, birth_year)
VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);


INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

---------------------------------------------------------------------
-- 3. CREATE INDEXES
-- Indexes improve query performance on frequently searched columns
---------------------------------------------------------------------

CREATE INDEX idx_grades_student_id ON grades(student_id);
CREATE INDEX idx_grades_subject ON grades(subject);

---------------------------------------------------------------------
-- 4. REQUIRED QUERIES
---------------------------------------------------------------------

-- 4.1 All grades for a specific student (Alice Johnson)
SELECT subject, grade FROM grades
WHERE student_id = (
    SELECT id FROM students 
    WHERE full_name = 'Alice Johnson'
    );

-- 4.2 Average grade per student
SELECT students.full_name,
        ROUND(AVG(grades.grade), 2) AS avg_grade
    FROM students
    JOIN grades
    ON students.id = grades.student_id
    GROUP BY students.id;

-- 4.3 Students born after 2004
SELECT *
    FROM students
    WHERE birth_year > 2004;

-- 4.4 Average grade per subject
SELECT subject,
        ROUND(AVG(grade), 2) AS avg_grade
    FROM grades
    GROUP BY subject;

-- 4.5 Top 3 students with highest average grade
SELECT students.*,
        ROUND(AVG(grades.grade), 2) AS avg_grade
    FROM students
        JOIN grades ON students.id = grades.student_id
        GROUP BY students.id
        ORDER BY avg_grade DESC
        LIMIT 3;

-- 4.6 Students who scored below 80 in any subject
SELECT DISTINCT students.*
    FROM students
    JOIN grades
    ON students.id = grades.student_id
    WHERE grades.grade < 80;