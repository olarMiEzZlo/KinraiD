#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

def db():
    try:
        return mdb.connect('128.199.148.180', 'psit_project', '1234', 'psit_project')
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)



