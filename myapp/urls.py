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

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)