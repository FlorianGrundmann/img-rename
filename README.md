# img-rename

Small program for renaming image files based on their creation date.

Calling the main.py with a folder as an argument renames all images (.jpg) in that 
folder if the EXIF data can be read.

Example: python main.py C:\imgFolder

## Name format

The new names will have the format yyyy-mm-dd-img-nnn.jpg, 
for example 2016-12-24-img-012.jpg.
The last number is just a counter if multiple images are taken that day and
stored in the same folder.

## License

img-rename is released under the [MIT License](http://www.opensource.org/licenses/MIT).
