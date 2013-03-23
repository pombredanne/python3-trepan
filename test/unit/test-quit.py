#!/usr/bin/env python3
'Unit test for trepan.processor.command.quit'
import unittest

from import_relative import *

Mquit = import_relative('processor.command.quit', '...trepan')

from cmdhelper import dbg_setup

class TestQuit(unittest.TestCase):
    """Tests QuitCommand class"""

    def test_quit(self):
        """Test processor.command.quit.QuitCommand.run()"""
        d, cp = dbg_setup()
        command = Mquit.QuitCommand(cp)
        try:
            command.run(['quit'])
        except:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        return

if __name__ == '__main__':
    unittest.main()