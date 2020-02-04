from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^student.html$', views.student , name="student"),
    url(r'^project_m.html$', views.project_m , name="project_m"),
    url(r'^list_stu.html$', views.student_details , name="student_details"),
]