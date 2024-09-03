---
grand_parent: Produce Trades
has_children: false
layout: default
nav_order: 41905
parent: Guides
title: Redirect, Remove and Return Pallets
---

# Redirect, Remove and Return Pallets

Redirect Pallets
----------------

Pallets on a produce trade can be redirected to another customer. This caters for scenario's where pallets in the freight container were, for example, allocated to the wrong customer, or rejected at the original customer.

To redirect a pallet, the posted trade amount on the pallet line must be zero. Thus, if a pallet line was already invoiced, first post a full credit memo for the line.

For cases where you do not want to redirect the full quantity of the pallet line, the pallet can be split - on the condition that the posted trade amount for the line is zero. To split the quantity, enter the quantity that needs to be 'split' in the **Split Quantity** field. Then select the line and choose **Split Pallet** in the Produce Trade Lines menu. The quantity on the original pallet lot will be reduced and a new pallet lot for the split quantity will be created. The necessary pallet lot can then be redirected.

To redirect a pallet, select the **Redirected Delivery Point** on the relevant pallet lots. A **Redirect Reference** may be entered, and will be stored on the pallet line for reporting purposes. Specify the **Redirected Sales Currency Code** and **Redirected Sales Price**. The **Redirected Purchase Currency Code** and **Redirected Purchase Price** can also be entered if the circumstances of the redirect require an update of these values.

Select the lines to redirect, and then choose **Process Redirection** from the Produce Trade Lines menu.

You can choose to force the creation of a new produce trade. If so selected, a new produce trade will be created for the redirect customer, even if a produce trade for the same freight container and customer already exists. Else, the pallets will be added to an already existing produce trade for the customer and freight container. If no produce trade exists for the combination of customer and freight container, a new produce trade will be created irrespective of the selected 'force' option.

Remove pallets from produce trades
----------------------------------

It may sometimes be necessary to remove pallets from produce trades and their freight containers, for example if the pallet/s were never loaded into the container, or when the intended sales and purchase prices may need to be corrected.

A pallet can only be removed from the produce trade if the posted trade amount of all pallet lots for the relevant pallet ID is zero.

To process the removal, select the pallet from *Produce Trade Lines* and choose **Process Removal**. All pallet lines for the selected Pallet ID will be removed from the produce trade and related freight container. The Allocated Delivery Point and related allocated customer fields will also be cleared. The pallet will again become available for selection and allocation.

Return pallets to the Lot Billing Party
---------------------------------------

Pallets can be returned to the Lot Billing Party directly from the produce trade. Such pallets will be flagged as **Returned to Lot Billing Party** and will no longer be available for allocation to delivery points and customers.

Only pallets where the posted trade amount is zero are eligible for return. To process a return, select the pallet lot in *Produce Trade Lines* and choose **Return to Lot Billing Party** in the Produce Trade Lines menu.