from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.


def platform(request):
    title = "Главная"
    context = {
        'Title': title,
    }
    return render(request, 'fourth_task/platform.html', context)


def games(request):
    title = "Игры"
    games = ["Atomic Heart", "Cyberpunk", "PayDay 2"]
    buy = "Купить"
    context = {
        'Title': title,
        'games': games,
        'buy': buy,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title = "Корзина"
    img = "/static/Корзина.jpg"
    text_1 = "Здесь"
    text_2 = "ничего"
    text_3 = "НЕТ!"
    context = {
        'Title': title,
        'img': img,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
    }
    return render(request, 'fourth_task/cart.html', context)