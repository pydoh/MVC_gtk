# -*- coding: utf-8 -*-

# Python imports
import os

# Application imports
#from utils import definitions


class FileUtil(object):
    """Manage file operations"""
    # initialization is explicit
    def __init__(self):
        """"""
        return

    def get_home(self):
        return os.getenv('HOME')

    def folder_exists(self, foldername):
        """Check if a folder already exists."""
        return os.path.isdir(foldername)

    def create_folder(self, foldername):
        """Create a new folder"""
        if not os.path.exists(foldername):
            return os.mkdir(foldername)

    def file_exists(self, filename):
        """Check if a file already exists."""
        if filename is not None:
            return os.path.isfile(filename)

    def write_file(self, filename, text):
        """Write text to filename"""
        try:
            #TODO: For python3
            #mode='w', encoding='utf-8'  # You can never go wrong with utf-8.
            with open(filename, 'w') as outfile:  # as [variable]
                outfile.write(text)
        except:
            #title = "Error saving file!"
            #message = "Could not save file:" + "\n" + "%s"
            #return False, title, message
            print("Error writing file:\n", filename)
        return

    def read_file(self, filename):
        """Read content from filename"""
        try:
            with open(filename, 'r') as tmpfile:
                content = tmpfile.read()
                return content
        except:
            #title = "Error reading file!"
            #message = "Could not read file:" + "\n" + "%s"
            #return False, title, message
            print("Error reading file:\n", filename)
        return

    def file_or_folder(self, folder):
        """Check if file or folder"""
        fillist, follist = [], []
        for fil in os.listdir(folder):
            if os.path.isfile(fil):
                fillist.append(fil)
            elif os.path.isdir(fil):
                follist.append(fil)
        fillist.sort()
        follist.sort()
        #[follist.append(j) for j in fillist]
        return fillist, follist

    pass  # End of class FileUtil
