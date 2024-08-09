---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21002
parent: Master Data
title: Linc Setup
---

# Linc Setup

ProduceLinc allows your business to dynamically choose how some of the features in the system function - rather than having only one set of built-in rules. This is accomplished by several parameters that can be switched on or off in the *ProduceLinc* section of **Linc Setup**.

Number Series to be used in ProduceLinc
A number of fields are provided in the *ProduceLinc* section to specify the number series that should be used for:
- Freight Trip Nos.
- Freighter Trip Leg Nos.
- Freight Container Nos.
- Produce Order Nos.
- Produce Trade Nos.
- Pallet Lot Nos.
- Produce Bill Nos.
- Produce Bill Batch Nos.
- Produce Bill Payment Batch Nos.
- Pooling Keys Nos.

## Check Pallet Mandatory Fields
If switched on, the system will prevent the confirmation of lines on pallet file entries if values for any of the mandatory fields are not present as per the rules defined in **Pallet Line Mandatory Fields**. For more information, see [How to resolve errors and confirm pallet lines](/files/articles/Stock%20and%20Logistics/Pallet%20Files/Guides/How%20to%20resolve%20errors%20and%20confirm%20pallet%20lines).

## Trade Exch. Rate Date Basis
Define the default date basis on which the currency factor for the posting of produce trades must be based. Options include *Posting Date*, *Estimated Departure Week*, *Actual Departure Week*, *Estimated Arrival Week,**Actual Arrival Week*and *Container Load Date*.

If a *Week*-basis is selected, the currency factor on produce trades will be set based on the Monday of the week-basis, using the produce trade's related Freighter Trip Leg. This ensures that all invoices and credit memo's from a produce trade is posted with the same exchange rate.

If *Container Load Date* is selected, the currency factor on produce trades will be based on the container load date, and if no currency exchange rate is found for this date, the most recent exchange rate before the container load date will be used.

If the *Posting Date* option is selected, each sales invoice and credit memo from the produce trade will be posted using the relevant exchange rate of the posting date.

# Limit Trade Exch. Rate Usage
If a non-posting date trade exchange rate date basis is used, and this parameter is not switched on, the standard pallet charges on cost produce bills are converted to LCY amounts using the same exchange rate as the related produce trade. If *Limit Trade Exch. Rate Usage* is switched on, the posting date of the produce bill is used for calculating LCY amounts of standard pallet charges that are defined in a foreign currency.

# Produce Bill Channel Basis and Produce Bill Grouping Basis
Select the Channel Basis (*Inbound* or *Outbound*) and relevant *Week*-basis that must be used for the grouping of pallets into produce bills. For more information on the effect of these settings, see **[# How to Generate Produce Bills](https://linc.freshdesk.com/en/support/solutions/articles/8000097855)**.

## Defer Sales
This parameter governs how and when the income and pallet charge costs of pallets with lot billing type *Purchase* is posted.

If **Defer Sales** is switched on, the income and income charges from produce trades are posted to the **Sales Account (Interim)** as specified in **Produce Posting Setup**. The income will then be reversed from the interim sales account and posted to the final **Sales Account** on the first posting of the cost produce bill that includes the posting of charges. Pallet charges will then only calculate and post on the cost produce bill if the related produce trade is **closed** and **Post Charges** selected in the cost produce bill header.

If **Defer Sales** is switched off, the income and income charges from produce trades are immediately posted to the **Sales Account** specified in **Produce Posting Setup** and no reversal is done on the posting of cost produce bills.

## Always Calculate Bill Costs
Where *Defer Sales* is switched on, charges are by default not calculated for lines on cost produce bills for purchase fruit if the related produce trade is not yet closed. Switching on the *Always calculate bill costs* parameter allows for charge calculation on purchase cost produce bills irrespective of the status of the related produce trades.

## Advance Reversal Method
*Nett Invoice*: advances are reversed on the same purchase document on which the final produce amount is posted.
*Credit Memo*: consignment advances are reversed on a separate purchase credit memo.

For more information, see **Cost Produce Bills**.

## Limit Purchase Currencies
If switched on, the intended purchase currency on pallets is limited to the default currency code of the Lot Billing Party (as per the Vendor Card).

## Limit Sales Currencies
If switched on, the intended sales currency on pallets is limited to the default currency code of the Allocated Customer (as per the Customer Card).

## Synchronise Trade Currencies
If switched on, the systems checks - on allocation of pallets to **Allocated****Delivery Point** - that the intended purchase currency and intended sales currency is the same. If not, the Delivery Point will not be assigned. This option cannot be switched on together with **Limit Purchase Currencies**, as this will invariably result in the currencies of the Lot Billing Party and Allocated Customer not being the same.

# Default Document Titles
Default document titles can be defined for the *Proforma Invoice*, *Trade Invoice*, *Trade Credit Memo* and *Commercial Invoice*. These default values are set up as master data in Linc Lookup Values.

On create of the produce trade, default document titles for the Proforma Invoice, Trade Invoice and Trade Credit Memo are populated to the produce trade header. The system first looks at produce trade defaults to find the appropriate document titles in a customer specific rule. If no such rule is found for the customer, the document titles from Linc Setup is used. The document titles on the produce trade determine the title that prints on the documents.

## Common Income Incoterm Level
A common income-level for **purposes of reporting** can be selected in this field. The income of pallets is then dynamically re-calculated on the produce bill export sheet, without affecting the actual income of the pallet or posting any financial transactions.

## Pallet File Storage Account
ProduceLinc allows for the automatic import of pallet files. Such pallet files should be stored in an Azure storage account. Specify the account in **Pallet Files Storage Account**, the Azure blob container in **Pallet Files Container** and the SAS token for the container in **Pallet Files SAS Token**.

## Pallet Line Archive Date Filter Calc
Use a date formula in *Pal. Archive Date Filter Calc.* to determine the date filter that will be used for the calculation of the LCY income and cost fields on pallet line archive. The *Pal. Archive Date Filter* field shows the effective date filter that will be used, based on the date formula.

This date filter allows for ‘as at date’ reporting of LCY income and costs from the pallet line archive.

## Allow Manual Confirmation Dates
If this is switched on, the confirmation date on pallet file entry lines will not automatically derive from the current work date, and must be specified before confirmation of the lines. Functions then exist on the pallet file entry to either derive the confirmation date from the intake date of the lines, or assign a ‘manual confirmation’ date in bulk to selected pallet file lines.

## Suppress VGM on SOLAS 2
If switched on, Solas Method 2 can be selected for freight containers even if some of the pallets in the container do not have a verified gross weight.

## Default SOLAS Method
Select the default Solas Method (Method 1 or Method 2) that should be used when new freight containers are created. The Solas method on individual freight containers can be modified after creation.

## Suppress Allocation Batching
 If switched on, access to *pallet selection summary* is prevented. Allocations can then be imported from Excel using the *import allocation batch* function on pallet allocation summary, but without requiring users to first add the pallet lines to an allocation batch. The import temporarily adds all pallet lines with allocation values in the Excel file to the import user’s batch, and thus make them visible on pallet allocation summary after the import.