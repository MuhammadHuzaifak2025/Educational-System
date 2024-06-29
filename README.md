# Soft Codix Test Rest Api Educational System Project
# ERD 
- Erd Link: [LUCID CHART](https://lucid.app/lucidchart/50a1337e-6b99-493f-9a7f-7d616186cbd8/edit?view_items=BNuPDUs6YzPC&invitationId=inv_18d18b9d-e9e6-4017-bbe4-4545ffea12ff
)

![Lucid Chart](![image](https://github.com/MuhammadHuzaifak2025/SoftCodix/assets/115894335/25e88e74-0891-43fb-b4b6-e3b72ad812b1)
)

# FrameWorks

- Django
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- SQLLITE 3

# Education System API

This project is a RESTful API for an education system, built using Django and Django REST Framework. It provides endpoints to manage students, teachers, courses, classes, and marks.

## Features

- CRUD operations for users, students, teachers, courses, classes, and marks.
- Validation to ensure a student cannot be a teacher and vice versa.
- Retrieve enrolled courses for a specific student.
- Comprehensive error handling.

## Endpoints

### User Endpoints

- `GET /users/` - List all users.
- `GET /users/{id}/` - Retrieve a specific user.
- `POST /users/` - Create a new user.
- `PUT /users/{id}/` - Update a user.
- `DELETE /users/{id}/` - Delete a user.

### Student Endpoints

- `GET /students/` - List all students.
- `GET /students/{id}/` - Retrieve a specific student.
- `POST /students/` - Create a new student.
- `PUT /students/{id}/` - Update a student.
- `DELETE /students/{id}/` - Delete a student.

### Teacher Endpoints

- `GET /teachers/` - List all teachers.
- `GET /teachers/{id}/` - Retrieve a specific teacher.
- `POST /teachers/` - Create a new teacher.
- `PUT /teachers/{id}/` - Update a teacher.
- `DELETE /teachers/{id}/` - Delete a teacher.

### Course Endpoints

- `GET /courses/` - List all courses.
- `GET /courses/{id}/` - Retrieve a specific course.
- `POST /courses/` - Create a new course.
- `PUT /courses/{id}/` - Update a course.
- `DELETE /courses/{id}/` - Delete a course.

### Class Endpoints

- `GET /classes/` - List all classes.
- `GET /classes/{id}/` - Retrieve a specific class.
- `POST /classes/` - Create a new class.
- `PUT /classes/{id}/` - Update a class.
- `DELETE /classes/{id}/` - Delete a class.

### Mark Endpoints

- `GET /marks/` - List all marks.
- `GET /marks/{id}/` - Retrieve a specific mark.
- `POST /marks/` - Create a new mark.
- `PUT /marks/{id}/` - Update a mark.
- `DELETE /marks/{id}/` - Delete a mark.

### Retrieve Student's Enrolled Courses

- `GET /students/{id}/courses/` - Retrieve a student's enrolled courses for a specific class.


# IMP: Some Assumptions Taken
- One Teacher can Teach one Course only
- User Model used so later if authentication is needed then adding hanler of @login-required can make it possible with ease.
- Cust Model Used Because if any feild need to be added it can be done
- We can have same Student and Teacher models but if we want to add maritial status or some other fields it can be added. 

## Thank U, 
### Muhammd Huzafia , mhuzaifa91@gmail.com, +923002293822.
