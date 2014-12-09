#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

def db():
    try:
        return mdb.connect('127.0.0.1', 'root', '112233', 'psit_project')
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)



