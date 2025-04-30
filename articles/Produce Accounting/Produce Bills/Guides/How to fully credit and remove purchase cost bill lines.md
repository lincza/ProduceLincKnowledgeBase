---
grand_parent: Produce Bills
has_children: false
layout: default
nav_order: 52905
parent: Guides
title: How to fully credit and remove purchase cost bill lines
---

# How to fully credit and remove purchase cost bill lines

### In this guide

[Step 1: Reverse posted bill amounts, prioritised charges and recharges](#step-1-reverse-posted-bill-amounts-prioritised-charges-and-recharges)  
[Step 2: Remove the bill lines (optional)](#step-2-remove-the-bill-lines-optional)  

---
## Purchase Cost Bill: reverse bill amounts and charges  
<br/>
Below are the steps to fully reverse the posted bill amounts and prioritised charge entries from some or all of the lines in an already posted purchase cost bill.

## Step 1: Reverse posted bill amounts, prioritised charges and recharges   

In this step we will take the purchase cost bill through a calculation, prepare the reversing amounts and then post the reversing amounts and vendor credit.  


### Re-open the cost produce bill

First, re-open the purchase cost bill.

![](/media/ProduceBills_Guide_ReversePurchBill_01._ReOpenBill.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_02._ReOpenBillChooseYes.png)  


### Calculate charges

Next, _Calculate Charges_ for the purchase cost bill.

![](/media/ProduceBills_Guide_ReversePurchBill_03._BillCalcCharges.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_04._BillChargesCalculated.png)  


### Reverse the prioritised charges and recharges

Now select the first produce bill line that you want to fully reverse. Use the _Reverse Prioritised Charges_ button in the produce bill subpage to create reversing charge entries for the prioritised charges. 

If there are also recharges for the bill line, the _Prioritised Charges (LCY)_ will not yet show zero after the above step. If this is the case, remain on the bill line and click on the _Reverse Recharges_ button in the produce bill subpage. 

Repeat these steps for all the bill lines for which you want to fully reverse the prioritised charges and recharges.

Once you have reversed the prioritised charges and recharges, double-check that _Prioritised Charges (LCY)_ and _Recharges Amount PCY_ on the relevant bill lines are now zero.

Follow along with the visuals below.

![](/media/ProduceBills_Guide_ReversePurchBill_05._BillReversePrior.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_06._BillReversePriorChooseYes.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_07._BillReversePriorNowZero.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_08._BillReverseRecharges.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_09._BillRechargesReversed.png)  




### Calculate Bill and prepare credit amounts for the vendor

Next, _Calculate Bill_ to get the bill in a status that will allow you to prepare the credit amounts for the vendor.

![](/media/ProduceBills_Guide_ReversePurchBill_10._CalculateBill.png)  


Enter the full negative/opposite value of _Posted Amount (PCY)_ into the _Posting Amount (PCY)_ field for all the bill lines you want to reverse. If _Posted Amount (PCY)_ is eg 1 000, then ensure that _Posting Amount (PCY)_ is filled in with a value of - 1 000. You can enter these amounts on the page itself, or use edit in excel if there are a lot of lines you want to fully credit.

Once you have entered full credit posting amounts for all the lines you want to reverse, it is a good idea to check your total amount in the factbox _Posting Amounts_.

Then add _Credit Posting Reason Codes_ for all the lines you are about to post a credit for. 

Follow along with the visuals below.

![](/media/ProduceBills_Guide_ReversePurchBill_11._EnterCreditPostingAmounts.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_12._PostingFullOppositeOfPosted.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_13._CheckFactboxPostingAmount.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_14._EnterCreditReason.png)  



### Post the bill to post the vendor credit and financial entries for reversing charges  

Next you will release and post the purchase cost bill to post the purchase credit memo for the vendor and create the financial entries in your GL for the reversing charges.

After posting the credit for the bill amounts the _Posted Amount (PCY)_ on the bill lines you have fully credit should now show zero. 
It is a good idea to also check the factbox of the bill again after this posting. 

Follow along with the visuals below.  

Release the bill.

![](/media/ProduceBills_Guide_ReversePurchBill_15._ReleaseBill.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_16._ReleaseBillChooseYes.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_17._StatusReleased.png) 

Post the bill.

![](/media/ProduceBills_Guide_ReversePurchBill_18._PostBill.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_19._PostBillChooseYes.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_20._BillPosted.png)  


## Step 2: Remove the bill lines (optional)  

If you reversed the bill amounts, prioritised charges and recharges with the intention of completely removing the bill lines from the produce bill, then also do the following:

Re-open the produce bill.

![](/media/ProduceBills_Guide_ReversePurchBill_21._ReOpenBillAgain.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_22._ReOpenBillAgainChooseYes.png)  


Select the bill lines from which bill amounts, prioritised charges and recharges were fully reversed in the above steps.

![](/media/ProduceBills_Guide_ReversePurchBill_23._SelectLinesToDelete.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_24._SelectALL_LinesToDelete.png)  

Select the _Delete Line_ button in the produce bill subpage. Note that this action can be performed for multiple selected bill lines at once.

![](/media/ProduceBills_Guide_ReversePurchBill_25._DeleteSelectedLines.png)  

Do a final check on the factbox to see if the bill quantity (cartons) is correct.

![](/media/ProduceBills_Guide_ReversePurchBill_26._CheckFactboxAgain.png)  


You can take the bill through _Calculate Charges_, _Calculate Bill_, _Release_ and _Post_ steps again to set the status to _Posted_ again - even if no further posting amounts exist.

![](/media/ProduceBills_Guide_ReversePurchBill_27._CalcAgainReleaseSetPosted.png)  

![](/media/ProduceBills_Guide_ReversePurchBill_28._StatusPostedAgain.png)  