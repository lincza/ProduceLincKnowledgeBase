---
grand_parent: Operational Finance
has_children: false
layout: default
nav_order: 41002
parent: Produce Trades
title: Produce Trade Posting
---

# Produce Trade Posting

The posting of a Produce Trade generates a Business Central sales invoice (if the sum of posting amounts is positive) or sales credit memo (if the sum of posting amounts is negative).

The individual posting amounts of the produce trade lines (pallets) and pallet charges are populated as lines on the sales document and will post to the relevant G/L Account/s as defined in **Interim Sales Account** in **Produce Posting Setup**.

In cases where **Defer Sales** in **Linc Setup** is not switched on, the posting amounts for pallets with a *Purchase* Lot Billing Type will post to the **Final Sales Account**.

How to post an invoice or credit memo for the produce trade
-----------------------------------------------------------

* Select the **Trade Type** in the produce trade header. The **Trade Type** can be used to distinguish between different types of sales, for example 'fixed price' trades and 'account sale' trades. Trade types can be set up as master data in **Linc Lookup Values**.
* Complete the **External Document No.** in the header. The customer's order number would typically be used for this field.
* The **Trade Type** and **External Document No.** are mandatory fields for posting invoices and credit memo's, but once you have entered the values before the posting of the first invoice, the values will remain for subsequent postings.
* In the *Posting Section* of the produce trade: select *Invoice* or *Credit Memo* as the **Posting Type**and choose the **Posting Date**. Should the exchange rate be based on a different date than the posting date, an alternative option can be set up in **Linc Setup**. This option will default to **Trade Exch. Rate Date Basis.** The applicable exchange rate will be visible under **Trade Exch. Rate Date.**In the case where the source date changes, the **Exch. Rate Date Change Pending** flag will be switched on. The **Currency Factor** will auto-populate from the Exchange Rates, based on the produce trade currency and exchange rate basis of the invoice or credit memo. The **Payment Terms Code** will default from the customer card, but can be manually edited before posting. Enter values in **Your Reference** and **Posting Description**. **Final Posting** can be switched on or off to distinguish between advance and final invoices/credit memo's. Note that a produce trade can only be **Closed** if at least one of the posted documents was a final posting.
* The functions in the menu of the *Produce Trade Lines* section can be used to easily enter prices for selected lines. **Apply Posting Price** applies the value in **New Posting Price**. Positive or negative amounts can be entered in this field - depending on the posting type (invoice or credit memo). **Apply Remaining Posting Price** calculates the difference between already posted amounts and the intended sales amounts and populates the posting prices with the difference.
* Negative posting amounts are only allowed for lines where **Posting Credit Reason Code** and **Posting Credit Quantity** values exist. To fully credit the already posted amounts on lines, select the relevant lines and choose **Credit Posted Amounts**.
* Produce trade pallet charges can be posted together with the invoice or credit values of the produce. See [Post produce trade pallet charges](https://lincza.github.io/Linc-ProduceLinc/documentation/produce-trades-pallet-charges) for more information.
* Once all posting values are completed, choose the **Refresh** function in the produce trade menu or press F5 on your keyboard to refresh the **Produce Trade Totals Factbox** and review the total values that will be posted under *Posting Amounts*.
* To post the invoice or credit memo, choose **Release** under the **Process** menu in the produce trade header, and then choose **Post**. The posted document type, document no. and document amount will appear in the **Produce Trade Doc. Factbox** once posted. From here the document can be printed and emailed.

How to close the Produce Trade
------------------------------

Multiple invoices and credit memo's can be posted from a produce trade. When the income for a produce trade has been finalised and the last invoice or credit memo posted, the produce trade should be closed.

The **Closed** status of a produce trade impacts reporting and cost produce bill behaviour in the following ways:

* it signifies that the income on the related pallet lots have been finalised
* where the lot billing type of the related pallet lots is *Consignment*, the produce trade must be closed before the pallet lots will be allowed onto a cost produce bill
* where the lot billing type of the related pallet lots is *Purchase* and **Defer Sales** in **Linc Setup** is switched on, pallet charges on the cost produce bill can only calculate and post if the produce trade is closed.