---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 42001
parent: Produce Orders
title: Outbound Produce Orders
---

# Outbound Produce Orders

Outbound Produce Orders allows your marketing team to capture a client's order information even if the pallets are not on stock yet. Creating a outbound produce order and completing the necessary information typically kicks off the sales and logistics process.

There are various sections in an outbound produce order. The _General_ fast tab contains information about the customer, sales currency, salesperson (marketer), shipment method (incoterm), expected load date, loading freight points, commodities to load, order totals (amounts and quantities) and allocated totals (pallets and quantities).

Freight details can be captured in the _Freight_ fast tab and the relevant freighter trip leg and freight container on which the pallets must load can be created directly from the outbound produce order.
The marketing team can provide instructions to the logistics department to request a booking by submitting the booking directly from the outbound produce order. _Booking_ fields visually show the status of the booking, as well as the internal Booking Request No. and external Booking Confirmation No.

Order lines can be captured to represent the specifications and selling prices of the customer's order. These lines can exist whether pallets are already in stock or still being packed. This allows for order totals to be updated and reporting on debtors exposure, even if pallets have not yet been allocated.

Once pallets are available, these can be allocated to the order lines by using either a manual select method, auto-allocating (oldest pallets first) or importing the allocation from an Excel file. 
Outbound produce orders go through a life cycle as identified by the _Status_ field on the outbound produce order.

- While in an _Open_ status the information on the order, including pricing and allocated pallets, can be amended.

- Once the outbound produce order is just about ready for loading, it is updated to a _Submitted_ status.

For the load instruction to be issued and the pallets to be added to the container, the outbound produce order must then be _Released_. Releasing the outbound produce order triggers a credit limit check to ensure that the customer has enough available credit before allowing the pallets to load. Using the credit limit check functionality is, however, optional.

A factbox on the outbound produce order provides visiblity of the customer's current balance, overdue balance, credit limit, total of open and submitted orders and total of released/loaded pallets still to be invoiced. 

Load instructions can be printed digitally for sending to the cold store and other third parties such as the freight forwarder or transporter.

The marketing team can also digitally print an order confirmation to send to the customer, if required.

Two options exist for adding the allocated pallets to the system freight container:

- The pallets can be added to the container with the click of a button from the outbound produce order itself. This is useful in cases where a load file (PO file) is not received from the cold store.

- Pallets can also be automatically added to the system freight container by processing a outbound produce order confirmation pallet file (typically the PO file received from the cold store). This method offers richer functionality, since the system will automatically reconcile the allocated pallets with the loaded pallets, amend the allocation in cases where some pallet IDs were not loaded and replaced by pallet IDs that were not allocated, and amend the pallets in the system freight container accordingly. 

ProduceLinc offers full synchronization between the outbound produce order and the related freighter trip leg and freight container. This means that information such as estimated departure date, estimated arrival date, ports of loading and arrival, consignee of the container, etc. can be updated either directly on the outbound produce order, or from the freighter trip leg and freight container pages. Changing any of the values that are included in the _Freight_ fast tab will synchronise the value across the outbound produce order, freighter trip leg and freight container pages.