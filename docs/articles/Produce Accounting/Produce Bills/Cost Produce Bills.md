---
grand_parent: Produce Accounting
has_children: false
layout: default
nav_order: 53003
parent: Produce Bills
title: Cost Produce Bills
---

Cost Produce Bills

A Cost Produce Bill is the mechanism with which the final trade income and supply chain costs for produce pallets are reconciled and reviewed, the purchase value (*Purchase* lot billing type) or producer payment value (*Consignment* lot billing type) is determined and all income and costs reversed from interim accounts and posted to the final sales and costs of sales accounts.




The posting of the cost produce bill creates and posts a purchase invoice for the relevant Lot Billing Party. Each line in the posted purchase document represents a pallet lot from the source produce bill.




When the cost produce bill is posted, all previously posted consignment advances for each of the pallet lots are reversed - either on the same purchase document that will post the purchase value of the fruit, or on a separate purchase credit memo. The preferred **Advance Reversal Method** can be selected in **Linc Setup**.




The produce purchase values are posted to the G/L Account specified in **Produce Bill Account (Final)** in **Produce Posting Setup**.




Produce Bill Lines in the Produce Bill Subform
----------------------------------------------

Each line in the Produce Bill Subform represents a pallet lot. Key information about the pallet lot is visible in the line. This includes the Pallet Lot No., Pallet ID, produce specification fields, Quantity and Standard Outer Pack Quantity for the pallet lot. The intended purchase and intended sales values, as assigned during initial allocation, are also shown. Here the total trade income, income charges, pallet charges, posted advances and posting amounts (purchase value) are also summarised per pallet lot.




Trade Income
------------

The sum of the actual posted trade values (sales) and income charges posted on the related produce trade are shown in both SCY (sales currency) and LCY (local currency). The **Posted Trade Exchange Rate** shows the average exchange rate for the sum of the posted trade amounts.




The **Net Trade Amount (LCY)** is calculated as the sum of the Posted Trade Amounts less Income Charges, converted to LCY values. This value is by default calculated based on the **Posted Trade Exchange Rate**, but the user can choose a different exchange rate for this calculation by using the **Preferred Exchange Rate** options in the produce bill header.




Preferred Exchange Rate options
-------------------------------

The **Preferred Trade Ex. Rate Date** and **Preferred Trade Exchange Rate** fields in the produce bill lines are populated during the **Calculate Charges** step, and the values in these fields are determined by the **Preferred Exchange Rate** options selected in the produce bill header.

* If **Use Preferred Exch. Rate** is switched on the value in **Preferred Trade Ex. Rate Date** will default to the posting date of the produce bill.
* The **Use Shipment Method Dates** option allows for the **Preferred Trade Ex. Rate Date** to be populated based on the date field that is specified in **Shipment Method Date Mapping**. The rules in this table can, for example, specify the Estimated Arrival Date of the Freighter Trip Leg for pallets that were traded with shipment method CIF. **Use Shipment Method Dates** can only be switched on if Use **Preferred Trade Exch. Rate** is also selected.
* If none of the Preferred Exchange Rate options are selected in the header, the **Preferred Trade Ex. Rate Date** and **Preferred Trade Exchange Rate** fields will default to the posting date and exchange rate of the produce bill.
* The value in **Preferred Trade Exchange Rate** is, for all three scenarios above, derived from the currency exchange rates based on the currency code of the produce bill and the date value in **Preferred Trade Ex. Rate Date**.

If **Use Preferred Trade Exch. Rate** in the header is switched on, the **Preferred Trade Ex. Rate Date**in the produce bill line will be used to find the relevant exchange rate to calculate **Net Trade Amount (LCY)** and convert standard pallet charges that calculated in foreign currency to LCY amounts. In cases where none of the preferred exchange rate options are exercised, the **Net Trade Amount (LCY)** calculates with the use of the **Posted Trade Exchange Rate** (average); and foreign currency pallet charges are converted to LCY amounts using the applicable exchange rate for the posting date of the produce bill and the charge currency code.




Note that the Preferred Trade Exchange Rate options can only be switched on/off if the status of the produce bill is *Charges Calculated*.




Standard, Actual and Prioritised Charges
----------------------------------------

