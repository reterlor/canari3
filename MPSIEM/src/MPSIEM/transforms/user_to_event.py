
from canari.maltego.entities import Alias
from canari.maltego.transform import Transform
from MPSIEM.transforms.common.entities import Event
from canari.framework import EnableDebugWindow
from MPSIEMprovider import MPSIEMqueries
import os

@EnableDebugWindow
class user_to_event(Transform):


    input_type = Alias

    def do_transform(self, request,response, config):
        alias = request.entity
        name = alias.value
        start_time = alias.start_time
        end_time = alias.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = session.event_query(query=('object.account.name = \'{}\''.format(name)),time_start=start_time,time_end=end_time, count=12)
        if len(service_events.index) < 12:
            count = len(service_events.index)
        else:
            count = 12
        for i in range(0,count):
            row=service_events.iloc[i]
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
