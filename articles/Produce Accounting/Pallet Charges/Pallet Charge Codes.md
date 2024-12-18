---
grand_parent: Produce Accounting
has_children: false
layout: default
nav_order: 51002
parent: Pallet Charges
title: Pallet Charge Codes
---

Pallet Charge Codes


ProduceLinc's comprehensive Pallet Charge functionality can track, manage and post costs that are incurred throughout the supply chain.

This feature includes the ability to set up Pallet Charge Codes for different types of costs on a detailed and grouped level, define standard rates with dynamic filter options and assign and post actual cost invoices or credit memo's.

The final costs can be reviewed on a pallet lot level on the cost produce bill in the context of the income and produce costs of the pallet lot.

Pallet Charge Codes must be defined in **Pallet Charges** before standard rates can be set up or actual costs for produce pallets posted. The table includes setup fields that determine when and how pallet charges will calculate, how actual charges will be spread to pallet lots and how charges will post to the G/L Accounts.




### **Code, Description and Grouping**

Specify a **Code** and **Description** for the pallet charge in the **Pallet Charges** page.  Pallet charges can be 'grouped' for reporting purposes in the **Grouping** field.

###

### **Recharge**

Pallet charges that should be tracked, managed and posted on a detailed level, but charged back to the Lot Billing Party can be flagged as **Recharge**. Such charges will, when applicable, be posted as deductions on the purchase document that posts when the produce bill is posted.




### **Shipment Method Level**

The **Shipment Method Level** (incoterm) has some important functions, and the value selected in this field should thus be carefully considered for each pallet charge.




This field is first used to determine if the standard rates for the pallet charge should calculate, or not. If the Shipment Method Level of the pallet charge is ranked 'higher' than the Shipment Method of a pallet lot's related produce trade, the standard rates for the pallet charge will not calculate on such a pallet lot.




Shipment Method Codes are 'ranked' from low to high based on sorting. To ensure proper sorting and ranking, prefix Shipment Method Codes with numbers, eg. 01-EXW has a lower ranking than 05-CIF. A Pallet Charge standard rate with Shipment Method Level 05-CIF will, for instance, not calculate for a pallet that was traded as 04-FOB. The standard rates of pallet charges with a lower or equal shipment method as the pallet lot's produce trade, will calculate.

If the pallet charge must calculate as a percentage of income (where **Charge Calculation Method** is *Income Percentage*), the rate is calculated as a percentage of the Shipment Method Level income of the pallet lot.





```
**Example**

A pallet lot was shipped as 05-CIF with an income of 100.00. Pallet Charge X with **Shipment Method Level** 05-CIF and rate of -10.00 applies to the pallet lot. Pallet Charge Y has **Shipment Method Level** 04-FOB, **Charge Calculation Method** defined as *Income Percentage* and a standard rate of 10%. The system thus deducts Pallet Charge X of -10.00 from the income of 100.00 to arrive at a 04-FOB income level of 90.00. Pallet Charge Y is then calculated as 10% of the 90.00, and results in a rate of -9.00.



```
### **Always Applicable**

This field can be switched on for pallet charges that should always calculate, irrespective of its Shipment Method Level. However, **Always Applicable** should not be switched on if the **Charge Calculation Method** of the pallet charge is *Income Percentage*.




### **Default Allocation Method**

This field determines how actual pallet charge assignments, that could be assigned on a higher level than the pallet lot, eg. the Freight Container or Pallet ID, will be spread to the individual pallet lots when the assigned cost is allocated during the calculation of the cost produce bill.




#### **Default Allocation Method Options**

* *Quantity*: The pallet charge assignment amount is divided by the total Quantity (number of Outer Packs) for all the pallet lots in the assignment target to determine a 'cost per Outer Pack'; and then multiplied by the Quantity of the pallet lot.
* *Weight*: The pallet charge assignment amount is spread across the pallet lots of the assignment target based on the net weight of the pallet lots.
* *Pallet*: The pallet charge assignment amount is spread across the pallet lots based on the number of Pallet IDs in the assignment target. The same cost amount is thus allocated to each pallet ID in the assignment target.
* *Amount*: the income of each pallet lot in the assignment target is calculated as a percentage of the total income of the assignment target. The percentage is then applied to the total pallet charge assignment amount and the result allocated to the individual pallet lot. Pallet lots with a higher income will thus carry a higher portion of the pallet charge.




### **Priority**

When charges are calculated on cost produce bills, the system will calculate standard rates as defined in Pallet Charge Standard Rates and also allocate actual pallet charges that may have been posted. The priority setting of the pallet charge will then determine which of these rates - standard or actual - should be prioritised. The prioritised cost will post to the Final Produce Bill Account (as defined in **Produce Posting Setup**) on posting of the produce bill.




#### **Priority Options**

* *Standard*: the standard rate will be used. If no standard rate is defined, no cost amount for the relevant pallet charge will post for the pallet lot.
* *Actual*: the actual posted pallet charge cost will be used. If no actual pallet charge cost was posted, the relevant pallet charge will post no cost amount for the pallet lot, even if a standard rate for the pallet charge was defined.
* *Prefer Actual*: the actual posted pallet charge cost will be used if it exists. If no actual cost was posted for the pallet charge, the standard rate will be prioritised.
* *Higher*: if an actual cost were posted and standard rate calculated for a pallet charge, the system will compare the two rates and prioritise the higher rate.




### **Treatment**

The **Treatment** defines the behaviour of pallet charges in produce trades and produce bills of various purposes.




#### **Treatment Options**

* *Advance*: these pallet charges calculate for produce bills of purpose *Advance*.
* *Cost*: calculates on cost produce bills
* *Commission*: calculates on cost produce bills and behave in the same manner as *Cost*pallet charges. This treatment option exists separate from the *Cost* option to allow for easier reporting on commission income earned.
* *Income*: pallet charge assignments on produce trades can only be posted to pallet charges with treatment *Income*. These charges are posted to the relevant sales accounts (as per Produce Posting Setup) and reduces the income of a pallet, rather than increasing its costs.




### **Charge Calculation Method**

The Charge Calculation Method determines how standard rates for the pallet charge will be calculated on the pallet lot. Options include *Outer Pack Qty.*, *Std. Outer Pack Qty.*, *Advance Percentage*, *Income Percentage*, *Pallet* and *Net Weight*.




### **Accrual Account and Deferred Cost Account**

Pallet Charge Assignments as posted on purchase documents are posted to the **Deferred Cost Account** for the pallet charge. These costs are reversed from the **Deferred Cost Account** during the posting of the cost produce bill. The difference between the actual and prioritised cost will remain in the **Accrual Account** after the produce bill posting. This amount represents the over/under recovery of the cost (in cases where an actual cost was posted) or the 'suspense' amount that still awaits an actual cost invoice.




### **VAT Prod. Posting Group**

The VAT Product Posting Group defines if VAT is applicable for the pallet charge when costs are posted. The combination of this VAT Product Posting Group and the VAT Business Posting Group of the customer or vendor determines if and how much VAT is calculated and posted for the pallet charge when posting pallet charge assignments and recharges.




### **Sorting Key**

The Sorting Key - an option text field - allows for easier sorting of pallet charges. Pallet Charges are also presented in order of the sorting key on the Produce Bill Export Sheet.