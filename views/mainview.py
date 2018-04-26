# -*- coding: utf-8 -*-

# Python imports
import sys

# Gtk imports
import gi
try:
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
except:
    sys.exit("This script requires Gtk 3.0 or newer!")

# Application imports
from utils.definitions import MAIN_GLADE
#from views.dialogs import FileChooserDialog, PreferenceDialog, EIQWDialog

# Instantiate and pass objects, 0.1.0 and 0.2.0
builder, buildable = Gtk.Builder(), Gtk.Buildable


class MainView(object):
    """"""
    def __init__(self):
        """Initializes the mainview"""
                                        # for testing
        self.gladefile = MAIN_GLADE
        self.builder = builder
        self.buildable = buildable
        self.builder.add_from_file(self.gladefile)

        # sandbox-0.2.0 Auto construction of (buildable) widgets
        for wid in self.builder.get_objects():
            try:
                widname = self.buildable.get_name(wid)
                widobj = self.builder.get_object(widname)
                # Name buildable widgets
                super(MainView, self).__setattr__(widname, widobj)
            except TypeError:
                continue

        # sandbox-0.2.0 Manual construction of (non-buildable) widgets
        # This will help determine what widgets are buildable
        #
        #(dir(self))
        # Buffers
        # Models
        # Filters
        # Renderers
        # Adjustments

        # Settings and configuration

        self.mainwindow.show()

        #self.return_objects()
        return None

    def file_chooser(self, *args):
        """"""
        #(<Builder object at 0x7ff01c1c6370 (GtkBuilder at 0x1900290)>, 'OPEN',
        #'Open file', 'False', 'False',
        #'/home/kmetzker/projects/VirtualEnvs/Sandbox/Sandbox',
        #<Window object at 0x7ff0132d9780 (GtkWindow at 0x1a3c230)>)

        #nargs = builder, args[0], args[1], args[2], args[3], args[4], \
                    #self.mainwindow

        # We seem to only use the FileChooserDialog.run(self)
        #return FileChooserDialog(*nargs).run(self)
        pass

    def return_objects(self):
        """Returns Gtk and builder objects to the control module so that
            we can do Gtk.main.quit() and builder.connect_signals()"""
        return Gtk, builder

    pass  # end of class MainView


#class FileDialogCtrl(FileChooserDialog):
    #"""OpenFileDialog controller class"""
    #def __init__(self, *args):
        #res = FileChooserDialog.__init__(self, *args)
        #return res

    ##def File logic here?

    #def run(self):
        #return FileChooserDialog.run(self)

    #pass  # end of class FileDialogCtrl


#class PreferenceCtrl(PreferenceDialog):
    #""""""
    #def __init__(self, *args, **kwargs):
        #prefres = PreferenceDialog.__init__(self, *args, **kwargs)
        #return prefres

    ##def Preference logic here?

    #def config_ran(self, *args):
        ##TODO: Temporary, for testing dialogs
        #eiqwres = EIQWDialog(*args).run()
        #return eiqwres

    #def run(self):
        #prefres, kwargs = PreferenceDialog.run(self)
        #if prefres == "ACCEPT":
            ##ERROR, INFO, QUESTION, WARNING
            #args = "INFO", "INFO & PREFERENCE test", \
                                        #"You chose to SAVE the PREFERENCES"
        #elif prefres == "CANCEL":
            #args = "INFO", "INFO & PREFERENCE test", \
                                        #"You chose to CANCEL the PREFERENCES"
        #self.config_ran(*args)
        #return

    #pass  # end of class PreferenceCtrl

        #TODO SANDBOX--------------------------------------
        #TODO
        #TODO
        #TODO SANDBOX--------------------------------------
