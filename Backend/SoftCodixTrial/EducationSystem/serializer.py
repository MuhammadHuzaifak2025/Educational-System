from rest_framework import serializers
from EducationSystem.models import Student, CustUser, Teacher, Course, Class, Mark

class Serz_Student(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Serz_CustUser(serializers.ModelSerializer):
    class Meta:
        model = CustUser
        fields = '__all__'

class Serz_Teacher(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class Serz_Course(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Serz_Class(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class Serz_Mark(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
