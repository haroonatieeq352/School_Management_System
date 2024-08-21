from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from myapp.models import *
from django.contrib import messages

@login_required(login_url='/')
def Home(request):
    return render(request, "HOD/home.html")

@login_required(login_url='/')
def Add_Student(request):
    course = Student.objects.all()
    courses = Courses.objects.all()

    if request.method=="POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already exits plase try again")
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already exits plase try again")
            return redirect('add_student')
        else:
            user = CustomUser(
                profile_pic = profile_pic,
                username = username,
                email = email,
                user_type = '3',
                password = password,
            )
            user.set_password(password) 
            user.save()

            course = Courses.objects.get(id=course_id)

            student = Student(
                admin = user,
                first_name = first_name,
                last_name = last_name,
                number = number,
                address = address,
                course_id = course,
                gender = gender,

            )
            student.save()
            messages.success(request, student.first_name + " " + student.last_name + " " + "successfully added")
            return redirect("add_student")


    context = {
        "cources" : courses,
        "course" : course,
    }
    return render(request, "HOD/add_student.html", context)

def View_Student(request):
    student = Student.objects.all()

    context = {
        'student' : student,
    }
    return render(request, "HOD/view_student.html", context)

def Edit_Student(request, id):
    student = Student.objects.filter(id = id)
    courses = Courses.objects.all()

    context = {
        "student" : student,
        "courses" : courses,
    }
    return render (request, "HOD/edit_student.html", context)

def Update_Student(request):
    if request.method=="POST":
        student_id = request.POST.get("student_id")
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        course_id = request.POST.get("course_id")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        #print(gender, course_id)

        user = CustomUser.objects.get(id = student_id)
        user.username = username
        user.email = email

        if password != None and password != "":  
            user.set_password(password)

        if profile_pic != None and profile_pic != "":  
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.first_name = first_name
        student.last_name = last_name
        student.number = number
        student.address = address
        student.gender = gender
        # if course_id == None and course_id != None and course_id == "" and course_id != "":
        #     student.gender = gender

        

        #if course != None and course != "" or course == None and course == "":
        
        course = Courses.objects.get(id = course_id)
        student.course_id = course
            
        # else:
        #     messages.error(request, "Please select a valid course.")
        student.save()
        messages.success(request, "Congratulations! Student Update Successfully")
        return redirect("view_student")
    
    return render (request, "HOD/edit_student.html")

def Delete_Student(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, "Student Delete Successfullly")
    return redirect("view_student")

def Add_Course(request):
    if request.method=="POST":
        course_name = request.POST.get("course_name")
        
        course = Courses(
            course_name = course_name
        )
        course.save()
        messages.success(request, "Congratulations! Course Successfully Add")
        return redirect("add_course")

    return render(request, "HOD/add_course.html")

def View_Course(request):
    course = Courses.objects.all()
    context = {
        "course" : course
    }
    return render(request, "HOD/view_course.html", context)

def Update_Course(request, id):
    #course = get_list_or_404(Courses, id=id)
    course = Courses.objects.get(id=id)
    if request.method=="POST":
        course.course_name = request.POST.get("course_name")
        course.save()
        messages.success(request, "Course Update Successfully")
        return redirect("view_course")
    
    context = {
        "course" : course
    }
    return render(request, "HOD/update_course.html", context)

def Delete_Course(request,id):
    course = Courses.objects.get(id=id)
    course.delete()
    messages.success(request, "Course Remove Successfullly")
    return redirect("view_course")

def Add_Teacher(request):
    if request.method=="POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already exits plase try again")
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already exits plase try again")
            return redirect('add_student')
        else:
            user = CustomUser(
                profile_pic = profile_pic,
                username = username,
                password = password,
                email = email,
                user_type = '2',
            )
            user.set_password(password)
            user.save()

            teacher = Teacher(
                admin = user,
                first_name = first_name,
                last_name = last_name,
                number = number,
                address = address,
                gender = gender,

            )
            #teacher.set_password(password)
            teacher.save()
            messages.success(request, "Congratulations!" + teacher.first_name + " " + teacher.last_name + " " + "successfully added")
            return redirect("add_teacher")

    return render(request, "HOD/add_teacher.html")

def View_Teacher(request):
    teacher = Teacher.objects.all()

    context = {
        'teacher' : teacher,
    }
    return render(request, "HOD/view_teacher.html", context)