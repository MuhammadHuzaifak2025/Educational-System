from django.contrib import admin
from EducationSystem.models import CustUser, Student, Teacher, Course, Class, Mark
# Register your models here.
admin.site.register(CustUser)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Mark)