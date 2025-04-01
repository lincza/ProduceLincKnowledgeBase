---
grand_parent: Produce Bills
has_children: false
layout: default
nav_order: 52905
parent: Guides
title: How to credit charges and posted bill amounts
---

# How to credit charges and posted bill amounts



### In this article

[Consignment Cost Bill: reverse bill amounts and charges](#consignment-cost-bill-reverse-bill-amounts-and-charges)  
[Purchase Cost Bill: reverse bill amounts and charges](#purchase-cost-bill-reverse-bill-amounts-and-charges)  

---
## Consignment Cost Bill: reverse bill amounts and charges
<br/>
To fully credit the posted bill amounts and posted prioritised charges from a consignment cost produce bill, the income must also first be reversed on the related produce trade(s). This ensures that the final calculation on the consignment cost produce bill results in a zero (for consignment bills the system calculates the bill amount based on the income less prioritised charges)

Below are the steps to fully reverse the posted bill amounts and prioritised charge entries from some or all of the lines in an already posted consignment cost bill.

### Step 1: Reverse the income on the related produce trade(s)  

- Re-open the cost produce bill first. The bill must be open to allow posting of the produce trade credit.

- From the produce trade(s): 
    - Re-open the produce trade if it is already closed.
    - Post a full credit for the relevant pallet(s). This credit must be posted using the exchange rates as previously used for income postings on the produce trade. In essence, both the _Posted Trade Amount_ and _Posted Trade Amount (LCY)_ for the pallets must be zero after the trade credit is posted.
    - Close the Produce Trade again.


### Step 2: Reverse the posted bill amounts  

- The produce bill should already be in _Open_ status (re-opened in step 1 above)
- Calculate Charges

- Calculate Bill
    - Fill in 0 (zero) in _Adjusted Bill Amount (PCY)_ on the lines you want to reverse/credit. The system will ask if you want to insert adjustment charges. Choose _Yes_ in this prompt. Repeat this for all the lines you want to post a full credit for in the produce bill. 
        - If there are a lot of bill lines to fully credit, it may be easier to export the bill sheet, make the _New Price Per Outer Pack_ in the Excel sheet zero, and import the bill sheet again.
    - Double-check that _Posting Amount (PCY)_ shows the full negative of the values in _Posted Amount (PCY)_. If _Posted Amount (PCY)_ is eg. 1 000, then _Posting Amount (PCY)_ must be -1 000.
    - Enter a _Posting Credit Reason Code_ for all the lines you are about to credit.
- Release the produce bill
- Post

After step 2, the _Posted Amount (PCY)_ on the bill lines you have fully credit should now show zero. 
Proceeed to step 3.

### Step 3: Reverse the prioritised charges and recharges  

- Re-open the produce bill again
- Calculate charges

- Select the first produce bill line that you have fully credit the posted bill amounts for in step 2 above.
  - Use the _Reverse Prioritised Charges_ button in the produce bill subpage to create reversing charge entries for the prioritised charges.
  - If there are also recharges for the bill line, the _Prioritised Charges (LCY)_ will not yet show zero after the above step. If this is the case, remain on the bill line and click on the _Reverse Recharges_ button in the produce bill subpage. 
    * Repeat these two steps for all the bill lines for which you want to fully reverse the prioritised charges and recharges.

- Double-check that _Prioritised Charges (LCY)_ and _Recharges Amount PCY_ on the relevant bill lines are now zero.
- Calculate Bill
  - Double-check that _Posting Amount (PCY)_ are still zero on all the lines for which you have previously reversed the bill amounts and for which you are about to reverse the prioritised charges and recharges. Since a consignment bill calculates posting amounts for the vendor as income less prioritised charges, these _Posting Amount (PCY)_ values should be zero at this point, since the income has been fully reversed and you have also already created reversal entries for the prioritised charges and recharges. 
- Release
- Post

The _Post_ action is needed to actually post the financial transactions for the prioritised charges and recharges for which you have created reversal lines.

### Step 4: Remove the bill lines (optional)  

If you reversed the bill amounts, prioritised charges and recharges with the intention of completely removing the bill lines from the produce bill, then also do the following:

- Re-open the produce bill
- Select the bill lines from which bill amounts, prioritised charges and recharges were fully reversed in the above steps.
- Select the _Delete Line_ button in the produce bill subpage. Note that this action can be performed for multiple selected bill lines at once.
- You can take the bill through _Calculate Charges_, _Calculate Bill_, _Release_ and _Post_ again to set the status to _Posted_ again - even if no further posting amounts exist



---
## Purchase Cost Bill: reverse bill amounts and charges  
<br/>
Below are the steps to fully reverse the posted bill amounts and prioritised charge entries from some or all of the lines in an already posted purchase cost bill.

### Step 1: Reverse posted bill amounts, prioritised charges and recharges   

- Re-open the cost produce bill
- Calculate charges

- Select the first produce bill line that you have fully credit the posted bill amounts for in step 2 above.
  - Use the _Reverse Prioritised Charges_ button in the produce bill subpage to create reversing charge entries for the prioritised charges.
  - If there are also recharges for the bill line, the _Prioritised Charges (LCY)_ will not yet show zero after the above step. If this is the case, remain on the bill line and click on the _Reverse Recharges_ button in the produce bill subpage. 
    * Repeat these two steps for all the bill lines for which you want to fully reverse the prioritised charges and recharges.

- Double-check that _Prioritised Charges (LCY)_ and _Recharges Amount PCY_ on the relevant bill lines are now zero.

- Calculate Bill
  - Enter the full negative/opposite value of _Posted Amount (PCY)_ into the _Posting Amount (PCY)_ field for all the bill lines you want to reverse. If _Posted Amount (PCY)_ is eg 1 000, then ensure that _Posting Amount (PCY)_ is filled in with a value of - 1 000. You can enter these amounts on the page itself, or use edit in excel if there are a lot of lines to prepare reversing data for.
    - Double-check that _Posting Amount (PCY)_ are still zero on all the lines for which you have previously reversed the bill amounts and for which you are about to reverse the prioritised charges and recharges. Since a consignment bill calculates posting amounts for the vendor as income less prioritised charges, these _Posting Amount (PCY)_ values should be zero at this point, since the income has been fully reversed and you have also already created reversal entries for the prioritised charges and recharges. 
- Release
- Post

### Step 2: Remove the bill lines (optional)  

If you reversed the bill amounts, prioritised charges and recharges with the intention of completely removing the bill lines from the produce bill, then also do the following:

- Re-open the produce bill
- Select the bill lines from which bill amounts, prioritised charges and recharges were fully reversed in the above steps.
- Select the _Delete Line_ button in the produce bill subpage. Note that this action can be performed for multiple selected bill lines at once.
- You can take the bill through _Calculate Charges_, _Calculate Bill_, _Release_ and _Post_ steps again to set the status to _Posted_ again - even if no further posting amounts exist