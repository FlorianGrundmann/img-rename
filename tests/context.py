import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import main
from imgrename import core as ir
from imgrename import EXIF, exifutil, fileutil, slogging
