from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello, world. You're at the scheduler index.")


def api_tester(request):
    return render(request, "api_test.html")


