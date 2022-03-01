from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

def index(request):
    return render(request, "por/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "por/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "por/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        FirstName = request.POST["FirstName"]
        LastName = request.POST["LastName"]
        description = request.POST["description"]
        facebook = request.POST["facebook"]
        whats = request.POST["whats"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "por/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, FirstName=FirstName, LastName=LastName, description=description, facebook=facebook, whats=whats)
            user.save()
        except IntegrityError:
            return render(request, "por/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "por/register.html")

def createPor(request):
        if request.method == "GET":
            return render(request, "por/createPor.html")
        elif request.method == "POST":
            username = request.user.username
            title = request.POST["title"]
            description = request.POST["description"]
            webLink = request.POST["webLink"]
            imageLink = request.POST["imageLink"]
            imageOnHoverLink = request.POST["imageOnHoverLink"]
            work = Work(title=title, description=description, username=username, webLink=webLink, imageLink=imageLink, imageOnHoverLink=imageOnHoverLink)
            work.save()
            request.user.worksList.add(work)
            return HttpResponseRedirect(reverse("yourPor"))

def yourPor(request):
    if request.user.is_authenticated:
        workList = request.user.worksList.all()
        if workList:
            return render(request, "por/yourPor.html", {
                "workList":workList
            })
        else:
            return HttpResponseRedirect(reverse("createPor"))
    else:
        return HttpResponseRedirect(reverse("login"))

def addWork(request):
    if request.method == "GET":
        return render(request, "por/addWork.html")
    elif request.method == "POST":
        username = request.user.username
        title = request.POST["title"]
        description = request.POST["description"]
        webLink = request.POST["webLink"]
        imageLink = request.POST["imageLink"]
        imageOnHoverLink = request.POST["imageOnHoverLink"]
        work = Work(title=title, description=description, username=username, webLink=webLink, imageLink=imageLink,
                    imageOnHoverLink=imageOnHoverLink)
        work.save()
        request.user.worksList.add(work)
        return HttpResponseRedirect(reverse("yourPor"))

def publicPor(request, username):
    user1 = User.objects.get(username=username)
    workList = user1.worksList.all()
    return render(request, "por/publicPor.html", {
        "user1": user1,
        "workList": workList
    })