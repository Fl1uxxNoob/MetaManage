# MetaManage - MetaData Manager

## Overview

This Python program allows you to manage image metadata using exiftool. The main features include displaying and removing metadata from images. The program features a menu-driven interface that allows you to choose from several options.


## Prerequisites
- Python 3.x installed on your machine. 
- Make sure you have exiftool installed and available in your system PATH. You can download it from the [official ExifTool website](https://exiftool.org/).
- The colorama library is used to color the terminal output. Install it using the following command:
  ```
  pip install colorama
  ```
  
## Features

- List Metadata: Shows the metadata of the specified image file.
- Clear Metadata: Removes all metadata from the specified image file.
- Edit any metadata that is detected *(Incoming)*.
- Autospoof of all metadata in the file *(Incoming)*.

## Usage

1. **Run the Program:**

   Execute the program from the command line:
   ```
   python MetaMange.py
   ```

2. **Select an Option:**

   Choose an option from the menu by entering the corresponding number and press `Enter`.

3. **Enter the File Path:**

   When prompted, enter the full path to the image file. Make sure the path is correct and that the file exists.

4. **View or Remove Metadata:**

- Option 1 will show the metadata of the file.
- Option 2 will remove all metadata from the file.
- Option 3 will clean the screen and reprint the header.
- Option 4 will exit the program.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details
