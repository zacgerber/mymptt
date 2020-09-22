from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from mpttapp.models import Mydata
from mpttapp.forms import Folderform, LoginForm
from django.contrib.auth.models import User
# Create your views here.


@login_required
def index(request):
    html = "index.html"
    my_folder = Mydata.objects.all()
    return render(request, html, {"post": my_folder})


def post_detail(request, post_id):
    html = "index.html"
    my_folder = Mydata.objects.filter(id=post_id).first()
    return render(request, html, {"post": my_folder})


@login_required
def folder_form(request):
    if request.method == "POST":
        form = Folderform(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Mydata.objects.create(
                title=data.get('title'),
                body=data.get('body')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = Folderform()
    return render(request, "base.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse("homepage"))
                return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))

    form = LoginForm()
    return render(request, "base.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


