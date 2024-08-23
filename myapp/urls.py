from django.urls import path
from .import views, HOD_views, Staff_views, Student_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.Index, name='index'),
    path('base/', views.Base, name='base'),

    path('', views.Login, name='login'),
    path('dologin/', views.DoLogin, name = "dologin"),
    path('dologout/', views.DoLogout, name = "logout"),

    

    # profile and profile update
    path('profile/', views.Profile, name = "profile"),
    path('profile/update', views.Profile_Update, name = "profile_update"),
   # path('register/', views.Register, name='register'),

   # Hod pannal
    path('HOD/Home/', HOD_views.Home, name="hod_home"),
    path('HOD/Student/Add/', HOD_views.Add_Student, name='add_student'),
    path('HOD/Student/View/', HOD_views.View_Student, name='view_student'),
    path('HOD/Student/Edit/<str:id>/', HOD_views.Edit_Student, name='edit_student'),
    path('HOD/Student/Update/', HOD_views.Update_Student, name='update_student'),
    path('HOD/Student/Delete/<str:admin>/', HOD_views.Delete_Student, name='delete_student'),

    path('HOD/Teacher/Add/', HOD_views.Add_Teacher, name='add_teacher'),
    path('HOD/Teacher/View/', HOD_views.View_Teacher, name='view_teacher'),
    path('HOD/Teacher/Update/<int:id>/', HOD_views.Update_Teacher, name='update_teacher'),
    path('HOD/Teacher/Delete/<int:id>/', HOD_views.Delete_Teacher, name='delete_teacher'),

    path('HOD/Course/Add/', HOD_views.Add_Course, name='add_course'),
    path('HOD/Course/View/', HOD_views.View_Course, name='view_course'),
    path('HOD/Course/Update/<int:id>/', HOD_views.Update_Course, name='update_course'),
    path('HOD/Course/Delete/<int:id>/', HOD_views.Delete_Course, name='delete_course'),

    path('HOD/Subject/Add/', HOD_views.Add_Subject, name='add_subject'),
    path('HOD/Subject/View/', HOD_views.View_Subject, name='view_subject'),
    path('HOD/Subject/Update/<int:id>/', HOD_views.Update_Subject, name='update_subject'),
    path('HOD/Subject/Delete/<int:id>/', HOD_views.Delete_Subject, name='delete_subject'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)