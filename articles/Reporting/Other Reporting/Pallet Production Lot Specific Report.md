---
grand_parent: Reporting
has_children: false
layout: default
nav_order: 62001
parent: Other Reporting
title: Pallet Production Lot Specific Report
---

# Pallet Production - Lot Specific Report

Business that use ProduceLinc's lot-specific pallet production functionality (pallet production lines) can use this report for insight into what has been repacked and the outcomes of those repacks in pallet production runs.

### In this article
[Navigating to the report](#navigating-to-the-report)  
[Report format](#report-format)  
[Filter options](#filter-options)  
[Understanding the data in the report](#understanding-the-data-in-the-report)  

---


## Navigating to the report

The report name is **Pallet Production Report - Lot Specific**.
Use the search functionality in Business Cneetral to find it. You can also bookmark the report to your landing page.

![](/media/ReportingOther_PalletProductionLotSpecific_1.%20NavigateToReport.jpeg)

---
## Report format

We designed the report with no built-in layout, but rather as a dataset that you can use to create your own pivots, views, graphs/charts from in Excel. It works in the same way as the Freight Shipments report.  

To build a new layout, run the report with "Send to Excel Data Only", build your pivots and views, save the file and upload it as a new layout in Report Layouts. Once your layout is uploaded, you can run the report with the "Download" option in future - in which case the download will include the pivots/views/graphs/charts you designed for the layout.  

You can build multiple layouts of the report to cater for various reporting purposes.  

---
## Filter Options

When you run the report, you can provide filters for the data:

![](/media/ReportingOTher_PalletProductionLotSpecific_2.%20FilterOptions.jpeg)

- If you want to see the inputs and output results of a specific Pallet Production "run", use the Production Document No. filter. This filter is optional.
<br/>
<br/>
- Use the filters in the Filter: Pallets section to filter the input pallets by any pallet line field. Some examples would be to see the inputs and related outputs for a set of cost produce bills you are preparing for grower payments; or running the report for a specific lot billing party's input pallets for the season. Note that the filters work for the INPUT pallets only - the system will automatically then find the related final output pallet lines and include them in the report.

---
## Understanding the data in the report

The data for input and output pallets are structured vertically. This means that the output pallet line and its details do not sit on the same line as the input pallet line. There are valid reasons for this, which we'll explain with an example:

![](/media/ReportingOther_PalletProductionLotSpecific_3%20UnderstandingTheData.jpeg)

- Pallet A with LOT001 has 100 cartons. This is our original source pallet.
<br/>
<br/>
- In the first production run 20 cartons are used. ProduceLinc splits off the 20 cartons to LOT002 and uses it. It outputs Pallet B LOT003 with eg. 25 cartons.
<br/>
<br/>
- In a next production run 20 cartons from Output Pallet B is then used. ProduceLinc splits off the 20 cartons into a separate LOT004 for Pallet B and uses it. Pallet C with LOT005 and 8 cartons is created as a new and final output.
<br/>
<br/>
- Subsequent production runs used the remaining 5 cartons from Output Pallet B LOT003 and the remaining 80 cartons from Pallet A LOT001. New and final output Pallet D is created (LOT006 with 4 cartons and LOT007 with 76 cartons).
<br/>
<br/>
- Pallet A is our original source pallet. Pallet B is both an output and an input, and has also been split during usage. (We call these pallets that are outputs that were again used as inputs "middle pallets"). Pallet C and Pallet D are the final outputs that are loaded into outbound containers and invoiced on produce trades.
<br/>
<br/>
- From a reporting purpose you want to know what happened to the original 100 cartons on Pallet A, LOT001. You also want to see how the outputs that resulted from these original 100 cartons were sold, what the income was, etc. The final pallet lines has two lines for Pallet A and 3 lines for their related final outputs (Pallet C and Pallet D). It is this not possible to present the final 3 outputs in the same report line as the 2 'source' lines.
<br/>
<br/>
We have thus structured the lines in the report dataset vertically.
<br/>
<br/>
This is a snippet of how the dataset looks:

![](/media/ReportingOther_PalletProductionLotSpecific_4%20ExampleDataResult.jpeg)

- The Record Type distinguishes between Input and Output lines.
<br/>
<br/>
- The Original Pallet ID and Original Pallet Lot No. are the values that "tie" everything back to the source pallet and quantities. In the above example for our original source pallet ID PALLET A there was originally only a single pallet line with LOT001 and 100 cartons. The final outcome of the pallet production were the outputs in the red section - which all reference back to the original pallet ID and pallet lot.
<br/>
<br/>
- The "middle pallet lines" - PALLET B - is excluded from the report.
<br/>
<br/>
- In addition to the columns shown in the snippet above, the rest of the fields from pallet lines are also included in the dataset, including the produce specifications, outbound trip leg and container for the output pallets, the active produce trade, posted trade amounts, etc.
<br/>
<br/>


