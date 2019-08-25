from django.db import models

# Create your models here.
class Admin(models.Model):
    # content = models.TextField(default='i am bored')
    name = models.TextField()
    password = models.TextField()
    community = models.ForeignKey('Community', on_delete=models.CASCADE)

class Community(models.Model):
    locality_name = models.TextField()



class CommunitySchoolRel(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    school  = models.ForeignKey('School', on_delete=models.CASCADE)

class School(models.Model):
    name = models.TextField()
    community_name = models.TextField(default="varanasi1")
    students_no = models.IntegerField()
    teacher_no = models.IntegerField()
    resource1_no = models.IntegerField()
    resource2_no = models.IntegerField()
    resource3_no = models.IntegerField()

    # cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE)

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    # timetable = models.ForeignKey('Timetable' , on_delete = models.PROTECT)

class Volunteer(models.Model):
    name = models.CharField(max_length=30)
    cluster = models.ForeignKey('Community', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=30)

class Grievance(models.Model):
    name =models.TextField()
    community = models.TextField()
    msg = models.TextField()


