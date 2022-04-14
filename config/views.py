from django.http import JsonResponse


def ping(request):
    """
    Tests if the connection to application works.
    """
    data = {'ping': 'pong!'}
    return JsonResponse(data)
