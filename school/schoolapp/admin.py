from django.contrib import admin

# Register your models here.
from .models import Student,Parent,Teacher,Attendance,Class,Grades,Course

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Class)
admin.site.register(Grades)
admin.site.register(Course)
