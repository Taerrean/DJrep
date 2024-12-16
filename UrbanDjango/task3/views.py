from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):
    page_name = "Игры"
    game_1 = "Dead By Daylight"
    game_2 = "Mortal Kombat I"
    game_3 = "Watch Dogs 2"
    buy = "Купить"
    context = {
        'Title': page_name,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'buy': buy,
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    page_name = "Корзина"
    img = "/static/Корзина.jpg"
    text_1 = "Здесь"
    text_2 = "ничего"
    text_3 = "НЕТ!"
    context = {
        'Title': page_name,
        'img': img,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
    }
    return render(request, 'third_task/cart.html', context)
