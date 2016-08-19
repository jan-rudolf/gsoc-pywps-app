#activation of Virtualenv's Python
#activate_this = '/Users/janrudolf/Sites/gsoc-pywps-env/bin/activate_this.py'
activate_this = '/var/www/gsoc-pywps-env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os

#this 4 lines are needed only for the develop installation
import sys
sys.stdout = sys.stderr
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


from pywps.server.wsgi import application

from processes.sleep import Sleep
from processes.dummy import Dummy
from processes.buffer import Buffer


#PyWPS configuration file
pywps_configuration_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pywps.cfg")
#PyWPS processes
pywps_processes = [Sleep(), Dummy(), Buffer()]


if __name__ == '__main__':
	#run PyWPS as a demo application locally
	application.run_pywps(processes=pywps_processes, configuration_file=pywps_configuration_file, run_locally=True)
else:
	#let be PyWPS served by a web server
	application.run_pywps(processes=pywps_processes, configuration_file=pywps_configuration_file)
