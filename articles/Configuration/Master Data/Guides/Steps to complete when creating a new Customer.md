---
grand_parent: Master Data
has_children: false
layout: default
nav_order: 21910
parent: Guides
title: Steps to complete when creating a new Customer
---

# Steps to complete when creating a new Customer

1. Navigate to the customer page on Business Central
2. On the page, select the "New" button.
3. ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8131426436/original/heyKmB309mXolBhQIAXOrZBwdhcZF7pK5A.png?1718787251)If your Customer Number is generated from a number series (e.g. CUST001, CUST002), only populate the Name field. If not, populate both the No. and Name Fields:
4. ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8131426434/original/-yq3wAMfGsfRqix53lajtB9FNUGjgMluTQ.png?1718787251)Select a General Business Posting Group, Customer Posting Group & VAT Business Posting Group under the Invoicing fast tab as well as the customer's currency code and VAT registration number:
5. ![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8131426435/original/X5tnv7VpPoocMpKKxu47Zz_17wqFbf35lw.png?1718787251)Select a Shipment Methode Code under the Shipping Fast tab:
6. Populate the address fields under the Address & Contact fast tab




1. Create New Customer
* Search for **Customer**
* Choose **New**
* Complete all relevant fields on **General, Invoicing** and **Payments**tabs




       2. Create Ship To Address

* On the Customer Card, go to *Menu, Navigate, Ship To Addresses*
* Create new Ship To Address code
* This will be the code used by the Commercial team when allocating pallets (Allocated Delivery Point)

      3.  Point Mappings

* Search for **Point Mappings**
* Choose a**Freight Point** (from Linc Lookup Values)
* Select *Customer* as the **Mapping Type**
* Map the freight point to a **Mapping Parent No.** (Customer No.)
* Select a**Mapping Code** (a Ship-to Code that is linked to the selected Customer No. in **Mapping Parent No.**) **Mapping Name**will auto-populate.
* **Region Code** and **Country Code** are optional fields for Customer Freight Points. If values are defined, these values are used to update the **Next Freight Point Region** and **Current Freight Point Region** of pallet lines that are allocated to the Freight Point when the related Freighter Trip Leg is set as *Departed* and *Arrived.*
* **Consignee No.** and **Notify Party No.** are also not mandatory, but can be defined where default values can be linked to a Customer Freight Point. During pallet line container population, the default consignee and notify party is added to the Container. These fields have a lookup to Business Central's **Contacts** master data, and values must first be set up in **Contacts**.





| **Freight Point** | **Mapping Type** | **Mapping Parent No.** | **Mapping Code** | Mapping Name | Region Code | Country Code | Consignee No. | Notify Party No. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DFRESH | Customer | CFRUIT043 | DFRESH | DFRESH SON |  |  |  |  |




       4.  Set up Document Layouts per Customer

* On the Customer Card, go to *Menu, Navigate, Document Layouts*
* Set up email addresses for each of the following, should you wish to send documents via email:

           a) Produce Trade Invoice (Report ID 50073)

           b) Produce Trade Credit Memo (Report ID 50072)

           c) Customer Statement (Report ID 50085)

* Email addresses should be separated by ; and can be up to 200 characters