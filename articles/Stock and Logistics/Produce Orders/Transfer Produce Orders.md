---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 42002
parent: Produce Orders
title: Transfer Produce Orders
---

# Transfer Produce Orders

Pallets may need to be transferred from one cold store to another. The transfer process in the system is kicked off by creating a transfer produce order. Users can provide information about the freight point (location) from where pallets will transfer, the freight point to which the pallets must transfer, the expected load date and commodities in the _General_ fast tab of the produce order.
This _General_ tab also shows the total allocated pallets and quantities.

Freight details for the transport can be captured in the _Freight_ fast tab and the relevant transfer freighter trip leg and freight container on which the pallets must load can be created directly from the transfer produce order. 

The term “freight container” refers to a ‘unit’ in the system to which the pallets are linked, and does not necessarily imply a 40 ft high cube container that will be loaded onto a vessel. For transfer purposes, the freighter trip leg and freight container essentially represent the “truck”.

Order lines can be captured to represent the specifications of the pallets to be transferred. Pallets are then allocated to these order lines by using either a manual select method, auto-allocating (oldest pallets first) or importing the allocation from an Excel file. 

When pallets are allocated to a transfer produce order, the system updates the **Current Freight Point** of these pallet lines to the "IN TRANSIT" freight point that your business has defined in Linc Setup. This "IN TRANSIT" value in Current Freight Point then aids allocation users in knowing where the pallets are. 

When the order and pallets are ready for loadout, the order is released so that a load instruction can be digitally printed from the produce order and sent to the loading freight point and other third parties such as the transporter.

Two options exist for adding the allocated pallets to the system freight container:

- The pallets can be added to the container with the click of a button from the transfer produce order itself. This is useful in cases where a load file (PO file) is not received from the cold store.

- Pallets can also be automatically added to the system freight container by processing a transfer produce order confirmation pallet file (typically the PO file received from the cold store). This method offers richer functionality, since the system will automatically reconcile the allocated pallets with the loaded pallets, amend the allocation in cases where some pallet IDs were not loaded and replaced by pallet IDs that were not allocated, and amend the pallets in the system freight container accordingly. 

The Current Freight Point of transfer pallets must be updated to the "destination" freight point at some stage. This can happen in two ways:

- The relevant freighter trip leg can be set as _Arrived_ by entering an actual arrival date. This triggers the update of the current freight point to the allocated transfer point, and de-allocates the pallets from the transfer produce order.

- A pallet verification file (PS file) or Pallet Transfer Intake file (PI file for transfer intake) from the "receiving" freight point can be processed. Processing such a file in essence acknowledges arrival of the pallets at the destination freight point, updates the Current Freight Point and de-allocates the pallets from the transfer produce order.

A pallet can only be allocated to one transfer produce order at a time. This ensures that the transfer process is completed before initiating a subsequent transfer. It is for this reason that pallets remain allocated on the transfer produce order until they arrive, and are automatically de-allocated from the transfer produce order when they arrive. These pallets will, however, remain in the relevant system freight container so that pallet charges that relate to the transfer can be assigned to this freighter trip leg or freight container.