from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   Alias
from MPSIEM.transforms.common.entities import Event
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class event_to_user(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        entity = request.entity
        account = entity.account
        start_time = entity.start_time
        end_time = entity.end_time
        url = entity.host
        login = entity.login
        password = entity.password
        if not account:
            uuid = entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            if service_events['subject.name'].values[0] == None:
                value_alias = 'None'
            else:
                value_alias = service_events['subject.name'].values[0]
            response += Alias(value=value_alias, start_time = start_time, end_time = end_time, host = url, login = login, password = password)
        else:
            response += Alias(value=account, start_time = start_time, end_time = end_time, host = url, login = login, password = password)
        return response
