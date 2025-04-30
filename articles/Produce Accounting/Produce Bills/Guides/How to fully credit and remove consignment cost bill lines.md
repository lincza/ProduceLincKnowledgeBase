---
grand_parent: Produce Bills
has_children: false
layout: default
nav_order: 52904
parent: Guides
title: How to fully credit and remove consignment cost bill lines
---

# How to fully credit and remove consignment cost bill lines


### In this guide

[Step 1: Reverse the income on the related produce trade(s)](#step-1-reverse-the-income-on-the-related-produce-trades)  
[Step 2: Reverse the posted bill amounts](#step-2-reverse-the-posted-bill-amounts)  
[Step 3: Reverse the prioritised charges and recharges](#step-3-reverse-the-prioritised-charges-and-recharges)  
[Step 4: Remove the bill lines (optional)](#step-4-remove-the-bill-lines-optional)  


---
## Consignment Cost Bill: reverse bill amounts and charges
<br/>
To fully credit the posted bill amounts and posted prioritised charges from a consignment cost produce bill, the income must also first be reversed on the related produce trade(s). This ensures that the final calculation on the consignment cost produce bill results in a zero (for consignment bills the system calculates the bill amount based on the income less prioritised charges)

Below are the steps to fully reverse the posted bill amounts and prioritised charge entries from some or all of the lines in an already posted consignment cost bill.

---
## Step 1: Reverse the income on the related produce trade(s)  
<br/>
Re-open the cost produce bill first. The bill must be open to allow posting of the produce trade credit. Follow along with the visuals below.  

![](/media/ProduceBills_Guide_ReverseConsignBill_01._Bill%20currently%20posted.png)

![](/media/ProduceBills_Guide_ReverseConsignBill_02._ReopenConsignmentBill.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_03._ReopenConsignmentBill_SelectYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_04._ReopenConsignmentBill_BillNowOpen.png)  


### Re-open the produce trade(s) if already closed  

If the produce trade(s) that are related to the consignment cost bill you want to reverse are already closed, you must first re-open it to prepare the credit for the income. Follow along with the visuals below.

![](/media/ProduceBills_Guide_ReverseConsignBill_05._CheckIfTradeClosed.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_06._OpenTradeCard.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_07._ReopenTrade.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_08._ReopenTradeSelectYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_09._TradeNowOpen.png)  



### Post a full credit for the relevant pallet(s)  

The credit for the produce trade must be posted using the exchange rates as previously used for income postings on the produce trade. In essence, both the _Posted Trade Amount_ and _Posted Trade Amount (LCY)_ for the pallets must be zero after the trade credit is posted.  

Follow the along with the visuals below.  

![](/media/ProduceBills_Guide_ReverseConsignBill_10._TradePrepPostingSection.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_11._TradeOpenFocusMode.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_12._TradeAddPostingCreditReason.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_12._TradeAddPostingCreditReasonRepeatForAllLines.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_13._TradeEnterCreditQty.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_14._TradeSelectAllLinesToCredit.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_15._TradeCreditPostedAmounts.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_16._TradeCheckCreditPostingPrices.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_17._TradeExitFocusMode.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_18._TradeCheckFactBoxPostingAmount.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_19._TradeRelease.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_20._TradeCreditPost.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_21._TradeCreditPostSelectYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_22._TradeFactBoxCheckAfterCreditPosting.png)  


### Close the Produce Trade again

Close the produce trade again; else ProduceLinc will not allow you to run a calculation and post the credit for the consignment cost bill.

Follow along with the visuals below.

![](/media/ProduceBills_Guide_ReverseConsignBill_23._TradeReleaseAgainPrepForClose.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_24._TradeClose.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_25._TradeStatusClosedAgain.png)  


---
## Step 2: Reverse the posted bill amounts  
<br/>
The produce bill should already be in _Open_ status (re-opened in step 1 above).

![](/media/ProduceBills_Guide_ReverseConsignBill_26._BillStatusAlreadyOpen.png)  

### Calculate Charges and Bill  Amounts again

Next, run the _Calculate Charges_ and _Calculate Bill_ for the consignment cost bill again.

![](/media/ProduceBills_Guide_ReverseConsignBill_27._BillCalculateCharges.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_28._BillCalculateBill.png)

![](/media/ProduceBills_Guide_ReverseConsignBill_29._BillStatusBillCalculated.png)  


### Adjust the bill amounts

Fill in 0 (zero) in _Adjusted Bill Amount (PCY)_ on the lines you want to reverse/credit. The system will ask if you want to insert adjustment charges. Choose _Yes_ in this prompt. Repeat this for all the lines you want to post a full credit for in the produce bill.  

![](/media/ProduceBills_Guide_ReverseConsignBill_30._BillAddZeroInAdjustedBillAmount.png) 

![](/media/ProduceBills_Guide_ReverseConsignBill_30._BillInsertAdjustmentEntryConfirm.png)

If there are a lot of bill lines to fully credit, it may be easier to export the bill sheet, make the _New Price Per Outer Pack_ in the Excel sheet zero, and import the bill sheet again.  

Double-check that _Posting Amount (PCY)_ shows the full negative of the values in _Posted Amount (PCY)_. If _Posted Amount (PCY)_ is eg. 1 000, then _Posting Amount (PCY)_ must be -1 000.  

![](/media/ProduceBills_Guide_ReverseConsignBill_31._BillCheckFactboxPostingAmount.png)
  
Enter a _Posting Credit Reason Code_ for all the lines you are about to credit.  

![](/media/ProduceBills_Guide_ReverseConsignBill_32._BillEnterCreditReasonCodes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_33._BillRepeatCreditReasonForAllLines.png)  


### Release and post the bill to fully credit the vendor amounts

Now release and post the bill. 

After posting the credit for the bill amounts the _Posted Amount (PCY)_ on the bill lines you have fully credit should now show zero. 
It is a good idea to check the factbox of the bill after this posting. The Posted Amounts should be zero.

Follow along with the visuals below.  

![](/media/ProduceBills_Guide_ReverseConsignBill_34._BillRelease.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_35._BillPost.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_36._BillRecheckFactboxAfterCreditPosting.png)

---
## Step 3: Reverse the prioritised charges and recharges  
<br/>
You have now credited the bill amounts, but have not yet reversed the charges. You must thus re-open the consignment cost bill again, and take it through another calculation and reversal of charges. 

### Re-open the produce bill again

![](/media/ProduceBills_Guide_ReverseConsignBill_37._BillReopenAgain.png)  


### Calculate charges and reverse the prioritised charges and recharges

First, _Calculate Charges_ again.

![](/media/ProduceBills_Guide_ReverseConsignBill_38._BillCalcChargesAgain.png)  

Now select the first produce bill line that you have fully credited the posted bill amounts for in step 2 above. Use the _Reverse Prioritised Charges_ button in the produce bill subpage to create reversing charge entries for the prioritised charges. 

If there are also recharges for the bill line, the _Prioritised Charges (LCY)_ will not yet show zero after the above step. If this is the case, remain on the bill line and click on the _Reverse Recharges_ button in the produce bill subpage. 

Repeat these steps for all the bill lines for which you want to fully reverse the prioritised charges and recharges.

Once you have reversed the prioritised charges and recharges, double-check that _Prioritised Charges (LCY)_ and _Recharges Amount PCY_ on the relevant bill lines are now zero.

Follow along with the visuals below.

![](/media/ProduceBills_Guide_ReverseConsignBill_39._BillReversePriorCharges.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_40._BillReversePriorChargesSelectYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_41._BillReverseRecharges.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_42._BillReverseRechargesSelectYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_43._BillCheckPriorAndRechargesZero.png)  


### Calculate Bill and check that bill posting amounts are still zero

Now _Calculate Bill_ again

![](/media/ProduceBills_Guide_ReverseConsignBill_44._BillCalcBillAgain.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_45._BillStatusBillCalculatedAgain.png)  


Before you proceed with _release_ and _post_, first double-check that _Posting Amount (PCY)_ are still zero on all the lines for which you have previously reversed the bill amounts and for which you are about to post the reversing prioritised charges and recharges. Since a consignment bill calculates posting amounts for the vendor as income less prioritised charges, these _Posting Amount (PCY)_ values should be zero at this point, since the income has been fully reversed and you have also already created reversal entries for the prioritised charges and recharges. 

![](/media/ProduceBills_Guide_ReverseConsignBill_46._BillCheckPostingsAmtZeroAfterCalc.png)  

### Release and Post the bill to post the reversing prioritised charges and recharges

The steps you took to reverse the prioritised charges and recharges simply created reversing pallet charge entries, but these reversing entries have not yet been posted through to your GL and financials. The bill must thus go through another posting to post the financial entries for the reversing charge entries.

![](/media/ProduceBills_Guide_ReverseConsignBill_47._BillReleaseAgain.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_48._BillPostAgain.png)  


---
## Step 4: Remove the bill lines (optional)  
<br/>
If you reversed the bill amounts, prioritised charges and recharges with the intention of completely removing the bill lines from the produce bill, then also do the following:

Re-open the produce bill

![](/media/ProduceBills_Guide_ReverseConsignBill_49._BillReopenAgainToPrepLineRemoval.png)  

Select the bill lines from which bill amounts, prioritised charges and recharges were fully reversed in the above steps.

![](/media/ProduceBills_Guide_ReverseConsignBill_50._BillSelectLinesToDelete.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_51._BillSelectAllLinesToDelete.png)  

Select the _Delete Line_ button in the produce bill subpage. Note that this action can be performed for multiple selected bill lines at once.

![](/media/ProduceBills_Guide_ReverseConsignBill_52._BillDeleteSelectedLines.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_53._BillDeleteSelectedLinesChooseYes.png)  

![](/media/ProduceBills_Guide_ReverseConsignBill_54._BillLinesDeletedBillEmpty.png)  

You can take the bill through _Calculate Charges_, _Calculate Bill_, _Release_ and _Post_ again to set the status to _Posted_ again - even if no further posting amounts exist.

![](/media/ProduceBills_Guide_ReverseConsignBill_55._BillSetStatusOfEmptyBillToPosted.png)  



