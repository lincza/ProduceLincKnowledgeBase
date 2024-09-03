---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21007
parent: Master Data
title: Produce Trade Defaults
---

# Produce Trade Defaults

Produce Trade Defaults allows for defining customer-specific default rules and values that the system will apply in processes that involve sales allocation, Produce Trades, and printing of sales-related reports from the Produce Trade.

The fields for *Customer No.* and *Commodity Group Code* are the filter fields that the system uses when trying to find a relevant matching rule. The remaining fields for *Salesperson Code*, *Trade Type Code*, *Proforma Invoice Title*, *Trade Invoice Title* and *Trade Credit Memo Title* are the **default values** that are applied by the system during various processes.

*Customer No.* is a mandatory field in this table, while *Commodity Group Code* is an **optional** filter field. It is thus possible to define more than one default rule per customer; where one such rule could be the more generic rule with only the *Customer No.* filter field filled in, and additional rule(s) for the same Customer No. can be Commodity Group Code specific. If the system finds more than one matching rule, the default values of the most specific rule will be used.

When are the default values applied?

**Salesperson Code:**this value is applied to the *Salesperson*Code field on pallet lines during sales allocation when the Allocated Delivery Point - and thus Customer - is assigned to pallet lines.

Note that when the system applies the salesperson code to pallet lines, it will look for and apply the default value first from the related Customer Card, then from User Setup (the salesperson code mapped to the user who is performing the allocation), and last from Produce Trade Defaults. The last salesperson code value found, is the value that remains on the pallet line. Thus, if Produce Trade Default rules are defined, all such rules must have a value in *Salesperson Code.*

**Trade Type Code:**When the Produce Trade is created, the system attempts to find a default Trade Type Code in Produce Trade Defaults, and automatically populates the *Trade Type* field on the Produce Trade header with this value. If no default value is found, the *Trade Type* on the Produce Trade header will be empty but can then be manually selected by a user.

**Proforma Invoice Title, Trade Invoice Title and Trade Credit Memo Title:** When the Produce Trade is created, the system attempts to find the default values for these fields in Produce Trade Defaults, and automatically populates the values to the corresponding fields on the Produce Trade. If no matching rule is found in Produce Trade Defaults, the system will use the global default values for these fields from *Linc Setup* and use those values for the fields on the Produce Trade header. Should no global default values exist in *Linc Setup* either, the fields are left empty on the Produce Trade header and can then be manually filled in on the Produce Trade header itself. The print titles on the Produce Trade header will determine the titles of the printed documents for Proforma Invoice, Produce Trade Invoice and Produce Trade Credit Memo reports that are printed from the Produce Trade.

EXAMPLES

Consider the example produce trade defaults below.

| **Customer No.** | **Commodity Group Code** | **Salesperson Code** | **Trade Type Code** | **Proforma Invoice Title** | **Trade Invoice Title** | **Trade Credit Memo Title** |
| --- | --- | --- | --- | --- | --- | --- |
| C0001 |  | JOHN | FIXED | Proforma Invoice | Tax Invoice | Tax Credit Memo |
| C0001 | SF | SARAH | ACC SALE | Proforma Invoice | Sales Invoice | Sales Credit memo |
| C0002 |  | MARY | FIXED | Commercial Invoice | Invoice | Credit Memo |

If pallets are allocated to customer C0001 and the commodity group code of the pallets is anything other than SF, then the salesperson code will be *JOHN*, and the resulting Produce Trade header will show *FIXED*for the Trade Type. The print titles will be *Proforma Invoice*, *Tax Invoice* and *Tax Credit Memo*.

If pallets with commodity group code SF are allocated to the same customer C0001, salesperson code *SARAH*will be assigned to the pallets, the Trade Type in the resulting Produce Trade header will be *ACC SALE*, and the print titles will be *Proforma Invoice*, *Sales Invoice* and *Sales Credit Memo*.

If pallets are allocated to customer C0002 - irrespective of the commodity group code - MARY will be the assigned salesperson code and the print titles will be *Commercial Invoice*, *Invoice*and *Credit Memo*.