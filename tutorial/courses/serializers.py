from rest_framework import serializers
from courses.models import Category, Course, Contact, Branch

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many = True)
    branches = BranchSerializer(many = True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')

        course = Course.objects.create(**validated_data)
        for contact_data in contacts_data:
            Course.objects.create(course=course, **contact_data)

        for branch_data in branches_data:
            Course.objects.create(course=course, **branch_data)
        return course