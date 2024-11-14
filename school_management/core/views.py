from django.shortcuts import render
from .models import Schedule, Attendance, Assignment

def class_schedule(request, class_id):
    schedules = Schedule.objects.filter(class_name__id=class_id)
    return render(request, 'core/class_schedule.html', {'schedules': schedules})

def attendance(request, class_id):
    attendance = Attendance.objects.filter(schedule__class_name__id=class_id)
    return render(request, 'core/attendance.html', {'attendance': attendance})

def assignments(request, class_id):
    assignments = Assignment.objects.filter(class_name__id=class_id)
    return render(request, 'core/assignments.html', {'assignments': assignments})
