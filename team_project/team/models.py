from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100, default='no name')
    location = models.CharField(max_length=100, default='no location')
    division = models.CharField(max_length=100, default='no division')
    win = models.CharField(max_length=100, default='no wins')
    loss = models.CharField(max_length=100, default='no name')
    
    def __str__(self):
        return self.name

class Driver(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers')
    name = models.CharField(max_length=100, default='no name')
    position = models.CharField(max_length=100, default='no position')
    age = models.CharField(max_length=100, default='no age')
    years_of_experience = models.CharField(max_length=100, default='no years of experience')
    
    
    def __str__(self):
        return self.name