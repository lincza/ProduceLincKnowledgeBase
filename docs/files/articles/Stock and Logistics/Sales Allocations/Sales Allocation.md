---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 44001
parent: Sales Allocations
title: Sales Allocation
---

Sales Allocation

When pallets are confirmed on the pallet file entries, they are inserted into pallet lines and become available stock, ready to be allocated for sales by commercial staff. In most produce marketing businesses pallets are allocated for sales by various staff members. ProduceLinc thus uses a batch-principle for allocations to ensure that a pallet is not allocated by more than one user at the same time.




The system features an easy-to-use sales allocation functionality that is based on a two-step process.

* Pallets are added to a **sales allocation batch** from **Pallet Selection Summary**. The batch is identified by the **User ID** value in the **Allocation Batch** field of the related pallet lines. Pallets that are in a user’s batch are still visible to other users on Pallet Selection Summary, but another user cannot remove such pallets from an existing batch and add to his/her own batch.
* Pallets in a **sales allocation batch** are then visible in **Pallet Allocation** from where delivery points, customers and intended prices can be assigned.




Pallet Selection
----------------

The **Pallet Selection Summary** page shows all available palletised produce. This includes pallets that have already been allocated for sales and/or freight, but for which **Produce Trades** have not yet been created.




Summary buttons make it easy to summarise available pallets on a grouped level - based on various combinations of the pallet line values. Summary lines in the *Selection Summary* then provide a summarised overview of available pallets - much like an Excel pivot table. The *Commodities Only*summary button will eg. group pallets based on the Commodity Code of available pallet lines and result in a summary line for each Commodity Code found.




The summary lines show the pallet, quantity and weight totals of the pallets that are included in the summary. When a summary line is selected in the top section of the page, the bottom section will show only the pallet lines that are included in the selected summary line.




Further filters can be applied to the pallet lines by using built-in Filter Sets or manual filters.




Pallet Allocation
-----------------

The **Pallet Allocation** page is pre-filtered to only show pallets that are in the logged-in User ID’s allocation batch. This ensures that users do not allocate pallets in one another’s batches.




The page design is similar to Pallet Selection Summary - with the same functionality to summarise pallets with the use of summary buttons as well as additional filters on the detail pallet lines.




A *Pallet Allocation* section between the selection summaries and pallet lines provides a place where allocation values such as allocation groups, delivery points and intended prices can be specified and assigned to multiple selected pallets at a time. As an alternative, allocations can also be imported from an Excel file with the use of the **Import Allocation Batch** function in the *Pallet Allocation* menu.