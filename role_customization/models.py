from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Criteria(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='criteria')

    def __str__(self):
        return self.name


class LinkedAssessment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='linked_assessments')

    def __str__(self):
        return self.name