The **Calculate Charges** function in the header menu calculates the relevant standard rates for pallet charges, allocates actual pallet charge assignments to the relevant pallet lots, and prioritises either the standard rate or actual rate (as per each pallet charge’s priority setting).




Pallet Charge Entries with amounts per pallet lot and pallet charge are generated for all three charge types (Standard, Actual, Prioritised). The total pallet charge rates for each pallet lot is summarised in **Standard Charges Amount (LCY)**, **Actual Charges Amount (LCY)** and **Prioritised Charges Amt. (LCY)**. All three fields have drilldown capability to the underlying pallet charge entries where users can see and review the detail of the pallet charges.




If the calculated standard rates look incorrect, correct the standard rate rule and calculate the charges on the cost produce bill again. The **Calculate Charges** function will recalculate all standard rates and re-prioritise charges with every run instance.




The prioritised charges can also be reviewed in the Produce Bill Export Sheet. This Excel-based spreadsheet shows a breakdown of prioritised charges per pallet lot and pallet charge.




Calculate the Produce Bill, adjust posting prices and post
----------------------------------------------------------

### **Calculate Bill**

Once the pallet charges are reviewed, the posting amounts for the produce (purchase values) can be calculated with the use of the **Calculate Bill** function in the header menu. The calculated result will be populated in **Posting Amount (PCY)** (purchase currency).




The logic used for the calculation depends on the lot billing type.

* For *Consignment* produce the posting amount is calculated as **Net Trade Amount (LCY)** less **Prioritised Charges (LCY)**. The resulting LCY value is converted to **Posting Amount (PCY)** using the currency factor of the produce bill. Note that Prioritised Recharges are excluded in this calculation.
* For *Purchase* produce the **Posting Amount (PCY)** value is set equal to the Intended Purchase Amount (PCY) of the pallet lot - on condition that **Posted Bill Amount (PCY)** is zero (thus, no previously posted bill amounts exist, or such amounts have been fully credited). In cases where **Posted Bill Amount (PCY)** is not zero, the **Posting Amount (PCY)** will by default be set to zero.




Calculated posting amounts can be adjusted by entering a new amount to post in **Adjusted Bill Amount (PCY)**. This value will then populate in **Posting Amount (PCY)**. The amounts can also be adjusted in the Produce Bill Export Sheet and imported.




### **Manual adjustments**

It is possible to adjust the posting amounts by manually entering values in **Adjusted Bill Amount (PCY)**. When values are entered in this field, the **Posting Amount (PCY)** for the pallet lot is updated to the newly entered value and the **Adjusted Bill Amount (PCY)** cleared again.




Note that adjustments are only allowed if the produce bill is in *Bill Calculated* status. Use the **Calculate Bill** function in the menu to first update the status from *Charges Calculated* to *Bill Calculated*. Where the lot billing type of the produce bill is *Consignment* a prioritised pallet charge entry will be generated for the difference between the calculated posting amount and the adjusted amount. The system uses the **Consignment Adjustment Charge** code as per the Produce Posting Setup for this adjustment entry.




### **Import multiple adjustments**

Adjustments can also be made in the Excel-based **Produce Bill Sheet**, and then imported again. This is an efficient method for adjusting to the posting values for multiple produce bill lines, and even across multiple produce bills.




To export the **Produce Bill Sheet**, go to the **Produce Bills** page, choose **Export Produce Bill Sheet**and use the filter fields in the options screen to define which produce bills must be exported. Then choose **OK** and open the generate Excel workbook.




The posting amounts can now be adjusted by entering new amounts to be paid (per Outer Pack) in the **New Price Per Outer Pack** column of the Excel sheet. Dynamic formulas in the Excel sheet will update the **Adjusted Amount to Import (PCY)**. When all adjustments are made and reviewed, save the Excel file.




Import the saved Excel file using the **Import Adjustment Sheet** function on the **Produce Bills** page. The posting amounts and posting price fields in the related produce bills will now reflect the imported values.




Post the Cost Produce Bill
--------------------------

Once the posting amounts have been reviewed, the produce bill can be posted. Choose **Request Approval** and then **Release** in the **Process** menu of the produce bill. Then **Post**