from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import AS
from MPSIEM.transforms.common.entities import Incident
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os

@EnableDebugWindow
class incident_to_asset(Transform):

    input_type = Incident

    def do_transform(self, request, response, config):
        entity = request.entity
        incident_id = entity.value
        start_time = entity.start_time
        end_time = entity.end_time
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        session = MPSIEMqueries.session()
        session.connect(host=url, username=login, password=password)
        service_events = session.incident_query(id=incident_id)['targets']['assets']
        if len(service_events) > 12:
            service_events = service_events[:12]
        for i in service_events:
            response += AS(
                value=i['id'],
                start_time = start_time,
                end_time = end_time
                            )
        return response
