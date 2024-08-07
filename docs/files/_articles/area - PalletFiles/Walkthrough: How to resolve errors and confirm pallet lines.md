# Walkthrough: How to resolve errors and confirm pallet lines

Once a pallet file is imported, errors on the file need to be resolved and the lines confirmed before the lines become available pallet stock (in the case of *Pallet Creation* file), or values on the existing pallet and/or freight container are updated (in the case of *Pallet Verification* and *Container Confirmation* files).

  


The total number of errors that exist are shown in the header of the pallet file card, and the number of errors for each line is indicated on the line itself in the **File Errors** field. To see the detail of the error, click on the value that indicates the number of errors - either from the pallet file header, or on the individual lines.

  


The File Errors Page lists all Unresolved errors for the specific Import Buffer line.

  


Some errors are 'warning' errors and flagged as *Ignorable* in the error list page. These can be ignored by selecting the **Ignore Error** from the menu in the error page.

  


Errors that cannot be ignored need to be resolved in an appropriate manner. It may be necessary to add missing setup or master data, or manually edit the values on the pallet file line. Once the errors has been addressed, attempt to validate the line/s again with the **Recheck** function in the pallet file header menu (this rechecks all lines in the file), or select the lines that you want to validate and choose **Validate Selected Lines** from the Pallet Line Import Buffer menu.

Once an error has been resolved, a Resolved Date, Resolved Time and Resolved User ID stamp will be allocated to the error line. The status of the line will update to *Validated* and the line can then be *Confirmed*.

During the validation step, the system will:  
- apply the lot billing defaults  
- calculate the Net Weight of the pallet line, based on the weight rules in Pallet Packing Setup  
- calculate the Standard Outer Pack Quantity

Multiple *Validated* lines can be selected and confirmed simultaneously with the **Confirm Selected Lines** function in the Pallet Line Import Buffer menu.

  


Mandatory Pallet Fields
-----------------------

During the confirmation step, there is an additional check for **mandatory pallet fields** (if **Check Pallet Fields Mandatory Fields** in **Linc Setup** is switched on). In such cases the line will not confirm if mandatory fields have missing values. Valid values must then first be entered and the line validated again before it can be confirmed.

  


Mandatory pallet fields are checked against the rules defined in **Pallet Line Mandatory Fields**. This table includes a pre-populated list of system mandatory fields. Additional user-defined rules can be set up with optional filters for Commodity Group code, Inbound Channel Code and Outbound Channel Code. 

  


  


System mandatory pallet fields include:

  
- Pallet ID

- Pallet Base Code

- Producer Code

- Commodity Group Code

- Commodity Code

- Variety Group Code

- Variety Code

- Outer Pack Code

- Quantity

- Intake Date

- Inbound Channel Code

- Outbound Channel Code

- Current Freight Point

- Current Freight Point Date

- Intake Freight Point

- Loading Freight Point

 

