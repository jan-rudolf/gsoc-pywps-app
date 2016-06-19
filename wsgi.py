import os

###############
#can be deleted
import sys
#this line could be deleted thanks to Apache config
sys.stdout = sys.stderr
#this 3 lines are needed because of develop mode of python package
sys.path.insert(0, '/Users/janrudolf/Sites/gsoc-pywps-env/src/pywps/pywps/')
sys.path.insert(0, '/Users/janrudolf/Sites/gsoc-pywps-env/src/pywps/pywps/server/app/')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
###############

from pywps.server.wsgi import *

from processes.sleep import Sleep
from processes.dummy import Dummy
from processes.buffer import Buffer

#PyWPS configuration file
pywps_configuration_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pywps.cfg")
#PyWPS processes
pywps_processes = [Sleep(), Dummy(), Buffer()]

application = ServerConnection(processes=pywps_processes, configuration_file=pywps_configuration_file).run()