from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def sign_up(request):
    return render(request, "sign_up.html")

def sign_in(request):
    return render(request, "sign_in.html")


def sign_up_api(request):
    password = request.POST['passwd']
    username = request.POST['username']
    email = request.POST['email']
    try:
        user = User.objects.create_superuser(username, email, password)
        user.save()
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse({'signup':'success'})


def sign_in_api(request):
    password = request.POST['passwd']
    username = request.POST['username']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'signup': 'success'})
    else:
        return JsonResponse({'message': 'Login failed'}, status=400)

