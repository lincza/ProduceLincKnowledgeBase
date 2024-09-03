---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21006
parent: Master Data
title: Pallet Line Mandatory Fields
---

# Pallet Line Mandatory Fields

Rules for fields that are mandatory are stored in Pallet Line Mandatory Fields. There are two kinds of rules, as indentified by the **_Type_**:

## System
System rules cannot be removed. They define the fields on pallet lines that may never have an empty value, and are required by the system itself to reliably perform other functions.

## User-Defined
User-Defined rules can be added for additional fields that your business regards as mandatory for pallet lines. You can define these rules with or without specifying additional criteria such as the commodity group code, inbound channel code or outbound channel code. 

### Examples
Your business exports citrus, and Producer Site Code (the orchard code) is mandatory on a number of official export documentation for citrus.
The Producer Site Code is however not essential for other commodity groups or even for citrus you sell to the local market.
You can thus define a rule that Producer Site Code is mandatory for Commodity Group _Citrus_ and Outbound Channel Code _E_ (exports).

Your business regards the Brand Code as mandatory for ALL commodity groups, regardless of whether the product is exported or sold locally.
For this you would define a rule for Brand Code and leave the additional criteria fields empty.

[Click here for an example](/media/Configuration_MasterData_PalletLineMandatoryFields.jpeg)