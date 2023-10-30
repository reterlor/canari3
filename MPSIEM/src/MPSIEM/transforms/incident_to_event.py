from MPSIEMprovider import MPSIEMqueries
from MPSIEM.transforms.common.entities import Incident, Event
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class incident_to_event(Transform):

    input_type = Incident

    def do_transform(self, request, response, config):
        entity = request.entity
        incident_id = entity.value
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = session.incident_query(id=incident_id,time_start=start_time,time_end=end_time)['events']
        if len(service_events) > 12:
            service_events = service_events[:12]
        for i in service_events:
            response += Event(
                id=i['id'],
                time=i['date'],
                text=i['description'],
                notes=i['description'],
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                            )
        return response
