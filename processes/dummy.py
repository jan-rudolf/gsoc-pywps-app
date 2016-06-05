from pywps import Process, LiteralInput, LiteralOutput


class Dummy(Process):
    def __init__(self):
        inputs = []
        outputs = [LiteralOutput('output', 'Output', data_type='string')]

        super(Dummy, self).__init__(
            self._handler,
            identifier='dummy',
            version='None',
            title='Dummy Process',
            abstract='This is dummy process, nothing useful.',
            profile='',
            wsdl='',
            metadata=['Sleep', 'Wait', 'Delay'],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.outputs['output'].data = 'Done. Haha.'

        return response