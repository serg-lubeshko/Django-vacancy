from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос 400!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен 403!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден 404!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера 500!')
