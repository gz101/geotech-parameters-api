import random
from datetime import datetime, timezone

from django.http import JsonResponse


def water_standpipe(request):
    """
    Generate random water standpipe sample point.
    """
    surface_level = round(random.uniform(75.0, 120.0), 2)
    data = {
        'bh_no': f'BH-{random.randrange(1, 120)}',
        'surface_level': surface_level,
        'northing': round(random.uniform(200000.0, 5000000.0), 1),
        'easting': round(random.uniform(400000.0, 7000000.0), 1),
        'water_level': round(surface_level + random.uniform(-10.0, 2.0), 2),
        'timestamp': datetime.now(timezone.utc),
        'message': 'All elevations in reduced level (AHD).'
    }
    return JsonResponse(data)


def pore_pressure(request):
    data = {

    }
    return JsonResponse(data)


def settlement_x(request):
    data = {

    }
    return JsonResponse(data)


def settlement_y(request):
    data = {

    }
    return JsonResponse(data)


def settlement_z(request):
    data = {

    }
    return JsonResponse(data)
