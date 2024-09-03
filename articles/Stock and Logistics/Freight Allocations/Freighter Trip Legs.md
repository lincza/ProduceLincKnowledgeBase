---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 43002
parent: Freight Allocations
title: Freighter Trip Legs
---

Freighter Trip Legs

A Freighter Trip Leg represents the movement of pallets between a departure point and arrival point. These legs are associated with a Freighter Trip and Freighter Code. The Freighter Code identifies the freighter, eg. a vessel, truck or airplane/airline, and the Freighter Trip Code is used to signify eg. the voyage code (for sea vessels), or flight number (for air transport).

Multiple Freighter Trip Legs can be associated with a Freighter Trip and Freighter Code - to support cases where more than one departure point and/or arrival point exist for the trip.

Freight containers represent the 'units' in which pallets in a trip leg are transported. These freight containers may or may not be actual physical containers. In cases where pallets are not loaded into physical containers, they are still allocated to an 'internal' freight container code (identified by a unique **Freight Container Code**based on the relevant number series as specified in **Linc Setup**). Multiple freight containers can exist for a trip leg.

The **Freighter Trip Leg** page provides fields to store and manage important information about the trip leg.

## **Freighter Trip Leg Purpose**

The system distinguishes between three trip leg purposes: *Inbound*, *Transfer* and *Outbound*.

Pallets can be allocated to *Inbound* trip legs if the need exists to track, and possibly allocate costs, to the freight on which pallets were delivered to the freight point from where you will process the intake of the pallets into the system. *Inbound* trip legs would typically be used where produce is imported and proper tracking of departures and arrivals, as well as allocation of these freight costs, are required.

*Transfer* purpose is used to track movement of pallets between 'internal' freight locations, eg. a transfer from one cold store to another.

*Outbound* purpose signifies the movement of pallets to allocated customers.

A pallet can be allocated to multiple *Inbound* and *Transfer* trip legs, but only to one *Outbound* trip leg.

## **Transport Method, Freighter Code, Freighter Trip Code and Freighter Trip Leg**

Multiple **Transport Methods** can be defined in **Linc Lookup Values** to distinguish between different modes of transport, eg. sea, land, air, rail, etc. **Freighter Codes** are linked to a defined transport method through a parent-child relationship in **Linc Lookup Values**, and Freighter Trip Codes to a 'parent' Freighter Code.

When a new Freighter Trip Leg is created, the user must specify the **Purpose** of the trip leg and select the relevant **Freighter Code** and **Freighter Trip Code**. The **Transport Method** is automatically populated based on the parent-child relationship the Freighter Code and Transport Method. A unique Freighter Trip Leg Code is assigned to each trip leg, using the number series as specified in **Linc Setup**.

## **Stack Dates**

The date and time when stacks open and close can be stored on a Freighter Trip Leg.

## **Departure and Arrival Points and Dates**

The **Freighter Trip Leg** page provides fields where the **Departure Point** and **Arrival Point** are specified, along with estimated and actual departure and arrival dates.

The **Status** of a freighter trip leg can be set as *Planned*, *Departed* or *Arrived*. Setting the status as *Departed* updates the **Next Arrival Point** and **Next Arrival Region** of the related pallet lines to their assigned **Transfer Points** (*Inbound* and *Transfer* trip legs) or **Delivery Points** (*Outbound* trip legs). When the **Status** is updated to *Arrived*, the **Current Freight Point** and **Current Freight Region** of pallets in all associated freight containers are updated to the pallets' assigned **Transfer Points** or **Delivery Points**.

**Destination Point**will default to the **Arrival Point,**but can be edited on this page

New Freighter Trip Legs can be created directly from the Freighter Trip Leg page, or at the time of allocating pallets for freight (see **Freight Allocations**).

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8089916121/original/O9CAbv6-t1onWoYLGRv4Jj1nl1eF4688jg.png?1637132183)