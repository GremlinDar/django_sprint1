from django.shortcuts import render

# Create your views here.


def about(request):
    """Главная страница. Список постов."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Главная страница. Список постов."""
    template = 'pages/rules.html'
    return render(request, template)
