---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 35001
parent: Pallet Production
title: Pallet Production
---

Pallet Production

The pallet production functionality allows for pallets to be repacked to new pallets from one outer pack to another and includes apportionment and reallocation of revenue and costs of the output pallets to the related input pallets.




Two options exist for the basis on which production is tracked and revenue and costs apportioned to the input pallet lots:




* **Production Batch tracking**

In this scenario, the individual output pallet lot cannot be tracked to a specific input pallet lot. The lowest level of tracking detail is the batch number in which a selection of input lots was used. Revenue and costs from an output lot are then apportioned across all input lots that took part in the production batch.

Where there is no definite relationship between the input and output pallet lots, production runs are typically processed with the Pallet Wizard. Note that Production Document produce bills are not automatically generated for the output pallets produced via the Pallet Wizard.



* **Lot Specific tracking**

In a lot specific tracking scenario, the output pallet lot can be tracked to a specific input pallet lot. Revenue and costs from the output lot are thus passed back to its specific input pallet lot.

If repacking and production happen on this basis in your business, the *Lot Specific Tracking* parameter in Linc Setup must be switched on.

Pallet production with Lot Specific Tracking is typically done with the ***Pallet Production Lines*** functionality.






**Pallet Production Lines**




Usage and output are entered into *pallet production lines* - either manually or via Edit in Excel. Freight allocation group, allocated delivery point and intended sales prices for the output pallets can be captured on the pallet production lines themselves before processing the batch. On processing the pallet production lines, output pallets for which freight and sales allocation values were entered on the lines are automatically added to the user's allocation batch - from where they can be allocated to freight trip legs and containers. The output pallets are then sold on normal produce trades.




A pallet ID can be used in multiple production batches. It is thus possible to use 10 outer packs from a pallet lot with a quantity of 100 today, another 20 the next day in a different batch, and so forth. The usage quantities are tracked, so as to prevent usage from exceeding the full quantity on the input pallet lot, and for purposes of reporting on remaining quantities on the input lot (i.e. has the pallet been fully used, or not). The quantity on the input lot remains the same, as the Lot Billing Party will be paid for the input pallet and its quantity.




Input pallets are marked as *used* on all of the pallet IDs member pallet lots. This renders all the pallet lots of the input pallet ID as non-eligible for sales allocations. If an un-used pallet lot no. that is part of a used pallet needs to be sales allocated in its current state, it must be processed through pallet production to a new pallet ID - even if the outer pack and quantities essentially remain the same.




The history of pallet production is tracked in *Pallet Movement Entries* where usage and output events are logged when pallet production lines are processed. For each pallet production line two entries are stored in *Pallet Movement Entries*. The first entry is of type *usage* and shows the used pallet ID, pallet lot and quantity. The second entry is of type *output* and shows the output pallet ID, generated pallet lot no. and output quantity. The Production Document No. as was entered on the pallet production lines are also stored in a field in *Pallet Movement Entries*. By filtering the pallet movement entries by Document No. it is thus eg. possible to see the full details of the 'run' that was processed.




**Reallocation of revenue and costs from output lots to input lots**




When pallet production lines are processed, *production document*cost produce bills are automatically generated for the output pallets. (The bill grouping basis of these cost produce bills are *Production Document*, and this is what set them apart from 'normal' cost produce bills.)




*Production Document* cost produce bills cannot be posted, but is the mechanism the system uses to apportion and reallocate revenue and costs posted for the output pallet lots to the source input pallet lots. The reallocation occurs during charge calculation of the production document produce bill.




Produce Trade Entries of the output lots are reallocated to the relevant input lots - essentially by generating 'system' produce trade entries for the input lots. In the same way income charges and actual costs posted for output lots are also reallocated by generating 'system' pallet charge entries for the related input lots.



**Revenue and Cost apportionment logic**



Output pallet lots' revenue and costs are apportioned based on the following logic:

* The system first finds the output pallet's*Production Output Batch*. In cases where *Lot Specific Tracking*is used, this value will be the input pallet lot number itself. Else, it is the Production Batch No.
* Input pallets are then filtered for this batch number/pallet lot number to find the input pallet lot(s) that were involved in producing the output pallets.
* Each found input pallet lot's 'percentage contribution' to the batch is then calculated based on its net weight as a percentage of the total batch weight. If *Lot Specific Tracking* is used, the input lot's percentage contribution would be 100%.
* The revenue or cost of the output pallet lot is then multiplied by the input pallet lot's percentage contribution to calculate the input pallet lot's apportioned revenue and cost




For information on how to process pallet production lines with lot specific tracking, see [# How to set up and process Pallet Production](https://linc.freshdesk.com/en/support/solutions/articles/8000099254)