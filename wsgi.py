#activation of Virtualenv's Python
activate_this = '/var/www/gsoc-pywps-env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os

#this 4 lines are needed only for develop installation
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


application.load_pywps_app(pywps_processes, pywps_configuration_file)