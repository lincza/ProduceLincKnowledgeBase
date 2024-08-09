---
grand_parent: Freight Allocations
has_children: false
layout: default
nav_order: 43902
parent: Guides
title: How to change the trip leg of a freight container
---

# How to change the trip leg of a freight container




You may at times need to move a freight container to another trip leg. A typical example of such a scenario is when the container has already been loaded but is short-shipped for some reason. Thus, while the pallets are already in the container, the container missed the vessel and will now ship on a different vessel - i.e. freighter trip leg.




The good news is that you can move the freight container to another trip leg (vessel-voyage) without having to remove the pallets from the freight container and re-allocate/re-populate from stock into a different freight container for the correct trip leg.




**Here are the steps to follow**:




* Go to the freight container that you'd like to move. Then choose **Actions**; then **Change Trip Leg**

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101709168/original/h8Dbl3VtZnGOqqgePsUPCe5LUn0vEM45Vg.png?1659555203)







* In the lookup page for available freighter trip legs, search/navigate to the new trip leg to which the freight container must be moved. Select the appropriate new trip leg; then click on OK at the bottom of the page




![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101709218/original/NNQF5AA0buGM_bAOPKyIhynio8sLnxOwcg.png?1659555265)




* The following confirmation message will show - specifying the details of both the current and new freighter trip leg. Review the information. Once you have verified that the new freighter trip leg is the correct one, choose **Yes**.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101709415/original/aUyuQ4KKcwVGqoBnf45hC4omjQzrcuIVcA.png?1659555548)







The system will perform some tests to ensure that the freight container may indeed be moved to another trip leg - depending on the status of financial entries for the pallets in the freight container. For more information regarding this, see additional information at the end of this article.




If the trip leg change is indeed allowed, the entire freight container - including all the values that you so carefully filled in for the container, as well as the pallets in the container - will move to the new trip leg.

The image below shows the freight container as associated with the new freighter trip leg.




![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101709724/original/b37_5IF-qaTkcuyTjkmXU-A7q7SOfxTeBw.png?1659555906)







**Additional information: what do these messages and/or errors mean?**




If a produce trade was already created for the freight container, you may still move it to another trip leg - provided that the trade has either not been invoiced yet, or it has been invoiced but fully credited. If the pallets in the container are found on such a produce trade, the following information message will be shown. This is not an error, and if you choose **Yes** the system will proceed with moving the container to the new trip leg

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101710129/original/jtHkMVCbsSojVr6bZMe4LGvSBA8eUJsNdg.png?1659556471)




If the related produce trade(s) have been invoiced and not fully credited, the following error message will be shown, and the freight container can then not be moved to a different trip leg. To proceed with changing the trip leg, the produce trade(s) must first be fully credited.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101710194/original/aCuUJEw_RjD4O9L5U3WeODbyzjlfyRx43w.png?1659556551)




If the pallets in the freight container already exist on an advance or cost produce bill, the system also checks the grouping basis of these produce bill(s). If the grouping basis is estimated departure week, actual departure week, estimated arrival week or actual arrival week, the bill grouping code is checked against the target trip leg's corresponding field to make sure that the change of trip leg will not violate the bill grouping code.




Examples:
The pallets in the container are found on a produce bill that is grouped by estimated departure week and for which the estimated departure week (bill grouping code) is 202230. If the user wants to move the container to a trip leg with a different estimated departure week, the trip leg change will not be allowed. If the target trip leg has the same departure week, the container can be moved.




This is an example of the error that will be shown if the change of trip leg will result in a violation of the produce bill(s) grouping code.

![](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/8101710492/original/B9SO8OAZtIRI1kuu_CivH4ZF2V7TYXfzfA.png?1659557006)







If the pallets in the container are found in an advance or cost bill that is not grouped by a trip leg week, eg. intake week, then the trip leg change will be allowed.

If the pallets in the container are in a forecast bill only, the trip leg change will be allowed irrespective of the grouping basis of the forecast bill.