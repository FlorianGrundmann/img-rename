"""Utility module which simplifies the use of the python loggin module.

    TODO:
        * Enable to load the config file from sub folders.
"""

import logging
import logging.config


def get_logger(name):
    """Returns a fully configured and ready to use logger.

    This function creates a logger object with the given name und configures
    it with a 'logging.conf' file. 
    This file has to be in same folder like the module. 

    Args:
        name(string): Name for the logger.
    Return:
        logger: Configured logger.
    """

    logging.config.fileConfig("imgrename\\logging.conf")
    logger = logging.getLogger(name)
    return logger