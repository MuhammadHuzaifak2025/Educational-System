from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserModelVs, basename='user')
router.register('customusers', views.CustUserModelVS, basename='Cust_user')
router.register('students', views.StudentModelVS, basename='Student')
router.register('classes', views.ClassModelsVS, basename='Class')
router.register('teachers', views.TeacherModelsVS, basename='Teacher')
router.register('marks', views.MarkModelsVS, basename='Marks')
router.register('courses', views.CourseModelsVS, basename='Courses')


urlpatterns = [
    path('', include(router.urls)),
    path('student/enrolled/<int:pk>/', views.Retrieve_student_enrolled_courses.as_view(), name='Retriever'),
    # path('marks/<int:pk>/', views.MarkDetail.as_view(), name='mark-detail'),
    # path('student/class/<int:pk>/', views.MarkDetail.as_view(), name='mark-detail'),
]