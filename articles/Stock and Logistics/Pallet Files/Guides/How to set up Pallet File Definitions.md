---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31901
parent: Guides
title: How to set up Pallet File Definitions
---

# How to set up Pallet File Definitions


### In this article
[Create a pallet file defintion](#create-a-pallet-file-defintion)  
[Map Pallet File Fields](#map-pallet-file-fields)

---

## Create a pallet file defintion
<br/>

- Search for **Pallet File Definitions**.  

- Choose **New** or select the first empty line in the page.  

- Provide a **Code** and **Name** for the file definition.  

- Select the **File Type**. Options are _Variable_ (for csv files), _Fixed_ (for text files). If you have selected _Variable_, specify the _Field Delimiter_ (this is usually a comma or semi-colon).  

- Select **Primary** or **Secondary** in **Section Type**.  

    **Section Type** 
	Fixed file types (text files) such as PI, PO, RL, PS and MT files typically consist of some header rows, detail rows with the pallet information and a footer row. It is possible to map information from both the detail rows as well as the header rows of such files. 
	
	Create a pallet file definition with Section Type as Primary to read the pallet information. If you also need information from header rows (for example consignment numbers or inspection points) you will also need to create a pallet file definition with Section Type as Secondary for those header values and 'link' it to the Primary pallet file definition by selecting it in Parent File Definition Code.
	
	

![](/media/1.Configuration_PalletFileDefinition_Guide.jpeg)


- Define the **File Prefix** by typing in the characters that should match with the first characters of the pallet file. The number of characters you specify in this field will depend on how generic or specific the file definition must be.  

    > **EXAMPLE**  

    > To create a generic pallet file definition to be used for most PO files, specify the prefix as **ZPO**.
    > (The "Z" is to ensure that the generic defintion will be last in the list of matching file definitions found, and ensure that it is not used when a more specific file definition should be used.)
    > To create a more specific pallet file definition for PO files from location 789, define the prefix as **PO789**


- Define the **File Suffix** by specifying the file extension of the pallet file. Alternatively, leave the file suffix field blank to create a more generic rule that can be used for the import of pallet files with different file extensions

- **File Prefix Case Sensitive** and **File Suffix Case Sensitive** can be individually selected to make the file definition more specific.

- If you are creating a _Variable_ pallet file definition (i.e. for a csv file) then specify the **Top Rows to Skip**. If your csv file has one row of column headers, then Top Rows to Skip will be 1. There is no need to specify **Top Rows to Skip** or **Bottom Rows to Skip** for _Fixed_ pallet file definitions - as long as you clearly specify which rows must be imported in the **Exclude Rows Not Starting With** field.

- Set **Active** as *TRUE*. Pallet File definitions that are set as inactive will not be used for the import of pallet files.

- Define the **Date Fields Format** according to the format used in the pallet file. The date 2019/08/23 in a pallet file would, for example, be specified as YYYY.MM.DD in the pallet file definition.

- The detail lines of _Fixed_ pallet files usually have different record types. These record types are identified by the first two characters of the line in the file. Specify which type of line records to import in the **Exclude Rows Not Starting With** field. Example: if only the records of type "OP" in the pallet file must be imported, type _OP_ in this field.

- The **Parent File Definition Code**: If you are creating a pallet file definition with Section Type as Secondary, then link it to the relevant "parent" primary file definition in this field. Click on the drop-down arrow to select the relevant Parent File Definition Code.


---
## Map Pallet File Fields
<br/>

- Choose the **Pallet File Definition** for which you want to map fields from the pallet file to fields in the system.

- Choose **Pallet File Fields** from the page menu.

- Select a **Field ID** (select the three dots to go to a lookup page with a list of Field IDs). The **Field Name** and **Field Caption** will automatically populate once a **Field ID** is selected. Use the search box in the lookup page to search for specific fields by name.

- If the **File Type** in the Pallet File Definition is set as _Variable_ specify the column number in the pallet file where the value can be found for the **Field ID** that you have selected. If the File Type is set as _Fixed__ (a text-based file) specify the **Start Position** and **Width** (number of characters) of the value in the pallet file

- **Default Value** can be used for cases where the pallet file will always have a blank/incorrect value for the field.

- **Field Concatenation Order** allows you to map more than one value from the same line in the pallet file to a single field in the system in a concatenated manner. The same **Field ID** would then exist more than once in the **Pallet File Fields**. Specify the appropriate **Start Position** and **Width** for each instance of the Field ID, and use numbers in **Field Concatenation Order** to determine in what order the values from the pallet file will be concatenated into a single value in the system.

- **Pallet Verification Update** can be switched on or off to specify if an imported pallet file with Pallet Transaction Types **Pallet Verification** or **Pallet Update** must update the value in the field of the existing matched pallet line.

- **Pallet Verification Compare**: switch this on if you want the imported pallet file with purpose **Pallet Verification** to compare the imported value from the pallet file with the value of the field of the existing matched pallet line.

- **Container Confirmation Update** can be switched on or off to specify if a pallet file with Pallet Transaction Types **Container Confirmation** or **Produce Order Confirmation** must update the value in the field of the existing matched pallet line.

- **Container Confirmation Compare**: switch this on if you want pallet filse with Pallet Transaction Types **Container Confirmation** or **Produce Order Confirmation** to compare the imported value from the pallet file with the value of the field of the existing matched pallet line.

Repeat the steps above to set up the mapping for the rest of the Field IDs.