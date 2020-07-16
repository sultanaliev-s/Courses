from django.db import models


class Category(models.Model):
    name = models.CharField('name of the category', max_length = 200)
    imgpath = models.CharField('image path', max_length = 300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Course(models.Model):
    name = models.CharField('name of the course', max_length = 200)
    description = models.TextField('descriptopn of the course')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    logo = models.CharField('idk', max_length = 200)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField('latitude of the branch', max_length = 10)
    longitude = models.CharField('longitude of the branch', max_length = 10)
    address = models.CharField('address of the branch', max_length = 200)
    course = models.ForeignKey(Course, related_name='branches', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name_plural = "Branches"

class Contact(models.Model):
    CONTACT_TYPE = [
        (1, 'Phone'),
        (2, 'Email'),
        (3, 'Facebook'),
    ]

    type = models.IntegerField('type of contact information', choices = CONTACT_TYPE)
    value = models.CharField('contact information', max_length = 50)
    course = models.ForeignKey(Course, related_name='contacts', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.value