from rest_framework import serializers
from EducationSystem.models import Student, CustUser, Teacher, Course, Class, Mark
from django.contrib.auth.models import User

import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        write = ['password']
class Serz_Student(serializers.ModelSerializer):
    Student_Name = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'

    def get_Student_Name(self, obj):
        if obj.User.User.first_name is "":
            return obj.User.User.username
        else:
            return obj.User.User.first_name

class Serz_CustUser(serializers.ModelSerializer):
    Name = serializers.SerializerMethodField()
    Email = serializers.SerializerMethodField()

    class Meta:
        model = CustUser
        fields = '__all__'
    
    def get_Name(self, obj):
        return obj.User.username   

    def get_Email(self, obj):
        return obj.User.email
class Serz_Teacher(serializers.ModelSerializer):
    Teacher_Name = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = '__all__'
    
    def get_Teacher_Name(self, obj):
        if obj.User.User.first_name == "":
            return obj.User.User.username
        else:
            return obj.User.User.first_name

class Serz_Course(serializers.ModelSerializer):
    Course_Instructor = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_Course_Instructor(self, obj):
        if  obj.Teacher.User.User.first_name == "":
            return obj.Teacher.User.User.username
        else:
            return  obj.Teacher.User.User.first_name

class Serz_Class(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class Serz_Mark(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class EnrolledCourses(serializers.ModelSerializer):
    Student_Name = serializers.SerializerMethodField()
    class Meta:
        model = Class
        exclude = ['Student']

    def get_Student_Name(self, obj):
        return self.context['request'].user.username
