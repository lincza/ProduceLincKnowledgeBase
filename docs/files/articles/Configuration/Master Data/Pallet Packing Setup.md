---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21004
parent: Master Data
title: Pallet Packing Setup
---

# Pallet Packing Setup

Pallet Packing Setup is used to store and maintain master data for two purposes:

* Pallet Quantity for specified pallet configurations
* Net Weight, Gross Weight and Standard Outer Pack Conversion rates for Outer Packs

The fields that are used for setup depends on the purpose. Thus, some fields are left empty for Pallet Quantity Setup, but used for Weight setup, and the other way around.

Pallet Quantity for specified pallet configurations
---------------------------------------------------

Pallet quantity setup is used during the validation of imported pallet lines in pallet file entries to check if the quantity on the pallet line matches the 'prescribed' quantity as per matching rule in Pallet Packing Setup. An ignorable error is generated if the quantity differs. If no matching rule is found for the pallet file line, a non-ignorable error is generated.

Net Weight, Gross Weight and Standard Outer Pack Conversion rates for Outer Packs
---------------------------------------------------------------------------------

Weight rules are used to calculate the **Net Weight** and **Standard Outer Pack Quantity** on pallet lines when the line is validated on the import line of a pallet file entry. If no matching weight rule can be found during validation of the pallet line, a non-ignorable error is generated. The weight rule must then first be created in Pallet Packing Setup - after which the line in the pallet file can be validated and the required weight fields calculated.