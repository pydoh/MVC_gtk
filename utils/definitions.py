# -*- coding: utf-8 -*-

# Python imports
import os.path
import sys

if sys.argv[0]:
    TOP_DIR = os.path.split(os.path.split(__file__)[0])[0]
    #print(top_dir)
    #top_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
else:
    TOP_DIR = "."

# ----------------------------------------------------------------------
HOME = os.getenv('HOME')

RESOURCES_DIR = os.path.join(TOP_DIR, "resources")
GLADE_DIR = os.path.join(RESOURCES_DIR, "glade")
MAIN_GLADE = os.path.join(GLADE_DIR, "mvc_gtk.glade")
DIALOGS_GLADE = os.path.join(GLADE_DIR, "dialogs.glade")
#_GLADE =

STYLES_DIR = os.path.join(RESOURCES_DIR, "styles")
CONFIG_ROOT = HOME + '/.config'
CONFIG_DIR = HOME + '/.config/sandbox'
CONF_FILENAME = HOME + '/.config/sandbox/sandbox.cfg'
APPL_SHORT_NAME = "sandbox"
APPL_VERSION = (0, 1, 0)
# ----------------------------------------------------------------------

# Configuration --------------------------------------------------------
DEFAULT_CONF = (
            'General', (
                    {'projects_default_dir': HOME + '/Projects'},
                    {'remember_opened_files': True},
                    {'remember_opened_files_cl': True},
                    {'opened_files': ''},
                    {'reload_on_crash': True},
                    {'web_browser': ''},
                    {'run_file_if_no_project': True}
                    ),
            'Appearance', (
                    {'sidebar_position': ''},
                    {'main_toolbar_text': True},
                    {'editor_toolbar_text': True},
                    {'doc_toolbar_text': True},
                    {'hide_sidebar': False},
                    {'hide_main_toolbars': False},
                    {'hide_editor_toolbar': False}
                    ),
            'Compilation', (
                    {'compile_action': 'project'},
                    {'auto_close_compiler': False},
                    ),
            'Editor', (
                    {'insert_spaces_instead_of_tabs': True},
                    {'tabs_width': 4},
                    {'editor_font': 'Monospace Bold 11'},
                    {'wrap_mode': True}
                    ),
            'Documentation', (
                    {'url': []},
                    {'pydoc_html': []},
                    {'pydoc_text': []},
                    {'hide_sidebar_on_doc': True},
                    {'hide_toolbars_on_doc': True},
                    {'python_doc_auto_completion': -1},
                    {'devhelp_index': -1}
                    ),
            'Terminal', (
                    {'cd_term_to_prj_dir': False},
                    {'close_term_exec_end': False}
                    ),
            'Filebrowser', (
                    {'cd_browser_to_prj_dir': True},
                    )
            )

        #'dock_layout': ('horizontal', 1, gtk.gdk.screen_width() - 400),

    #'Tags': {
            #('BUG!', {'desc': lang.get_string('BUG!'), 'foreground': '#FF0000',
                #'bold': True, 'background': '#FFFF00', 'italic': False}),
            #('BUG', {'desc': lang.get_string('BUG'), 'foreground': '#FF0000',
                #'bold': True, 'background': '#FFFFFF', 'italic': False}),
            #('TODO!', {'desc': lang.get_string('TODO!'), 'foreground': '#000000',
                #'bold': True, 'background': '#FFFFFF', 'italic': False}),
            #('TODO', {'desc': lang.get_string('TODO'), 'foreground': '#000000',
                #'bold': False, 'background': '#FFFFFF', 'italic': False}),
            #('IDEA', {'desc': lang.get_string('IDEA'), 'foreground': '#636363',
                #'bold': False, 'background': '#FFFFFF', 'italic': False}),
            #'show_todo': True,
            #},
# ----------------------------------------------------------------------
