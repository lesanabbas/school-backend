from django.db import models
from school.models import School

class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.course_name
