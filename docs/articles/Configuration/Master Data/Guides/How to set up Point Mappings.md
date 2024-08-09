---
grand_parent: Master Data
has_children: false
layout: default
nav_order: 21904
parent: Guides
title: How to set up Point Mappings
---

# How to set up Point Mappings

**TABLE OF CONTENTS**

* [Customer Freight Points](#Customer-Freight-Points)
* [Location Freight Points](#Location-Freight-Points)
* [Port Freight Points](#Port-Freight-Points)




* Search for **Point Mappings**
* Choose **New**or select the first empty line in the page

Customer Freight Points
-----------------------

* Choose a**Freight Point** (from Linc Lookup Values)
* Select *Customer* as the **Mapping Type**
* Map the freight point to a **Mapping Parent No.** (Customer No.)
* Select a**Mapping Code** (a Ship-to Code that is linked to the selected Customer No. in **Mapping Parent No.**) **Mapping Name**will auto-populate.
* **Region Code** and **Country Code** are optional fields for Customer Freight Points. If values are defined, these values are used to update the **Next Freight Point Region** and **Current Freight Point Region** of pallet lines that are allocated to the Freight Point when the related Freighter Trip Leg is set as *Departed* and *Arrived.*
* **Consignee No.** and **Notify Party No.** are also not mandatory, but can be defined where default values can be linked to a Customer Freight Point. During pallet line container population, the default consignee and notify party is added to the Container. These fields have a lookup to Business Central's **Contacts** master data, and values must first be set up in **Contacts**.





| **Freight Point** | **Mapping Type** | **Mapping Parent No.** | **Mapping Code** | Mapping Name | Region Code | Country Code | Consignee No. | Notify Party No. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DFRESH | Customer | CFRUIT043 | DFRESH | DFRESH SON |  |  |  |  |




Location Freight Points
-----------------------

* Choose a **Freight Point** (from Linc Lookup Values)
* Select *Location* as the **Mapping Type**
* The **Mapping Parent No.** is not used for Location Freight Points
* Select a valid Location Code in **Mapping Code**(lookup to Location Table).**Mapping Name**will auto-populate.
* **Region Code** and **Country Code** are optional fields for Location Freight Points. If values are defined, these values are used to update the **Next Freight Point Region** and **Current Freight Point Region** of pallet lines that are allocated to the Freight Point when the related Freighter Trip Leg is set as *Departed* and *Arrived*.






| **Freight Point** | **Mapping Type** | Mapping Parent No. | **Mapping Code** | Mapping Name | Region Code | Country Code | Consignee No. | Notify Party No. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FPTDBN | Location |  | FPTDBN | FPT Durban |  |  |  |  |




Port Freight Points
-------------------

* Choose a **Freight Point** (from Linc Lookup Values)
* The **Mapping Type**, **Mapping Parent No.** and **Mapping Code** is not used for Port Freight Points.
* Select the relevant **Region Code** and **Country Code**






| **Freight Point** | Mapping Type | Mapping Parent No. | Mapping Code | Mapping Name | **Region Code** | **Country Code** | Consignee No. | Notify Party No. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AEDMN |  |  |  |  | MEA | SA |  |  |