---
grand_parent: Pallet Verification
has_children: false
layout: default
nav_order: 33901
parent: Guides
title: How to Interpret Pallet Verification Results
---

# How to Interpret Pallet Verification Results

The Pallet Verifications page shows you the comparison between each cold store/depot's stock file and the available pallet stock you have in the system for each cold store/depot.
So, this is your stock reconciliation.

For this recon, the system categorises pallets into 4 different categories (Verification Results), and shows the number of pallets for each.
- System and Freight Point File
- Only in System
- Only in Freight Point File
- Incomplete Transfers

Okay great, so we have some pallets sitting under each of these verification results on the page, but what does it mean? Here's your quick guide:

### System and Freight Point File
This one is quite obvious. It shows the number of pallets that matches between the cold store/depot's stock file and your available pallets in the system. 
These are the ones that you don't need to investigate further.

### Only in System
According to ProduceLinc, these pallets are still available stock, but they are no longer at the depot, and thus not in their PS file.

Possible reasons for this:

**Scenario 1:** The cold store has already loaded the pallets for your customer, so it's no longer in their PS file. In ProduceLince these pallets are allocated to the customer, but the PO file has not been received and/or processed and the outbound freighter trip leg and freight container not yet populated. 

If this is the case, you want to chase down those PO files (if you expect to receive one) and get it processed. If you don't receive PO files from that specific cold store, you can always manually load the pallets with the "Populate Trip Leg" function on the order (once you've confirmed that the actual loading and your allocated pallets are the same).

**Scenario 2:** The pallets were created in the system (pallet creation). The depot no longer has this pallet in stock for  you, perhaps because they did the intake for the wrong organisation code, or the pallet was damaged/destroyed, or relabeled. 

For these pallets you'll have to get in touch with the depot and check what the situation really is. If you then do need to remove these pallets, you can unconfirm them from the pallet file entry with which they were created.

### Only in Freight Point File

The cold store/depot has these pallets in stock, but according to ProduceLinc, they're not available stock.

**Scenario 1:** You are likely missing some intake files. The cold store/depot has taken in some new pallets, and you haven't yet received/processed the intake file.

**Scenario 2:** A user allocated the pallets and manually populated the freight trip leg and container. According to ProduceLinc these pallets are thus no longer in stock. But the cold store/depot has not yet physically loaded these pallets, so they are still included in their stock file.

If the freighter trip leg and freight container was manually populated by mistake, you can remove the pallets from the freight container.

### Incomplete Transfers

These pallets were allocated for transfer to another location, but the cold store/depot has not yet physically loaded them. They're still in the cold store/depot's stock file.


## Example

A stock file from cold store X was received. The file itself has 8 pallets in it. In ProduceLinc there are also 8 pallets, but the pallet IDs do not quite match between the stock file and the system.
The Pallet Verifications page show the following results:

![](/media/Verification%20Results.jpeg)

And this is what the pallets for cold store X look like in ProduceLinc _versus_ the pallets in the stock file.

![](/media/Verification%20Results%20illustrated.jpeg)