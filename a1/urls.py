from django.urls import path
from a1 import views
urlpatterns = [
    path("", views.register, name="index"),
    path("qr/<str:pk>", views.qr, name="qrcode"),
    path("student/<str:pk>", views.student, name="student"),
    path("student/update/<str:pk>", views.update, name="updte"),
    path("delete", views.delete, name="delete")

]
