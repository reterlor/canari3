from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import  Alias, AS
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class user_to_login(Transform):

    input_type = Alias

    def do_transform(self, request, response, config):
        alias = request.entity
        name = alias.value
        start_time = alias.start_time
        end_time = alias.end_time
        url = alias.host
        login = alias.login
        password = alias.password
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query=('subject.name = \'{}\' and msgid = 4624'.format(name)), time_start = start_time,time_end=end_time)).drop_duplicates('event_src.asset')
        if len(service_events.index) < 12:
            count = len(service_events.index)
        else:
            count = 12
        for i in range(0,count):
            row = service_events.iloc[i]
            response += AS(
                value = row['event_src.asset'],
                ip = row['src.ip'],
                start_time = start_time,
                end_time = end_time,
                host = url,
                login = login,
                password = password
                            )
        return response
