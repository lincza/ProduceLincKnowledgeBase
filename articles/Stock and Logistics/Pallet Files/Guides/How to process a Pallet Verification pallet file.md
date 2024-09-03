---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31910
parent: Guides
title: How to process a Pallet Verification pallet file
---

How to process a Pallet Verification pallet file

What does it do?

* Does not create new pallets
* Can compare and/or update fields on the matched pallet ID and pallet lot with values from the file line - for fields that are marked for compare and/or update in the related pallet file definition
* Can perform a reconciliation for the location / current freight point and identify pallets that are in the file (in stock at the location) but not in the system; and pallets that are in the system but not in the file (no longer in stock at the physical location)

How do I process a pallet verification file?

* Resolve any validation errors - as you would with a pallet creation file. For more information, see: [How to resolve errors and confirm pallet lines](/articles/Stock%20and%20Logistics/Pallet%20Files/Guides/How%20to%20resolve%20errors%20and%20confirm%20pallet%20lines)
* Once line is Validated, the system automatically tries to find the matching pallet ID and pallet lot in the system. An error is show if no match is found (i.e. if the pallet does not exist in the system)
* When the line is Validated and has a Matched Pallet ID and Matched Pallet Lot, 'compare' errors will be generated for the fields marked in the pallet file definition for 'compare'. For such fields the system checks if the value on the file line is the same as on the pallet line in the system. If the values differ, the compare error is shown. Compare errors can be ignored, or the value/s on the file line can be corrected to 'match' the value of the pallet in the system.
* Lines that are validated, have a Matched Pallet ID and Matched Pallet Lot No. and zero errors (thus, compare errors ignored/resolved) can be confirm.
* On confirm fields that were marked for 'update' in the pallet file definition will have their values in the system updated from the value on the file line.

To do a full reconciliation of the pallets in the file versus the pallets for that location (Current Freight Point),

* choose the Verification Freight Point in the header of the pallet file entry for which this reconciliation must be done.
* In this "Verification Freight Point" mode the pallet verification file will do everything as per the notes above, but also insert lines for pallets that it finds in the system at that Current Freight Point, but that are not in the file.
* These are typically pallets that may have already loaded and are no longer in stock at the location (and thus not in their stock file), but for which the freighter trip leg has not yet been 'arrived' (i.e., the Current Freight Point of the pallets have not yet been updated to the new location) or the produce trade has not yet been created.