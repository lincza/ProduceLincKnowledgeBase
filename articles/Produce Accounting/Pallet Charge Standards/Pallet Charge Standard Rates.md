---
grand_parent: Produce Accounting
has_children: false
layout: default
nav_order: 51003
parent: Pallet Charge Standards
title: Pallet Charge Standard Rates
---

Pallet Charge Standard Rates

Standard cost rates are set up in **Pallet Charge Standard Rates**. Start by selecting a **Pallet Charge Code**. Once selected, the **Treatment** and **Charge Calculation Method**fields are automatically populated as per the setup in **Pallet Charges**. A Unique **ID** will also be assigned to the standard rate rule. This **ID** is shown on the calculated standard pallet charge entries from a cost produce bill, and makes it easy to find the appropriate rate in Pallet Charge Standard Rates if any adjustments need to be made to the standard rate rule.

The **Sorting Key** is an optional text field that can be used to simplify the 'grouping', sorting and managing of standard rates.




Ensure that the appropriate **Freight Trip Leg Purpose** is selected. The option in this field will default to *Outbound*, but can be changed to *Inbound* or *Transfer*.

If a rate is only applicable for a certain date parameter, this can be defined by selecting an appropriate **Date Basis** with valid **Start Date** and **End Date** filters. Available options for **Date Basis** include *Harvest Date*, *Pack Date*, *Inspection Date*, *Estimated Departure Date*, *Actual Departure Date*, *Estimated Arrival Date*, *Actual Departure Date* and *Load Date* (this last option refers to the Load Date of the freight container).

The **Rate Type** for a newly entered standard rate will default to **Base**. It is possible to set up **Exception rates** by 'linking' such an exception rate to a base rate in the **Parent Base Rate ID**field (select the ID of the parent base rate). This then automatically changes the rate type of the exception rate to *Exception*. Exception rates can only be defined for pallet charge codes where the treatment is either 'cost' or 'commission'.

When standard charges are calculated for a produce bill line and a base rate and one or more 'linked' exception rates for a pallet charge code is found, the last exception rate will remain as the 'effective' standard rate for the pallet charge code.

Define the currency and standard rate in the **Charge Currency Code** and **Charge Rate**fields. Pallet Charges that are defined in a foreign currency will calculate in the specified currency and also convert to LCY using the appropriate currency factor as per the cost produce bill from where the standard rate calculation function is performed. For more information, see **Cost Produce Bills**.

The remaining fields in **Pallet Charge Standard Rates** are filter fields that can be used to define and limit the pallet lots for which the standard rates should calculate. It is not necessary to enter a value in every one of these fields, thus allowing for more 'generic' rules to be set up. Filter values should thus be selected to **limit** the pallet lots for which a standard rate should calculate.

```
**Example**

A standard rate is set up with a filter value of CI in the Commodity Group Code field, and no specified filter in Outer Pack Code. This charge will calculate for pallet lots where the Commodity Group Code is CI, irrespective of the Outer Pack Code value. The charge will not calculate for pallet lots where the Commodity Group Code is not CI.

```