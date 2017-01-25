"""Module which renames all image files in the current working directory

    This module searches in the current working directory for image files
    and changes it names to include the date created.
    A file 'picture.jpg' becomes '2016-02-01-img.jpg'.
    If there is already a file with that name, an additional number will be
    appended (e.g. '2016-02-01-img-2.jpg')

    It does that by reading the EXIF data of the images.

    To change all image names in an directory just call:
        >> imgrename.rename_imgs(<dirPath>)

    Methods:
        rename_imgs(dirPath): Renames all images in dirPath, if possible.
        create_name(imgPath): Creates a name for the image based on it's
                                creation date.
        
"""

import os
import os.path

import imgrename.EXIF as exif
import imgrename.fileutil as fu
import imgrename.exifutil as eu

import imgrename.slogging as slogging


logger = slogging.get_logger("imgrename")


def rename_imgs(dirPath):
    """This methods renames all images in at the given directory.
        
        Args:
            dirPath(string): Path to the directory with the images that should
                                be renamed.
        
    """
    imgs = fu.get_all_file_names(dirPath, ".jpg")
    if imgs is not None:
        logger.info("Found {0} images in {1}. Starting to rename files.".format(len(imgs), dirPath))
        n = 0
        for img in imgs:
            name = get_new_name(os.path.join(dirPath, img), dirPath)
            if name is not None:
                n += 1
                os.rename(os.path.join(dirPath, img), os.path.join(dirPath, name))
        
        logger.info("Finished renaming.")
        logger.info("Renamed {0} files. Failed to rename {1} files.".format(n, len(imgs)-n))

def _search_for_files(dirPath, extension):
    try:
        return fu.get_all_file_names(dirPath, extension)
    except NotADirectoryError:
        logger.error("Path doesn't exist or is not a directory")
        return None


def get_new_name(imgPath, destinationPath):
    """Creates a new name for the img based on it's creation date.
    
    Args:
        imgPath (string): Path to the image.

    Returns:
        string: New file name
        None: If no EXIF data could be found.
    """
    
    date = eu.get_creation_date(imgPath)
    if date is None:
        logger.debug("Couldn't get creation date for the file {0}".format(imgPath))
        return
    n = 0
    name = _construct_name(date, n)
    new_path = os.path.join(os.path.dirname(imgPath), name)
    while os.path.isfile(new_path) == True:
        n += 1
        name = _construct_name(date, n)
        new_path = os.path.join(os.path.dirname(imgPath), name)
    
    return name

def _construct_name(date, n):
    """Helper method to construct a name including the directory path"""
    name = "".join((date, "-img-", "{:03d}".format(n), ".jpg"))
    return name


    