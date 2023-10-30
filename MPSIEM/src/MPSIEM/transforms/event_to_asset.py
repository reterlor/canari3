from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   AS
from MPSIEM.transforms.common.entities import Event
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class event_to_asset(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        entity = request.entity
        asset = entity.asset
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        if not asset:
            uuid = entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            if service_events['event_src.asset'].values[0] == None:
                value_asset='None'
            else:
                value_asset = service_events['event_src.asset'].values[0]
            response += AS(value=value_asset, start_time = start_time, end_time = end_time, host = url, login = login, password = password)
        else:
            response += AS(number=asset, start_time = start_time, end_time = end_time, host = url, login = login, password = password) 
        return response