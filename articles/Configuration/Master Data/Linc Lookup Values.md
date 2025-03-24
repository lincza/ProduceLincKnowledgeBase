---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21001
parent: Master Data
title: Linc Lookup Values
---

# Linc Lookup Values


### In this article

[Overview of Linc Lookup Values](#overview-of-linc-lookup-values)  
[Master data that must be set up in Linc Lookup Values](#master-data-that-must-be-set-up-in-linc-lookup-values)  
[Lookup Field Names explained : where and how are they used](#lookup-field-names-explained--where-and-how-are-they-used)  

Related Guide
<br/>
[How to create new data in Linc Lookup Values](/articles/Configuration/Master%20Data/Guides/How%20to%20create%20new%20data%20in%20Linc%20Lookup%20Values)  

---
## Overview of Linc Lookup Values
<br/>
Most of the produce and logistics related master data are maintained in Linc Lookup Values. Various tables, pages and features in ProduceLinc point to this master data to look up and validate values.

The Lookup Field Name defines the 'type' of master data field. This allows for a comprehensive list of master data, such as producer codes, packhouse code, shipping temperature codes, variety codes, etc. to be maintained in a single table - rather than having to set these up in separate master data tables.

Multiple codes for the same Lookup Field Name are set up by simply inserting more lines with the same Lookup Field Name and defining a unique Code and Description (optional) for each line.

Some master data types have inherent parent-child relationships. A good example of this is the relationship between Commodity Code and Commodity Group Code. Oranges (Commodity Code) fall within a 'parent' group (Commodity Group Code) called Citrus. Oranges is certainly not stone fruit or pome fruit.

To support these inherent parent-child relationships codes for some Lookup Field Names must be 'linked' to its parent by specifying the Parent Lookup Field Name (this should exist independently as a Lookup Field Name in the same table) and Parent Code.

Additional attributes and relationships between different types of master data can be set up with the use of Extended Lookup Values. For Example: Lookup Field Name: Producer Code = A0010 linked to Extended Lookup Field Name: Production Area = NC (Northern Cape).

---
## Master data that must be set up in Linc Lookup Values
<br/>
- Pallet Base Code
- Pallet Height Code
- Channel Code
- Commodity Group Code
- Commodity Code (Parent Lookup Field Name _Commodity Group Code_)
- Variety Group Code (Parent Lookup Field Name _Commodity Code_)
- Variety Code (Parent Lookup Field Name _Variety Group Code_)
- Color Code (Parent Lookup Field Name _Commodity Code_)
- Outer Pack Code
- Inventory Code
- Inner Pack Code
- Class Code
- Addendum Class Code
- Size Code
- Brand Code
- Market Code
- Region Code
- Country Code (Parent Lookup Field Name _Region Code_)
- Inspection Point
- Inspection Status
- Rejection Reason
- Harmonised System Code
- Freight Point
- Organisation Code
- Packhouse Code
- Producer Code
- Producer Site Code (Parent Lookup Field Name _Producer Code_)
- Global Gap Number (Parent Lookup Field Name _Producer Code_)
- Production Area
- Warehouse Zone Code
- Variety Licensor Code
- Transport Method
- Freighter Code (Parent Lookup Field Name _Transport Method_)
- Freight Agent Code
- Freight Forwarder Code
- Exporter
- Shipper
- Haulier
- Container Type Code
- Temptale Type Code
- Shipping Temperature Code
- Customs Deduction
- Defect Code
- Quality Grade Code
- Customer Quality Code
- Produce Trade Claim Type
- Quality Document Type
- Trade Type
- Return to Vendor Reason Code
- Claim Code
- Proforma Invoice Title
- Trade Invoice Title
- Trade Cr. Memo Title

---
## Lookup Field Names explained : where and how are they used
<br/>
Setting up master data in Linc Lookup Values takes a bit of getting used to some of the terminology. Below are some explanations of what the Lookup Field Name is used for. Understanding what the Lookup Field Name means and where the system will use it, can assist in setting up more complete and accurate data. 

---
### Pallet Base Code & Pallet Height Code
<br/>
Pallet Base refers to the physical wooden/plastic/CHEP pallet base that the cartons or bins are stacked on. Pallet Base is usually present in pallet files.
Pallet Height indicates if the pallet is packed as standard height (making it possible to load on convention/break-bulk vessels), high cube (typically loaded in containers and trucks) or another stacking variance that indicates that the pallet is suitable for air freight.

---
### Channel Code
<br/>
The channel code that is specified in the pallet file indicates if the pallet is packed and suitable for export (channel E) or for the local market (channel L). In ProduceLinc a pallet carries two channel codes: Outbound Channel and Inbound Channel.
The Outbound Channel indicates if the pallet is packed for export market or local market (thus, the value from the pallet file)
The Inbound Channel indicates the 'source' of the pallet - thus whether it was produced locally in this country (Inbound Channel L) or imported from overseas (Inbound Channel I).

---
### Commodity Group Code, Commodity Code, Variety Group Code and Variety Code
<br/>
These four Lookup Field Names exist in a specific hierarchy. 

Commodity Group Code sits at the top of the hierarchy. Examples are Pome Fruit, Stone Fruit, Exotics, Subtropical, Citrus, etc.

Each Commodity Group Code has one or more Commodity Code linked to it. Examples are Necatarines, Peaches, Apricots and Plums that are linked to the Commodity Group for Stone Fruit; or Apples and Pears that are linked to the Commodity Group for Pome Fruit.

For each Commodity Code there can be one or more variety group. Examples are Green Pears, Red Pears and Bi-Color Pears that are linked to the commodity for Pears.

For each Variety Group Code there then exist variety codes, such as Abate Fetel and Williams Bon Chretion that are linked to the Variety Group for Green Pears.


|Lookup Field Name     |Parent Lookup Field Name |Parent Code |Code |Description |
|:---                  |:---                     |:---        |:--- |:---        |
| Commodity Group Code |                         |            |PF   |Pome Fruit  |
| Commodity Code       |Commodity Group Code     |PF          |PR   |Pears       |
| Variety Group Code   |Commodity Code           |PR          |GP   |Green Pears |
| Variety Code         |Variety Group Code       |GP          |ABF  |Abate Fetel |

---
### Color Code
<br/>
Color codes are used to identify the flesh color of varieties for certain commodities. They thus have a child-parent relationship with Commodity Group Code.

These color codes are stored as part of the pallet information and used for export documentation such as the export addendum. Color codes are not mandatory for all commodity codes, but should be set up for commodities where the flesh colour is required on the export addendum, for example nectarines and peaches.

_Examples of Linc Lookup Values for Color Code_

|Lookup Field Name |Parent Lookup Field Name |Parent Code |Code |Description             |
|:---              |:---                     |:---        |:--- |:---                    |
| Color Code       |Commodity Code           |NE          |YN   |Yellow Flesh Nectarines |
| Color Code       |Commodity Code           |NE          |WN   |White Flesh Nectarines  |
| Color Code       |Commodity Code           |PE          |YP   |Yellow Flesh Peaches    |
| Color Code       |Commodity Code           |PE          |WP   |White Flesh Peaches     |
| Color Code       |Commodity Code           |PL          |RE   |Red Plums               |
| Color Code       |Commodity Code           |PL          |YE   |Yellow Plums            |
| Color Code       |Commodity Code           |PL          |BK   |Black Plums             |

---
### Outer Pack Code
<br/>
The Outer Pack Code identifies the outer pack (carton, lug, bin) in which the produce is packed. In pallet files and industry terms this is usually referred to as the "Pack". Examples are M18T (for apples), M12T (apples and pears), B04I (grapes), M05I (plums) etc.

---
### Inventory Code and Inner Pack Code
<br/>
The Inventory Code is typically a two-character code that is present in some pallet files. This short code identifies how the produce is packed inside the outer pack. Examples include PU (punnets), UL (Unlabelled), WA (Wrapped Alternatively), etc.

The Inner Pack Code allows your business to store further details about how the produce is packed inside the outer pack. While the Inventory Code code be PU to indicate punnets, not all punnets are the same size or type. By importing the specific details of the Inner Pack from the pallet files you can for example distinguish between punnets where the Inner Pack indicates 10 x 500g clamshell punnets and other punnets where the Inner Pack indicates 12 x 300g punnets.

---
### Class Code & Addendum Class Code
<br/>
A specific set of classes are eligible for use in export addendums. These are class 1, 2, P and X. But what if want to distinguish EU1 and class 1 pallets from one another? To solve this challenge you can set up the more detailed classes as "Class Code", set up the Addendum Class Codes separately and then **link** the Class Codes to the appropriate Addendum Class Code.
This link is done in **Extended Lookup Values**

_Example of Class Code an Addendum Class Code in Linc Lookup Values_

|Lookup Field Name    |Parent Lookup Field Name |Parent Code |Code |Description        |
|:---                 |:---                     |:---        |:--- |:---               |
| Class Code          |                         |            |EU1  |Class EU1          |
| Class Code          |                         |            |1    |Class 1            |
| Class Code          |                         |            |1S   |Superior Class 1   |
| Addendum Class Code |                         |            |1    |Class 1            |

_Example of how Class Code an Addendum Class Code are "linked" in Extended Lookup Values_

|Lookup Field Name    |Lookup Field Code |Extended Lookup Field Name |Extended Lookup Field Code |
|:---                 |:---              |:---                       |:---                       |
| Class Code          |EU1               | Addendum Class Code       |1                          |
| Class Code          |1                 | Addendum Class Code       |1                          |
| Class Code          |1S                | Addendum Class Code       |1                          |



---
### Size Code and Commodity Code
<br/>
The Size Code refers to the physical size or the "count" of the produce. In industry terms this is often referred to in combination as the "Size/Count" of the produce. Sizes are specific to a commodity and the master data must thus be set up with the Commodity Code as the 'parent' of the Size Code.

_Examples of Linc Lookup Values for Size Code_

|Lookup Field Name |Parent Lookup Field Name |Parent Code |Code |Description             |
|:---              |:---                     |:---        |:--- |:---                    |
| Size Code        |Commodity Code           |AP          |100  |Count 100               |
| Size Code        |Commodity Code           |AP          |110  |Count 110               |
| Size Code        |Commodity Code           |AP          |120  |Count 120               |
| Size Code        |Commodity Code           |AP          |135  |Count 135               |

---
### Brand Code
<br/>
This is sometimes referred to in the industry as the "Mark". The Brand Code identifies the brand of the outer pack. Examples are GENER (Generic), BLACK, etc. These can also be brands that are specific to a retailer or to your own business.

---
### Market Code
<br/>
Master data for Market Code is used for the target market of pallets.

---
### Region Code and Country Code
<br/>
The Region and Country code master data is used for the pallets' target region and target country. These values are typically present in pallet files.
Country Codes are linked to parent Region Codes.

_Examples of Linc Lookup Values for Region Codes_

|Lookup Field Name |Parent Lookup Field Name |Parent Code |Code |Description   |
|:---              |:---                     |:---        |:--- |:---          |
| Region Code      |                         |            |EUN  |Europe        |
| Country Code     |                         |            |AFR  |Africa        |
| Country Code     |                         |            |MEA  |Middle East   |


_Examples of Linc Lookup Values for Country Codes linked to appropriate parent regions_

|Lookup Field Name |Parent Lookup Field Name |Parent Code |Code |Description             |
|:---              |:---                     |:---        |:--- |:---                    |
| Country Code     |Region Code              |EUN         |NL   |Netherlands             |
| Country Code     |Region Code              |AFR         |ZA   |South Africa            |
| Country Code     |Region Code              |MEA         |AE   |United Arab Emirates    |

---
### Inspection Point, Inspection Status and Rejection Reason
<br/>
These three Lookup Field Names all refer to the official inspection data of the pallet - as inspected by PPECB. The information for these three fields will typically be present in pallet files.

Inspection Point: the 4-digit code assigned to a PPECB accredited inspection point
Inspection Status: this is often found in the position for "Stock Pool" in pallet files. Values can for example be NI for Not Inspected or CE for Certified. 
Rejection Reason: these are the 'formal' rejection reasons that come in from pallet files and indicate why the pallet was rejected by PPECB for export. Examples include FCM, CBS, PHYTO, etc.

---
### Harmonised System Code
<br/>
This is often referred to in the industry as the HS Code or Tariff Code. Master data for Harmonised System Codes must be set up for the various commodity codes. This information is then used in layouts for export documentation where the HS Code is required for customs declaration purposes.

---
### Freight Point
<br/>
Freight Points refer to any point where a pallet can be store, transported from or transported to. For this purpose various types of freight points must be defined. These fall into three main categories:

- Locations: Define the cold stores and depots for storing and loading of pallets
- Ports: Define the sea ports, air ports and even "local" land ports from where and to which vessels, planes and trucks can move pallets. 
- Delivery Points of Customers: Set up Freight Points for the various points where pallets can be delivered to for customers.

In Linc Lookup Values these three types of freight points are all simply set up with Lookup Field Name as _Freight Point_. The type is identified in a separate table. Refer to [Point Mappings](/Articles/Configuration/Master%20Data/Point%20Mappings%20)

---
### Producer Code and Producer Site Code
<br/>
The PUC codes of farms must be set up as Producer Codes in Linc Lookup Values.
The Producer Site Code refers to the orchard code from the pallet files. These producer site codes have a child-parent relationship with the producer code.

_Examples of master data for producer codes_

|Lookup Field Name  |Parent Lookup Field Name |Parent Code |Code  |Description             |
|:---               |:---                     |:---        |:---  |:---                    |
|Producer Code      |                         |            |P0086 |Lekker Apples Farm      |
|Producer Code      |                         |            |W0332 |Uncle Jack's farm       |

_Examples of master data for producer site code with the relevant parent producer code defined_

|Lookup Field Name  |Parent Lookup Field Name |Parent Code |Code |Description             |
|:---               |:---                     |:---        |:--- |:---                    |
|Producer Site Code |Producer Code            |P0086       |1K   |Orchard 1K              |
|Producer Site Code |Producer Code            |P0086       |1B   |Orchard 1B              |


---
### Global Gap Number
<br/>
Defining master data for producers" global gap numbers is optional. The system has functionality to get the global gap numbers from either the pallet files themselves or from your master data.  Note that the global gap number itself is placed in the Description field. Make the code unique by concatenating GGN and the Producer Code.

_Examples of master data for global gap numbers_

|Lookup Field Name  |Parent Lookup Field Name |Parent Code |Code      |Description       |
|:---               |:---                     |:---        |:---      |:---              |
|Global Gap Number  |Producer Code            |P0086       |GGN-P0086 |564581245975148   |
|Global Gap Number  |Producer Code            |W0332       |GGN-W0332 |408954611254803   |

---
### Production Area
<br/>
_Production Area master data must be set up as per the formal values as required by PPECB on export addendums. These production areas are then linked to the various producer codes (PUC codes) in Extended Lookup Values._

_Example of Production Areas in Linc Lookup Values_

|Lookup Field Name    |Parent Lookup Field Name |Parent Code |Code |Description        |
|:---                 |:---                     |:---        |:--- |:---               |
| Production Area     |                         |            |WC   |Western Cape       |
| Production Area     |                         |            |EC   |Eastern Cape       |
| Production Area     |                         |            |FS   |Free State         |


_Example of how Class Code an Addendum Class Code are linked in Extended Lookup Values_

|Lookup Field Name    |Lookup Field Code |Extended Lookup Field Name |Extended Lookup Field Code |
|:---                 |:---              |:---                       |:---                       |
|Producer Code        |P0086             | Production Area           |WC                         |
|Producer Code        |W0332             | Production Area           |WC                         |
|Producer Code        |B0001             | Production Area           |FS                         |

---
### Warehouse Zone Code
<br/>
Warehouse Zones refer to specific areas within cold stores or pack houses. Some pallet files from pack houses and cold stores include this information - in which case it can be imported and stored against the pallet in the system. The warehouse zone code can be useful for the marketing department, and can be used to show which pallets are eg. still in cooling and not on temperature, which pallets are ready for marketing, etc. 

Defining master data for warehouse zone codes is optional.

---
### Variety Licensor Code
<br/>
Setting up master data for variety licensor codes is optional, but strongly recommended if your business trades in varieties for which royalties must be paid to the variety licensor. If variety licensors are defined and linked to the relevant variety codes, you can set up standard rates for the royalties based on the variety licensor, rather than for each individual variety code. This simplifies management of standard rates.

To properly set up variety licensor codes, the individual variety licensors must first be defined as master data records themselves. These variety licensors can then be linked to the relevant variety codes in _Variety Licensors_.

_Example of Variety Licensor Codes in Linc Lookup Values_
 
|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description         |
|:---                   |:---                     |:---        |:---        |:---                |
| Variety Licensor Code |                         |            |TOPF PLD    |Topfruit Pink Lady  |
| Variety Licensor Code |                         |            |TOPF STONE  |Topfruit Stone Fruit|



_Example of Variety Licensor Codes linked to Variety Codes in Variety Licensors_

|Variety Code     |Variety Licensor Code |Effective Date |
|:---             |:---                  |:---                      
|PLD              |TOPF PLD              |01/01/2023     |
|ABR              |TOPF STONE            |01/01/2023     |
|DMD              |TOPF STONE            |01/01/2023     |

---
### Freighter Code and Transport Method
<br/>
_Transport Methods are defined by your business and the relevant freighter codes "linked" to these methods using a parent-child relationship_

|Lookup Field Name  |Parent Lookup Field Name |Parent Code |Code       |Description            |
|:---               |:---                     |:---        |:---       |:---                   |
|Freighter Code     |Transport Method         |SEA         |MSC MOZART |MSC Mozart             |
|Freighter Code     |Transport Method         |SEA         |ANTIBES    |Antibes Express        |
|Freighter Code     |Transport Method         |AIR         |AIR FRANCE |Air France             |
|Freighter Code     |Transport Method         |AIR         |BA         |British Airways        |
|Freighter Code     |Transport Method         |LAND        |CHILLI     |Chilli Logistics       |
|Freighter Code     |Transport Method         |LAND        |VDV        |Van der Vyfer Transport|


---
### Freight Agent Code
<br/>
The Freight Agent master data is used to identify the party that secured the booking/space with the shipping line. These freight agents can be shipping lines themselves or a third party. Set up this master data if you require the freight agent to show on export documentation and/or if you need to set up standard rates for a pallet charge where the rate will vary depending on the freight agent.
Freight Agent Codes are not typically required for local business.

---
### Freight Forwarder Code
<br/>
The Freight Forwarder master data is used for freight containers to indentify the freight forwarding party. Set up this master data if you require the freight forwarder to show on export documentation and/or if you need to set up standard rates for a pallet charge where the rate will vary depending on the freight forwarder.
Freight Forwarder Codes are not typically required for local business.

---
### Exporter
<br/>
Master data for Exporter is used for freight containers where the exporter needs to be specified. Set up this master data if you require the exporter to show on export documentation and/or if you need to set up standard rates for a pallet charge where the rate bill vary depending on the exporter.
Exporter codes are not typically required for local business.

---
### Shipper
<br/>
Master data for Shipper is used for freight containers where the shipper needs to be specified. If you ship on your own shipping contract, the shipper will be your own business, but there can be cases where you ship produce on a third party's shipping contract. Set up this master data if you require the shipper to show on export documentation and/or if you need to set up standard rates for a pallet charge where the rate bill vary depending on the shipper.
Shipper codes are not typically required for local business.

---
### Haulier
<br/>
The haulier master data is used for freight containers to identify the transporter of the container between the depot/cold store and port. 
Haulier codes are not used for local business.

---
### Container Type Code
<br/>
Set up master data for container type code if you need to identify the type of container. Examples include 40ft high cube container, 20ft container. 

---
### Temptale Type Code
<br/>
Set up master data for temptale type codes if you need to distinguish between various kinds of temptales used in freight containers. 

---
### Shipping Temperature Code
<br/>
Master data for shipping temperature codes are typically defined based on the official codes used in the fresh produce export industry. 

_Examples of Shipping Temperature Codes in Linc Lookup Values_

|Lookup Field Name          |Parent Lookup Field Name |Parent Code |Code   |Description                                             |
|:---                       |:---                     |:---        |:---   |:---                                                    |
|Shipping Temperarture Code |                         |            |C0.5   |Carry at 0.5 C for the full duration of the voyage      |
|Shipping Temperarture Code |                         |            |EC01   |Minus 1.0 C for 30 days, then 4.0 C until discharge     |

---
### Customs Deduction
<br/>
If you export produce and need to print customs clearing invoices where deductions are shown, define the list of customs deductions codes that the system must automatically insert for the customs clearing invoice in Linc Lookup Values. These are typically Freight and Insurance. Note that this master data is merely to provide the list of individual decuction codes, and not where the actual deduction amounts are specified.

If your business trades locally only, then no master data needs to be set up for customs deductions. 

_Examples of Customs Decutions in Linc Lookup Values_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description         |
|:---                   |:---                     |:---        |:---        |:---                |
|Customs Deduction      |                         |            |FREIGHT     |Freight             |
|Customs Deduction      |                         |            |INSURANCE   |Insurance           |

---
### Defect Code
<br/>
Specific defect codes can be captured against pallets in quality documents for pre-departure and/or arrival QCs. These values identify the actual defects of the produce, and must not be confused with the higher-level quality grade code or customer quality code. Also note that only the LAST defect code will be visually shown against the actual pallet line in the pallet line list. But what if there is more than just one defect for the produce? One solution to this is to create defect codes that combines various defects into a single code.

_Examples of Defect Codes in Linc Lookup Values where defect codes are not combined_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description         |
|:---                   |:---                     |:---        |:---        |:---                |
|Defect Code            |                         |            |BRU         |Bruising            |
|Defect Code            |                         |            |BLE         |Blemishes           |
|Defect Code            |                         |            |SOFT        |Soft Fruit          |
|Defect Code            |                         |            |DECAY       |Decay               |

_Examples of Defect Codes in Linc Lookup Values where defect codes are combined_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description               |
|:---                   |:---                     |:---        |:---        |:---                      |
|Defect Code            |                         |            |BRU-BLE     |Bruising and Blemishes    |
|Defect Code            |                         |            |BRU-SOFT    |Bruising and Soft Fruit   |
|Defect Code            |                         |            |BRU-SCA     |Bruising and Scaling      |

---
### Quality Grade Code
<br/>
Quality Grade Codes are used to identify the quality of produce and pallets before departure. These master data values are thus used and captured in pre-departure quality documents based and provide information to the marketing team that may impact decisions for the sales allocation of pallets. Capturing quality grade codes for pre-departure can also be useful in comparative reporting later on when the pre-departure quality grade code is for example compared with the customer quality code that is assigned to the pallet on arrival.

_Examples of Quality Grade Codes in Linc Lookup Values_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description          |
|:---                   |:---                     |:---        |:---        |:---                 |
|Quality Grade Code     |                         |            |RED         |Red                  |
|Quality Grade Code     |                         |            |AMBER       |Amber                |
|Quality Grade Code     |                         |            |GREEN       |Green                |

---
### Customer Quality Code
<br/>
Customer Quality Code master data is used when capturing Arrival QCs for containers/loads. These are assigned to pallets and stored against the pallet lines. The master data you define here should make sense for your business and for both internal reporting and reporting to your producers.

This master data can be as simple as distinguishing between Sound and Unsound, or more detailed, depending on your reporting requirements.

_Examples of Customer Quality Codes in Linc Lookup Values_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description          |
|:---                   |:---                     |:---        |:---        |:---                 |
|Customer Quality Code  |                         |            |RED         |Red                  |
|Customer Quality Code  |                         |            |AMBER       |Amber                |
|Customer Quality Code  |                         |            |GREEN       |Green                |

_More examples of Customer Quality Codes in Linc Lookup Values for Sound and Unsound only_

|Lookup Field Name      |Parent Lookup Field Name |Parent Code |Code        |Description          |
|:---                   |:---                     |:---        |:---        |:---                 |
|Customer Quality Code  |                         |            |SOUND       |Sound Arrival        |
|Customer Quality Code  |                         |            |UNSOUND     |Unsound Arrival      |


---
### Produce Trade Claim Type
<br/>
Definining master data for Produce Trade Claim Type is optional. This master data is merely used to visually distinguish between various types of produce trade claims in the produce trade claim register. This master data is ONLY stored on the produce trade claim register that is essence a log of possible claims against produce trades and containers. It can assist users in easily filtering the produce trade claim register for certain produce trade claim types, for example shipping claims or produce quality claims.
Note that the produce trade claim type is not stored anywhere on the pallets themselves and has no direct impact on any financial postings.

_Examples of Produce Trade Claim Type in Linc Lookup Values_

|Lookup Field Name         |Parent Lookup Field Name |Parent Code |Code        |Description                   |
|:---                      |:---                     |:---        |:---        |:---                          |
|Produce Trade Claim Type  |                         |            |Shipping    |Shipping and Logistics claim  |
|Produce Trade Claim Type  |                         |            |Packaging   |Packaging claim               |
|Produce Trade Claim Type  |                         |            |Quality     |Produce Quality claim         |

If there is no real benefit for you business in differentiating between various produce trade claim types for easier management of the produce trade claim register, you don't need to create this master data.

---
### Quality Document Type
<br/>
When a user creates a quality document in ProduceLinc, they have to first choose from one of four built-in purposes.

- Re-Inspection
- Pre-Departure QC
- Arrival QC
- Return to Vendor

If you want a to distinguish between different quality document types within each of these built-in puruposes, you can define master data for Quality Document Type in Linc Lookup Values and then map your master data to the built-in purposes in _Quality Document Purposes_. You may for example want to visually distinguish between re-inspections for target market _versus_ re-inspections for age.

_Examples of Quality Document Types in Linc Lookup Values_

|Lookup Field Name         |Parent Lookup Field Name |Parent Code |Code        |Description                   |
|:---                      |:---                     |:---        |:---        |:---                          |
|Quality Document Type     |                         |            |TKM         |Target Market Re-Inspection   |
|Quality Document Type     |                         |            |AGE         |Age Re-Inspection             |
|Quality Document Type     |                         |            |ARRIVE 1    |Arrival 1st inspection        |
|Quality Document Type     |                         |            |ARRIVE FIN  |Arrival Final Inspection      |

_In Quality Documement Purposes this how the above values could then be mapped to the built-in purposes for quality documents_

|Quality Document Type     | Document Purpose         |
|:---                      |:---                      |
|TKM                       |Re-Inspection             |
|AGE                       |Re-Inspection             |
|ARRIVE 1                  |Arrival QC                |
|ARRIVE FIN                |Arrival QC                |    

Based on the above examples a user can then specify the quality document type on a Re-Inspection quality document as either TKM or AGE; and on an Arrival QC as either ARRIVE 1 or ARRIVE FIN.

The Quality Document Type has no impact on the financial posting of claims, nor is it stored anywhere else other than the quality document card and list of quality documents. It is merely a tool to visually differentiate and easily filter between different types of quality document using values that make sense to your business. Defining this set of master data values is thus optional.

---
### Trade Type
<br/>
Trade Types are used to visually differentiate between different types of sales. These values are stored on the produce trade itself and is also visible on the list of produce trades. (Produce Trades represent the sale of pallets in a container to a specific customer). When setting up this master data, think of how your business categorise sales internally. Examples include diffentiating between export _versus_ local; or _Export Fixed_, _Export MGP_, _Export Consignment_, and so forth.

While the Trade Type is not posted together with the financial values of the sales invoices or credit memo, it is mandatory to have a value in the Trade Type on a produce trade before it can be posted. Setting up of master data for Trade Type is thus not optional, but mandatory.

_Examples of Trade Types in Linc Lookup Values_

|Lookup Field Name         |Parent Lookup Field Name |Parent Code |Code        |Description                    |
|:---                      |:---                     |:---        |:---        |:---                           |
|Trade Type                |                         |            |EXP-CONS    |Export Consignment             |
|Trade Type                |                         |            |EXP-FIXED   |Export Fixed Price             |
|Trade Type                |                         |            |EXP-MGP     |Export Minimum Guarantee Price |
|Trade Type                |                         |            |LOC-FIXED   |Local Fixed Price              |
|Trade Type                |                         |            |LOC-MUN     |Local Municipal Market         |


---
### Return to Vendor Reason Code
<br/>
Pallets in ProduceLinc can be flagged as returned to vendor. This is also often referred to in the industry as "Back to Grower". When processing a pallet as a return to vendor, it is mandatory that the user select a Return to Vendor Reason Code from your master data. If you do not need to distinguish between various reasons for pallets that are flagged as _Return to Vendor_ you should still set up at least one reason code for this in Linc Lookup Values, even if it is a very generic reason.

_Examples of Return to Vendor Reason Codes in Linc Lookup Values_

|Lookup Field Name             |Parent Lookup Field Name |Parent Code |Code        |Description                    |
|:---                          |:---                     |:---        |:---        |:---                           |
|Return to Vendor Reason Code  |                         |            |WRONG ORG   |Wrong organisation code        |
|Return to Vendor Reason Code  |                         |            |VEND SELL   |Vendor will sell pallet        |


---
### Claim Code
<br/>
The claim codes are used when posting sales credit memos for customers from produce trades. When preparing for the produce trade credit, it is mandatory that the user choose a posting credit reason code from your master data for Claim Codes. The master data you set up for claim codes are thus used in financial postings and should clearly indicate the **financial** reason for posting the credit to the customer. These are **not** supposed to indicate the detailed information of the defects of the produce. You should also take into consideration that credit memos can be posted for reasons other than quality claims. Think of reasons such as internal corrections for incorrect prices or incorrect exchange rates _versus_ credit memos that are the result of actual quality claims.

_Examples of Claim Codes in Linc Lookup Values_

|Lookup Field Name         |Parent Lookup Field Name |Parent Code |Code        |Description                    |
|:---                      |:---                     |:---        |:---        |:---                           |
|Claim Code                |                         |            |MARKET      |Market Support                 |
|Claim Code                |                         |            |PRICE       |Incorrect Price                |
|Claim Code                |                         |            |X-RATE      |Incorrect Exchange Rate        |
|Claim Code                |                         |            |QUALITY     |Quality Claim                  |
|Claim Code                |                         |            |B2S         |Back to Stock                  |


---
### Proforma Invoice Title, Trade Invoice Title, Trade Cr. Memo Title
<br/>
When documents for the proforma invoice, produce trade invoice and produce trade credit memo are printed, the title that appears at the top of the printed or PDF document is not cast in stone, so to speak. The system dynamically prints the title as is specified on the specific produce trade for which the document is printed. You can set up more than one title for each of these documents. Then define one title for each document as the default in Linc Setup, and specify specific document titles for specific customers in Produce Trade Defaults.

The value the system prints is the value from the "Description" field of the master data in Linc Lookup Values.

_Examples of titles for documents in Linc Lookup Values_

|Lookup Field Name         |Parent Lookup Field Name |Parent Code |Code        |Description                    |
|:---                      |:---                     |:---        |:---        |:---                           |
|Proforma Invoice Title    |                         |            |PROF-1      |Proforma Invoice               |
|Trade Invoice Title       |                         |            |TRADE-IN-1  |Invoice                        |
|Trade Invoice Title       |                         |            |TRADE-IN-2  |Tax Invoice                    |
|Trade Invoice Title       |                         |            |TRADE-IN-3  |Final Invoice                  |
|Trade Cr. Memo Title      |                         |            |TRADE-CR-1  |Credit Note                    |
|Trade Cr. Memo Title      |                         |            |TRADE-CR-2  |Credit Memo                    |
|Trade Cr. Memo Title      |                         |            |TRADE-CR-3  |Tax Credit Note                |

---