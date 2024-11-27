---
grand_parent: Operational Finance
has_children: false
layout: default
nav_order: 41001
parent: Produce Trades
title: Produce Trades
---

# Produce Trades

A produce trade represents the sale of pallets in a container to a customer. When produce trades are created, built-in logic groups pallets into trades per *Freight Container Code*, *Allocated Delivery Point*, *Intended Sales Currency Code*, *Shipment Method Code* and *Salesperson Code*.

From this single document users can print the commercial invoice, post advance and final sales invoices and credit memo's, post produce trade pallet charges that the customer will deduct from payments and redirect pallets to another customer and produce trade.

The produce trade header (*General* section in the top of the produce trade) shows information about the customer, the sales currency and shipment method (incoterm), and detail about the freighter trip leg and freight container on which the pallets were shipped. All the fields in the header are also visible on the produce trade list page - thus making it possible to use these values as filters for finding produce trades.

The *Posting* section of the trade contains a number of fields that are filled in when invoices or credit memo's are posted. These fields are cleared after each posting - allow for a subsequent posting.

Produce trade pallet charges are defined in the *Pallet Charge Assignment* section of the trade.

The *Produce Trade Lines* section of the produce trade shows the detail of pallets that were shipped to the customer. Information about the fruit specification, producer, quantity and intended purchase and sales prices per pallet lot are included in this section of the produce trade. Actual posting prices per pallet lot are also defined here.

A factbox on the right shows a useful summary of the Trade Quantities, Posting Amounts, Posted Amounts, Totals, and posted documents.

The commercial invoice can be printed directly from the produce trade by choosing the *Commercial Invoice* button under *Reports* in the menu of the produce trade header.

The title dynamically prints as either *Commercial Invoice* or *Proforma Invoice*, depending on the selected option in the *Commercial Invoice Title* field of the produce trade header. The default *Commercial Invoice Title* is based on the global setup in **Linc Setup**, but can be manually edited per produce trade.

Intended sales prices are used for the printing of the commercial invoice.

Produce trades are created with the *Create/Update Produce Trades* function on Freight Containers. This will add pallets to an existing produce trade for the customer and freight container, or create a new produce trade if none exists.

Produce Trades can only be created if the freight container is *Confirmed*.

Produce Trades are listed in the **Produce Trades** page. This page can be filtered and sorted based on any of the values from the produce trade headers, and allows for easy management of the growing list of produce trades. From here individual produce trades can be opened for viewing or editing (posting).