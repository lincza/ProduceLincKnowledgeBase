---
grand_parent: Produce Trades
has_children: false
layout: default
nav_order: 44904
parent: Guides
title: Redirect Pallets to another Customer
---

Redirect Pallets to another Customer

You may wish to redirect pallets to another customer.




Typical scenario’s:

* The original customer has rejected the pallets, and you want to now sell them to another customer
* The pallet(s) ended up at the wrong customer. It was intended for customer A and is on a produce trade for customer A, but it was somehow delivered to customer B. You need move the pallet from customer A’s produce trade to a produce trade for customer B.

  


To Redirect pallets:

* Ensure that the pallet line(s) has been fully credited. Thus, the posted amount on the line must be zero.
* Choose the new customer by entering a value in ‘redirected delivery point’
* Enter values for the new intended sales and purchase currencies and prices in the relevant ‘redirect’ fields.
* Select the relevant pallet lines and then choose the ‘redirect’ action in the menu
* This will remove these pallet lines from the existing produce trade and either create a new produce trade for them, or add them to an existing produce trade for customer B – if such a produce trade for the same freight container already exists for customer B. (When you choose the redirect action, you can select to ‘force’ the pallets to go to a completely new produce trade for customer B – even if a produce trade for this customer already exists for the same freight container)
* You can now proceed with invoicing the pallets to the new customer from the relevant produce trade.

  


Note: For cases where you do not want to redirect the full quantity of the pallet line, the pallet can be split. To split the quantity, enter the quantity that needs to be ‘split’ in the Split Quantity field. Then select the line and choose Split Pallet in the Produce Trade Lines menu. The quantity on the original pallet lot will be reduced and a new pallet lot for the split quantity will be created. The necessary pallet lot can then be redirected.