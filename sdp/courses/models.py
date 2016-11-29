# Change log
# AK - responsible for change 1
#

from django.db import models

# Create your models here.
# change 1 -
from staff.models import Staff
from sdp.utilities import *


# from staff.models import Participant, Instructor


class Course(models.Model):
    instructor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    courseCode = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    isPublished = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.courseCode + ' ' + ' ' + self.title + ' ' + self.category + ' Published: ' + str(self.isPublished)


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    moduleTitle = models.CharField(max_length=200)
    sequenceNumber = models.IntegerField()

    def __str__(self):
        return 'CourseID: ' + str(self.course.courseCode) + ' SequenceNo: ' + str(self.sequenceNumber)


class Component(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    order = models.IntegerField()
    contentType = models.CharField(max_length=200)
    content = models.TextField()
    contentTitle = models.CharField(max_length=200)

    def __str__(self):
        return 'Component: ' + self.module.moduleTitle + ', order: ' + str(self.order)

    class Meta:
        abstract = True
        ordering = ['order']


class TextComponent(Component):
    contentType = TEXT
    content = models.TextField()

    def __str__(self):
        return 'Text component with order: ' + str(self.order) + ' in module with id: ' + str(self.module.id)


class FileComponent(Component):
    contentType = FILE
    content = models.FileField()

    def __str__(self):
        return 'File component with order: ' + str(self.order) + ' in module with id: ' + str(self.module.id)


class ImageComponent(Component):
    contentType = FILE
    content = models.ImageField()

    def __str__(self):
        return 'Image component with order: ' + str(self.order) + ' in module with id: ' + str(self.module.id)


class Enrollment(models.Model):
    isCompleted = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    participant = models.ForeignKey(Staff, on_delete=models.CASCADE)
    modules_completed = models.IntegerField(default=0)

    def __str__(self):
        return 'Course: ' + self.course.courseCode + ", Participant: " + self.participant.username
