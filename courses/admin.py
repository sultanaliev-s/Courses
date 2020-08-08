from django.contrib import admin
from courses.models import Category, Course, Contact, Branch

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Branch)