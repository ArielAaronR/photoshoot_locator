from django.shortcuts import render, redirect
from django.core.serializers import serialize

from shoot_locator_app.models import *
from django.contrib import messages
from django.contrib.messages import get_messages
import bcrypt
import json


# Create your views here.
from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'shoot_locator_app/index.html')


def dashboard(request):
    uid = request.session.get("uid")

    if not uid:
        return redirect("/")

    user = User.objects.get(id=uid)

    all_markers = Marker.objects.all()
    all_markers_list = list(Marker.objects.all())
    all_markers_data = serialize('json', all_markers_list)

    context = {
        "user": user,
        "all_markers": all_markers,
        "all_markers_data": all_markers_data


    }

    return render(request, 'shoot_locator_app/dashboard.html', context)


def register(request):
    matched_users = User.objects.filter(email=request.POST['email'])

    if matched_users:
        return redirect('/')

    if not User.objects.basic_validation(request):
        return redirect('/')

    hashed = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(first_name=request.POST["first_name"],
                                   last_name=request.POST["last_name"],

                                   email=request.POST["email"],
                                   password=hashed)
    request.session["uid"] = new_user.id
    print(new_user)
    return redirect("/dashboard")


def login(request):

    matched_users = User.objects.filter(email=request.POST["email"])
    if matched_users:
        user = matched_users[0]

        pw_matched = bcrypt.checkpw(
            request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))

        if pw_matched:
            request.session['uid'] = user.id
        else:
            messages.error(request, "Invalid credentials")
            return redirect("/")
    else:
        messages.error(request, "Invalid credentials")
        messages.error(request, "Try again")
        return redirect("/")
    return redirect("/dashboard")


def new(request):
    uid = request.session.get("uid")

    if not uid:
        return redirect("/")
    return render(request, "shoot_locator_app/new.html")


def new_process(request):
    uid = request.session.get("uid")

    if not uid:
        return redirect("/")

    Marker.objects.create(
        name=request.POST['name'],
        address=request.POST['address'],
        image=request.POST['image'],
        descriptors=request.POST['descriptors'],
        description=request.POST['description'],
    )

    return redirect("/dashboard")


def delete(request, id):
    remove_job = Marker.objects.get(id=id)
    print(remove_job)
    remove_job.delete()

    return redirect("/dashboard")


def logout(request):
    request.session.clear()
    return redirect('/')
