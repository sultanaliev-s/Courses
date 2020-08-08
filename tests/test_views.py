from django.test import TestCase, Client
from django.urls import reverse
from courses.models import Category, Course, Contact, Branch
from courses.serializers import CourseSerializer
import json


class CoursesListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_courses = 10
        Category.objects.create(name = "Test category", imgpath = "Test image")

        for i in range(1, number_of_courses + 1):
            Course.objects.create(name = "Test name" + str(i), description = "Test description" + str(i), logo = "Test logo" + str(i), category = Category.objects.get(id=1))
            Contact.objects.create(type = 1, value = "Test value" + str(i), course = Course.objects.get(id=i))
            Branch.objects.create(latitude = "Test latitude" + str(i), longitude = "Test longitude" + str(i), address = "Test address" + str(i), course = Course.objects.get(id=i))


    def test_lists_all_courses(self):
        response = self.client.get(reverse('coursesList'))
        self.assertEqual(response.status_code, 200)


class CourseDetailsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_courses = 2
        Category.objects.create(name = "Test category", imgpath = "Test image")

        for i in range(1, number_of_courses + 1):
            Course.objects.create(name = "Test name" + str(i), description = "Test description" + str(i), logo = "Test logo" + str(i), category = Category.objects.get(id=1))
            Contact.objects.create(type = 1, value = "Test value" + str(i), course = Course.objects.get(id=i))
            Branch.objects.create(latitude = "Test latitude" + str(i), longitude = "Test longitude" + str(i), address = "Test address" + str(i), course = Course.objects.get(id=i))

    def test_course_details_GET(self):
        response = self.client.get(reverse('courseDetail', kwargs ={'pk': Course.objects.get(id=1).pk}))
        serializer = CourseSerializer(Course.objects.get(id=1))

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_course_details_GET_invalid(self):
        response = self.client.get(reverse('courseDetail', kwargs ={'pk': Course.objects.get(id=1).pk}))
        serializer = CourseSerializer(Course.objects.get(id=2))
        
        self.assertFalse(response.data == serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_course_details_DELETE(self):
        response = self.client.delete(reverse('courseDetail', kwargs ={'pk': Course.objects.get(id=2).pk}))

        self.assertEquals(response.status_code, 204)
    

class CourseCreateTest(TestCase):

    @classmethod
    def setUp(self):
        Category.objects.create(name = "Test category", imgpath = "Test image")
        self.info = {
                        "name": "Some courses",
                        "description": "Some description",
                        "category": "Test category",
                        "logo": "Some logo",
                        "contacts": [
                            {
                                "type": 1,
                                "value": "Some contact information"
                            }
                        ],
                        "branches": [
                            {
                                "latitude": "1234",
                                "longitude": "13",
                                "address": "Chui street"
                            }
                        ]
                    }

    def test_course_POST(self):

        response = self.client.post(reverse('coursesList'), data = json.dumps(self.info), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

