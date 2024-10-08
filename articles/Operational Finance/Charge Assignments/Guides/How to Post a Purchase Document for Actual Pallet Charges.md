---
grand_parent: Charge Assignments
has_children: false
layout: default
nav_order: 44901
parent: Guides
title: How to Post a Purchase Document for Actual Pallet Charges
---

How to Post a Purchase Document for Actual Pallet Charges

1. Create a new purchase invoice or credit memo and complete the necessary fields in the header of the purchase document (eg. the Vendor No., Posting Date, Vendor Invoice No., etc.).
1. Choose **Process** from the menu in the purchase document, and then select **Pallet Charge Assignment**.
1. Choose the **Assignment Level**. Where possible and relevant, choose *Freight Container*as the assignment level to benefit from the delayed spreading of pallet charges to individual pallet lots. Other assignment level options are *Pallet* and *Pallet Lot*.
1. Specify the **Assignment Target**. If the assignment level was selected as *Freight Container* the dropdown list in this field will show eligible freight container codes to choose from. For assignment levels *Pallet* and *Pallet Lot*, choose the relevant Pallet ID or Pallet Lot No.
1. Choose the **Pallet Charge Code** for which the cost was incurred and fill in the **Amount**. The **Amount (LCY)** will automatically populate with the same value if the currency code of the purchase document is LCY; else the entered **Amount** will be converted to **Amount (LCY)** using the currency factor of the purchase document. Note that the amount field should be completed with the VAT exclusive amount.
1. Complete as many pallet charge assignment lines as needed to represent the total purchase invoice or credit memo amount. Then **Close** the screen. When the screen is closed a purchase lines will be inserted for each pallet charge assignment line that was created. The **Type** of the purchase line is set as *G/L Account* and the relevant G/L Account No. will automatically be populated in the **No.** field - as per the **Deferred Cost Account** setup for the Pallet Charge Code in **Pallet Charges**.
1. VAT will be calculated and populated for the lines and document if the combination of the VAT Business Posting Group of the vendor and the VAT Product Posting Group of the Pallet Charge requires this.
1. Review the document totals and VAT; then post the purchase document.