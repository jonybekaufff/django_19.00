from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.surename}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surename}"
