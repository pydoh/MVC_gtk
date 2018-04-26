# -*- coding: utf-8 -*-

# Ptyhon imports
#import os

# Application imports
from views.mainview import MainView
#from views.dialogs import EIQWDialog
from controls.dialogsctrl import FileDialogCtrl
from controls.configuration import ConfigurationParser
from models.mainmodel import MainModel

from utils.definitions import TOP_DIR

# Instantiate and return objects, 0.1.0 and 0.2.0
MainView = MainView()
# we import all of our Gtk stuff in the view, but we want to do
# builder.connect_signals() and Gtk.main_quit() here in mainctrl
Gtk, builder = MainView.return_objects()
MainModel = MainModel()


class MainCtrl(object):
    """"""

    def __init__(self):
        """
        0.3.0 Instantiate view and model globally
        0.4.0 Now we have a test runner script
        0.5.0 And now basic dialogs
        0.6.0 A crude setup.py script
        0.7.0 configuration.py
        """

        # This will help determine what is self
        #print(dir(self))

        #TODO Parse or write, not both
        self.parse_config()

        self.connect_signals()
        return

    def connect_signals(self):
        """"""
        sigs = {
            'on_mainwindow_destroy': self.on_mainwindow_destroy,
            # File menu
            'on_open_activate': self.on_open_activate,
            'on_save_activate': self.on_save_activate,
            'on_saveas_activate': self.on_saveas_activate,
            'on_new_activate': self.on_new_activate,
            'on_quit_activate': self.on_quit_activate,
            # Edit menu
            "on_preference_activate": self.on_preference_activate,
            }
        builder.connect_signals(sigs)
        return

    def register_view(self):
        """"""
        # setup of widgets
        return

    def register_adapters(self):
        """"""
        # setup of adapters
        return

    # ---------------------------------------------------------------
    #        Signal handlers
    # ---------------------------------------------------------------
    def on_mainwindow_destroy(self, event):
        """"""
        Gtk.main_quit()  # say goodbye
        return True

    def on_new_activate(self, event):
        return

    def on_open_activate(self, event):
        args = builder, "OPEN", "Open file", "False", "False", TOP_DIR, \
                MainView.mainwindow
        filename = FileDialogCtrl(*args).run()
        #print("filename: ", filename)
        #('res: ', None)
        #('filename: ', '')
        #('res: ', None)
        #('filename: ', -3)
        return filename

    def on_save_activate(self, event):
        args = builder, "SAVE", "Save file", "False", "False", TOP_DIR
        filename = FileDialogCtrl(*args).run()
        return filename

    def on_saveas_activate(self, event):
        args = builder, "SAVE", "Save file as", "False", "False", TOP_DIR, \
                MainView.mainwindow
        filename = FileDialogCtrl(*args).run()
        return filename

    def on_quit_activate(self, event):
        Gtk.main_quit()
        return True

    def on_preference_activate(self, event):
        args = builder, MainView.mainwindow
        kwargs = ConfigurationParser().get_prefs(*args)
        return kwargs

    def parse_config(self):  # get_config
        """Read the configuration file"""
        #TODO
        # Parsing and naming of configuration attributes
        self.config = ConfigurationParser().parse()
        ##cats = ('General', 'Appearance', 'Editor', 'Documentation')
        ##for cat in cats:
        for sec in self.config.sections():
            options = self.config.options(sec)
            for att in options:
                try:
                    attval = self.config.get(sec, att)
                    # Name the attributes
                    super(MainCtrl, self).__setattr__(att, attval)
                    #print(att)
                except TypeError:
                    print('Broken')
                    continue

        #openfiles = self.textfile, self.imagefile
        #for f in openfiles:
            #if FileCtrl.file_exists(f) is True:
                #path, name, ext = FileCtrl.split_path(f)
                #if f.endswith('.txt'):
                    #content = FileCtrl.read_file(f)
                    #MainView.filenamelabel.set_text(name)
                    #MainView.load_texbuff(content)
                #elif f.endswith('.png'):
                    #MainView.imagefile = self.imagefile
            #else:
                #self.config.set('General', f, None)
                #self.write_config()
        return

    def write_config(self):  # set_config
        """Write the configuration file"""
        return ConfigurationParser().write()

    pass  # end of class MainCtrl
