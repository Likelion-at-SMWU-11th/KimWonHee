from django.shortcuts import render
from django.http import HttpResponse


def Lottopage(request):
    import random

    lotto_number = list()
    for _ in range(7):
        number = random.randint(1, 45)
        lotto_number.append(number)

    return render(request, "lottopage.html", {"lottonumber": lotto_number})


# Create your views here.
