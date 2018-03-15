#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# Python imports
import os.path
import sys

# Gtk imports
from gi.repository import Gtk


def setup_path():
    """Sets up the python include paths to include needed directories"""
    from sandbox.utils.definitions import TOP_DIR
    # We change this line;
    #sys.path.insert(0, reduce(os.path.join, (TOPDIR, "resources", "external")))
    # to this, and it works with Python3:
    sys.path.insert(0, os.path.join(TOP_DIR, "resources", "external"))
    sys.path.insert(0, os.path.join(TOP_DIR, "sandbox"))
    return


def check_requirements():
    """Checks versions and other requirements"""
    # Gtk version
    import gi
    try:
        gi.require_version("Gtk", "3.0")
    except:
        sys.exit("This script requires Gtk 3.0 or newer!")
    #print(Gtk.get_major_version(),
            #Gtk.get_minor_version(),
                #Gtk.get_micro_version())  # 3L, 10L, 9L

    # Python version
    if sys.version_info < (2, 7, 5):
        sys.exit("This script requires Python 2.7.5 or newer!")
    #print(sys.version[0:5])

    return


def main(*args, **kargs):
    """"""
    # Application imports
    from ctrls.mainctrl import MainCtrl as MainCtrl

    MainCtrl()

    Gtk.main()
    return

if __name__ == "__main__":
    #setup_path()
    check_requirements()
    main()
    pass
