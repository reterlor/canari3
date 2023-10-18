from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   AS, IPv4Address
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class ip_to_asset(Transform):

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
        service_events = (session.event_query(query='src.ip = {}'.format(ip),count = 1))
        row=service_events.iloc[0]
        response += AS(
                value = row['event_src.asset'], 
                ip = ip,                
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                    )
        return response
