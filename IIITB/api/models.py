from django.db import models

# Create your models here.

class Student(models.Model):

    ACTIVE, INACTIVE, DELETED = 'A', 'I', 'D'
    STATUS_TYPES = ((ACTIVE, 'Active'), (INACTIVE, 'Inactive'), (DELETED, 'Deleted')) 

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default=ACTIVE)
    email = models.CharField(max_length=50, default=None)
    gender = models.CharField(max_length=1, default='M')      # M, F, O
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    upd_by = models.CharField(max_length=50)
    upd_on = models.DateTimeField(blank=True, null=True, db_index=True)


class Branch(models.Model):
    name = models.CharField(max_length=50)
