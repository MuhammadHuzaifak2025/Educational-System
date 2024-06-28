from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('students/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('teachers/', views.TeacherListCreate.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view(), name='teacher-detail'),
    path('courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('classes/', views.ClassListCreate.as_view(), name='class-list-create'),
    path('classes/<int:pk>/', views.ClassDetail.as_view(), name='class-detail'),
    path('marks/', views.MarkListCreate.as_view(), name='mark-list-create'),
    path('marks/<int:pk>/', views.MarkDetail.as_view(), name='mark-detail'),
    path('student/class/<int:pk>/', views.MarkDetail.as_view(), name='mark-detail'),
]