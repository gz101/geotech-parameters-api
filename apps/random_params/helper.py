import random 
import enum


class AllInstruments:
    '''
    Represents all instruments within the project.
    '''
    def __init__(self):
        self.borehole_ids = set()
        self.ws_container = set()
        self.pp_container = set()
        self.sx_container = set()
        self.sy_container = set()
        self.sz_container = set()


    class Borehole:
        '''
        Represents a single borehole with an id, instrument, and location.
        '''
        def __init__(self, id: int, instrument):
            self.id = id
            self.instrument = instrument
            self.northing = random.randrange(5810000, 5816000)
            self.easting = random.randrange(316045, 325000)
            self.surface_level = round(random.uniform(75.0, 120.0), 2)


        class Instrument(enum.Enum):
            '''
            Represents instrument used in a borehole, where:
                ws = water standpipe
                pp = piezometer
                sx = settlement marker (x-dimension)
                sy = settlement marker (y-dimension)
                sz = settlement marker (z-dimension)
            '''
            ws = 1
            pp = 2
            sx = 3
            sy = 4
            sz = 5


            def __str__(self):
                if self.value == 1: return 'water_standpipe'
                if self.value == 2: return 'piezometer'
                if self.value == 3: return 'settlement marker x'
                if self.value == 4: return 'settlement marker y'
                if self.value == 5: return 'settlement marker z'


        def serialize(self):
            '''
            Serialized representation of borehole.
            '''
            return {
                'borehole_number': f'BH-{self.id}',
                'instrument': self.instrument,
                'surface_level': self.surface_level,
                'northing': self.northing,
                'easting': self.easting
            }


    def generate_unique_id(self):
        '''
        Generate a unique id which has not been used by any borehole.
        '''
        id = None 
        while id == None or id in self.borehole_ids:
            id = random.randrange(1, 9999)
        self.borehole_ids.add(id)
        return id


    def generate_container(self, instrument: Borehole.Instrument):
        '''
        Generate a set of boreholes for an `instrument`.
        '''
        n = random.randrange(50, 150)
        return {
            self.Borehole(
                self.generate_unique_id(), 
                self.Borehole.Instrument(instrument)
            ) 
            for _ in range(n)
        }
    

    def fill_containers(self):
        '''
        Fill all containers with randomly generated boreholes.
        '''
        self.ws_container.update(
            self.generate_container(self.Borehole.Instrument.ws)
        )
        self.pp_container.update(
            self.generate_container(self.Borehole.Instrument.pp)
        )
        self.sx_container.update(
            self.generate_container(self.Borehole.Instrument.sx)
        )
        self.sy_container.update(
            self.generate_container(self.Borehole.Instrument.sy)
        )
        self.sz_container.update(
            self.generate_container(self.Borehole.Instrument.sz)
        )
    

    def serialize_container(self, instrument: Borehole.Instrument):
        '''
        Serialize the container for the instrument, `instrument`.
        '''
        container = None 
        if instrument == self.Borehole.Instrument.ws:
            container = self.ws_container 
        elif instrument == self.Borehole.Instrument.pp:
            container = self.pp_container
        elif instrument == self.Borehole.Instrument.sx:
            container = self.sx_container 
        elif instrument == self.Borehole.Instrument.sy:
            container = self.sy_container
        elif instrument == self.Borehole.Instrument.sz:
            container = self.sz_container
        else:
            raise Exception(
                f'Can\'t serialize container with instrument: {instrument}'
            )
        return [x.serialize() for x in container]
