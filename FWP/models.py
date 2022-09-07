from django.db import models
from django.urls import reverse
# Create your models here.


class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete = models.PROTECT, null=False)
    day = models.ForeignKey('Day', on_delete=models.PROTECT, null=False)
    number_lesson = models.ForeignKey('NumberLesson', on_delete=models.PROTECT, null=False)
    type_lesson = models.ForeignKey('TypeLesson', on_delete=models.PROTECT, null=False)
    is_even = models.ForeignKey('Parity', on_delete=models.PROTECT, null=False)
    classroom = models.CharField(max_length=20, blank=True)


    # def get_absolute_url(self):
    #     return Subject.get_absolute_url(Subject)
    #     #return reverse("subject", kwargs={"subject_slug": Subject.slug})

class Day(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("post", kwargs={"post_slug": self.slug})


class Subject(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subject", kwargs={"subject_slug": self.slug})


class NumberLesson(models.Model):
    name = models.PositiveIntegerField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return str(self.name)

class TypeLesson(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Parity(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name