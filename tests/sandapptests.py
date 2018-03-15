import unittest

from ctrls.sandcontrol import SandCtrl


class SandboxTests(unittest.TestCase):
    """Test validity"""

    def testGuiTrue(self):
        """Test the control script"""
        result = SandCtrl()
        #if result is not None:
            #result = True
        self.failUnless(result is not None)

    #def testSandboxModelFalse(self):
        #""""""
        #self.failIf(result is True)

    pass  # End of class SandboxTests


def main():
    """Run tests"""
    unittest.main()

if __name__ == '__main__':
    main()
