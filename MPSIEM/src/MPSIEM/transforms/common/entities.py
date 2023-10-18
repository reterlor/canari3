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
    MPSIEM_url = StringEntityField('MPSIEM_url', display_name='MPSIEM_url')
    login = StringEntityField('login', display_name='login')
    password = StringEntityField('password', display_name='password')

