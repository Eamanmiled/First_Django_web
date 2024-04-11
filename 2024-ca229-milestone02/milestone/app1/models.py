from django.db import models

# Create your models here.

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name

    def get_county(self):
        return self.county

    def get_attractions(self):
        return self.attractions.all()

class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='attractions')
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_descripation(self):
        return self.description
    
    def get_area(self):
        return self.area.get_name()