***
### Description
Implementation of socket server, client-user frontend page, and client-server interaction.

User commands:

    1. auth [user] [password]       authorization user  
    2. list                         list files directory  
    3. info [FILE]...               print information about files: mime type, size, time created  
    4. retr [FILE]...               move files specified in string to directory  
    5. exit                         exit from account  
    6. help                         help on commands  

The **pass** file contains 2 lines: username and password for login. [its presence is required]

---

To compile the program with python3, you need to install the pyinstaller module:
> **pip3 install pyinstaller**

The program is compiled in the repository folder:
> **sh scripts/make.sh**

Also, deleting unnecessary files, after assembly, of the project:
> **sh scripts/clean.sh**

Complete removal of files after build:
> **sh scripts/fclean.sh**
