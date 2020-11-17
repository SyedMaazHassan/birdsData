from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
import os
import json

# main page function

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")

    mycursor = connection.cursor()
    mycursor.execute("SELECT id, brief_description FROM application_bird_orders")
    data = mycursor.fetchall()
    print(data)
    return render(request, 'main.html', {'listing': data})


# function to retreive bar chart data
def getData(request):
    if request.method == "GET":
        order_id = int(request.GET.get("order_id"))
        mycursor = connection.cursor()
        mycursor.execute(
            f'''
            SELECT
                id,
                scientific_name,
                (SELECT count(*) FROM application_birds WHERE family_id = application_bird_families.id) AS "coutning"
            FROM application_bird_families
            WHERE bird_orders_id = {order_id};
            '''
        )
        data = mycursor.fetchall()

        output = {}
        header = []
        counting = []

        for i in data:
            header.append(i[1])
            counting.append(i[2])

        output["header"] = header
        output["counts"] = counting

        return JsonResponse(output)


# function for signup

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        country_code = request.POST['country']
        context = {
            "name":name,
            "l_name":l_name,
            "email":email,
            "pass1":pass1,
            "pass2":pass2,
            "country": country_code
        }
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "email" 
                return render(request, "signup.html", context)

            user = User.objects.create_user(username=email, first_name=name, password=pass1, last_name=l_name, email=country_code)
            user.save()
            
            return redirect("login")
        else:
            messages.info(request, "Your pasword doesn't match!")
            context['border'] = "password"
            return render(request, "signup.html", context)


    
    return render(request, "signup.html")


def open_sighting(request):
    all_birds = birds.objects.all()
    return render(request, "sighting.html", {"birds": all_birds})


def add_sighting(request):

    if request.method == "POST" and request.user.is_authenticated:
        bird_id = request.POST.get("bird")
        location = request.POST.get("location")
        comment = request.POST.get("comment")

        for i, j in request.POST.items():
            print(i, j)

        new_sighting = sighting(
            user = request.user,
            bird = birds.objects.get(id = int(bird_id)),
            location = location,
            comments = comment
        )

        new_sighting.save()

        messages.info(request, "Bird sighting has been added!")

    return redirect("add-sighting")

# function for login

def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'email': email,
            'password': password
        }
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Incorrect login details!")
            return render(request, "login.html", context)
            # return redirect("login")
    else:
        return render(request, "login.html")


# function for logout

def logout(request):
    auth.logout(request)
    return redirect("index")

