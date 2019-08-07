from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@require_GET
def empty_200(request):
    return HttpResponse()


@require_GET
def not_found(request):
    return HttpResponse(status=404)


@require_GET
def slug_route(request, *args):
    # print(request.GET)
    response = HttpResponse(args)
    return response


@require_GET
def sum_route(request, *args):
    response = HttpResponse(str(int(args[0]) + int(args[1])))
    return response


@require_GET
def sum_get_method(request):
    get_dict = request.GET.dict()
    # if get_dict["a"].isdigit() and get_dict["b"].isdigit():
    try:
        response = HttpResponse(str(int(get_dict['a']) + int(get_dict['b'])))
        return response
    except (ValueError, KeyError):
        response = HttpResponse(status=400)
        return response


@csrf_exempt
@require_POST
def sum_post_method(request):
    # post_dict = request.POST.dict()
    # if get_dict["a"].isdigit() and get_dict["b"].isdigit():
    try:
        response = HttpResponse(str(int(request.POST['a']) + int(request.POST['b'])))
        return response
    except (ValueError, KeyError):
        response = HttpResponse(status=400)
        return response