---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21005
parent: Master Data
title: Lot Billing Defaults
---

# Lot Billing Defaults


### In this article

[Lot Billing Concepts](#lot-billing-concepts)  
[When and were are Lot Billing Defaults used](#when-and-were-are-lot-billing-defaults-used)  
[Understanding the Lot Billing Defaults page](#understanding-the-lot-billing-defaults-page)  
[Correct and Incorrect set up of multiple rules for the same Producer Code](#correct-and-incorrect-set-up-of-multiple-rules-for-the-same-producer-code)  
[Best Practice for setting up Lot Billing Defaults](#best-practice-for-setting-up-lot-billing-defaults)  

Related articles
<br/>
[How to set up Lot Billing Defaults](/articles/Configuration/Master%20Data/Guides/How%20to%20set%20up%20Lot%20Billing%20Defaults)

---
## Lot Billing Concepts
<br/>
ProduceLinc does not allow a pallet line to exist without information about who the vendor is that must be paid for the pallet and whether the produce was procured on a purchase or consignment basis.
The system stores this information in these two fields for every pallet line:  

**Lot Billing Party No.:** the vendor that must be paid  
**Lot Billing Type:** the procurement method (for example Purchase or Consignment)  

The lot billing type determines how the final amounts payable to the vendor are calculated by the system:  

For lot billing type _**Purchase**_ the system calculates the amount to pay based on the intended purchase price but allows modification to this price. From an accounting perspective it means that the produce income less pallet costs and produce costs is your business profit (the Gross Profit model).  

For lot billing type _**Consignment**_ the system calculates the amount to pay as the final produce income less the pallet costs. In this scenario your business charges a commission amount – which is included in the pallet costs. This commission is then your business’ income / revenue.

Here’s a snippet of pallet lines showing the Lot Billing Type and Lot Billing Party No.

![](/media/ConfigMasterData_LotBillingDefaults_Documentation_1.%20Pallet%20Line%20List%20example.jpeg)



---
## When and were are Lot Billing Defaults used
<br/>

Lot Billing Defaults (Lot Billing Type and Lot Billing Party No.) are applied every time a pallet is created or updated in the system.  

When pallets in a pallet creation file entry are validated, the system finds the appropriate Lot Billing Default rule for each of the lines in the pallet file and applies the Lot Billing Type and Lot Billing Party No. on the file lines.  

The Inbound Channel Code for each pallet line is also applied from the same lot billing default rule.  

When the lines in the pallet file are then confirmed, ProduceLinc stores this Lot Billing Type and Lot Billing Party No. on the pallet lines that it creates.  

Pallet files that don’t create new pallets but simply update existing pallet lines (eg. produce order confirmation or pallet verification pallet files) go through the same process of finding the correct lot billing type and lot billing party number for the pallets and then updating that information on the existing pallet lines if necessary.  

Pallet file lines that have **no** Lot Billing Type, Lot Billing Party No. and Inbound Channel Code cannot be confirmed. This means that the appropriate rules must be set up in Lot Billing Defaults beforehand so that the system can find the correct lot billing type and lot billing party number.  

**Note on Inbound Channel Code**  

Industry Pallet Files include a single channel code that typically indicates if the pallet was packed for export (E) or local market (L). In ProduceLinc this value is stored in pallet lines as the Outbound Channel Code.  

But ProduceLinc also has an Inbound Channel Code where the _source_ channel is stored. This allows businesses that import produce from overseas and sells it either locally or internationally to differentiate between pallets that were produced locally versus pallets that were imported. For pallets produced locally, the _Inbound Channel Code_ would normally be **L**; whereas pallets that were imported would have Inbound Channel Code as **I**.



---
## Understanding the Lot Billing Defaults page
<br/>
Lot Billing defaults consists of:  

- Filter fields  
- Fields with the default lot billing values that will be applied to pallets  

The conditions you provide in the filter fields are the criteria against which ProduceLinc matches pallets to find the correct default lot billing values to apply. 



### Minimum fields required for a lot billing default rule
<br/>
Every Lot Billing Default rule **must** have a:  

- Producer Code (minimum and mandatory filter)
- Default Lot Billing Type
- Default Lot Billing Party No.
- Default Inbound Channel Code


### Optional and additional filters
<br/>
The page includes some optional filters that can be used in addition to the Producer Code filter. These include:  

- Organisation Code
- Packhouse Code
- Commodity Group Code
- Commodity Code
- Variety Group Code
- Variety Code
- Outbound Channel Code
- Target Region Code

Use of the optional filters come in handy in cases where you get pallets from the same Producer Code (PUC) from various vendors. We'll illustrate with two examples.

**Example 1**
<br/>
You procure produce from Producer Code A directly from the producer itself. The producer sends produce to a packhouse that takes it in under your business’ organisation code (let’s say organisation X). You must pay Vendor A (the producer itself) for this produce.  

The producer also delivered produce to another marketing company – under their organisation code (let’s say organisation Y). You now purchase some of these pallets with the same Producer Code from the other marketing company, but have to pay this company for the pallets, and not the producer itself.  

To solve this challenge, you can set up two rules for Producer Code A:  

- One with Organisation Code X and Default Lot Billing Party as Vendor A
- The second with Organisation Code Y and Default Lot Billing Party as Vendor B

_Visual of Example 1_
![](/media/ConfigMasterData_LotBillingDefaults_Documentation_3.%20LotBillingRule_OptionalFilterExample_a.jpeg)

**Example 2**
<br/>
You procure grapes and stone fruit from Producer Code A. For the grape pallets you must pay the producer directly (Vendor A). But the stone fruit pallets must be paid to the packhouse where the pallets are packed (Vendor C) – and the packhouse will do the final payment to the producer after deducting their packing costs.  

To solve this challenge, you can set up two rules for Producer Code A:  

- One with Commodity Group Code as GR (grapes) and Default Lot Billing Party as Vendor A
- The second with Commodity Group Code as SF (stonefruit) and Default Lot Billing Party as Vendor C

_Visual of Example 2_
![](/media/ConfigMasterData_LotBillingDefaults_Documentation_4.%20LotBillingRule_OptionalFilterExample_b.jpeg)



### Visual of mandatory and optional values in Lot Billing Defaults
<br/>
Below is a visual from Lot Billing Defaults. The fields marked in red are mandatory (minimum filter for Producer Code, plus minimum Defaults to apply). The fields in blue show the optional filter fields.

![](/media/ConfigMasterData_LotBillingDefaults_Documentation_2.%20LotBillingDefaultsExample.jpeg)



### Responsibility Center and Global Dimensions 1 and 2
<br/>
The Lot Billing Defaults page also includes three additional values that ProduceLinc can apply and store on Pallet Lines when the lot billing defaults are applied. These three values are Responsibility Center and values for your business Global Dimension 1 and Global Dimension 2.  

Providing values for these three fields in Lot Billing Defaults is not mandatory. In fact, there are perhaps but a few use cases where it could be useful to have default values for these three fields, and we suggest that you leave these fields empty on your lot billing default rules.  


---
## Correct and Incorrect set up of multiple rules for the same Producer Code
<br/>
In cases where you set up more than one rule for the same Producer Code with the use of optional filters (like in our examples above), ensure that you fill in the filter fields for all the lines for that Producer Code to the same filter level.  

Let’s take example 1 from above again: If we are going to specify the organisation code as an optional filter, we must ensure that organisation code is filled in for both rules for Producer Code A. If we only fill in Organisation Code for the first rule and leave it empty for the second rule, the system will find both rules when it tries to apply the Lot Billing Type and Lot Billing Party for the pallet(s), and then won’t know which one it must use.  

Below is an example of two rules for the same Producer Code that are set up incorrectly. The first rule includes a filter for Organisation Code, but the second rule has an empty value in this filter field. As a result, ProduceLinc will find both rules when trying to apply the lot billing default values and not know which one to apply.

![](/media/ConfigMasterData_LotBillingDefaults_Documentation_5.%20LotBillingRule_IncorrectFilters.jpeg)



---
## Best Practice for setting up Lot Billing Defaults
<br/>
We suggest that you always include organisation code for all your Lot Billing Default rules. When this filter is used together with the Producer Code, it caters for most cases where pallets are taken in for the same PUC, but from different vendors.  

In our experience, it is very seldom necessary to use any of the other additional filters, like packhouse code, commodity group, commodity, variety group, variety, outbound channel and target region.  

Keep the setup as simple as possible to ensure both easy maintenance and accurate lot billing details on pallet lines.

