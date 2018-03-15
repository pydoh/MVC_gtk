# -*- coding: utf-8 -*-

# Application imports
from views.dialogs import FileChooserDialog, PreferenceDialog, EIQWDialog


class FileDialogCtrl(FileChooserDialog):
    """OpenFileDialog controller class"""
    def __init__(self, *args):
        res = FileChooserDialog.__init__(self, *args)
        #print("res: ", res)
        return res

    #def File logic here?

    def run(self):
        return FileChooserDialog.run(self)

    pass  # end of class FileDialogCtrl


class PreferenceCtrl(PreferenceDialog):
    """"""
    def __init__(self, *args, **kwargs):
        prefres = PreferenceDialog.__init__(self, *args, **kwargs)
        return prefres

    #def Preference logic here?

    def config_ran(self, *args):
        #TODO: Temporary, for testing dialogs
        eiqwres = EIQWDialog(*args).run()
        return eiqwres

    def run(self):
        prefres, kwargs = PreferenceDialog.run(self)
        if prefres == "ACCEPT":
            #ERROR, INFO, QUESTION, WARNING
            args = "INFO", "INFO & PREFERENCE test", \
                                        "You chose to SAVE the PREFERENCES"
        elif prefres == "CANCEL":
            args = "INFO", "INFO & PREFERENCE test", \
                                        "You chose to CANCEL the PREFERENCES"
        self.config_ran(*args)
        return

    pass  # end of class PreferenceCtrl
