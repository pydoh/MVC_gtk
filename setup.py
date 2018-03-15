# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

#import sys

# may god have mercy on my soul
from setuptools import setup


setup(name='sandbox',
    version='0.1.0',
    author='Who Knows',
    author_email='whoknows@no.mail',
    maintainer='Who Knows',
    maintainer_email='whoknows@no.mail',
    description='Example environment',
    packages=['models', 'views', 'ctrls', 'utils',
                'resources.glade', 'resources.styles'],
    package_data={'resources.glade': ['*.glade'], },
    scripts=['sandbox'],
#    entry_points={'console_scripts': ['sandbox = ctrls:main'], },
)
