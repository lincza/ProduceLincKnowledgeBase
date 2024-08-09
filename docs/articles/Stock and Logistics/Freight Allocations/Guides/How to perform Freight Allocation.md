---
grand_parent: Freight Allocations
has_children: false
layout: default
nav_order: 43901
parent: Guides
title: How to perform Freight Allocation
---

# How to perform Freight Allocation

Freight allocation, like sales allocations, is supported by a batch-principle. This allows for users to add pallets to a freight allocation batch that is identified by their User ID, and prevents other users from allocating the same pallets for freight.




Allocate pallets to Freight Allocation Groups
---------------------------------------------

Pallets are allocated to individual freight containers based on their Freight Allocation Group. This Freight Allocation Group is assigned to a selection of pallets in **Pallet Allocation**.

To Assign a Freight Allocation Group:

* Search for **Pallet Selection Summary**, select the relevant pallets, choose *Freight Allocation* as the **Allocation Batch Purpose** and select **Add to Allocation Batch**. For more information on the use of summary buttons, summary lines and filter options in this page, see **Pallet Selection**.
* Close the Pallet Selection Summary page
* Search for **Pallet Allocations**.
* Assign **Freight Allocation Group** values to selected pallets with the use of the **Freight Allocation**field in *New Allocations*. Ensure that pallets are grouped in freight container ‘units’. If the Sales Allocation Group already groups pallets together in container units, you can copy this value to the **Freight Allocation Group** by selecting the relevant pallets and using the **Copy Sales to Freight**function in the Pallet Allocation subform menu.




Populate pallets to Freighter Trip Legs and Freight Containers
--------------------------------------------------------------

Once Freight Allocation Groups are assigned, the pallets can be allocated to Freighter Trip Legs and Freight Containers.




To populate trip legs and containers, pallets must be summarised by **Freight Allocation Group** (use the appropriate summary button) in **Pallet Allocations**. Each summary line in the *Allocation Summary*section will represent a Freight Allocation Group.




The total Outer Pack Quantity, Nett Weight, Gross Weight, number of Pallet Lines and Pallets can be reviewed on the summary line itself.




Then select a **Transport Method**, **New Freighter Code**, **New Freighter Trip Code** and **New Freighter Trip Leg Purpose** for the Freight Allocation summary line/s you wish to allocate to a trip leg and freight container. Choose an existing trip leg and container in **New Freighter Trip Leg Code** and **New Freight Container Code**, or create a new leg and container with the use of the assist-edit function (three dots) in these cells.




Once all the freight fields are specified, choose **Populate** from the main menu, and then select **Populate Freight Trip Legs**. This function adds the related pallets in the Freight Allocation Group to the selected Freighter Trip Leg and Freight Container.




**Show Freight Trip Leg** can be used to instantly navigate to the Freighter Trip Leg of the selected summary line.