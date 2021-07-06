from django.shortcuts import render


def main_view(request):
    return render(request, template_name='vacancy/index.html')
