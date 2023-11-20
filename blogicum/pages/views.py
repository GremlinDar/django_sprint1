from django.shortcuts import render


def about(request):
    template_name = 'about.html'
    return render(request, template_name)


def rules(request):
    template_name = 'rules.html'
    return render(request, template_name)
