from pywps import Process, LiteralInput, LiteralOutput


class Sleep(Process):
    def __init__(self):
        inputs = [LiteralInput('delay', 'Delay between every update', data_type='integer')]
        outputs = [LiteralOutput('sleep_output', 'Sleep Output', data_type='string')]

        super(Sleep, self).__init__(
            self._handler,
            identifier='sleep',
            version='None',
            title='Sleep Process',
            abstract='This process will sleep for a given delay or 10 seconds if not a valid value',
            profile='',
            metadata=['Sleep', 'Wait', 'Delay'],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        import time

        response.update_status('Process started. Waiting...', 0)

        sleep_delay = request.inputs['delay'][0].data
    
        if sleep_delay:
            sleep_delay = int(sleep_delay)*10
        else:
            sleep_delay = 10

        time.sleep(sleep_delay)
        response.update_status('Process running...', 20)
        time.sleep(sleep_delay)
        response.update_status('Process running...', 40)
        time.sleep(sleep_delay)
        response.update_status('Process running...', 60)
        time.sleep(sleep_delay)
        response.update_status('Process running...', 80)
        time.sleep(sleep_delay)
        response.outputs['sleep_output'].data = 'done sleeping'

        return response