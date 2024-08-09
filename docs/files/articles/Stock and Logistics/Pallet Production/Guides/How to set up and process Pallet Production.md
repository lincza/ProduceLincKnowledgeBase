---
grand_parent: Pallet Production
has_children: false
layout: default
nav_order: 35901
parent: Guides
title: How to set up and process Pallet Production
---

How to set up and process Pallet Production

**Setup:**

1. Go to **Linc Setup** and switch on the setup parameter **Lot Specific Production.**This ensures that the output pallets are linked to their actual source/input pallet lot, as opposed to a scenario where the output pallets are not linked to specific input lots, but rather a production batch.
2. Go to **No. Series** and set up a number for Pallet Movement Entries and Pallet ID's.
3. Specify the number series in **Linc Setup** for *Pallet Movement Nos*and *Pallet ID Nos.*
4. Create a Warehouse Zone Code in**Link Lookup Values**. This warehouse zone code can be the same value as the freight point where the production takes place, or it can be a different value, eg. if various 'zones' exist at the particual freight point.

**To process pallet production on Pallet Production Lines:**

* Go to **Pallet Production Lines**
* **Choose edit list and start entering data in the first empty line, or click on "new".**
* **To capture subsequent lines, simply click in the next empty row. Proceed with entering data in as many rows as needed to represent your production batch(es) and production document(s).**
* Enter a **Production Batch No**. This is used for the Packhouse Lot No. on the output pallet lines or any other value user chooses for batch purposes
* Enter a **Production Document No.**This value is stored in the *Pallet Build Reference No.* of the output pallet lines. The value is also used as the grouping number for the auto-generated "Production Document" produce bills for the output pallet lines.
* Choose a **Warehouse Zone Code**
* Choose a **Production Date.** This becomes the pack date and confirmation date for the output pallet lines. Also stored as the *Pallet Date* in pallet movement entries for the usage and output.
* Choose a **Usage Pallet ID** and **Usage Pallet Lot No.**
* Enter the **Usage Quantity**. Full quantity of the pallet lot does not have to be used - thus no need to split lots beforehand if you intend to use less than the quantity of the pallet lot.  On posting of the production lines, an error check is done to ensure that the usage quantity does not exceed the 'remaining' quantity of the lot.
* Enter a **Output Pallet ID**
* Choose a **Output Pallet Base Code** and a **Output Pallet Height Code:** If left *blank*, the output pallet will inherit its base and height code from the input pallet used. Alternatively, a different base and height code can be entered for the output pallet.
* Choose a **Output Outer Pack Code** and **Output Inner Pack Code**
* Enter the **Output Quantity.**
* Enter a **Freight Allocation Group, Allocated Delivery Point, Intended Sales Currency Code, Intended Sales Price, External Sales Reference**. It is not mandatory to fill in these fields, but if they do have values when the lines are posted, these assignment values will be written to the corresponding fields of the output pallet lines - thus making it quick and easy to complete the freight allocation (populate the pallets to a trip leg and container, create and invoice the trade)
* Note that the output pallets will inherit their fruit spec fields (excluding outer pack and inner pack) and lot billing type and Lot Billing Party from the input pallet. Fields relating to inspection (inspection points, inspection dates, reasons, etc.) on the output pallet line will be 'blank'
* When ready click on *Actions*; then on *Post All Lines*. This action creates the new output pallet IDs and their pallet lines, registers the necessary records for usage and output in *Pallet Movement Entries* and also automatically generates the Production Document Produce Bills containing the posted output pallet lines.

  


Note: As soon as a pallet ID is used in production, the pallet is flagged as "used" for all member pallet lots of the pallet ID,  whether or not all the lots have been used. Such pallets are no longer available on stock and cannot be allocated to a customer.

  


**Complete Freight Allocation:**




If a Freight Allocation Group and Allocated Delivery Point was specified in the pallet production lines, the output pallet lines that are generated on posting of the lines will automatically be placed in a sales allocation batch for the user IDwho posted the production lines. Thus, this user can then simply open his/her *Pallet Allocation Summary*page to complete the freight allocation.


* Go to **Pallet Allocation Summary**
* If complete values for allocated delivery point and prices were entered on the production lines, the user would merely have to summarise by freight allocation group and assign the necessary freight values. Else, if any of the allocation values need to be modified before populating the trip leg, this can be done using the normal allocation functionality on pallet selection summary.
* Assign values for **T****ransport Method, Freighter Code, Freighter Trip Code**, choose the **Freighter Trip Leg Purpose** as *Outbound*, create/select the**New Freighter Trip Leg Code**and **New Freight Container Code.**
* In the Menu, click on 'Populate' and 'Populate Freight Trip Legs'
* Follow normal processes to confirm the container and create/update the produce trade(s).




For detailed information on the pallet production functionality, please read [Pallet Production](/files/articles/Stock%20and%20Logistics/Pallet%20Production/Pallet%20Production)(/files/articles/Stock%20and%20Logistics/Pallet%20Production/Pallet%20Production.md)(/docs/files/articles/Stock%20and%20Logistics/Pallet%20Production/Pallet%20Production.md)(docs/files/articles/Stock and Logistics/Pallet Production/Pallet Production.md)(https://linc.freshdesk.com/en/support/solutions/articles/8000099884)