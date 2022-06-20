from django.shortcuts import render

# Create your views here.

def game(request):
    if request.method == "GET":
        return render(request, "choose_numbers.html")
