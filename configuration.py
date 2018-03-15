# -*- coding: utf-8 -*-

# Python imports
#import os
#import libxml2
#import pickle
import ConfigParser

# Application importsfile
from views.dialogs import PreferenceDialog, EIQWDialog
from utils.fileutils import FileUtil
from utils.definitions import CONFIG_ROOT, CONFIG_DIR, CONF_FILENAME, \
                                DEFAULT_CONF  # , TYPE_REPR

config = ConfigParser.RawConfigParser(allow_no_value=True)


class ConfigurationParser(object):
    '''class doc'''

    def __init__(self):
        '''
            Correct 'HOME' string, check for configdir, create
            appdir folder and name application config file.
        '''
        #Check for root configuration folder
        if not FileUtil().folder_exists(CONFIG_ROOT):
            title = "WARNING"
            message = "Configuration root folder ~/.config doesn't exist. " \
                        "Using default configuration."
            args = title, message
            EIQWDialog(*args).run()
            return
        #Check for application configuration folder and create
        if not FileUtil().folder_exists(CONFIG_DIR):
            FileUtil().create_folder(CONFIG_DIR)
        self.options = DEFAULT_CONF
        self.appconfig = CONF_FILENAME
        pass

    def parse(self):
        """Parse a configuration file"""
        if FileUtil().file_exists(self.appconfig):
            config.read(self.appconfig)
            for sec in config.sections():
                pass
                #print
                #print(sec)
                #options = config.options(sec)
                #for opt in options:
                    ##config.get(sec, opt)
                    #print(opt + ' = ' + config.get(sec, opt))
                    ##val = config.get(sec, opt)
                    ##if val == '-1':
                        ##val = -1
                        ##print
                        ##print(opt + ' = ' + str(val))
                        ##print("skip: " + opt)
                    ##else:
                        ##print(opt + ' = ' + val)
                ##print
                ##print(sec + ': dict1')
                ##self.config_section_map(sec)
        else:
            self.write_default()
        return config

    def config_section_map(self, section):
        """Map section options to a dictionary"""
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                #if dict1[option] == -1:
                    #print("skip: " + option)
                    ##DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        print(dict1)
        return  # dict1

    def get_prefs(self, *args):  # args instead of builder
        """Get preferences from the dialog"""
        #builder, parent = args[0], args[1]  # don't need this
        #args = builder, None  # or this
        kwargs = {}
        kwargs = PreferenceDialog(*args, **kwargs).run()
        #self.write()
        return kwargs

    def set_config(self, sec, opt, val):
        """Set a config option"""
        config.set(sec, opt, val)
        self.write()
        return

    def write_default(self):
        """Write default configuration to config"""
        n = 0
        for sec in self.options:
            if not isinstance(sec, dict) and not isinstance(sec, tuple):
                config.add_section(sec)
            n += 1
            if n < len(self.options):
                for opt in self.options[n]:
                    if isinstance(opt, dict):
                        for k, v in opt.items():
                            config.set(sec, k, v)
        self.write()
        return

    def write(self):
        """Write configuration file"""
        try:
            with open(self.appconfig, 'wb') as configfile:
                config.write(configfile)
        except:
            return 'FALSE'
        return

    pass  # end of class ConfigurationParser
