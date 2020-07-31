from django.test import TestCase
from courses import serializers, models
from courses.serializers import CourseSerializer
from courses.models import Category, Course, Contact, Branch


class SerializersTest(TestCase):

    def setUp(cls):
        category = Category.objects.create(name = "coding", imgpath = "Test image")

    def test_serializer_isvalid(self):
        course_data = {
            'name' : 'coding101',
            'description' : 'learn to code', 
            'category' : 'coding', 
            'logo': 'python', 
            'contacts': [
			        {
			        	'type': 1,
			        	'value': '+743248932324'
			        }
			    ],
			'branches': [
			        {
			            'latitude': '1212',
			            'longitude': '1313',
			            'address': 'Pushinskaya st.'
			        }
			    ]
			}		



        serializer = serializers.CourseSerializer(data = course_data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        self.assertIsNotNone(Course.objects.get(id = 1))