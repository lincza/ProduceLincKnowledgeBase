---
grand_parent: Pallet Editor
has_children: false
layout: default
nav_order: 37901
parent: Guides
title: How to set up Change Log for Pallets
---

# How to set up Change Log for Pallets

To switch on Business Central's change log to track changes made to pallets:

* Search for **Change Log Setup**
* Select **Setup**, and then select **Tables**
* Search for the table named **Pallet Line** in the list of available tables
* Select **Some Fields** in the **Log Modification** field for the Pallet Line table, and then select the assist-edit button (three dots) in the field to navigate to a list of available fields on the pallet line table.
* Select **Log Modification** for the fields for which you wish to track changes. To enable the **Pallet Edit factbox** on the **Pallet Lines** page can show the modifications for selected pallet lines, ensure that you also switch on **Log Modification** for the **Pallet Edit Reason** field.
* Close the **Change Log (Field) List** page, as well as the **Edit - Change Log Setup (Table) List**.
* On the **Change Log Setup** page, switch on **Change Log Activated**.
* Log out of Business Central and log in again to activate the change log.