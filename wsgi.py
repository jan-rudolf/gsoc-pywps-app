#!/usr/bin/env python3
import sys, os

sys.stdout = sys.stderr

sys.path.insert(0, '/Users/janrudolf/Sites/gsoc-pywps-env/src/pywps/pywps/')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


#def application(environ, start_response):
#    status = '200 OK'
#    output = 'Hello World!'

#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]

#    start_response(status, response_headers)

#    return [output]

import pywps
from pywps.app import Service, Process
from pywps import configuration
from pywps import Process, LiteralInput, LiteralOutput


class Sleep(Process):
    def __init__(self):
        #inputs = [LiteralInput('delay', 'Delay between every update', data_type='float')]
        inputs = []
        outputs = [LiteralOutput('sleep_output', 'Sleep Output', data_type='string')]

        super(Sleep, self).__init__(
            self._handler,
            identifier='sleep',
            version='None',
            title='Sleep Process',
            abstract='This process will sleep for a given delay or 10 seconds if not a valid value',
            profile='',
            wsdl='',
            metadata=['Sleep', 'Wait', 'Delay'],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        import time

        #sleep_delay = request.inputs['delay'].data
        sleep_delay = False
        if sleep_delay:
            sleep_delay = float(sleep_delay)
        else:
            sleep_delay = 10

        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 20)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 40)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 60)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 80)
        time.sleep(sleep_delay)
        response.outputs['sleep_output'].data = 'done sleeping'

        return response

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pywps.cfg")
configuration.load_configuration(config_file)

application = Service(processes=[Sleep()])