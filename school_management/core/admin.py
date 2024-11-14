from django.contrib import admin
from .models import Class, Student, Teacher, Schedule, Attendance, Assignment, AssignmentSubmission

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
