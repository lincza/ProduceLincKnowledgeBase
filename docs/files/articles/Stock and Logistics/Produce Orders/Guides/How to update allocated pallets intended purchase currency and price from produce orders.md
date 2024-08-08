---
grand_parent: Produce Orders
has_children: false
layout: default
nav_order: 42903
parent: Guides
title: How to update allocated pallets intended purchase currency and price from produce
  orders
---

How to update allocated pallets intended purchase currency and price from produce orders

You may have noticed that the intended purchase currency and price on the allocated pallets sometimes update when you enter/modify these values on the produce order line; and sometimes they don't. While this may seem random, there is logic behind it.




**Here's how this works:**
==========================

  


A user allocates a pallet from a produce order line that has an intended purchase currency and price, or they modify the intended purchase currency and price on a produce order line that has allocated pallet(s).

  


The allocated pallet is then subjected to a few tests to see if

a) the intended purchase currency may be updated

b) the intended purchase price may be update










The pallet is on no produce bill and the vendor may be paid in any currency
---------------------------------------------------------------------------




If the pallet is not on ANY produce bill yet AND if the vendor of the pallet is not limited to a specific currency, then both the intended purchase currency and price on the pallet will update with the information entered on the order line - even if the allocated pallet already had values in these fields




The pallet is NOT on any produce bill, but the vendor may only be paid in a specific currency
---------------------------------------------------------------------------------------------

If the vendor is limited to a specific currency and the intended purchase currency entered on the order line is different, then the system keeps the intended purchase currency of the allocated pallet and updates the pallet's intended purchase price with a converted value.




**Example:**

Vendor may only be paid in LCY

Order line intended purchase currency is USD and the price is 10.00

The exchange rate for USD is 18.

The result: the allocated pallet will be updated with intended purchase currency "blank" (i.e. LCY) and intended purchase price of 180 (USD 10.00 x exch. rate of 18)







The vendor may be paid in any currency, but the pallet is already on one or more produce bill
---------------------------------------------------------------------------------------------




If the pallet is found on any kind of produce bill, then the intended purchase currency can of course not update. But what if it's only found on a forecast bill that was generated very early on? Since we don't want a 'temporary' bill like a forecast bill to prevent the update of currency and price, the system will first remove the allocated pallet from the forecast bill if the user modifies the intended purchase currency and price on the order line.




Then the system proceeds to check if the pallet is on any other produce bills. Both the purpose and status of any other produce bills the pallet is found on matters:




* If the pallet is on an advance bill **only**, the currency cannot update, but the system will update the intended price with a converted price




* If the pallet is on an invoice produce bill / cost produce bill, then the intended purchase currency can of course not update, but if the status of the invoice and/or cost produce bill is still OPEN, then the price may still update - in which case the system will update the intended purchase price of the allocated pallet with a converted price. If the status is NOT OPEN, then the intended purchase price will NOT update on the pallet.










Illustrative matrix
-------------------








| Produce Order Line: Intended Purchase Currency & Price modified to: | | | | USD | 10 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pallet Line:Current Intended Purchase Currency & Price | | | |  | 100 |  |  |  |  |
| USD/ZAR exchange rate | | | |  | 18 |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| Vendor Currency Limited | Vendor Currency | Pallet on Advance Produce Bill | Pallet on Invoice Produce Bill | Invoice Produce Bill Status | Pallet on Cost Produce Bill | Cost Produce Bill Status | Resulting Intended Purchase Currency on pallet | Resulting Intended Purchase Price on pallet | Notes |
| NO | ANY CURRENCY |  |  |  |  |  | USD | 10 | Currency and price updates |
| YES | LCY |  |  |  |  |  |  | 180 | Updates with converted price |
|  | | | | | | | | | |
| NO | ANY CURRENCY | YES |  |  |  |  |  | 180 | Updates with converted price |
|  | | | | | | | | | |
| NO | ANY CURRENCY |  | YES | OPEN |  |  |  | 180 | Updates with converted price |
| NO | ANY CURRENCY |  | YES | NOT OPEN |  |  |  | 100 | Invoice bill not open. Neither currency or price may update |
|  | | | | | | | | | |
| NO | ANY CURRENCY |  |  |  | YES | OPEN |  | 180 | Updates with converted price |
| NO | ANY CURRENCY |  |  |  | YES | NOT OPEN |  | 100 | Cost bill not open. Neither currency nor price may update |
|  | | | | | | | | | |
| NO | ANY CURRENCY |  | YES | NOT OPEN | YES | OPEN |  | 100 | Cost bill open, but invoice bill is not. Neither currency nor price may update |