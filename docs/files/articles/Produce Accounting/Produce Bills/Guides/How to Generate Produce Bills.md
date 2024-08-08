---
grand_parent: Produce Bills
has_children: false
layout: default
nav_order: 53901
parent: Guides
title: How to Generate Produce Bills
---

# How to Generate Produce Bills

Produce Bills are generated at various stages of the lifecycle of produce pallets and for various purposes. Advance produce bills are, for instance, normally generated soon after the departure of Freight Trip Legs to calculate and post advances to producers. Cost produce bills are typically only generated much later when the final income on pallets have been posted on the relevant produce trades and possible quality claims processed.




The **Generate Produce Bills** batch report makes it quick and easy to generate multiple produce bills at once. Cost Produce Bills for pallets where the **Lot Billing Type** is *Purchase* can also be generated directly from the produce trade.




* Search for **Generate Produce Bills** to open the batch report.
* Select the **Produce Bill Purpose**. Options are *Advance*, *Cost* and *Forecast*.
* Select *Purchase* or *Consignment* as the **Lot Billing Type**. Note that produce bills with purpose *Advance* can only be generated for *Consignment* pallets.
* Parameters for **Produce Trades Not Required** and **Freight Trips Not Required** may be switched on if produce bills must be generated for *Purchase* pallets that are respectively not yet in a produce trade or freighter trip leg. These options are often used when pallets are purchased at a fixed price and needs early posting of the purchase invoice.
* Built-in grouping logic ensures that pallets are grouped into produce bills by **Lot Billing Type**, **Lot Billing Party No.** and **Currency Code**. Pallets are additionally grouped by the **Produce Bill Channel Basis** (*Inbound* or *Outbound*) and **Produce Bill Grouping Basis** (a week-basis) as defined in **Linc Setup**. These grouping fields are part of the header of a produce bill, and the individual pallet lots in the produce bill lines can thus not have a mixture of these values.
* The **Use Custom Grouping** option - if used - will override the built-in **Produce Bill Grouping Basis**. To illustrate the impact of custom grouping, let us assume that **Produce Bill Channel Basis**in Linc Setup is defined as *Outbound* and the **Produce Bill Grouping Basis** as *Inspection Week*. The specified filters in the batch report finds two pallets lots with the same Lot Billing Type, Lot Billing Party No., Currency Code and Outbound Channel, but the Inspection Week for pallet A is week 20, and for Pallet B it is week 21. If custom grouping is **not used**, two separate produce bills will be generated for each of these pallets. If custom grouping **is used**, both pallets will be included in the same produce bill.
* Specify a **Custom Grouping Code** if custom grouping is used.
* You can pre-select the **Use Preferred Trade Exch. Rate** if required. You can also manually switch this setting on/off on the produce bill headers once they are generated. For more information of the Preferred Trade Exch. Rate functionality, see **Cost Produce Bills**.
* Select the **Posting Date** that must populate in the headers of the produce bills that will be generated. The posting dates can also be manually edited on produce bills once they are generated.
* If **Calculate Lines** is selected in the batch report, the system will generate the produce bills and also calculate the pallet charges. Alternatively, charges can be calculated per produce bill after they have been generated.
* Use the filter fields in the sections for *Freighter Trip Leg*, *Freight Container*, *Freight Container Lines* and *Pallet Lines* to ensure that only the required pallets are included in the produce bills that will be generated.
* Once all the options and filters are specified, choose **OK** at the bottom of the report. A confirmation message will provide information of the produce bill numbers that have been generated and/or updated, and also note the number of pallet lines that have been skipped. Pallet lots of Lot Billing Type *Consignment* are not eligible for inclusion on a cost produce bill if their related produce trades are not yet closed. Such pallet lines will thus be skipped - even if the specified filters include them. For more information, see **Close the Produce Trade**. A pallet can only be on one Advance or Cost Produce Bill at a given time.