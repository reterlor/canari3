from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   Event, Phrase, AS
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
from canari.maltego.message import Bookmark
@EnableDebugWindow
class pdql_request(Transform):

    input_type = Phrase

    def do_transform(self, request, response, config):
        entity = request.entity
        pdql = entity.text
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query=pdql,time_start=start_time,time_end=end_time,count=12))
        for i in range(0,len(service_events.index)):
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