# backup-updater <br/>

This script works by regularly scanning your folder for changes (_modified files, new files, etc._) and automatically copies those changes to your backup folder based on the time interval set.

## How to use?
> Python is required to use this script. If you already have Python installed on your system but it doesn't work, try updating to a newer version.

To set the <ins>paths</ins> to your folders / set a custom <ins>time interval</ins>, open the script in a text editor and edit the value of the following variables: 

`folderPath` = path to the folder you want to backup. <br/>
`backupPath` = path to your backup folder. <br/>
`interval` = time (in seconds) of how often to check for changes in your original folder; By default, the value is set to <ins>300</ins>.

**_Note:_** make sure paths are separated by `\\` (double backslash) or `/` (forward slash) and finally enclosed in `""` (double quotes.)