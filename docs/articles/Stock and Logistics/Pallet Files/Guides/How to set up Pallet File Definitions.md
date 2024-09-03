---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31901
parent: Guides
title: How to set up Pallet File Definitions
---

How to set up Pallet File Definitions




* Search for **Pallet File Definitions**
* Choose **New** or select the first empty line in the page
* Provide a **Code** and **Name** for the file definition
* Select the **File Type**. Options are *Variable* (for csv files), *Fixed* (for text files) and *XLS* (for Excel files). If you have selected *Variable*, specify the *Field Delimiter* (this is usually a comma or semi-colon)
* Select *Body*or *Header*as the **Section Type**
	+ **Section Type**: Fixed file types (text files) such as PI, PO, RL, PS and MT files typically consist of some header rows, detail rows with the pallet information and a footer row. It is possible to map information from both the detail rows as well as the header rows of such files. First create a file definition with **Section Typ****e** selected as *B**ody*. To map information from the header of files for the same pallet file definition create one or more additional pallet file definition rows with the **Secti****on Type** selected as *H**eader*. Such *Header*definitions should be 'linked' to their parent *Body*definitions by selecting the relevant *Body*pallet file definition code in **Parent File Definition Code**




![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8093157315/original/YUF5D0_GpWzzkxU1I3iaB-PvYqGqcuSLxw.png?1643309305)







* Define the **File Prefix** by typing in the characters that should match with the first characters of the pallet file.The number of characters you specify in this field will depend on how generic or specific the file definition must be.




```
EXAMPLE:

To create a generic pallet file definition to be used for most PO files, specify the prefix as **ZPO**.
(The "Z" is to ensure that the generic defintion will be last in the list of matching file definitions found, and ensure that it is not used when a more specific file definition should be used.)

To create a more specific pallet file definition for PO files from location 789, define the prefix as **PO789**
```






* Define the **File Suffix** by specifying the file extension of the pallet file. Alternatively, leave the file suffix field blank to create a more generic rule that can be used for the import of pallet files with different file extensions
* **File Prefix Case Sensitive** and **File Suffix Case Sensitive** can be individually selected to make the file definition more specific
* Specify the number of **Header Rows** and **Footer Rows** in the pallet file. For **Section Type** *body* the system starts importing values from the row number after the number specified in **Header Rows**. For **Section Type** *Header* the system will only read the number of header rows as specified in the linked parent *body* definition. For **Section Type***Header*, leave the number of header rows and footer rows as zero
* Set **Active** as *TRUE*. Pallet File definitions that are set as inactive will not be used for the import of pallet files
* Where the **File Type** is set as *XLS*, specify which sheet in the file must be used in the **Excel Sheet No.** field
* Define the **Date Fields Format** according to the format used in the pallet file. The date *2019/08/23* in a pallet file would, for example, be specified as *YYYY.MM.DD* in the pallet file definition
* The detail lines of text-based pallet files usually have different record types. These record types are identified by the first two characters of the line in the file. Specify which type of line records to import in the **Exclude Rows Not Starting With** field. Example: if only the records of type "OP" in the pallet file must be imported, type *OP* in this field
* The **Parent File Definition Code**of *Header* type definitions should be the code of the appropriate *Body* type file definition code

Map Pallet File Fields
----------------------

* Choose the **Pallet File Definition** for which you want to map fields from the pallet file to fields in the system
* Choose **Pallet File Fields** from the page menu
* Select a **Field ID** (select the three dots to go to a lookup page with a list of Field IDs). The **Field Name** and **Field Caption** will automatically populate once a **Field ID** is selected. Use the *search*field in the lookup page to search for specific fields by name.
* If the **File Type** in the Pallet File Definition is set as *Variable* or *XLS* specify the column number in the pallet file where the value can be found for the **Field ID** that you have selected. If the File Type is set as *Fixed* (a text-based file) specify the **Start Position** and **Width** (number of characters) of the value in the pallet file
* **Default Value** can be used for cases where the pallet file will always have a blank/incorrect value for the field
* **Field Concatenation Order** allows you to map more than one value from the same line in the pallet file to a single field in the system in a concatenated manner. The same **Field ID** would then exist more than once in the **Pallet File Fields**. Specify the appropriate **Column No.** or **Start Position** and **Width** for each instance of the Field ID, and use numbers in **Field Concatenation Order** to determine in what order the values from the pallet file will be concatenated into a single value in the system
* **Pallet Verification Update** can be switched on or off to specify if an imported pallet file with purpose **Pallet Verification** must update the value in the field of the existing matched pallet line
* **Pallet Verification Compare**: switch this on if you want the imported pallet file with purpose **Pallet Verification** to compare the imported value from the pallet file with the value of the field of the existing matched pallet line
* **Container Confirmation Update** can be switched on or off to specify if an imported pallet file with purpose **Container Confirmation** must update the value in the field of the existing matched pallet line
* **Container Confirmation Compare**: switch this on if you want the imported pallet file with purpose **Container Confirmation** to compare the imported value from the pallet file with the value of the field of the existing matched pallet line

Repeat the steps above to set up the mapping for the rest of the Field IDs.