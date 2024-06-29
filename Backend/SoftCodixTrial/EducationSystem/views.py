from rest_framework import generics
from EducationSystem.models import Student, CustUser, Teacher, Course, Class, Mark
from django.contrib.auth.models import User
from EducationSystem.serializer import Serz_Student, Serz_CustUser, Serz_Teacher, Serz_Course, Serz_Class, Serz_Mark, EnrolledCourses
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class UserModelVS(viewsets.ViewSet):
    queryset = CustUser.objects.all()
    serializer_class = Serz_Student

    def list(self, request):
        queryset = CustUser.objects.all()
        serializer = Serz_CustUser(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = Serz_CustUser(user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = Serz_CustUser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        try:
            user = CustUser.objects.get(pk=pk)
            serializer = Serz_CustUser(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except CustUser.DoesNotExist:
            return Response({"Error":"User not found"})
    
    def destroy(self, request, pk=None):
        
        try: 
            user = CustUser.objects.get(pk=pk)
            user.delete()
            return Response({'msg': 'User deleted'})
        except CustUser.DoesNotExist:
            return Response({"Error":"User not found"}) 

class StudentModelVS(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Serz_Student

    def list(self, request):
        queryset = Student.objects.all()
        serializer = Serz_Student(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        Student_obj = get_object_or_404(queryset, pk=pk) 
        serializer = Serz_Student(Student_obj)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = Serz_Student(data=request.data)
        try:
            Teacher_var = Teacher.objects.get(User=request.data['User'])
            if (Teacher_var):
                return Response({'msg': 'Student cannot be a teacher'}, status=status.HTTP_400_BAD_REQUEST )
        except:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        try:
            querryset = Student.objects.get(pk=pk)

            try:
                Temp_teacher = Teacher.objects.get(User=request.data['User'])
                Temp_Stud = Student.objects.get(User=request.data['User'])
                if Temp_Stud :
                    return Response({'msg': 'Student cannot be a teacher'}, status=status.HTTP_400_BAD_REQUEST )
                if Temp_teacher:
                    return Response({'msg': 'User is already an Student'}, status=status.HTTP_400_BAD_REQUEST )
            except:
                serializer = Serz_Student(querryset, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
             
        except Student.DoesNotExist:
            return Response({"Error":"Student not found"})
    
    def destroy(self, request, pk=None):
        try:
            student_obj = Student.objects.get(pk=pk)
            student_obj.delete()
            return Response({'msg': 'Student deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response ({"Error":"Student not found"})
        
class TeacherModelsVS(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = Serz_Teacher

    def list(self, request):
        queryset = Teacher.objects.all()
        serializer = Serz_Teacher(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Teacher.objects.all()
        Teacher_obj = get_object_or_404(queryset, pk=pk)
        serializer = Serz_Teacher(Teacher_obj)
        return Response(serializer.data)
    
    
    def create(self, request):
        serializer = Serz_Teacher(data=request.data)
        try:
            Student_var = Student.objects.get(User=request.data['User'])
            
            if Student_var:
                return Response({'msg': 'Student cannot be a teacher'}, status=status.HTTP_400_BAD_REQUEST )
        except:            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def update(self, request, pk=None):
        try: 
            Teacher_obj = Teacher.objects.get(pk=pk)

            try:
                Temp_teacher = Teacher.objects.get(User=request.data['User'])
                Temp_Stud = Student.objects.get(User=request.data['User'])
                if Temp_Stud :
                    return Response({'msg': 'Student cannot be a teacher'}, status=status.HTTP_400_BAD_REQUEST )
                if Temp_teacher:
                    return Response({'msg': 'User is already an Teacher'}, status=status.HTTP_400_BAD_REQUEST )
            except:
                serializer = Serz_Teacher(Teacher_obj, data=request.data)     
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        
        except Teacher.DoesNotExist:
            return Response({"Error":"Teacher not found"})
        
    def destroy(self, request, pk=None):
        try:
            Teacher_obj = Teacher.objects.get(pk=pk)
            Teacher_obj.delete()
            return Response({'msg': 'Teacher deleted'})
        except Teacher.DoesNotExist:
            return Response({"Error":"Teacher not found"})
        

class ClassModelsVS(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = Serz_Class

    def list(self, request):
        queryset = Class.objects.all()
        serializer = Serz_Class(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Class.objects.all()
        Class_obj = get_object_or_404(queryset, pk=pk)
        serializer = Serz_Class(Class_obj)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = Serz_Class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        try:
            Class_obj = Class.objects.get(pk=pk)
            serializer = Serz_Class(Class_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Class.DoesNotExist:
            return Response({"Error":"Class not found"})
        

    def destroy(self, request, pk=None):
        try:
            Class_obj = Class.objects.get(pk=pk)
            Class_obj.delete()
            return Response({'msg': 'Class deleted'})        
        except Class.DoesNotExist:
            return Response({"Error":"Class not found"})
        


class CourseModelsVS(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Serz_Course

    def list(self, request):
        queryset = Course.objects.all()
        Courses = Serz_Course(queryset, many=True)
        return Response(Courses.data)
    
    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        Course_obj = get_object_or_404(queryset, pk=pk)
        serializer = Serz_Course(Course_obj)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = Serz_Course(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None):
        try:
            Course_obj = Course.objects.get(pk=pk)
            serializer = Serz_Course(Course_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Course.DoesNotExist:
            return Response({"Error":"Course not found"})
        
            
    def destroy(self, request, pk=None):
        try:
            Course_obj = Course.objects.get(pk=pk)
            Course_obj.delete()
            return Response({'msg': 'Course deleted'})
        except Course.DoesNotExist:
            return Response({"Error":"Course not found"})

class MarkModelsVS(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = Serz_Mark

    def list(self, request):
        queryset = Mark.objects.all()
        serializer = Serz_Mark(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Mark.objects.all()
        Mark_obj = get_object_or_404(queryset, pk=pk)
        serializer = Serz_Mark(Mark_obj)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            Student_var = Student.objects.get(StudentId=request.data['Student'])
            Course_var = Course.objects.get(pk=request.data['Course'])
            class_var = Class.objects.filter(ClassId=request.data['Class'], Student=Student_var, Course=Course_var)
            print(class_var)
            if class_var.count() > 0:
                serializer = Serz_Mark(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                class_var = Class.objects.filter(pk=request.data['Class'])
                if not class_var:
                    return Response({'Error': 'Class not found'}, status=status.HTTP_400_BAD_REQUEST )
                class_var = Class.objects.filter(pk=request.data['Class']).filter(Student=Student_var)
                if not class_var:
                    return Response({'Error': 'Student not enrolled in the class'}, status=status.HTTP_400_BAD_REQUEST )

                return Response({'Error': 'Student not enrolled in the course '}, status=status.HTTP_400_BAD_REQUEST )
        except:
            return Response({'msg': 'Student or Course not found'}, status=status.HTTP_400_BAD_REQUEST )
        
    
    def update(self, request, pk=None):
        try:
            Mark_obj = Mark.objects.get(pk=pk)
            serializer = Serz_Mark(Mark_obj, data=request.data)
            if not (serializer.initial_data['Student'] == request.data['Student'] and serializer.initial_data['Class'] == request.data['Class'] and serializer.initial_data['Course'] == request.data['Course']):
                return Response({"Response":"Only Marks can be Updated"})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response({"Error":"Mark not found"})
        
    def destroy(self, request, pk=None):
        try:
            Mark_obj = Mark.objects.get(pk=pk)
            Mark_obj.delete()
            return Response({'msg': 'Mark deleted'})
        except Mark.DoesNotExist:
            return Response({"Error":"Mark not found"})
        
class Retrieve_student_enrolled_courses(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = EnrolledCourses

    def get_queryset(self):
        student_id = self.kwargs['pk']
        Class_obj = Class.objects.filter(Student=student_id)
        
        return Class_obj
        
# class Name(viewsets.ModelViewSet):
#     queryset = 
#     serializer_class = 

#     def list(self, request):
        
    
#     def retrieve(self, request, pk=None):
        
    
#     def create(self, request):
    
#     def update(self, request, pk=None):
    
#     def destroy(self, request, pk=None):
        