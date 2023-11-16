from MPSIEMprovider import MPSIEMqueries
from MPSIEM.transforms.common.entities import Event
from canari.maltego.entities import AS
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os

@EnableDebugWindow
class asset_to_event(Transform):


    input_type = AS

    def do_transform(self, request, response, config):
        asset = request.entity
        name = asset.value
        start_time = asset.start_time
        end_time = asset.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query='event_src.host=\'{}\''.format(name),time_start=start_time,time_end=end_time,count=12))
        for i in range(0,len(service_events.index)):
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
