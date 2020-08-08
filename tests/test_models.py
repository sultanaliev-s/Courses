from django.test import TestCase
from courses.models import Category, Course, Contact, Branch


class ModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name = "Test category", imgpath = "Test image")
        Course.objects.create(name = "Test name", description = "Test description", logo = "Test logo", category = Category.objects.get(id=1))
        Contact.objects.create(type = 1, value = "Test value", course = Course.objects.get(id=1))
        Branch.objects.create(latitude = "Test latitude", longitude = "Test longitude", address = "Test address", course = Course.objects.get(id=1))
    
    def test_category_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name of the category')

    def test_category_imgpath_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('imgpath').verbose_name
        self.assertEquals(field_label, 'image path')
    
    def test_course_name_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name of the course')
    
    def test_course_description_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description of the course')
    
    def test_course_logo_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'image path')
    
    def test_branch_latitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'latitude of the branch')
    
    def test_branch_longitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'longitude of the branch')

    def test_branch_address_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address of the branch')
    
    def test_contact_type_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type of contact information')
            
    def test_contact_value_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'contact information')
