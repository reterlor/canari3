from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import Port
from MPSIEM.transforms.common.entities import Event
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os

@EnableDebugWindow
class event_to_port(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        entity = request.entity
        port = entity.port
        start_time = entity.start_time
        end_time = entity.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        if not port:
            uuid = entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            if service_events['src.port'].values[0] == None:
                value_port = 0
            else:
                value_port = service_events['src.port'].values[0]
            response += Port(value=value_port, start_time = start_time, end_time = end_time)
        else:
            response += Port(number=port, start_time = start_time, end_time = end_time)  
        return response
