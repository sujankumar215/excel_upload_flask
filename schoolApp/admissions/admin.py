from django.contrib import admin
from admissions.models import Student,Teacher

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']


class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','exp','subject','contact']

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)