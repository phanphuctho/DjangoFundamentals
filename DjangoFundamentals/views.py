# from django.http import HttpResponse
#
# def welcome(request):
#     return HttpResponse("Welcome")

from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, "DjangoFundamentals/welcome.html")