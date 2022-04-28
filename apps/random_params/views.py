import random
import json
from datetime import datetime, timezone

from django.http import JsonResponse

from . import helper


all_instruments = helper.AllInstruments()
all_instruments.fill_containers()


def water_standpipe():
    '''
    Generate random water standpipe sample points.
    '''
    try:
        ws_list = all_instruments.serialize_container(
            helper.AllInstruments.Borehole.Instrument.ws
        )
    except:
        return {'error': 'container could not be serialized.'}

    # add monitoring results for standpipe
    for entry in ws_list:
        entry['reading'] = round(
            entry['surface_level'] + random.uniform(-10.0, 2.0), 2
        )
        entry['timestamp'] = datetime.now(timezone.utc)
    
    return {
        'request_type': 'water_standpipe',
        'length': len(ws_list),
        'units': 'water level (m)',
        'timezone': 'UTC',
        'items': ws_list
    }


def pore_pressure():
    '''
    Generate random pore pressure sample points.
    '''
    try:
        pp_list = all_instruments.serialize_container(
            helper.AllInstruments.Borehole.Instrument.pp 
        )
    except:
        return {'error': 'container could not be serialized.'}

    # add monitoring results for piezometer
    for entry in pp_list:
        entry['reading'] = round(random.uniform(20.0, 200.0), 2)
        entry['timestamp'] = datetime.now(timezone.utc)
    
    return {
        'request_type': 'piezometer',
        'length': len(pp_list),
        'units': 'pressure (kPa)',
        'timezone': 'UTC',
        'items': pp_list
    }


def settlement(direction):
    '''
    Generate random settlement sample points.
    '''
    settlement_list = instrument_type = None
    try:
        if direction == 'x':
            settlement_list = all_instruments.serialize_container(
                helper.AllInstruments.Borehole.Instrument.sx
            )
            instrument_type = 'settlement marker (x-direction)'
        elif direction == 'y':
            settlement_list = all_instruments.serialize_container(
                helper.AllInstruments.Borehole.Instrument.sy 
            )
            instrument_type = 'settlement marker (y-direction)'
        elif direction == 'z':
            settlement_list = all_instruments.serialize_container(
                helper.AllInstruments.Borehole.Instrument.sz
            )
            instrument_type = 'settlement marker (z-direction)'
        else:
            return {'error': f'parameter {direction} is invalid.'}
    except:
        return {'error': 'container could not be serialized.'}

    # add monitoring results for settlement marker
    for entry in settlement_list:
        entry['reading'] = round(random.uniform(-30.0, 30.0), 2)
        entry['timestamp'] = datetime.now(timezone.utc)

    return {
        'request_type': instrument_type,
        'length': len(settlement_list),
        'units': 'displacement (mm)',
        'timezone': 'UTC',
        'items': settlement_list
    }


def render_water_standpipe(request):
    '''
    Return standpipe data in JSON format.
    '''
    data = water_standpipe()
    return JsonResponse(data)


def render_pore_pressure(request):
    '''
    Return piezometer data in JSON format.
    '''
    data = pore_pressure()
    return JsonResponse(data)


def render_settlement(request, direction):
    '''
    Return settlement data in JSON format.
    '''
    data = settlement(direction)
    return JsonResponse(data)


def all(request):
    '''
    Return combined data in JSON format.
    '''
    ws_data = water_standpipe()
    pp_data = pore_pressure()
    sx_data = settlement('x')
    sy_data = settlement('y')
    sz_data = settlement('z')
    total_length = (
        ws_data['length'] + pp_data['length'] + sx_data['length'] + 
        sy_data['length'] + sz_data['length']
    )
    
    return JsonResponse(
        {
            'request_type': 'all_instruments',
            'total_length': total_length,
            'standpipe_data': ws_data,
            'piezometer_data': pp_data,
            'settlement_x_data': sx_data,
            'settlement_y_data': sy_data,
            'settlement_z_data': sz_data
        }
    )
