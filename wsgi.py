import sys, os


sys.stdout = sys.stderr

sys.path.insert(0, '/Users/janrudolf/Sites/gsoc-pywps-env/src/pywps/pywps/')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


from pywps.app import Service
from pywps import configuration

from processes.sleep import Sleep
from processes.dummy import Dummy


configuration.load_configuration(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pywps.cfg"))

processes = [Sleep(), Dummy()]

application = Service(processes=processes)