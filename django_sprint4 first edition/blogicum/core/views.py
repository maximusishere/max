from django.shortcuts import render


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)

def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
