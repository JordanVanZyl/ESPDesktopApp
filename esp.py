import requests
from dateutil import parser
import json
import credentials as cred

class ESPCaller:

    def __init__(self, area_id) -> None:
        self.credentials = cred.Credentials()
        self.area_id = area_id
        self.url = f'https://developer.sepush.co.za/business/2.0/area?id={self.area_id}'
        self.payload = {}
        self.headers = {'token':f'{self.credentials.GetESPApiKey()}'}

    def get_next_schedules(self) -> str:  
        res = requests.request('GET', self.url, headers=self.headers, data=self.payload)
        parsed_response = self.parse_response(res)

        return parsed_response
    
    def parse_response(self, res) -> str:
        #TODO: Display names for days of the week instead of date
        schedule_string = ''
        res = json.loads(res.text)

        for event in res['events']:
            start = parser.parse(event['start'], ignoretz=True)
            end = parser.parse(event['end'], ignoretz=True)
            schedule_string += event['note']+'\n'\
                                +f'\tStart: {start}\n'\
                                +f'\tEnd: {end}\n'

        return schedule_string