# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('/'.join(os.getcwd().split('/')[:-1]))

from lib import app
app.run(debug=True)

