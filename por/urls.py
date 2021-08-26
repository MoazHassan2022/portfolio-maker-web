from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createPor", views.createPor, name="createPor"),
    path("yourPor", views.yourPor, name="yourPor"),
    path("addWork", views.addWork, name="addWork"),
    path("publicPor/<str:username>", views.publicPor, name="publicPor"),
    path("editWork/<int:id>", views.editWork, name="editWork")
]