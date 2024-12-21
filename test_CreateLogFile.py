# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:06:46 2024

@author: mcmah
"""

from loguru import logger
import GetLogFileName

logname = GetLogFileName.CreateLogfilename()

logger.add(logname, format="{time} (level} {message}")
logger.debug("Begin new run.")

    