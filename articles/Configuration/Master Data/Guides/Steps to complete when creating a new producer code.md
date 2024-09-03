---
grand_parent: Master Data
has_children: false
layout: default
nav_order: 21912
parent: Guides
title: Steps to complete when creating a new producer code
---

# Steps to complete when creating a new producer code

1. Create New **Producer Code**
* Search for Linc Lookup Values
* Choose New
* Choose Producer Code as the Lookup Field Name
* Enter the unique PUC code in the Code field and enter a description
* In the ribbon, click on Extended Lookup Values
* Link the producer code to a **production area** in the Extended Lookup Field Name and Extended Lookup Field Code fields


 2. Create New **Producer Site Code**

* Search for Linc Lookup Values
* Choose New
* Choose Producer Site Code as the Lookup Field Name
* Enter the producer site code (orchard) in the Code field and enter a description




      3.  Create **Lot Billing Default** rule

* Search for **Lot Billing Defaults**
* Choose **New** or select the first empty line in the page
* **Lot Billing Defaults** comprises of filter fields (used to 'find and match' the appropriate rule for an imported pallet line) and the default values that are applied
* Filter fields include **Organisation Code**, **Packhouse Code**, **Producer Code**, **Commodity Group Code**, **Commodity Code**, **Variety Group Code**, **Outbound Channel Code** and **Target Region Code**
* **Producer Code** is the only mandatory filter field for setting up a valid lot billing default rule
* Scenario's may exist where different lot billing defaults must apply for the same **Producer Code**, depending on the specifications of the produce. To cater for this, the remaining filter fields may be used to set up more specific rules
* Note that if multiple rules are set up for a **Producer Code** with the use of additional filter fields, then values must exist in the same filter fields for all rules for the relevant **Producer Code**
* The values in **Default Lot Billing Type**, **Default Lot Billing Party No.**, **Default Inbound Channel Code**, **Responsibility Centre**, **Global Dimension 1** and **Global Dimension 2** are applied on imported pallet lines
* **Lot Billing Type** (*Purchase* or *Consignment*) and **Lot Billing Party No.** (*Vendor No.*) must be specified. **Inbound Channel Code**should also be defined. If this is left 'blank', no value will be applied to pallet file lines when the lot billing defaults are applied, and the pallet file line will not be confirmed. The remaining default fields are optional