#can be deleted
import sys, os

#this line could be deleted thanks to Apache config
sys.stdout = sys.stderr
#this 3 lines are needed because of develop mode of python package
sys.path.insert(0, '/Users/janrudolf/Sites/gsoc-pywps-env/src/pywps/pywps/')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

#these to I want to delete
from pywps.app import Service
from pywps import configuration

#this will remain
from pywps.server.app import main

#this 2 are needed
from processes.sleep import Sleep
from processes.dummy import Dummy

#this want to delete
configuration.load_configuration(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pywps2.cfg"))

#needed/can delete
processes = [Sleep(), Dummy()]

#needed
application = Service(processes=processes)