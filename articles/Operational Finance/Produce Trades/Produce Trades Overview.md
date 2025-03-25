---
grand_parent: Operational Finance
has_children: false
layout: default
nav_order: 41001
parent: Produce Trades
title: Produce Trades Overview
---

# Produce Trades Overview


## In this article
[What is a produce trade](#what-is-a-produce-trade)  
[When and how are produce trades created](#when-and-how-are-produce-trades-created)  
[Grouping of pallets for produce trades](#grouping-of-pallets-for-produce-trades)  
[Areas in the produce trade](#areas-in-the-produce-trade)  
[General area](#general-area)  
[Posting area](#posting-area)  
[Pallet Charge Assignments](#pallet-charge-assignments)  
[Produce Trade Lines](#produce-trade-lines)  
[Produce Trade Factbox](#produce-trade-factbox)  
[Produce Trade Posting](#produce-trade-posting)  
[Closing the Produce Trade](#closing-the-produce-trade)  
[Add/Update Standard Charges](#addupdate-standard-charges)  

---
## What is a produce trade
<br/>
A produce trade represents the sale of pallets for a customer’s order. It is not the sales invoice itself, but a ‘system document’ that groups the pallets loaded for a customer’s order together. The produce trade is thus the place from where all invoices and credit memos for that set of pallets will be prepared and posted. 

---
## When and how are produce trades created
<br/>
Produce trades are created after the pallets have loaded into the freight container. When we say freight container, we mean the system’s freight container. This is not necessarily a 40FT high cube container, and could be a local truck, part of a local truck, a set of pallets loaded to a customer with air freight, or a set of pallets loaded with break-bulk/conventional sea freight to a customer.

Once the pallets are in the system freight container that is linked to the outbound produce order, a user confirms the freight container – essentially confirming that all the logistical information of the freight container is correct, and that it is ready to hand over to the finance department for customer.

![](/media/OperationalFinance_ProduceTradesOverview_01_ConfirmedContainers.jpeg)

 The produce trade(s) for the freight container is then created with a click of the Create/Update Produce Trades button. This can be done from either the freight container itself, outbound produce orders or produce shipments.

 ![](/media/OperationalFinance_ProduceTradesOverview_02_CreateTradesFromFreightContainer.jpeg)

 ![](/media/OperationalFinance_ProduceTradesOverview_03_CreateTradesFromOutboundOrder.jpeg)

 ![](/media/OperationalFinance_ProduceTradesOverview_04_CreateTradesFromShipments.jpeg)



---
## Grouping of pallets for produce trades
<br/>
When produce trades are created/updated, ProduceLinc automatically groups these pallets into a produce trade per:

> Delivery Point Code
<br/>
Sell-to-Customer
<br/>
Currency Code
<br/>
Freight Container
<br/>
Outbound Produce Order
<br/>
Salesperson Code
<br/>
Produce Shipment (if the outbound order is linked to a produce shipment)
<br/>

### Example to illustrate

Below is a simplified example to illustrate how pallets are grouped into produce trades.

We have a single freight container for pallets in three different produce orders. 

Pallet 1 to Pallet 6 are grouped into TRADE 1.

Pallet 7 to Pallet 10 are grouped into TRADE 2. While these pallets have the same delivery point code, customer and currency as Pallet 1 to Pallet 6, they come from a different outbound produce order and have a different salesperson code.

Pallet 11 to Pallet 20 are grouped into TRADE 3. These pallets are from a 3rd produce order linked to the freight container, and are for an entirely different delivery point code and customer than the first two produce orders.

![](/media/OperationalFinance_ProduceTradesOverview_05_ProduceTradeGrouping.jpeg)


---
## Areas in the produce trade
<br/>
Produce Trades are structured into 5 areas:

> General
<br/>
Posting
<br/>
Pallet Charge Assignments
<br/>
Produce Trade Lines
<br/>
Produce Trade Factbox
<br/>

---
### General area
<br/>
The General area is the ‘header’ of the produce trade. Most of the information in this area is automatically populated by ProduceLinc when the produce trade is created. It includes the produce order number, customer information, the currency and shipment method (incoterm) for the produce trade and freight information such as details of the freighter trip leg and freight container.

![](/media/OperationalFinance_ProduceTradesOverview_06_GeneralArea.jpeg)

There are two fields that in the General area that must be filled in by a user before any posting can be processed:

**Trade Type**  
A value must be selected from the master data for Trade Type as set up for your business. The Trade Type is used to classify produce trades for easier management of produce trades and for reporting purposes. 
Default produce trade types can be defined for customers in Produce Trade Defaults – in which case ProduceLinc will automatically populate the field when the produce trade is created. If no default trade types exist for the customer, the field will be left empty when the produce trade is created – leaving it up to a user to choose the appropriate value. 

Trade Types can, for example, be used to distinguish between consignment customers and fixed-price customers, export customers, local customers.

**External Document No.**  
The External Document No. must have a value when invoices or credit memos are posted. This is a text field where the user that prepares and posts the invoices / credit memos must specify an External Document No. Your business may have internal guidelines for what you should enter in this field for various scenarios. Some examples include using the customer’s order number, a combination of the system’s outbound produce order number and container number / out-consignment number of the container, etc. 

Once the External Document No. has been filled in during preparation of the first posting, the value will remain for subsequent postings.

---
### Posting area
<br/>
The posting area is filled in by a user every time an invoice or credit memo is prepared and posted. 

![](/media/OperationalFinance_ProduceTradesOverview_07_PostingArea.jpeg)


**Posting Type**  
Used to specify if you’re about to post an invoice or credit memo.


**Posting Date**  
This must be selected by the user when preparing the posting. This posting date will be carried through to the customer ledger entries and GL entries. 


**Trade Exch. Rate Date Basis** and **Trade Exch. Rate Date**  
ProduceLinc allows various options for the exchange rate that must be used for invoice and credit memo posting from the produce trade. The exchange rate (currency factor) is determined by the Trade Exch. Rate Date Basis and Trade Exch Rate Date. 

Options for the Trade Exch. Rate Date Basis include  
> Posting Date  
> Estimated Departure Week  
> Actual Departure Week  
> Estimated Arrival Week  
> Actual Arrival Week  
> Container Load Date
<br/>

If _Posting Date_ is used as the Trade Exchange Rate Date Basis, the posting date for the invoice or credit memo determines the exchange rate and the value that the system populates in the currency factor field. 

For the _week-based options_ (ETD week, ATD week, ETA week and ATA week) the Trade Exch. Rate Date will be the Monday of the relevant week, and the system will populate the currency factor based on the exchange rate for that Monday.

If _Container Load Date_ is used as the Trade Exchange Rate Date Basis, the system will set the Trade Exchange Rate Date of the produce trade to the container’s load date and populate the currency factor based on the exchange rate of the container’s load date.


**Trade Exch. Rate Date Change Pending**  
If you are using a Trade Exch. Rate Date Basis option other than Posting Date, the system will use this Trade Exch. Rate Date Change Pending to show a user that the date on which the exchange rate for the produce trade is based, has changed.  


**Payment Terms Code**  
ProduceLinc automatically populates the payment terms code from the customer master data when the produce trade is created. This value can, however, be changed by the user when preparing the produce trade for invoice posting.


**Your Reference** and **Posting Description**  
These two text fields must be filled in by a user for every posting of an invoice or credit memo from the produce trade. Your business may have some internal principles of what you should enter in these fields for various scenarios. You may, for instance, use the word “Advance” and the container number for advance invoice postings and “Final” and the container number for final account sale postings. Or the Delivery Note Number (Container External Document No.) when posting an invoice for a local sale. Or the number of the account sale you received from your consignment customer.

The Posting Description will carry through to the customer ledger entries. It’s thus a good idea to make this value something that could be useful in searching or filtering of the customer ledger entries.


**Final Posting**  
This check box indicates if you are about to post an advance invoice or final invoice. When the system creates the produce trade, the check box will initially be unchecked – indicating ‘advance invoice’. If you are about to post a final account sale or an invoice for a fixed-price customer, you should check the box.

![](/media/OperationalFinance_ProduceTradesOverview_10_FinalPostingNo.jpeg)

![](/media/OperationalFinance_ProduceTradesOverview_11_FinalPostingYes.jpeg)


---
### Pallet Charge Assignments
<br/>
This area of the produce trade is used for adding account sale costs that your customer deducted from the sale of the pallets and is typically used when you receive the final account sales from an overseas consignment customer of local municipal market customer.

Account sale costs are added by choosing the _Assignment Level_, _Assignment Target_ and _Pallet Charge Code_, and then entering the amount that must be posted.

These costs can be added on three different levels. 
<br/>

**Produce Trade**  
Most account sale costs are posted on produce trade level. If you choose this level, ProduceLinc will automatically populate the number of the Produce Trade you are working on in the Assignment Target field.

For this level, the amount you enter will apply to ALL the pallets in the produce trade.

**Pallet**  
In cases where your customer has deducted a cost that only applies to one or some of the pallet IDs in the produce trade, you can choose assignment level _Pallet_, choose the appropriate Pallet ID in the Assignment Target field and then enter the amount.

**Pallet Lot**  
Assignment Level _Pallet Lot_ can be used in cases where your customer has deducted a cost that applies to a specific part of a pallet ID. 

Here’s an example of the Pallet Charge Assignment Area with prepared details. 
![](/media/OperationalFinance_ProduceTradesOverview_08_PalletChargeAssignmentArea.jpeg)

In this example the amounts for _AS DUTY_ and _AS COMM_ will apply and spread across all the pallets in the produce trade. The amount for _AS STORE_ is only applicable to one specific pallet ID and an _AS MISC_ cost will be deducted from pallet lot LOT012917.


---
### Produce Trade Lines
<br/>
This area contains the detail of the pallets that were loaded for the customer’s order and freight container. It is also the place where you prepare the prices and amounts for the invoice or credit memo you want to post or perform other activities like redirecting some/all pallets to another customer, remove pallets from the produce trade, split some quantities of a line off to a separate pallet line or return pallets to the vendor.

![](/media/OperationalFinance_ProduceTradesOverview_09_ProduceTradeLinesArea.jpeg)

Various ‘buttons’ are included in the Produce Trade Lines area to assist you with activities:

**Edit in Excel**  
This allows you to prepare posting prices in Excel. It is typically used for final account sales where matching of the account sales prices to specific pallet lines and fruit spec is easier to do in Excel than on the page itself. Once the posting prices are prepared, you can publish the information to update the posting prices and amounts on the produce trade lines.

**Apply Posting Price**  
This button applies the price you enter in _New Posting Price_ to the produce trade lines you selected. It is typically used in consignment sale cases where you don’t want to invoice the intended sales price, but rather advance or final prices that differ from the intended sales price. 
It’s also useful to clear the posting prices for multiple lines. Make the “New Posting Price” zero, select the lines for which you want to clear the posting prices and choose _Apply Posting Price_.

![](/media/OperationalFinance_ProduceTradesOverview_12_ApplyPostingPrice.jpeg)

**Apply Min. Guarantee Price**  
This button applies the minimum guarantee sales price to the produce trade lines you selected.

![](/media/OperationalFinance_ProduceTradesOverview_13_ApplyMGP.jpeg)

**Apply Remaining Posting Price**  
This button is the one you’ll typically use for fixed-price sales where the intended sales price must be invoiced.

It updates the posting price of selected lines with the difference between the intended sales price and the price that was previously posted.

If nothing was posted yet/already posted amounts are zero, then _Apply Remaining Posting Price_ fills in the full intended sales price in the _Posting Price_ field of the lines you selected.
Let’s say the intended sales price is 15.00 and you have previously posted an advance of 5.00. Then _Apply Remaining Posting Price_ will fill in 10.00 in the _Posting Price_ for the lines that you selected.

![](/media/OperationalFinance_ProduceTradesOverview_14_ApplyRemainingPostingPrice.jpeg)

**Credit Posted Amounts**  
Makes the _Posting Price_ and _Posting Amount_ of the lines you selected the full negative of the already _Posted Trade Amounts_. Use this button when you want to post a full credit for some/all of the pallets.

![](/media/OperationalFinance_ProduceTradesOverview_15_CreditPostedAmounts.jpeg)

**Apply Intended Sales Credit Price**  
In cases where the intended sales credit prices were captured in a related Arrival QC and produce trade claim register, the produce trade lines will already have the Intended Sales Credit Price updated. The _Posting Credit Reason_, _Posting Credit Quantity_ will also be populated, and the _Quality Document No._ field will show the number of the Arrival QC quality document for which a credit memo must be posted.

In this scenario most of the preparation has thus already be done. The _Apply Intended Sales Credit Price_ button can be used to simply update the _Posting Price_ with the _Intended Sales Credit Price_. 

![](/media/OperationalFinance_ProduceTradesOverview_16_ApplyIntendedSalesCredit.jpeg)


**Process Redirection**  
This button is used in cases where pallets must be moved from one customer to another. 

Example case:

The original customer cannot accept the pallets due to quality issues, or delivery of pallets that they haven’t ordered. You have found another customer willing to accept the pallets.

To redirect pallets, you must provide the system with instructions about the new customer in the _Redirect_ fields on the produce trade lines. This includes the _Redirect Delivery Point_, _Redirect Sales Price_ and optionally a _Redirect Reference_.

The _Process Redirection_ then moves the selected pallets from the current produce trade to a produce trade for the new redirect customer. If no produce trade yet exists for the redirect customer for the same produce order and freight container, ProduceLinc will automatically create the new produce trade.

Pallets can only be redirected if they have not yet been invoiced or have been fully credited from the original customer.

![](/media/OperationalFinance_ProduceTradesOverview_17_ProcessRedirection.jpeg)


**Process Removal**  
This action removes the pallets for the lines you selected from the produce trade AND the freight container. 

The button is typically used in cases where the load file from the cold store was incorrect and the pallets never really loaded.

Note this action removes FULL pallet IDs. You cannot remove only a part of a pallet ID from a produce trade and container. 
Pallet IDs can also only be removed from a produce trade if they have not yet been invoiced, or their posted invoice amounts have been fully credited.

![](/media/OperationalFinance_ProduceTradesOverview_18_ProcessRemoval.jpeg)


**Return to Vendor**  
Use cases for this action:

You have sold a pallet to a customer who can no longer accept the pallet. The producer/vendor of the pallet has found a customer for a pallet and will invoice that new customer directly. Your business is thus no longer selling the pallet or receiving any income for it.

The button removes the produce trade lines you selected from the produce trade and freight container and removes its allocation information. Pallets that have been returned to vendor are flagged and no longer available for future sales allocations.

![](/media/OperationalFinance_ProduceTradesOverview_19_ReturnToVendor.jpeg)


**Prepare Credits**  
This action is used in cases where you don’t want to credit the full quantity of the pallet line(s).

An example to illustrate:

You want to post a credit for 20 of the 80 cartons on the selected pallet ID below. You filled in the credit quantity as 20, provided credit price and a credit reason code. The 20 cartons must be ‘split off’ into a new pallet line so that its credit price won’t negatively impact the remaining 60 cartons’ average price.

The Prepare Credits button then instructs ProduceLinc to split the 20 cartons off to a new pallet line with a new pallet lot number, carry over the credit posting information to this new line, reduce the quantity of the original pallet line to 60 cartons and clear the credit posting information from this original pallet line.

As a result, your lines in the produce trade are then ready for their credit posting.

Here’s what the produce trade lines look like in our example with credit information provided, but before choosing the _Prepare Credits_ button.
![](/media/OperationalFinance_ProduceTradesOverview_20_PrepareCredits_Before.jpeg)

And this is how the produce trade lines for this pallet ID look after choosing the _Prepare Credits_ button. There’s a new pallet line with its own unique pallet lot no. for the 20 cartons; and with the credit information carried over. The original pallet line has a reduced quantity of 60 and no credit posting information. When the credit memo is posted, it will only be for the 20 cartons on the new pallet lot.

![](/media/OperationalFinance_ProduceTradesOverview_21_PrepareCredits_After.jpeg)


**Split Pallet**  
This action splits off the quantity you specified in the _Split Quantity_ field, creates a new pallet line with new pallet lot number (but same pallet ID) for it and reduces the quantity on the original pallet line.

This is a useful action in cases where you want to redirect only some of the cartons from a pallet line. 

An example to illustrate:

You want to redirect 30 cartons of a pallet line with 80 cartons to a new customer. But when a redirect is processed, the system moves the entire pallet line to the new customer and produce trade. You thus need the 30 cartons to be on a separate pallet line. 

You enter the Split Quantity of 30. This is how the produce trade line for the pallet looks like before you choose the _Split Pallet_ button.
![](/media/OperationalFinance_ProduceTradesOverview_22_SplitPallet_Before.jpeg)

After choosing the _Split Pallet_ action, the produce trade lines for this pallet ID now look like below. The original pallet line has a reduced quantity of 50 and a new pallet line with new pallet lot number has been created with a quantity of 30. 
![](/media/OperationalFinance_ProduceTradesOverview_23_SplitPallet_After.jpeg)


---
### Produce Trade Factbox
<br/>
Each produce trade has a Factbox that users can show or hide as needed with a click on the Information icon at the top right of the produce trade.

![](/media/OperationalFinance_ProduceTradesOverview_24_ShowHideTradeFactbox.jpeg)

The factbox consists of three areas:
<br/>

> Summary of pallets and postings
<br/>
Sales invoices and credit memos posted for the produce trade
<br/>
Attachments
<br/>

**Summary of pallets and postings**  

The top area of the factbox shows a summary of the pallets in the produce trade, the amounts that are about to be posted and already posted amounts. 

![](/media/OperationalFinance_ProduceTradesOverview_25_TradeFactboxSummary.jpeg)

Here is an overview of the information fields:

#### Trade Pallets   
> Produce Trade Pallets: _total pallets in the produce trade_

> Posting Pallets: _the number of pallets that currently have posting amounts that are about to be posted. When your intention is to post an invoice or credit memo for ALL the pallets in the trade, it is good practice to check that Posting Pallets are the same as the total Produce Trade Pallets._

> Posting Credit Pallets: _the number of pallets that currently have credit posting quantities for which a credit memo is about to be posted._
<br/>

  
#### Trade Quantities   
> Produce Trade Quantity: _total number of cartons/outer packs in the produce trade_

> Posting Quantity: _the total number of cartons/outer packs that currently have posting amounts that are about to be posted._

> Posting Quantity: _the number of cartons/outer packs that currently have credit posting quantities and for which a credit memo is about to be posted._
<br/>

  
#### Posting Amounts    
> These refer to the amounts that are about to be posted.

> Posting Amount: _total of the posting amounts (in currency) that you are about to post for the produce trade._

> Posting Charges Amount: _total of the posting amounts or pallet charge assignments (account sale costs) you are about to post for the produce trade._

> Posting Charges VAT Amount: _the total VAT amount the system will calculate and post for the pallet charge assignments you are about to post for the produce trade._

> Net Posting Amount (incl.): _The Net total of the amount you are about to post, including VAT. When posting account sales for consignment customers, it is good practice to check the total amounts and VAT of the actual account sale against the amounts in this Posting Amounts area of the factbox to ensure that you have accurately captured the information of the account sale._
<br/>

  
#### Posted Amounts  
> Posted Trade Amount: _the total of amounts (in currency) already posted for the produce trade._

> Posted Charges Amount: _the total of amounts (in currency) already posted for income charges / account sales costs for the produce trade._

> Posted Charges VAT Amount (incl.): _total of the VAT amounts already posted for any charge assignments that were previously posted._

> Net Posted Amount (incl.): _The Net amount already posted for the produce trade, including the income for the pallets, pallet charge assignments and any VAT posted for these pallet charge assignments._

> Posted Trade Amount (LCY): _The amount already posted for the pallets in the produce trade, but in local currency._

> Posted Charges Amount (LCY): _the amount already posted for pallet charge assignments for the produce trade, but in local currency._

  
#### Totals   
> The Totals area again just shows a summary of values you are about to post and values already posted. 
<br/>

  
**Produce Trade Doc. Factbox**    

All sales invoices and credit memos posted from the produce trade are automatically stored in this area of the factbox. From here these documents can be printed or emailed directly to the customer from the system.

![](/media/OperationalFinance_ProduceTradesOverview_26_TradeDocFactbox.jpeg)

Each posted sales document shows the relevant Produce Trade Number, Posted Document Number, Document Amount and Document Amount including VAT.
These documents can be printed or emailed to the customer by using the actions from the drop-down. 

![](/media/OperationalFinance_ProduceTradesOverview_27_TradeDocFactboxActions.jpeg)


**Attachments**   

Supporting documents can be attached to the produce trade with an easy drag-and-drop to the Attachments area.

![](/media/OperationalFinance_ProduceTradesOverview_38_TradeAttachments.jpeg)


---
## Produce Trade Posting
<br/>
Produce trades must be prepared with the necessary posting amounts every time an Invoice or Credit Memo is posted.

This requires a user to first fill in the Posting area, then apply the necessary posting amounts for the produce trade lines and/or pallet charge assignments.

Thereafter the user must Release the produce trade and then Post.

![](/media/OperationalFinance_ProduceTradesOverview_28_ReleasePost.jpeg)

ProduceLinc will automatically clear values for Posting Type, Posting Date, Your Reference and Posting Description after Each posting; leaving the produce trade ready for a subsequent posting if needed.


---
## Closing the Produce Trade
<br/>
When all income and income costs were processed for the produce trade, it must be set to _Closed_ status. First _Release_ the Produce Trade, then _Close_. 

![](/media/OperationalFinance_ProduceTradesOverview_29_CloseButton.jpeg)

The _Closed_ status indicates that the pallets of the produce trade are ready for a cost produce bill and producer payment calculations.

**A produce trade can only be closed under the following conditions**

A final posting must exist for the produce trade. This ensures that a produce trade does not proceed to final calculations for producer payments if further income must still be posted for its pallets. If the last invoice or credit memo was not posted as final by mistake, it can be set as final with the use of the _Set as Final_ action in the Produce Trade Doc. Factbox.

![](/media/OperationalFinance_ProduceTradesOverview_30_FinalPostedIndicator.jpeg)

![](/media/OperationalFinance_ProduceTradesOverview_31_SetAsFinal.jpeg)

A produce trade can only be closed if _Posting Amount_ for all the produce trade lines are zero; meaning that the produce trade is not currently in a prepared status for another posting.

No open claims must exist for the produce trade. This is indicated in the _Open Claim_ field in the General area of the produce trade. This again ensures that pallets in the produce trade do not proceed to final calculations for producer payment if there are potential income credits that are still negotiated and not yet posted.

![](/media/OperationalFinance_ProduceTradesOverview_32_OpenClaimIndicator.jpeg)



---
## Add/Update Standard Charges
<br/>
ProduceLinc includes functionality to calculate standard rates for income charges on produce trades. This refers to the account sale costs that consignment customers will deduct on the account sale they send. In cases where certain customers always charge the same rate, for example a fixed commission percentage, this standard rate can be defined in Pallet Charge Standard Rates.

Using this feature is optional. Income pallet charge assignments can also be manually added to the produce trade when the posting amounts are prepared.

If standard rates are defined, ProduceLinc will automatically insert a pallet charge assignment line per pallet charge code when the produce trade is created. These charge assignment lines will already have calculated posting amounts.

In cases where the pallet charge code must calculate as a percentage of income, ProduceLinc will initially insert the line with a zero-posting amount, since there will not yet be posting amounts for the pallets in the produce trade.

Once the produce trade lines’ posting amounts are prepared, the _Add/Update Standard Charges_ button in the produce trade menu can be used to re-calculate the posting amounts for the income percentage-based pallet charges (such as account sale commission).

The standard rate amount is calculated based on the posting amount of pallets plus their already posted amounts.

The _Add/Update Standard Charges_ button will also re-calculate other pallet charge assignments, in case the standard rate has since been updated to a different rate.

The calculated posting amounts for these income charges can be manually adjusted before posting, if they do not correspond with the actual amounts on the account sale.

In the example below there are two pallet charge codes. The code for _AS COMM_ must calculate as 5 percent of the income of the pallets. With initial insert the posting amount for _AS COMM_ is thus zero. The standard rate of EUR 20.00 per pallet has already been calculated for _AS FREIGHT_ for the 10 pallets in the produce trade.

![](/media/OperationalFinance_ProduceTradesOverview_33_TradeStandardCharge_FirstInsert.jpeg)

This is what the income charge assignments look like after preparing posting amounts for the pallets to the total value of EUR 12,000 and choosing the _Add/Update Standard Charges_ button in the menu.

![](/media/OperationalFinance_ProduceTradesOverview_34_TradeStandardCharge_AddUpdateStandardCharges.jpeg)

This is the pallet charge assignments after posting. Note that Posting Amounts were cleared. The posted amounts are found under _Amount_ and _Amount (LCY)_.

![](/media/OperationalFinance_ProduceTradesOverview_36_TradePostedStdCharges.jpeg)

In our example we realised that our standard rate of 5% for _AS COMM_ was incorrect and we updated it to 7%. 

We prepared the produce trade with a further posting amount of EUR 800.00.

The total income for the pallets will thus be 12 800 (12 000 already posted, 800 about to be posted). The _Add/Update Standard Charges_ button recalculates the standard charge for _AS COMM_ as 1 024 (7% of the full 12 800). Since 600 was already posted for _AS COMM_, the posting amount is now calculated as the difference of 424.00.

This is how the pallet charge assignments look after again choosing _Add/Update Standard Charges_ in the menu.

![](/media/OperationalFinance_ProduceTradesOverview_37_TradeRecalcStdChargesForNewPosting.jpeg)

---