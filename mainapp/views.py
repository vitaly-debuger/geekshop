from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"mainapp/index.html")
def products(request):
    return render(request,"mainapp/products.html")
def contact(request):
    return render(request,"mainapp/contact.html")
def context(request):
    context={
        'title': 'test context',
        'header': 'Добро пожаловать',
        'username': 'Django освобожденный',
        'products': [
            {'name': 'Стулья', 'price': 6450},
            {'name': 'Шкаф', 'price': 16300},
            {'name': 'Стол', 'price': 12499},
        ]

    }
    return render(request,"mainapp/test_context.html", context)