from django.contrib import admin
from.models import (
    Student,
    Teacher,
)

#admin panelge registrasiya kylyp jatabyz:
admin.site.register(Student)
admin.site.register(Teacher)
