# Walkthrough: How to set up Automatic Pallet File Imports

* Specify the folders from which pallet files should automatically be imported and subsequently moved to (depending on the outcome of the automatic file import) in **Linc Setup** in the fields for **Pallet Files Path**, **Pallet Files Success Path**, **Pallet Files Error Path** and **Pallet Files Not Mapped Path**. Ensure that these directories/folders exist on the server from which Business Central runs.
* Set up rules in **Pallet File Purpose Mapping** to define for what purpose certain files (based on parts of the filename) should be imported (*Pallet Creation*, *Pallet Verification* or *Container Confirmation*). Specify a part of the pallet file name that will consistently be part of all file names from a given location in **Filename Regular Expression**. Use a 'dot' as a wild card in this field. Example: All PI files from freight point X have a file name that starts with PI123. Then enter "PI123." in Filename Regular Expression. Then specify the **File Purpose** for which the automatic pallet file import should create the pallet file entry.
* With the above setup done, you are now ready to set up a schedule job queue for the automatic import of pallet files. Go to **Job Queue Entries** and choose **New**.
* Set Object Type to Run as Report.
* Select the report in Object ID to Run by using the assist-edit function and searching for the Import Multiple Pallet Files report.
* Leave the Report Parameters section as is.
* Select the days on which pallet files must be automatically imported in the Recurrence section, and specify the No. of Minutes between Runs.
* Choose Process and Set Status to Ready.
* Then close the Job Queue Entry Card.
