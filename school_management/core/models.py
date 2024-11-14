from django.db import models
from django.contrib.auth.models import User

# Sınıf Modeli
class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Öğrenci Modeli
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class, related_name='students')

    def __str__(self):
        return self.user.username

# Öğretmen Modeli
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class, related_name='teachers')

    def __str__(self):
        return self.user.username

# Ders Programı Modeli
class Schedule(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name.name} - {self.subject} - {self.day_of_week}"

# Yoklama Modeli
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.student.user.username} - {self.schedule.subject} - {self.status}"

# Ödev Modeli
class Assignment(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

# Öğrenci Ödev Teslimi Modeli
class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.student.user.username} - {self.assignment.title}"
