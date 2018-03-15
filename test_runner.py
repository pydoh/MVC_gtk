#!/usr/bin/env python

import unittest
import sys

suite = unittest.TestLoader().discover('tests', 'sandapptests.py')
#suite = unittest.TestLoader().discover('tests', 'sandapptests.py')

results = unittest.TextTestRunner(verbosity=2).run(suite)
if len(results.errors) > 0 or len(results.failures) > 0:
    sys.exit(1)

sys.exit()
