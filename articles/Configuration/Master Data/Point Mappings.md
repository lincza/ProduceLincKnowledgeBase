---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21007
parent: Master Data
title: Point Mappings
---

# Point Mappings

Point Mappings are used to map Freight Points (as set up in **Linc Lookup Values**) to related Business Central master data, such as customers and locations. When pallets are allocated for transfer or sales, the relevant freight point is selected from this set of master data. Key values from the Business Central master data record to which the freight point is mapped are then automatically populated on the pallet line, for example the Customer No. and Customer Name.

Three types of freight points are set up in this table and defined by **Mapping Type**:

- Customer Freight Points
- Location Freight Points
- Port Freight Points

Customer Freight Points
-----------------------

When pallets are allocated for sales, users must select a valid **Delivery Point**. The list of Delivery Points available for selection is limited to Customer Freight Points in **Point Mappings**.

Location Freight Points
-----------------------

When pallets are allocated for transfer, users must select a valid **Transfer Point**. The list of Transfer Points available for selection is limited to Location Freight Points in **Point Mappings**.

Port Freight Points
-------------------

Port freight points are not specifically defined as ports in Point Mappings, nor are they mapped to any Business Central records. To ensure, however, that the Target Region and Target Country of the Freight Trip Leg's Arrival Point prints on the addendum all freight points that will be used as arrival points for Freight Trip Legs must be set up in Point Mappings.