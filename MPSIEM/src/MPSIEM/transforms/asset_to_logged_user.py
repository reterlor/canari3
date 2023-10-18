from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import  Alias, AS
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow

@EnableDebugWindow
class asset_to_logged_user(Transform):


    input_type = AS

    def do_transform(self, request, response, config):
        asset = request.entity
        name = asset.value
        start_time = asset.start_time
        end_time = asset.end_time
        url = asset.host
        login = asset.login
        password = asset.password
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = (session.event_query(query='msgid = 4624 and event_src.asset=\'{}\''.format(name),time_start=start_time, time_end=end_time)).drop_duplicates('subject.name')
        if len(service_events.index) < 12:
            count = len(service_events.index)
        else:
            count = 12
        for i in range(0,count):
            row=service_events.iloc[i]
            response += Alias(
                    alias=row['subject.name'],
                    start_time = start_time,
                    end_time = end_time,
                    host = url,
                    login = login,
                    password = password
                            )
        return response