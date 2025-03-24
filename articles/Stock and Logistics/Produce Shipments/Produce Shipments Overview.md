---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 43001
parent: Produce Shipments
title: Produce Shipments Overview
---

# Produce Shipments Overview

The Produce Shipments functionality in ProduceLinc offers businesses the ability to group multiple produce orders and containers for a customer on a specific freighter trip leg together. 

### In this article
[Relationship between Produce Shipments and Produce Orders](#relationship-between-produce-shipments-and-produce-orders)  
[Setup to enable visibility and use of Produce Shipments](#setup-to-enable-visibility-and-use-of-produce-shipments)  
[Business Case for use of Produce Shipments](#business-case-for-use-of-produce-shipments)  
[Create new Produce Shipment and provide customer and freight information](#create-new-produce-shipment-and-provide-customer-and-freight-information)  
[Create multiple produce orders with linked freight containers directly from the produce shipment](#create-multiple-produce-orders-with-linked-freight-containers-directly-from-the-produce-shipment)  
[Modify produce shipment’s customer information](#modify-produce-shipments-customer-information)  
[Modify produce shipment consignee and other freight container information](#modify-produce-shipment-consignee-and-other-freight-container-information)  
[Change Trip Leg for Produce Shipment](#change-trip-leg-for-produce-shipment)  
[Change shipment for selected orders](#change-shipment-for-selected-orders)  
[Print/Run logistics documents directly from produce shipments](#printrun-logistics-documents-directly-from-produce-shipments)  
[Create/Update Produce Trades for produce shipments](#createupdate-produce-trades-for-produce-shipments)  
[Filter and search by produce shipment in various pages](#filter-and-search-by-produce-shipment-in-various-pages)  

---
## Relationship between Produce Shipments and Produce Orders
<br/>
A Produce Shipment is a layer that sits above outbound produce orders. Think of it as the ‘parent’ of multiple outbound produce orders and freight containers that are destined for a single customer for a specific freighter trip leg.
<br/>
If a Produce Shipment is created by a user, it will have a unique system number that is number series driven. 
<br/>
The Produce Shipment itself has two areas:

- General
- Produce Orders and Freight

Here is an example of a Produce Shipment:

![](/media/KB_StockLogistics_ProduceShipmentsOverview_01_ProduceShipmentCard.jpeg)

<br/>
### General area
<br/>
The General area is the header of the Produce Shipment and contains the fields that will apply to ALL outbound produce orders that are linked to the produce shipment. This includes most header fields of the outbound produce order itself, freighter trip leg code and related information, and some values that pertain to the freight containers, but must apply to ALL the freight containers for the produce shipment.

**Important Note:** a freight container cannot be shared/used across multiple produce shipments. If you are planning to load a container for more than one customer, the produce orders for this freight container must either:
- NOT be linked to a produce shipment, or
- separate freight containers must be created for each produce order, even if there is only one physical container
  
  
**Fields from the Outbound Produce Order Header**
> Delivery Point Code
<br/> 
Sell-to Customer No. and Sell-to Customer Name
<br/> 
Bill-to Customer No. and Bill-to Customer Name
<br/> 
Currency Code
<br/> 
Salesperson Code
<br/> 
Shipment Method Code
<br/> 
  
**Fields from the freighter trip leg**
> Transport Method
<br/> 
Freighter Code and Freighter Description
<br/> 
Freighter Trip Code
<br/> 
Departure Point
<br/> 
Arrival Point
<br/> 
Estimated Departure Date
<br/> 
Estimated Arrival Date
<br/> 
Freighter Trip Leg Code
<br/> 
Freighter Trip Leg Status (this field is for visibility only)
<br/> 
  
**Freight Container fields**
<br/> 
> Shipper
<br/> 
Consignee No. and Consignee Name
<br/> 
Notify Party No. and Notify Party Name
<br/> 
Freight Agent Code
<br/> 
Freight Forwarder Code
<br/> 
Steri
<br/> 
  
**Other Produce Shipment Header fields**
> Number of produce orders: shows the total number of related produce orders
<br/> 
Number of freight containers: shows the total number of related freight containers
<br/> 
  
### Prodce Orders and Freight area
<br/>
The related outbound produce orders for the shipment are shown in the Produce Orders and Freight subpage of the Produce Shipment. For each related outbound produce order, this subpage also shows other related information from the produce order. These include: 
  
> Freight Container Code
<br/>
Sales Allocation Group
<br/>
External Sales Reference
<br/>
Completely Allocated indicator
<br/>
Completely Loaded indicator
<br/>
Produce Trades Exist indicator
<br/>
Number of Allocated Pallets
<br/>
Commodities (as per the produce order’s header)
<br/>
Loading Freight Points
<br/>
Booking fields
<br/>
External Container Number
<br/>
Shipping Temperature
<br/>
Load Date and YearWeek
<br/>
Container Type Code
<br/>
Temptale Type Code
<br/>
  
Functionality supports easy navigation to the outbound produce order with a click on the Produce Order No. in this subpage.
  
The Produce Shipment No. is also shown on the related outbound produce orders (the list page and individual orders), with ability to navigate to the produce shipment from there.
  
---
## Setup to enable visibility and use of Produce Shipments
<br/>
The use of Produce Shipments is optional and requires the following once-off setups.
<br/>
Enable Use Produce Shipments in the Pallet Allocation area of Linc Setup.

![](/media/KB_StockLogistics_ProduceShipmentsOverview_04_EnableUseOfProduceShipments.jpeg)
<br/>

Set up a new number series for Produce Shipments and specify this number series in Linc Setup in the Number Series area.

![](/media/KB_StockLogistics_ProduceShipmentsOverview_05_ProduceShipmentNoSeries.jpeg)
<br/>
If the Use of Produce Shipments is NOT enabled, users will not be able to open the Produce Shipments page, create or use Produce Shipments, or see the Produce Shipment No. field on related pages like the outbound produce orders, freight containers and produce trades. This is by design to keep users’ pages and digital workspace uncluttered if your business is not using produce shipments at all.
  

---
## Business Case for use of Produce Shipments
<br/>
The use of Produce Shipments can provide a business and its users a streamlined method for managing the delivery point and trip leg information (plus some container information) for cases where multiple containers must load for a customer on a specific freighter trip leg.
<br/>
  
**Example case**
<br/>
A customer has ordered 20 containers that must load onto the same vessel-voyage (freighter trip leg and freighter trip code).


**Without use of produce shipments**
<br/>
Without the use of Produce Shipments a user must manually create 20 outbound produce orders and fill in the header information (delivery point, customer, trip leg information) on each of these 20 orders. When changes must be made to the trip leg (eg. all the containers must now load on a different trip leg), changes must again be made on 20 individual orders. 
<br/>
Printing of a set of documents for these 20 orders would also require a user to carefully filter the appropriate produce orders or freight containers from the trip leg before printing to PDF or Excel.


**With use of produce shipments**
<br/>
If Produce Shipments are used, a user can create a single produce shipment, enter the customer and trip leg information once in the produce shipment. The 20 produce orders can then be created simultaneously from the produce shipment, and each of the orders will automatically inherit the customer and trip leg information (and some container information) from the parent produce shipment.
  
Changes to the customer or trip leg information can be done on the produce shipment itself, and ProduceLinc will automatically update the fields on the related produce orders. Printing of logistics documents for all 20 produce orders/freight containers can then be done directly from the Produce Shipment.
  
ProduceLinc supports synchronization of fields between Produce Shipments, their related produce orders, freight container and freighter trip leg.
  

---
## Available activities for produce shipments
<br/>
Various activities can be performed for produce shipments. An overview of these activities/functions below:

---
### Create new Produce Shipment and provide customer and freight information
  
Create a new Produce Shipment from Produce Shipments page and enter customer and trip leg information
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_06_CreateNewProduceShipment.jpeg)
<br/>
Create or select a freighter trip leg code for the produce shipment. The functionality works the same as it does for outbound produce orders. Provide the information for the freighter, then choose an existing trip leg (lookup from inside the freighter trip leg code field) or create a new trip leg (assist-edit button next to the freighter trip leg code field).
  
---  
### Create multiple produce orders with linked freight containers directly from the produce shipment
   
Use the Add Produce Orders button on the produce shipment to create multiple linked produce orders.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_07_AddOrdersButton.jpeg)
<br/>
  
Specify the number of orders to create and optionally provide more information in the freight container fields provided. (You can also update these freight container fields directly from the produce orders later). Click the Create Produce Orders and Freight Containers button in the top.
<br/>
ProduceLinc will carry over the optional freight container values you provide to the produce orders and freight containers it creates. 

You can, for example, create 5 containers with loading freight point A for Commodities AP, then stay on the page, make the No. of Produce Orders to create 3, change the loading freight point to B, commodities to PR and create three more orders. The first 5 orders will inherit loading freight point A and commodities AP, and the next three will have loading freight point as B and commodities as PR.

Note that ProduceLinc does not simply create the orders and containers when you close the page. You must click the button for Create Produce Orders and Freight Containers at the top of the page.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_08_AddOrdersNewOrders.jpeg)
<br/>
Add more produce orders to the produce shipment if additional containers must load for the same customer in the same produce shipment. You can, for example, create 10 orders in the morning, an additional 4 orders in the afternoon, and add a further 2 orders the next day.
  
If the produce shipment already has a freighter trip leg code specified, ProduceLinc will automatically also create and link a freight container for each produce order that you create with Add Produce Orders.
  
If no freighter trip leg code is specified on the produce shipment yet, Add Produce Orders will create the produce orders, but without linked freight containers. The freight containers can then be added and linked directly from the produce orders themselves.
  
---  
### Modify produce shipment’s customer information
    
Change the delivery point code / salesperson code / currency code on the produce shipment itself to update the customer information on all the related produce orders and allocated pallets.
  
System checks will be done to make sure that the delivery point may still be modified. Once pallets are on a produce trade, they must first be removed before the delivery point on the produce shipment can be modified.
  
---  
### Modify produce shipment consignee and other freight container information
  
Change the consignee, notify party, freight agent, freight forwarder, exporter, shipper and steri indicator on the produce shipment to update the information on the related produce orders and freight containers.
  
---  
### Change Trip Leg for Produce Shipment
  
Change the entire freighter trip leg for the produce shipment and all its related produce orders and freight containers
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_09_ChangeTripLeg.jpeg) 
<br/>
This function can be performed even if the pallets are already on produce trades and invoiced. Since the customer information and produce shipment number remain the same when the shipment’s trip leg is changed, ProduceLinc will simply update the trip leg code on all the related tables, including the relevant produce trades and produce trade entries.

Note that the trip leg attributes (such as the transport method, freight code, freighter trip code, etc.) can not be modified directly from the produce shipment once a freighter trip leg code has been specified for it. This is to ensure that a user does not, for example, make trip leg LEG001’s freighter the MOL Proficiency if LEG001 is actually for the DAL Kalahari. Trip leg codes are share across multiple produce orders, freight containers and also shipments. Changes to the attributes of a freighter trip leg must thus be done from the freighter trip leg page itself.

Once a trip leg code has been specified for a produce shipment, the lookup for existing freighter trip legs (lookup button inside the trip leg code field) and the button to create and link a new trip leg for the produce shipment (assist-edit button next to freighter trip leg code field) become inactive. To link the produce shipment to a new or different freighter trip leg, the Change Trip Leg button must then be used.

---
### Change shipment for selected orders

Use the Change Shipment for Selected Orders button in the Produce Shipment’s subpage to move some produce orders to a different produce shipment for either the same customer or a different customer. 

This action will open a list of available produce shipments (where trip legs are Planned or Departed) to which orders can be moved. Orders cannot be moved to produce shipments for which the freighter trip leg status is already Arrived.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_10_ChangeShipmentForSelectedOrders.jpeg)
<br/>
If the order(s) are moved to a produce shipment with a different Delivery Point Code/Currency Code/Salesperson and customer information, ProduceLinc will first check that the pallets in those produce orders are not on a produce trade. If they are, they must first be fully credited (if already invoiced) and removed from the produce trade before the orders can be moved to another produce shipment.

If the order(s) are moved to a produce shipment with the same delivery point/customer, currency and salesperson code, ProduceLinc will not require you to credit and remove pallets from produce trades. Since the customer information will remain the same, the system will simply update the produce shipment no. on the related produce trade(s), produce trade entries and customer ledger entries. If the new shipment also means that the trip leg will change, the trip leg code will also be updated on all the related tables – including produce trades, produce trade entries and customer ledger entries.
  
---
### Functions that are still performed per produce order or freight container

Allocation of pallets must still be done on a produce order level. Allocate pallets to produce orders with existing preferred method (Excel allocation import, manual allocation or auto-allocation).

Print of loading instructions are still done from the produce orders themselves (or from freighter trip legs). Functionality does not currently include print of loading instructions directly from Produce Shipments, since the various containers for a Produce Shipment may not all be allocated / ready for load instructions at once.

Process PO files for the containers that have loaded, using existing functionality for produce order confirmation or container confirmation.
  
---
### Print/Run logistics documents directly from produce shipments
  
Print logistics documents such as the loading notification, freight delivery note, export addendum, commercial invoice and customs invoice directly from the produce shipment. ProduceLinc will automatically filter for the correct freight containers.

Or use Save All Documentation from produce shipments to generate and store all the logistics documents to your Azure Blob Container.

Autosave all the logistic documents for the produce shipment to your Azure Blob Container directly from the produce shipments. These files are currently still generated per container, but the function from Produce Shipments will generate them all at the same time.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_11_LogisticsDocumentsFromShipments.jpeg)
<br/>
  
---
### Create/Update Produce Trades for produce shipments

Create/Update Produce Trades directly from the Produce Shipment.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_12_CreateTradesFromShipments.jpeg)   
<br/>
ProduceLinc will create produce trades for the containers of the produce shipment that has been confirmed. If you have for example confirmed 8 of the 10 containers and only 8 produce trades were created, you can run the Create/Update Produce Trades function from the shipment again when the last two containers are confirmed.

ProduceLinc will still create a separate produce trade per delivery point/customer and freight container. but now includes the produce shipment as part of the grouping logic
  
---
### Filter and search by produce shipment in various pages

ProduceLinc shows the produce shipment number on produce orders, freight containers, produce trades and customer ledger entries, and support search and filter by Produce Shipment Number on these pages.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_13_ShipmentNoOnOrders.jpeg)
![](/media/KB_StockLogistics_ProduceShipmentsOverview_14_ShipmentNoOnContainers.jpeg)
![](/media/KB_StockLogistics_ProduceShipmentsOverview_15_ShipmentNoOnTrades.jpeg)
![](/media/KB_StockLogistics_ProduceShipmentsOverview_15_ShipmentNoOnCustLedger.jpeg)
<br/>
The produce shipment number is also shown on the pallet line list and included in the query that is used in refreshable Excel pallet stock. We’ve also added the Produce Shipment No. to the datasets of the produce order confirmation report, loading instructions, loading notifications, freight delivery note, addendum, commercial invoice, customs invoice, proforma invoice, produce trade invoice and credit memo, produce statements and freight shipments report.
<br/>
![](/media/KB_StockLogistics_ProduceShipmentsOverview_16_ShipmentNoOnPalletLines.jpeg)
<br/>
  
---  