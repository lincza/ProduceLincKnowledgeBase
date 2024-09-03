---
grand_parent: Sales Allocations
has_children: false
layout: default
nav_order: 44901
parent: Guides
title: How to Allocate Pallets for Sales
---

How to Allocate Pallets for Sales

Option 1: Import from Excel file
--------------------------------

* Open your Excel Allocation Batch file and refresh the data. This file shows all the pallets that are in your batch
* Allocate the pallets in your Excel file (see notes further down on what values are imported/not imported)
* Save the file and close it
* In BC, search for **Pallet Allocation Summary**
* In the bottom section of the page: click on **Functions** and then choose**Import Allocation Batch** to import the data from your Excel allocation file
* Follow the prompts on screen to navigate to the Excel file on your PC and import the file




### Notes for Excel import:

* When importing, the **Pallet Lot No.** must be present in the sheet that you import
* The order of the fields in the Excel file are **not important**
* For fields that are imported, the field name in Excel must be typed ***exactly*** as it looks like in the system (thus, case and spaces are important). These fields must also be in row 1 of the Excel file
* **NB**: if your Excel sheet is filtered, ALL records in the sheet will still import – the system does not only import the 'visible' filtered values
* It is not necessary to have values in ALL the fields below all at the same time when importing the file. Fields marked in bold are however required by the time the produce trade is created/updated.



### Fields that can be imported from Excel:

* **Sales Allocation Group**
* **Allocated Delivery Point**
* **Intended Sales Currency Code**
* **Intended Sales Price**
* Min. Guarantee Sales Price
* Intended Sales Comment
* External Sales Reference
* Salesperson Code
* **Intended Purch. Currency Code**
* **Intended Purchase Price**
* Min. Guarantee Purch. Price
* Intended Purchase Comment
* External Purchase Reference
* Allocated Transfer Point
* Freight Allocation Group



Option 2: Allocate from Pallet Allocation Summary
-------------------------------------------------

* After you have added pallets to your batch (using Pallet Selection), search for **Pallet Allocation Summary**
* Use the summary buttons / filter fields in the summary section / filters in the bottom section to find and filter for the pallets that you want to allocate for sales
* To allocate: Use the fields in the “Pallet Allocation” section of the Pallet Allocation Summary page to assign values to **selected** pallets. (fill in the value in the 'input' fields and click on the three dots to assign)



### Important notes for sales allocation

* The Pallet Allocation Page is system-filtered to only show pallets that are in your batch
* If Batch Purpose = Sales Allocation, ALL values as per the list of allocation fields above may be assigned – thus, sales as well as freight. The trip legs and containers can also be populated from a batch with purpose 'Sales Allocation'
* If Batch Purpose = Freight Allocation only Freight Allocation Group and Allocated Transfer Point can be assigned/modified and trip legs populated. A Freight Allocation batch will not allow assignment/modification to allocated delivery point/allocated customer or any of the prices
* You must assign a Sales Allocation Group before you can assign an Allocated Delivery Point
* Salesperson Code: the default is inserted when Allocated Delivery Point is assigned (based on either customer setup, user setup or produce trade defaults). If no default salesperson is found, the system will show an error. You can override the salesperson code (assign a different value) if the scenario requires it
* Intended Sales and Purchase Prices and Currencies: these four fields must have values by the time the produce trade is created. A “BLANK” currency code implies ZAR. Intended Sales Price and Intended Sales Currency Code are allocated together. Thus, when user clicks the three dots next to any of these two fields, it assigns both the price and currency, and then clears both fields again. The same principle applies to Intended Purchase Price and Intended Purchase Currency Code.




Option 3: Allocate from Produce Orders
--------------------------------------




Produce orders have been introduced as an alternative method for sales allocation. A produce order can be created to represent an order from a customer. Order lines and prices are added on a fruit specification level and allows for varying degrees of specificity. It is thus possible to capture a customer's order even before pallets are in stock.

Order lines are matched to pallets by allocating specific pallets to each line. On release of the produce order, a credit limit check is performed (if this functionality is switched on). Once the produce order is in released status, the freight allocation can be performed directly from the order.




For more information on how to allocate from Produce Orders, see [# How to Allocate pallets with Produce Orders](https://linc.freshdesk.com/en/support/solutions/articles/8000098158)