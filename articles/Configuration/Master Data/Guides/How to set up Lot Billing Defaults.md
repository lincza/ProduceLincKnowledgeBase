---
grand_parent: Master Data
has_children: false
layout: default
nav_order: 21908
parent: Guides
title: How to set up Lot Billing Defaults
---

# How to set up Lot Billing Defaults

### In this guide

[Quick overview of Lot Billing Defaults](#quick-overview-of-lot-billing-defaults)  
[How to create a new Lot Billing Default rule](#how-to-create-a-new-lot-billing-default-rule)


Related articles
<br/>
[Lot Billing Defaults](/articles/Configuration/Master%20Data/Lot%20Billing%20Defaults)


---
## Quick overview of Lot Billing Defaults
<br/>
Lot Billing Defaults are a set of rules that ProduceLinc uses to determine what the Lot Billing Type for each pallet line is (Purchase or Consignment), and which Lot Billing Party (vendor) must be paid for it.  

Rules must be set up with Producer Code as the minimum required filter, and Default Lot Billing Type, Default Lot Billing Party No. and Default Inbound Channel Code as the minimum three values that must be applied to 'matching' pallet lines.  

Additional filter values can be provided in the optional fields to further refine your rule. One such optional filter is the Organisation Code, but even though it is not required, we do suggest that you always include this when setting up Lot Billing Default rules.  

Please refer to our related article on [Lot Billing Defaults](/articles/Configuration/Master%20Data/Lot%20Billing%20Defaults) for more detailed information on when and how these rules are used, how the filters work and best practices for setting up the rules.


---
## How to create a new Lot Billing Default rule
<br/>

**Step 1**  
Navigate to the Lot Billing Defaults page.  
![](/media/Configuration_LotBilingDefaults_Guide_1.NavigateToLotBillingDefaults.png)  


**Step 2**  
Create a new line.  
![](/media/Configuration_LotBilingDefaults_Guide_2.CreateNewLotBillingDefaultLine.png)

**Step 3**  
Fill in/choose values in the following fields in the new line you have just created.  

- Organisation Code
- Producer Code
- Default Lot Billing Type
- Default Lot Billing Party No.
- Default Inbound Channel Code

![](/media/Configuration_LotBilingDefaults_Guide_3.ProvideFiltersAndDefaults.png)

**Step 4**  
Repeat steps 1 to 3 for every new lot billing default rule you want to create.

**Step 5**  
Once you are done, make sure that you see _Saved_ in the top right corner of the page before you close it.  
![](/media/Configuration_LotBillingDefaults_Guide_4.CheckSaved.jpeg)
