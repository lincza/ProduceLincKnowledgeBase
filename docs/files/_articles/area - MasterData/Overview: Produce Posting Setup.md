# Overview: Produce Posting Setup

Sales documents from produce trades and purchase documents from produce bills post to G/L Accounts. In addition, cost produce bills also post the prioritised costs to G/L Accounts. The relevant G/L Accounts to which these various transactions must post are set up in **Produce Posting Setup**.

Posting rules are set up by **General Business Posting Group**, **Commodity Group Code** and **Lot Billing Type**. It is thus possible, for example, to post the sales for pallets with Lot Billing Type *Consignment* and Commodity Group Code *CI* to a different G/L Account than the sales for a pallet with the same Commodity Group Code but a *Purchase* Lot Billing Type.

When a Produce Trade or Produce Bill is posted, the system will find the matching rule in Produce Posting Setup, based on the General Business Posting Group of the Customer or Vendor, and the Commodity Group Code and Lot Billing Type of the pallet. It then posts the transaction to the relevant G/L Account/s as defined in the matching rule.

## Set up Produce Posting rules
Rules should be set up for all possible combinations of **General Business Posting Group**, **Commodity Group Code** and **Lot Billing Type** that could exist in produce transactions.

If, for example, you have specified different General Business Posting Groups for customers that will be invoiced for produce, a rule representing each of these General Business Posting Groups should exist. The same principle applies for the vendors (Lot Billing Parties) for whom Produce Bills will be posted. If different General Business Posting Groups exist for vendors, ensure that you set up a rule for all possible values.

## Account fields in Produce Posting Setup

### **Sales Account (Interim)**

Sales transactions from Produce Trades for Lot Billing Type *Consignment*, and also for *Purchase* pallets if **Defer Sales** in **Linc Setup** is switched on.

### **Sales Account**

On posting of the cost produce bill, amounts are reversed from Sales Account (Interim) and posted to this account. This is thus the 'final' sales account. Where **Defer Sales** in **Linc Setup** is not switched on, sales transactions from Produce Trades post directly to this account for pallets where the **Lot Billing Type** is *Purchase*.

### **Produce Bill Account (Interim)**

Advance Produce Bill amounts are posted to this account. If **Defer Sales** in **Linc Setup** is switched on, Cost Produce Bills for *Purchase* pallets will post the produce value to this account if the related Produce Trade is not yet closed and **Post Charges** in the Produce Bill header is not switched on. If **Defer Sales** in **Linc Setup** is switched off, the posting amount from cost produce bills for *Purchase* pallets will post to this account if produce trade entries do not yet exist.

### **Produce Bill Account**

Purchase transactions from the Cost Produce Bill, as well as Prioritised Costs, are posted to this account.

### **Real. Gain/Loss Clearing Acc.**

Forex gains and losses that may result from a revaluation of the Net Trade Amount (LCY) on Cost Produce Bills, as well as Forex gains and losses that result from the reversal of advances at a different exchange rate than the original advance posting.

### Global Dimensions in Produce Posting Setup
Dimension values can be specified for produce posting rules, but are not mandatory. If values exist in the field, these values will post on the related G/L entries that post to the G/L Account of the rule. Note that the global dimensions will not post to the G/L Accounts underlying the customer or vendor ledger entries.

### Consignment Adjustment Charge
When adjustments are made to the calculated posting price on cost produce bills for *Consignment* pallets, a pallet charge entry for the adjustment amount is generated using the pallet charge that is specified in the **Consignment Adjustment Charge** of the matching produce posting setup rule.