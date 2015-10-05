# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('/'.join(os.getcwd().split('/')[:-1]))


def main():
    from lib import app
    app.run(debug=True)


if __name__ == '__main__':
    main()

