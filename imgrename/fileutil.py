"""Helper module for handling files on the os."""

import os
import os.path

def get_all_file_names(path, extension=None):
    """Returns all files in the given directory.
    
        Args:
            path(string): Path to an existing directory.
            extension(string, optional): Set this to get only a certain 
                                        filetype, for example '.txt'. 
                                        Default: None
        
        Returns:
            list: List of file names.
    
        Raises:
            NotADirectoryError: If path doesn't exist or is not a directory.
    """
    if os.path.isdir(path):
        files = os.listdir(path)
        if extension is None:
            return files
        else:
            return _filter_files(files, extension)
    else:
        error_msg = "Path doesn't exist or is not a directory"
        raise NotADirectoryError(error_msg)

def _filter_files(files, extension):
    filtered_files = []
    for file in files:
        if file.lower().endswith(extension):
            filtered_files.append(file)
    return filtered_files
    
