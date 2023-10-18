from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   Port, Event
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class event_to_port(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        entity = request.entity
        port = entity.port
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        if port == '' or port == None:
            uuid=entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            response += Port(
                value=service_events['src.port'].values[0],
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                            )
        else:
            response += Port(
                number=port,
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                            )
        return response
