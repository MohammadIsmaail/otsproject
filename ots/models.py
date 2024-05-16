from django.db import models

class Candidates(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    passwors=models.CharField(max_length=20,null=False)
    name=models.CharField(null=False,max_length=30)
    test_attempted=models.IntegerField()
    points=models.FloatField()

class Questions(models.Model):
    qid=models.BigAutoField(primary_key=True,auto_created=True)
    que=models.TextField()
    a=models.CharField(max_length=256)
    b=models.CharField(max_length=256)
    c=models.CharField(max_length=256)
    d=models.CharField(max_length=256)
    ans=models.CharField(max_length=2)

class Result(models.Model):
    resultid=models.BigAutoField(auto_created=True,primary_key=True)
    username=models.ForeignKey(Candidates,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attempt=models.IntegerField()
    right=models.IntegerField()
    wrong=models.IntegerField()
    points=models.FloatField()


# Create your models here.
