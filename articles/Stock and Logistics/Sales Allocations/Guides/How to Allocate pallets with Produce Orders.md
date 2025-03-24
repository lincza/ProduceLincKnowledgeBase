---
grand_parent: Sales Allocations
has_children: false
layout: default
nav_order: 45902
parent: Guides
title: How to Allocate pallets with Produce Orders
---

How to Allocate pallets with Produce Orders

* Search for **Produce Orders**and create a new order or open an existing one
* **Produce Orders**is a summary of an order per Customer
* Enter values in the header - these will be used when the pallets are allocated to the lines to update the relevant fields on the allocated pallet lines
* Enter one or more order lines. Fill in commodity group code, commodity code, outer pack code, pallet base and pallet height. Optionally fill in values in the additional 'filter' fields of the order line(s).
* Use the *Pallet Multiplier* field to enter the number of pallets for the order line. The system will multiply this with the "Qty per Pallet" as per the pallet packing setup found for the combination of commodity group/commodity/outer pack/pallet base/pallet height) to calculate the Quantity field of the order line. The Pallet multiplier is cleared after the calculation has been done.
* Add prices (intended sales and purchase prices and MGPs where applicable)



### Allocate pallets to order lines

* Select the order line for which you want to allocate pallets. Then click on 'manage' in the menu just above the order lines and choose "Allocate Pallets"
* The pallet allocation page that then opens will be pre-filtered for the values as per your order line
* Click on 'select' in this page to allocate the appropriate pallets. To de-allocate, 'un-tick' the select field. When pallets are selected/allocated, the allocation fields are updated from the order header and lines (prices and intended purchase currency from lines, the rest from the order header).
* *Allocated Pallets* and A*llocated Quantity* on produce order line will update




### Freight Allocation

* Pallets in Produce Order lines cannot be allocated to Freight if the Order is in *Open* or *Submitted*state. Produce Order must be in *Released* state to allocate pallets to Freight. At this stage intended purchase and sales prices should have a value. To release Produce Order, it must first be *Submitted**.*
* The freight allocation section of the order works in the same way as it does on the Pallet Allocation page.
* On the Freighter subform, select the **Transport Method, Freighter Code** and**Freighter Trip Code.**
* Choose an existing trip leg and container in **Freighter Trip Leg Code**and **Freight Container Code,**or create a new leg and container with the use of the assist-edit function (three dots) in these cells.
* Once all the freight fields are specified, select **Populate Freight Trip Legs** from the menu. This function adds the related pallets in the Produce Order to the selected Freighter Trip Leg and Freight Container.
* **Show Freight Trip Leg**can be used to instantly navigate to the Freighter Trip Leg of the selected summary line.

### Additional notes on Produce Orders

* Two fields are available in the order header to show total 'Allocated Pallets' and 'Allocated Quantity
* To see only the allocated pallets for a particular order line, you can now click on the 'allocated pallets' or 'allocated quantity' fields on the order line. This will open the pallet lines and show only the allocated pallets for that line
* On release of the order we test that all allocated pallets have an intended purchase and intended sales price, and error if any are found with a zero price in any of these two fields.
* The freight allocation fields on the order header are non-editable when the order is in open or submitted status, and only become editable in released status
* The produce order includes a customer statistics factbox that provides an overview of the customer balance, credit limit, value of outstanding pallets (un-invoiced sales) and values of orders that are still in open or submitted status for the customer


When pallets are allocated to a line with zero intended purchase price and zero purchase MGP price,  the intended purchase and purchase MGP will not be updated on the allocated pallets. Note that these two fields are handled separately - thus if the intended purchase eg. has no value on the order line, but purchase MGP does, allocation of pallets will not override the existing intended purchase price of the pallet(s), but it will update the purchase MGP as per the order line. When pallets are de-allocated, and the 'linked' order line has zero intended purchase price and/or purchase MGP, then these fields on the de-allocated pallets also does not update to zero - these prices remain as they were.


Updating intended and MGP purchase prices for individual pallets linked to an order line
The intended purchase currency code, intended purchase price and purchase MGP price fields on the allocation page (when you click on 'allocated pallets') are editable in this screen, but only if there are no values in either the intended purchase price or purchase MGP price fields of the related order line.

Functions added to apply purchase price and purchase MGP from 'Produce Prices'
If you have prices set up in *Produce Prices* you can apply the intended and MGP purchase prices with two new functions directly from the order. You'll find the functions in the main menu of the produce order under *Actions > Process*.. then choose 'Apply Produce Purchase Prices' and/or 'Apply Produce Purch. Min. Guarantee'. These functions apply the relevant prices for allocated pallets across all the order lines - no need to select specific order lines.