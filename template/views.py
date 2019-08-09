from django.shortcuts import render
# from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_exempt
# @csrf_protect
@require_http_methods(["GET", "POST"])
def echo(request):
    # response = HttpResponse()
    if request.method == 'GET' and request.GET:
        key = [key for key, item in request.GET.dict().items()][0]
        return render(request, 'echo.html', context={
            'has_body': True,
            'method': 'get',
            'q_str': "{}: {}".format(key, request.GET[key]),
            'now': 'empty'
        })
    elif request.method == 'POST' and request.POST:
        # print(request.POST)
        key = [key for key, item in request.POST.dict().items()][0]
        return render(request, 'echo.html', context={
            'has_body': True,
            'method': 'post',
            'q_str': "{}: {}".format(key, request.POST[key]),
            'now': 'empty'
        })
    else:
        if 'http_X_Print_Statement'.upper() in request.META.keys():
            return render(request, 'echo.html', context={
                'has_body': False,
                # 'method': 'post',
                'now': request.META['http_X_Print_Statement'.upper()]
            })
        # print(request.META.keys())
        return render(request, 'echo.html', context={
            'has_body': False,
            # 'method': 'post',
            'now': 'empty'
        })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
