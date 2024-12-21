# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 06:48:09 2024

@author: mcmah
"""
import os
import sys
import shutil
import unittest
import CreateLogfilename

class Testing(unittest.TestCase):

    def test_NoLogsFolder(self):
        # Delete Logs folder, if it exists
        path = os.path.abspath(os.getcwd())
        path += "\\Logs"
        print(path)
        if os.path.exists(path):
            shutil.rmtree(path)
        folderIsGone = os.path.exists(path)    
        self.assertFalse(folderIsGone)
        
        # Call CreateLogfilename() and verify Logs folder exists.
        CreateLogfilename.CreateLogfilename()
        folderIsThere = os.path.exists(path)    
        self.assertTrue(folderIsThere)

    

if __name__ == '__main__':
    unittest.main()