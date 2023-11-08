from MPSIEMprovider import MPSIEMqueries
from canari.maltego.entities import   Alias, Port, IPv4Address, AS
from MPSIEM.transforms.common.entities import Event, Process
from canari.maltego.transform import Transform
from canari.framework import EnableDebugWindow
import os
import pandas as pd

@EnableDebugWindow
class extract_event_info(Transform):

    input_type = Event

    def do_transform(self, request, response, config):
        service_events = pd.DataFrame()
        entity = request.entity
        account = entity.account
        start_time = entity.start_time
        end_time = entity.end_time
        process = entity.process
        url = os.getenv('MPSIEM_URL')
        login = os.getenv('MPSIEM_LOGIN')
        password = os.getenv('MPSIEM_PASSWORD')
        port = entity.port
        ip = entity.ip
        asset = entity.asset

        if not account:
            uuid = entity.value
            session = MPSIEMqueries.session()
            session.connect(host=url, username=login, password=password)
            service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
            if service_events['subject.name'].values[0] == None:
                value_alias = 'None'
            else:
                value_alias = service_events['subject.name'].values[0]
            response += Alias(value=value_alias, start_time = start_time, end_time = end_time)
        else:
            response += Alias(value=account, start_time = start_time, end_time = end_time)

        if not port:
            if not service_events.empty:
                if service_events['src.port'].values[0] == None:
                    value_port= 0
                else:
                    value_port = service_events['src.port'].values[0]
                response += Port(value=value_port, start_time = start_time, end_time = end_time)
            else:  
                uuid = entity.value
                session = MPSIEMqueries.session()
                session.connect(host=url, username=login, password=password)
                service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
                if service_events['src.port'].values[0] == None:
                    value_port = 0
                else:
                    value_port = service_events['src.port'].values[0]
                response += Port(value=value_port, start_time = start_time, end_time = end_time)
        else:
            response += Port(number=port, start_time = start_time, end_time = end_time)        

        if not ip:
            if not service_events.empty:
                if service_events['src.ip'].values[0] == None:
                    value_ip = 'None'
                else:
                    value_ip = service_events['src.ip'].values[0]
                response += IPv4Address(value=value_ip, start_time = start_time, end_time = end_time)
            else:  
                uuid = entity.value
                session = MPSIEMqueries.session()
                session.connect(host=url, username=login, password=password)
                service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
                if service_events['src.ip'].values[0] == None:
                    value_ip = 'None'
                else:
                    value_ip = service_events['src.ip'].values[0]
                response += IPv4Address(value=value_ip, start_time = start_time, end_time = end_time)
        else:
            response += IPv4Address(number=ip, start_time = start_time, end_time = end_time) 

        if not asset:
            if not service_events.empty:
                if service_events['event_src.asset'].values[0] == None:
                    value_asset='None'
                else:
                    value_asset = service_events['event_src.asset'].values[0]
            else:
                uuid = entity.value
                session = MPSIEMqueries.session()
                session.connect(host=url, username=login, password=password)
                service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
                if service_events['event_src.asset'].values[0] == None:
                    value_asset='None'
                else:
                    value_asset = service_events['event_src.asset'].values[0]
            response += AS(value=value_asset, start_time = start_time, end_time = end_time)
        else:
            response += AS(number=asset, start_time = start_time, end_time = end_time) 

        if not process:
            if not service_events.empty:
                if service_events['object.process.name'].values[0] == None:
                    value_process= 'None'
                else:
                    value_process = service_events['object.process.name'].values[0]
                response += Process(value=value_process, start_time = start_time, end_time = end_time)
            else:
                uuid = entity.value
                session = MPSIEMqueries.session()
                session.connect(host=url, username=login, password=password)
                service_events = (session.event_query(query='uuid = {}'.format(uuid),count=1, time_start = start_time, time_end=end_time))
                if service_events['object.process.name'].values[0] == None:
                    value_process = 'None'
                else:
                    value_process = service_events['object.process.name'].values[0]
                response += Process(value=value_process, start_time = start_time, end_time = end_time)
        else:
            response += Process(number=process, start_time = start_time, end_time = end_time)  

        return response
