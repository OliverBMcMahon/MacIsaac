# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:29:50 2024

@author: mcmah
"""
import os
import time
import unittest
import MyLogger
import CreateLogfilename as clf

class Testing(unittest.TestCase):

    
    
    def test_logInfoMsg(self):
        path =  os.path.abspath(os.getcwd())
        fname = path + "\\Infolog.log"
        MyLogger.logInfoMsg(fname, "test_logInfoMsg")
        with open(fname, 'r') as logfile:
            lines = logfile.read(-1)
        self.assertTrue("test_logInfoMsg" in lines)
        # Clean up - remove log file.
        os.remove(fname)
        
    def test_logDebugMsg(self):
        path =  os.path.abspath(os.getcwd())
        fname = path + "\\Debuglog.log"
        MyLogger.logDebugMsg(fname, "test_logDebugMsg")
        with open(fname, 'r') as logfile:
            lines = logfile.read(-1)
        self.assertTrue("test_logDebugMsg" in lines)
        # Clean up - remove log file.
        os.remove(fname)
        
    def test_logWarnMsg(self):
        path =  os.path.abspath(os.getcwd())
        fname = path + "\\Warnlog.log"
        MyLogger.logDebugMsg(fname, "test_logWarnMsg")
        with open(fname, 'r') as logfile:
            lines = logfile.read(-1)
        self.assertTrue("test_logWarnMsg" in lines)
        # Clean up - remove log file.
        os.remove(fname)
        
    def test_logErrorMsg(self):
        path =  os.path.abspath(os.getcwd())
        fname = path + "\\Errorlog.log"
        MyLogger.logDebugMsg(fname, "test_logErrorMsg")
        with open(fname, 'r') as logfile:
            lines = logfile.read(-1)
        self.assertTrue("test_logErrorMsg" in lines)
        # Clean up - remove log file.
        os.remove(fname)
        
    def test_logFailMsg(self):
        path =  os.path.abspath(os.getcwd())
        fname = path + "\\Faillog.log"
        MyLogger.logDebugMsg(fname, "test_logFailMsg")
        with open(fname, 'r') as logfile:
            lines = logfile.read(-1)
        self.assertTrue("test_logFailMsg" in lines)
        # Clean up - remove log file.
        os.remove(fname)
        
    

if __name__ == '__main__':
    unittest.main()