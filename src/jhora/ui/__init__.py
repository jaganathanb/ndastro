import os
import sys
path_root = os.path.dirname(os.path.abspath('../../'))
if path_root not in sys.path:
    sys.path.append(str(path_root))
    print('ui',path_root,'added to system path',sys.path)