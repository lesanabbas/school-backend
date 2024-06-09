from django.db import models
from school.models import School
from teacher.models import Teacher
from course.models import Course

class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course} - {self.schedule} - {self.room_number}"
