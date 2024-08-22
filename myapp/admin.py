from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class UserModel(UserAdmin):
     list_display = ["username", "email", "user_type", "profile_pic"]
#admin.site.register(CustomUser)

#@admin.register(Course)
# class CourseAdmin(UserAdmin):
#      list_display = ["course_name", "username", "email", "number", "password", "created_at", "update_at"]
class StudentAdmin(admin.ModelAdmin):
     list_display = ["first_name", "last_name","course_id", "number", "created_at"]
admin.site.register(Student, StudentAdmin)

class CoursesAdmin(admin.ModelAdmin):
     list_display = ["course_name", "created_at", "update_at"]
admin.site.register(Courses, CoursesAdmin)

class TeacherAdmin(admin.ModelAdmin):
     list_display = ["first_name", "last_name", "gender", "number", "created_at"]
admin.site.register(Teacher, TeacherAdmin)