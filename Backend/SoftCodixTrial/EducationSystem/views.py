from rest_framework import generics
from EducationSystem.models import Student, CustUser, Teacher, Course, Class, Mark
from EducationSystem.serializer import Serz_Student, Serz_CustUser, Serz_Teacher, Serz_Course, Serz_Class, Serz_Mark


# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustUser.objects.all()
    serializer_class = Serz_CustUser

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustUser.objects.all()
    serializer_class = Serz_CustUser
    lookup_field = 'pk'

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Serz_Student

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Serz_Student
    lookup_field = 'pk'

class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Serz_Teacher

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Serz_Teacher
    lookup_field = 'pk'

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = Serz_Course

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = Serz_Course
    lookup_field = 'pk'

class ClassListCreate(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = Serz_Class

class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = Serz_Class
    lookup_field = 'pk'

class MarkListCreate(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = Serz_Mark

class MarkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = Serz_Mark
    lookup_field = 'pk'

