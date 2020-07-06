from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from marks.managers import SchoolUserManager


class SchoolUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SchoolUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(SchoolUser):

    class Meta:
        proxy = True


class Student(SchoolUser):

    class Meta:
        proxy = True


class StudentMark(models.Model):
    MARKS = (
        ('A', 'Excellent'),
        ('B', 'Good'),
        ('C', 'Average'),
        ('D', 'Bad'),
        ('F', 'Failed'),
    )
    mark = models.CharField(max_length=1, choices=MARKS, blank=False, null=False)
    comment = models.CharField(max_length=100, blank=True, null=False)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE, related_name='marks')

    class Meta:
        permissions = (
            ('can_add_marks', 'Can add marks in this app'),
            ('can_view_all_marks', 'Can view all marks in this app'),
            ('can_view_only_own_marks', 'Can view only his or her own marks in this app')
        )

    def __str__(self):
        return self.mark
