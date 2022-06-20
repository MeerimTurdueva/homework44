from django.shortcuts import render
from webapp.game import Game

# Create your views here.


def game(request):
    if request.method == "GET":
        return render(request, "choose_numbers.html")
    else:
        context = {
            "numbers_str": request.POST.get("numbers_str"),
        }
        numbers_str = context["numbers_str"].split(" ")
        game = Game()
        error = game.validation(numbers_str)
        if error:
            context["result"] = error
        else:
            result = game.get_result()
            context["result"] = result

        return render(request, "choose_numbers.html", context)

