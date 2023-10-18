from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   Event, IPv4Address
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class ip_to_event(Transform):

    input_type = IPv4Address

    def do_transform(self, request, response, config):
        entity = request.entity
        ip = entity.value
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query='src.ip = {}'.format(ip),time_start=start_time,time_end=end_time,count=12))
        if len(service_events.index) < 12:
            count = len(service_events.index)
        else:
            count = 12
        for i in range(0,count):
            row=service_events.iloc[i]
            response += Event(
                id=row['uuid'],
                account=row['object.account.name'],
                time=row['time'],
                msgid=row['msgid'],
                NewProcessName=row['object.name'],
                text=row['text'],
                ip=row['src.ip'],
                port=row['src.port'],
                notes=row['text'],
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                            )
        return response
