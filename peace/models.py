
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class model_relations(models.Model):
    u_id = models.TextField()
    team = models.CharField(max_length=20)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE,related_name='no')

    def __str__(self):
        return self.u_id

#####practice modals#####

#one to many and many to one relationship
class m1(models.Model):
    teamname = models.CharField(max_length=20)
    def __str__(self):
        return self.teamname

class m2(models.Model):
    name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    groupname = models.ForeignKey(m1, on_delete=models.CASCADE,related_name='tn')

    def __str__(self):
        return self.name

#many to many relationship
class student(models.Model):
    p_id = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class courses(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=20)
    enroll = models.ManyToManyField(student,related_name='el') 

    def __str__(self):
        return self.course_name


#model modifications
class yahiko(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

#form1 models:
class place(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place
    
class akatsukiteam(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default='coolbro@gmail.com')
    place = models.CharField(max_length=30)
    purpose = models.CharField(max_length=30,default='peace')
    
    def __str__(self):
        return self.fname