---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31908
parent: Guides
title: How to process a Pallet Creation pallet file
---

How to process a Pallet Creation pallet file

What does it do?

* Creates new pallets (intakes)




How do I process a pallet creation file?

* Resolve validation errors (correct values on the lines/add master data/create pallet file translation rule/ add missing pallet packing setup rules) For more information, see [How to resolve errors and confirm pallet lines](/files/articles/Stock%20and%20Logistics/Pallet%20Files/Guides/How%20to%20resolve%20errors%20and%20confirm%20pallet%20lines)
* Resolve ‘blank’ Lot Billing Default Type and Lot Billing Party No. issues by ensuring that rules exist in Lot Billing Defaults (file lines cannot be confirmed if the lot billing information is ‘blank’)
* Resolve issue where fields are not allowed to be blank by entering the necessary values
* Lines in “Validated” status with zero errors can be confirmed
* The “Confirm” action creates the pallet in the system and essentially puts it into stock