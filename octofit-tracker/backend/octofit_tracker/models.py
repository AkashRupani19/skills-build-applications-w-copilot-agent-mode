from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, db_column='_id')

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='_id')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='_id')
    description = models.CharField(max_length=255)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, db_column='_id')
    points = models.IntegerField()
