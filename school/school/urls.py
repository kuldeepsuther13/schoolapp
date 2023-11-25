from django.contrib import admin
from django.urls import path
from schoolapp.views import StudentList,StudentDetail,ParentList,ParentDetail,TeacherList,TeacherDetail,AttendanceList,AttendanceDetail,ClassList,ClassDetail,GradeList,GradeDetail,CourseList,CourseDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/studentlist/',StudentList.as_view()),
    path('api/studentlist/<int:pk>',StudentDetail.as_view()),
    path('api/parentlist/',ParentList.as_view()),
    path('api/parentlist/<int:pk>',ParentDetail.as_view()),
    path('api/teacherlist/',TeacherList.as_view()),
    path('api/teacherlist/<int:pk>',TeacherDetail.as_view()),
    path('api/attendancelist/',AttendanceList.as_view()),
    path('api/attendancelist/<int:pk>',AttendanceDetail.as_view()),
    path('api/classlist/',ClassList.as_view()),
    path('api/classlist/<int:pk>',ClassDetail.as_view()),
    path('api/gradelist/',GradeList.as_view()),
    path('api/gradelist/<int:pk>',GradeDetail.as_view()),
    path('api/courselist/',CourseList.as_view()),
    path('api/courselist/<int:pk>',CourseDetail.as_view()),
]
