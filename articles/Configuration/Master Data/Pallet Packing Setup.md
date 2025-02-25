---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21004
parent: Master Data
title: Pallet Packing Setup
---

# Pallet Packing Setup


### In this article

[Pallet Packing Setup purpose](#pallet-packing-setup-purpose)  
[Pallet Quantity Rules](#pallet-quantity-rules)  
[Setting up pallet quantity rules](#setting-up-pallet-quantity-rules)  
[How are pallet quantity rules used?](#how-are-pallet-quantity-rules-used)    
[Outer Pack weight rules](#outer-pack-weight-rules)  
[Setting up Outer Pack weight rules](#setting-up-outer-pack-weight-rules)  
[How is the Net Weight per Outer Pack used?](#how-is-the-net-weight-per-outer-pack-used)  
[Why do we calculate Standard Outer Pack Quantities?](#why-do-we-calculate-standard-outer-pack-quantities)  


---
## Pallet Packing Setup purpose
<br/>
This document provides an overview of Pallet Packing Setup master data, including guidelines for setting this up and information on when and how this master data is used.
Pallet Packing Setup is used to store and maintain two ‘facts’ or rules for your various outer pack codes:

- the default pallet quantity for different outer pack codes and pallet configurations
- the net weight, gross weight and standard outer pack conversions rates for outer packs

---
## Pallet Quantity rules
<br/>
Pallet Quantity rules define the default quantity of a pallet given its commodity code, outer pack code, pallet base and pallet height code. In the produce export industry, this is also known as the stacking variance.

---
### Setting up pallet quantity rules
<br/>
Rules for the default pallet quantity are set up by first specifying the commodity group code, commodity code and outer pack code. The commodity group and commodity itself are needed, since the same outer pack code can be used for various commodities but have a different number of cartons for each commodity.  

The next three fields that complete a Pallet Quantity rule are Pallet Base Code, Pallet Height Code and Quantity per Pallet. This is where you define how many cartons there should be on a full pallet for the outer pack when packed for a specific commodity, on a certain pallet base and with a certain pallet height.  

If the same outer pack can be stacked on the same pallet base, but with a different pallet height, then a separate rule must be defined for it.  

Consider the example below: here the rules state that M18T cartons for apples are packed to a total of 56 for a high cube pallet, but only 49 for a standard height pallet.

![](/media/Configuration_MasterData_PalletPackingSetup%20-%201.%20StackingVariance_example.jpeg)

Note that the fields for Net Weight per Outer Pack, Gross Weight per Outer Pack and Standard Outer Pack Conversion are all set as ZERO for these Pallet Quantity/stacking variance rules.  

---
### How are pallet quantity rules used?
<br/>
When pallet files are received, the system validates the total number of cartons against your pallet quantity rule to prevent incomplete pallets from being confirmed as stock.
Let’s illustrate with an example using one of the rules in the image above:  

We have defined a pallet quantity rule that says apples in M18T cartons should be packed to a total of 56 cartons if packed to high-cube on a standard pallet base.
A pallet file is received with Pallet X for M18T apples, but it only has 50 cartons on it.  

In this scenario ProduceLinc will write an error message that states that the quantity of the pallet does not match the default pallet packing setup. This error message can be “ignored” – in which case ProduceLinc will remove the error and allow the pallet to be confirmed.

_Pallet File with Pallet ID showing total of 50 cartons for the pallet_
![](/media/Configuration_MasterData_PalletPackingSetup%20-%202.%20StackingVariance_ImportBufferExample.jpeg)

_Error message_
![](/media/Configuration_MasterData_PalletPackingSetup%20-%203.%20StackingVariance_ImportBufferIgnorableError.jpeg)

If your business principle is to allow incomplete pallets into stock and you don’t want these errors to show, you can enable the **Suppress Pallet Qty Checking** in Linc Setup.

![](/media/Configuration_MasterData_PalletPackingSetup%20-%204.%20LincSetup_SuppressPalletQuantitySetup.jpeg)

---
## Outer Pack weight rules
<br/>
Outer Pack weight rules define the theoretical net weight, gross weight and conversion factor for each combination of commodity code and outer pack code.

---
### Setting up Outer Pack weight rules
<br/>
Rules to define the theoretical/system weights for an outer pack code are set up by first specifying the commodity group code, commodity code and outer pack code. The commodity group and commodity itself are needed, since the same outer pack code can be used for various commodities but have different pack weights depending on the commodity.  

The image below is an example of the weight rule for M18T cartons for apples. 
![](/media/Configuration_MasterData_PalletPackingSetup%20-%205.%20OuterPackWeightRule_example.jpeg)

- **Net Weight per Outer Pack:** specifies the system net weight of the produce in the carton, excluding the packaging material.  
- **Gross Weight per Outer Pack:** specifies the system gross weight of the carton – i.e. the produce plus the theoretical weight of the packaging.  
- **Standard Outer Pack Conversion:** this is used to calculate the Standard Outer Pack Quantity for pallets.  

Note that **no values** are filled in for Pallet Base Code, Pallet Height Code and Quantity per Pallet for the ‘weight’ rule.

---
### How is the Net Weight per Outer Pack used?
<br/>
The system uses the Net Weight per Outer Pack to calculate and store the Net Weight of every pallet line. The net weight of pallet lines can then be used to apportion costs.

#### Example:  

A cost of 1000.00 is posted for a Pallet X. Pallet X has two lines (pallet lots) for two different producer codes.
- LOT001: 800 kg
- LOT002: 480 kg
If the allocation method of the cost is "Net Weight", then the cost is apportioned to the two pallet lots as follows:

Total weight of LOT001 and LOT002: 1 280 kg

- LOT001 percentage of total weight: 62.5%
- LOT002 percentage of total weight: 37.5%

Based on each pallet lot's percentage of total weight, the cost of 1000 is apportioned as follows:

- LOT001: 625.00
- LOT002: 375.00

---
### Why do we calculate Standard Outer Pack Quantities?
<br/>
Produce of a commodity can be packed in various kinds of cartons, of which the net weight can vary greatly. When reporting on number of cartons/quantity for eg. a season, the use of the actual quantities can skew the reporting results.  

#### Example:  

You want to compare number of cartons sold between customer A and B. 
You sold 10 000 cartons of M12T apples to customer A, and 10 000 cartons of M18T to customer B.An M12T apple carton weighs approximately 12.5 kg, while an M18T apple carton weighs 18.25.  

By simply comparing the number of actual cartons, your reporting results inaccurately show that you have exported equal volumes to both customers.
But if you choose a ‘standard equivalent’ for each commodity you can… well… compare apples to apples.

In our example the ‘standard equivalent pack’ for apples weighs 12.5 kg. We thus want to convert the quantities for all apple outer packs to a 12.5 kg euiqvalent. 
So we give the weight rule for M18T apples a standard outer pack conversion of 1.46 (The M18T carton weight of 18.25 divided by standard weight of 12.5).
This means that every M18T apple carton is the equivalent of 1.46 "standard cartons" of 12.5kg.
For the M12T apple carton we make the conversion factor 1, since it weighs the standard apple carton weight of 12.5 kg.

Using this standard outer pack conversion factor the 10 000 cartons of M18T apples to customer B then becomes 14 600 ‘standard cartons’.
The 10 000 M12T cartons sold to customer B remains 10 000 standard cartons.
By comparing customer A’s 14 600 standard equivalent cartons to customer B’s 10 000 we get a more accurate result.