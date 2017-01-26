"""Helper class to collect EXIF informations."""

import re
import os.path
import imgrename.EXIF as exif

def get_creation_date(imgPath):
    """Gets the creation date of the image.
        
        Args: 
            imgPath (string): Path to the image file.
        
        Returns:
            Date image was created in the format yyyy-mm-dd
            or 'None' if no tags could be found.
        
        Raises:
            FileNotFoundError
    """
    if os.path.isfile(imgPath) is not True:
        raise FileNotFoundError(" ".join(["File", imgPath, "not found."]))
    
    tags = get_tags(imgPath)
    if tags is not None:
        datePattern = re.compile(r"(\d\d\d\d):(\d\d):(\d\d)")
        try:
            matchObject = datePattern.search(str(tags["EXIF DateTimeOriginal"]))
            return matchObject.group().replace(":", "-")
        except KeyError:
            return None
    else:
        return None


def get_tags(imgPath, stop_tag="DateTimeOriginal"):
    """Gets the EXIF tags of the image.

        Args:
            imgPath (string): Path to the image file.
            stop_tag (string): Stops processing after stop_tag is retrieved.
                              
        Returns:
            dictionary: EXIF tags.
            None: If no EXIF tags could be read.
    """
    try:
        with open(imgPath, "rb") as img:
            #Returns tags or an empty dictionary
            tags = exif.process_file(img, stop_tag)
            if len(tags) != 0:
                return tags
            else:
                return None
    except EnvironmentError:
        return None