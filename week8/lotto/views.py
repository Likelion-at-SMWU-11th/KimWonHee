from django.shortcuts import render
from django.http import HttpResponse


def Lottopage(request):
    import random

    lotto_number = list()
    for _ in range(7):
        number = random.randint(1, 45)
        lotto_number.append(number)

    return render(request, "lottopage.html", {"lottonumber": lotto_number})


def Lottoinput(request):
    return render(request, "lottoinput.html")


def Lottooutput(request):
    import random

    lotto_number = list()
    game = request.GET.get("game", 1)
    pull_number = [index for index in range(1, 46)]
    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number, 6))
    return render(
        request, "lottooutput.html", {"lotto_number": lotto_number, "game": game}
    )


# Create your views here.
