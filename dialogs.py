# -*- coding: utf-8 -*-

# Gtk imports
from gi.repository import Gtk  # , Gdk, GdkPixbuf, Pango, GObject

# Application imports
from utils.definitions import DIALOGS_GLADE


class FileChooserDialog(object):
    """A basic file chooser dialog"""
    def __init__(self, *args):
        self.gladefile = DIALOGS_GLADE
        builder = args[0]
        builder.add_from_file(self.gladefile)
        self.filechooser = builder.get_object("filechooser")
        action = self.conf_chooser(*args)
        self.filechooser.set_action(action)
        self.filechooser.set_title(args[2])
        self.filechooser.set_current_folder(args[5])  # Not recommended
        self.filechooser.set_transient_for(args[6])
        #print(args[6])
        pass

    def conf_chooser(self, *args):
        if args[1] is "OPEN":
            action = Gtk.FileChooserAction.OPEN
            self.filechooser.add_buttons(Gtk.STOCK_CANCEL,
                                            Gtk.ResponseType.CANCEL,
                                            Gtk.STOCK_OPEN,
                                            Gtk.ResponseType.ACCEPT)
        elif args[1] is "SAVE":
            action = Gtk.FileChooserAction.SAVE
            self.filechooser.add_buttons(Gtk.STOCK_CANCEL,
                                            Gtk.ResponseType.CANCEL,
                                            Gtk.STOCK_SAVE,
                                            Gtk.ResponseType.ACCEPT)
        #if args[3] is "True":
            #self.filechooser.set_select_multiple(True)
        #if args[4] is "True":  # Not working
            #self.filechooser.set_show_hidden(True)  # Not working
        #print(self.filechooser.get_show_hidden())  # for testing
        return action

    def run(self):
        self.filechooser.show_all()
        res = self.filechooser.run()
        if res == Gtk.ResponseType.OK:
            if self.filechooser.get_select_multiple():
                res = self.filechooser.get_filenames()
            else:
                res = self.filechooser.get_filename()
        elif res == Gtk.ResponseType.CANCEL:
            if self.filechooser.get_select_multiple():
                res = []
            else:
                res = ''
        self.filechooser.destroy()
        return res

    pass  # end of class FileChooserDialog


class PreferenceDialog(object):
    """"""
    def __init__(self, *args):
        self.gladefile = DIALOGS_GLADE
        builder = args[0]
        builder.add_from_file(self.gladefile)
        self.prefdialog = builder.get_object("prefdialog")
        self.prefdialog.add_buttons(Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_SAVE,
                                        Gtk.ResponseType.ACCEPT)
        self.prefdialog.set_title("Preferences")
        self.prefdialog.set_transient_for(args[1])
        return

    def get_config(self):
        """Get config from dialog"""
        return

    def set_config(self):
        """Set config in dialog"""
        return

    def run(self, *args, **kwargs):
        prefres = self.prefdialog.run()
        if prefres == Gtk.ResponseType.ACCEPT:
            prefres = "ACCEPT"
            kwargs = {"ACCEPT": "ACCEPT"}  # self.get_config()
        elif prefres == Gtk.ResponseType.CANCEL:
            prefres = "CANCEL"
            kwargs = {"CANCEL": "CANCEL"}
        self.prefdialog.destroy()
        return prefres, kwargs

    pass  # end of class PreferenceDialog


class EIQWDialog(Gtk.MessageDialog):
    """A basic ERROR, INFO, QUESTION, WARNING dialog"""
    def __init__(self, *args):
        eiqwtype, button = self.conf_eiqw(*args)
        title, message = args[0], args[1]
        self.eiqwdialog = Gtk.MessageDialog(self, 0, eiqwtype, button, title)
        self.eiqwdialog.format_secondary_text(message)
        pass

    def conf_eiqw(self, *args):
        if args[0] == "ERROR":
            eiqwtype = Gtk.MessageType.ERROR
            button = Gtk.ButtonsType.CANCEL
        elif args[0] == "INFO":
            eiqwtype = Gtk.MessageType.INFO
            button = Gtk.ButtonsType.OK
        elif args[0] == "QUESTION":
            eiqwtype = Gtk.MessageType.QUESTION
            button = Gtk.ButtonsType.YES_NO
        elif args[0] == "WARNING":
            eiqwtype = Gtk.MessageType.WARNING
            button = Gtk.ButtonsType.OK_CANCEL
        return eiqwtype, button

    def run(self):
        eiqwres = self.eiqwdialog.run()
        if eiqwres == Gtk.ResponseType.OK:
            eiqwres = "OK"
        elif eiqwres == Gtk.ResponseType.CANCEL:
            eiqwres = "CANCEL"
        elif eiqwres == Gtk.ResponseType.YES:
            eiqwres = "YES"
        elif eiqwres == Gtk.ResponseType.NO:
            eiqwres = "NO"
        self.eiqwdialog.destroy()
        return eiqwres

    pass  # end of class EIQWDialog
