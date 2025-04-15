from django.db import models


class login(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 191, blank= False)
    contact = models.CharField(max_length = 191, blank= False)
    username = models.CharField(max_length = 191, blank= False)
    password = models.CharField(max_length = 191, blank= False)
    is_admin = models.CharField(max_length = 50, choices=[('0', 'employee'),('1', 'admin')], default='0')
    is_deleted = models.CharField(max_length = 50, choices=[('0', 'not deleted'),('1', 'deleted')], default='0')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
