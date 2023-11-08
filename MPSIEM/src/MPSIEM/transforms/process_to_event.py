from MPSIEMprovider import MPSIEMqueries
from MPSIEM.transforms.common.entities import Event, Process
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os

@EnableDebugWindow
class process_to_event(Transform):

    input_type = Process

    def do_transform(self, request, response, config):
        entity = request.entity
        process = entity.value
        start_time = entity.start_time
        end_time = entity.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query='object.process.name = \'{}\''.format(process),time_start=start_time,time_end=end_time,count=12))
        if len(service_events.index) < 12:
            count = len(service_events.index)
        else:
            count = 12
        for i in range(0,count):
            row = service_events.iloc[i]
            response += Event(
                id = row['uuid'],
                account = row['object.account.name'],
                time = row['time'],
                msgid = row['msgid'],
                NewProcessName = row['object.name'],
                text = row['text'],
                ip = row['src.ip'],
                port = row['src.port'],
                notes = row['text'],
                start_time = start_time,
                end_time = end_time,
                process = row['object.process.name']
                            )
        return response