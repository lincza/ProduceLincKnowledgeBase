---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21006
parent: Master Data
title: Lot Billing Defaults
---

# Lot Billing Defaults

## Lot Billing Type and Lot Billing Party
The **Lot Billing Type** and **Lot Billing Party No.** are key concepts in ProduceLinc. The **Lot Billing Party** is the vendor for whom you will post a self-billing purchase invoice to pay for the pallet lot. The **Lot Billing Type** refers to the 'procurement method' of the produce pallets and determines how the final purchase value of the produce is calculated.

**Lot Billing Type** *Purchase* is used for produce that is purchased - normally at a fixed price. The produce becomes the stock or inventory of your company, supply chain costs incurred in the marketing of the produce is your company's expense, and the difference between the income of the produce and its supply chain and produce cost is your profit margin.

**Lot Billing Type** *Consignment* is used when you market the produce on behalf of the **Lot Billing Party**, without taking ownership. In this procurement model the income and supply chain costs are for the account of the **Lot Billing Party**, and payment value of the produce is calculated as income less costs. Such costs usually include a marketing fee or commission for your business.

ProduceLinc allows your business to use both procurement models while adhering to the differences in the financial accounting processes required. To accomplish this, the **Lot Billing Type** is set and stored on the pallet lot when the produce pallet is confirmed as stock in the system.

## The purpose of Lot Billing Defaults
It is usually not the responsibility of staff members who import and confirm pallets in the system to determine what the **Lot Billing Type** or who the **Lot Billing Party** should be. These decisions usually reside with a different group of employees. Thus, to minimise errors and allow for segregation of duties, the **Lot Billing Type** and **Lot Billing Party** can apply automatically on the lines of the imported pallet file. These values are applied based on the data set up in **Lot Billing Defaults**.

Built-in logic ensures that the **Lot Billing Type** and **Lot Billing Party No.** on imported pallet lines cannot be manually selected or edited if the Lot Billing Default table contains as much as a single rule.