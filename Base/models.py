from django.db import models

# Projects Table
class Project(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='projects/')
    technologies_used = models.TextField()
    description = models.TextField(null=True)
    github_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# Contact Table
class Contact(models.Model):
    fullname = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField()
    message = models.TextField(null=True)


# Skills Table
class Skill(models.Model):
    skill = models.CharField(max_length=255)

    def __str__(self):
        return self.skill

# Certifications Table
class Certification(models.Model):
    certification = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='certifications/')
    description = models.TextField()

    def __str__(self):
        return self.certification

# Story Table
class About(models.Model):
    picture = models.ImageField(upload_to='about/')
    name = models.CharField (max_length=50)
    surname = models.CharField (max_length=50)
    email = models.EmailField()
    story = models.TextField()
    age = models.IntegerField()


    def __str__(self):
        return f"about {self.name}"

