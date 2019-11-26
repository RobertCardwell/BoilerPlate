# this goes in MyProject/src/myproject/settings/

from .base import *

from .production import *

try:
   from .local import *
except:
   pass
