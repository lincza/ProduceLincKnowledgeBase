---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31904
parent: Guides
title: How to import a single pallet file
---

How to import a single pallet file

* Search for **Pallet File Entries**
* Choose **Import Single Pallet File**
* Use the assist-edit button (three dots) in **File Name** to choose the pallet file that you want to import
* Select the **File Purpose**.
- *Pallet Creation*: creates new palletised produce stock
- *Pallet Verification*: compares and updates fields on existing matched pallet lines
- *Container Confirmation*: compares and updates fields on existing matched pallet lines, and updates freight related details such as *External Container No.*, *Seal No.* and *Temptale ID*.
* **Suppress Field Validations** can only be used for File Purpose *Container Confirmation*. If this option is switched on, the *Container Confirmation* file will only update fields that are not validated against master data (eg. *Packhouse Lot No.* and *Producer Lot No.*) and that are selected for *Container Confirmation Update* in the pallet file definition. Pallet fields that are validated against master data (eg. *Commodity Code*, *Variety Code*) will not be validated or updated.
* **Preview Only**: if this option is selected, the lines of the pallet file will import to a preview screen, but without creating a Pallet File Entry or Pallet Import Lines. When the preview screen is closed, the data is not retained in the system.
* Choose **OK** to import the pallet file. If **Preview Only** was not selected, the system will generate and open the new **Pallet File Card**.