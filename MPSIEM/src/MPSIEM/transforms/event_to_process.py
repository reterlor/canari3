from MPSIEMprovider import MPSIEMqueries
from MPSIEM.transforms.common.entities import Event, Process
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os

@EnableDebugWindow
class event_to_process(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        entity = request.entity
        process = entity.process
        start_time = entity.start_time
        end_time = entity.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        if not process:
            uuid = entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            if service_events['object.process.name'].values[0] == None:
                value_process = 'None'
            else:
                value_process = service_events['object.process.name'].values[0]
            response += Process(value=value_process, start_time = start_time, end_time = end_time)
        else:
            response += Process(number=process, start_time = start_time, end_time = end_time)  
        return response