import requests
from dateutil import parser
import json

class ESPCaller:

    def __init__(self, url, payload, headers) -> None:
        self.url = url
        self.payload = payload
        self.headers = headers

    def GetNextSchedules(self):
        res = requests.request('GET', self.url, headers=self.headers, data=self.payload)
        return res
    
class ResponseParser():
    #TODO: Display names for days of the week instead of date
    def __init__(self) -> None:
        self.schedule_string = ''

    def ParseResponse(self, res):
        self.schedule_string = ''
        res = json.loads(res.text)

        for event in res['events']:
            start = parser.parse(event['start'], ignoretz=True)
            end = parser.parse(event['end'], ignoretz=True)
            self.schedule_string += event['note']+'\n'\
                                    +f'\tStart: {start}\n'\
                                    +f'\tEnd: {end}\n'

        return self.schedule_string