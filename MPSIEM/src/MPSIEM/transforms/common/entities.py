from canari.maltego.message import *

__author__ = 'daniel newman'
__copyright__ = 'Copyright 2023, MPSIEM Project'
__credits__ = []

__license__ = 'GPLv3'
__version__ = '0.1'
__maintainer__ = 'daniel newman'
__email__ = 'example@mail.com'
__status__ = 'Development'


class Start(Entity):
    _category_ = 'PT'
    _namespace_ = 'ptsecurity'

    properties_Time_start = StringEntityField('properties.Time_start', display_name='Time_start', is_value=True)
    Time_end = StringEntityField('Time_end', display_name='Time_end')

class Incident(Entity):
    _category_ = 'PT'
    _namespace_ = 'ptsecurity'
    
    name = StringEntityField('properties.name', display_name='Incident name', is_value=True)
    start_time = StringEntityField('start_time', display_name='Time_start')
    end_time = StringEntityField('end_time', display_name='Time_end')

class Event(Entity):
    _category_ = 'PT'
    _namespace_ = 'ptsecurity'
    id = StringEntityField('event.id', display_name='uuid', is_value=True)
    asset = StringEntityField('asset', display_name='asset')
    account = StringEntityField('event.account', display_name='account')
    time = StringEntityField('event.time', display_name='time')
    NewProcessName = StringEntityField('event.NewProcessName', display_name='NewProcessName')
    text = StringEntityField('event.text', display_name='text')
    ip = StringEntityField('event.ip', display_name='ip')
    port = StringEntityField('event.port', display_name='port')
    notes = StringEntityField('notes#', display_name='Notes')
    start_time = StringEntityField('start_time', display_name='Time_start')
    end_time = StringEntityField('end_time', display_name='Time_end')


