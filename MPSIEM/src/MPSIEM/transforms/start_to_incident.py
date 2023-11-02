from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
from MPSIEM.transforms.common.entities import Start, Incident
from canari.maltego.message import Field
import time
import datetime

@EnableDebugWindow
class start_to_incident(Transform):

    input_type = Start

    def do_transform(self, request, response, config):
        entity = request.entity
        start_time = entity.properties_Time_start
        end_time = entity.Time_end
        start_time = int(time.mktime(datetime.datetime.strptime(start_time, "%d.%m.%Y %H:%M:%S").timetuple()))
        end_time = int(time.mktime(datetime.datetime.strptime(end_time, "%d.%m.%Y %H:%M:%S").timetuple()))
        t = Incident(value='Type Value here')
        t += Field('start_time', start_time, display_name='Time start')
        t += Field('end_time', end_time, display_name='Time end')
        response += t
        return response
