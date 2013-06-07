import subprocess
from battiboy import *
if iscrsitical():
    subprocess.Popen(["notify-send", 'BATTERY', 'Bayyery low, you dig ?'])
    tempfile.mkstemp(suffix='.pybat')
