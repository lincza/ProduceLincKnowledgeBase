---
grand_parent: Produce Accounting
has_children: false
layout: default
nav_order: 52002
parent: Produce Bills
title: Advance Produce Bills
---

Advance Produce Bills

Advance Produce Bills provides a mechanism with which advances for produce pallets can be calculated and posted.

The posting of the advance produce bill creates and posts a purchase invoice for the relevant Lot Billing Party. Each line in the posted purchase document represents a pallet lot from the source produce bill.




The advance values are posted to the G/L Account specified in **Produce Bill Account (Interim)** in **Produce Posting Setup**. Posted advances are reversed on posting of the related cost produce bill when the full purchase value of the produce is posted to the final produce bill account.




Calculate Advance from Pallet Charge Standard Rates
---------------------------------------------------

Advances can be automatically calculated using the **Calculate Charges** function from the menu. This will find matching rules in **Pallet Charge Standard Rates** for pallet charges of treatment *Advance*. The advance amounts for each pallet lot are then populated in the **Posting Amount (PCY)** field in the produce bill lines. The value is converted to local currency in the **Posting Amount (LCY)** field.




When charges have been calculated, the **Status** in the produce bill header is updated to *Charges Calculated*.




Adjust Advance Amounts
----------------------

### **Manual adjustments**

It is possible to adjust the posting amounts for advances by manually entering values in **Adjusted Bill Amount (PCY)**. When values are entered in this field, the **Posting Amount (PCY)** for the pallet lot is updated to the newly entered value and the **Adjusted Bill Amount (PCY)** cleared again.

Note that adjustments are only allowed if the produce bill is in *Bill Calculated* status. Use the **Calculate Bill** function in

the menu to first update the status from *Charges Calculated* to *Bill Calculated*.




### **Import multiple adjustments**

Adjustments can also be made in the Excel-based **Produce Bill Sheet**, and then imported again. This is an efficient method for adjusting the posting values for multiple produce bill lines, and even across multiple produce bills.

To export the **Produce Bill Sheet**, go to the **Produce Bills** page, choose **Export Produce Bill Sheet**and use the filter fields in the options screen to define which produce bills must be exported. Then choose **OK** and open the generate Excel workbook.

The advance amounts can now be adjusted by entering new amounts to be paid (per Outer Pack) in the **New Price Per Outer Pack** column of the Excel sheet. Dynamic formulas in the Excel sheet will update the **Adjusted Amount to Import (PCY)**. When all adjustments are made and reviewed, save the Excel file.

Import the saved Excel file using the **Import Adjustment Sheet** function on the **Produce Bills** page. The posting amounts and posting price fields in the related advance produce bills will now reflect the imported values.




### **Post the Advance Produce Bill**

Once the advance posting amounts have been reviewed, the produce bill can be posted. Choose **Request Approval** and then **Release** in the **Process** menu of the produce bill. Then **Post**.