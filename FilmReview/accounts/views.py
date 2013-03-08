from django.shortcuts import render_to_response
from django.http import HttpResponse
from FilmReview.accounts.models import User
#from django.db.models.query import DoesNotExist

def login(request):
    usr = ""
    pwd = ""
    if 'username' in request.GET:
        usr = request.GET['username']
    if 'password' in request.GET:
        pwd = request.GET['password']
    try:
        user = User.objects.get(name=usr, password=pwd)
    except User.DoesNotExist:
        return render_to_response('login.html')
    return render_to_response('successlogin.html')
