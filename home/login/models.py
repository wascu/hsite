from django.db import models


# Create your models here.


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=False)
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    history = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return "{0},{1}".format(self.p_id, self.name)



class Meta:
    ordering = ['c_time']
    verbose_name = '用户'
    verbose_name_plural = '用户'
