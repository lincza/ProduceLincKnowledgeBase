---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 33003
parent: Pallet Verification
title: Pallet Verifications for update of pallet information
---

# Pallet Verifications for update of pallet information


### In this article
[Required setup to automatically update pallet information from pallet verification files](#required-setup-to-automatically-update-pallet-information-from-pallet-verification-files)  
[What happens when the job queue entry runs for update of pallet information](#what-happens-when-the-job-queue-entry-runs-for-update-of-pallet-information)  
[Update of Location related fields](#update-of-location-related-fields)  
[Update of Produce related fields](#update-of-produce-related-fields)  


Related Articles
<br/>
[Pallet Verifications overview](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20overview)  

---
## Required setup to automatically update pallet information from pallet verification files
<br/>
Some initial setup must be done to ensure that ProduceLinc can automatically process pallet verification files for update of pallet information.


**Pallet File Purpose Mapping:** If you want to use PS files to update information on pallet lines, make sure you set these up in Pallet File Purpose Mapping for Pallet Verification and that you have checked the box for _Automatically Confirm Lines_.

![](/media/StockLogistics_PalletVerification_PalletFilePurposeMapping.jpeg)

**Job Queue Entry:** A job queue entry for codeunit 85038 SnapshotFPointVer_FRP_LINC must be set up, and have a **blank** value in the parameter string. This blank parameter string is what tells the system to process the pallet verification files specifically for update of information on the existing pallet lines.
Set up this job queue for update of pallet information to run at regular intervals throughout the day, eg. every 4 hours.

![](/media/StockLogistics_PalletVerification_JobQueue_Snapshot_PalletUpdate.jpeg)



## What happens when the job queue entry runs for update of pallet information
<br/>
When the job queue entry for SnapshotFPointVer_FRP_LINC with a **blank** value in the parameter string runs, it finds the **latest** pallet verification file (stock file) for each location in the system and

- tries to validate the file lines for these files (checks it against your master data)
- tries to auto-match validated pallet lines to existing pallet lines (fills in the Matched Pallet ID and Matched Pallet Lot No.)
- checks if there are any 'compare' errors
- checks if the location related fields of the file lines may be updated

If the file lines of a Pallet ID in the file passes the above tests, the system will automatically confirm the lines and update the pallet information on the existing pallet lines. 
The fields that are updated fall into two main categories:

- Location related fields (fields that tell you at which location the pallet ID is)
- Produce related fields (fields that tell you what the specifications of the pallet ID and its pallet lines are, eg. the variety code, producer code, inspection date, etc.)


### Update of Location related fields
<br/>
You'll note we mentioned above that the lines of a Pallet ID in the file must pass the test that checks if location related fields on the pallet may be updated. So, what's this all about?
We'll illustrate with some examples.

**Scenario 1**
Pallet ID 1 in the system is at Current Freight Point A, and it has been allocated for transfer to Freight Point B.
You receive a stock file from Freight Point B that contains that Pallet ID. Freight Point B is essentially saying that they now have Pallet ID X in stock.
The pallet ID passes the test.

**Scenario 2**
Pallet ID 2 in the system is at Current Freight Point A. It is not allocated for transfer to another freight point.
You receive a stock file from Freight Point A that contains the Pallet ID. Since the 'existing' current freight point of the pallet already matches the current freight point of the file, there is nothing to update ini terms of the location of the pallet ID.
The Pallet ID passes the test.

**Scenario 3**
Pallet ID 3 in the system is at Current Freight Point A. It is not allocated for transfer to another freight point.
You receive a stock file from Freight Point B that contains the Pallet ID, but according to the system it wasn't allocated to move to Point B. 
The Pallet ID fails the test.

**Scenario 4**
Pallet ID 4 in the system is at Current Freight Point A. It is allocated for trasnfer to freight point B.
You receive a stock file from Freight Point C that contains the Pallet ID. Freight Point C is thus saying that they have Pallet ID 4 in stock, but in the system it is allocated to transfer to a different freight point (Point B).
The Pallet ID fails the test.

So, if the Pallet ID in the pallet verification file **does** pass the test, (and is properly matched to an existing pallet lot number), ProduceLinc will update the **Current Freight Point**, **Current Freight Point Date**, **Loading Freight Point**, **Packhouse Lot No.** and **Outbound Channel Code**. It will also clear the **Allocated Transfer Point** (since it has now arrived at its new destination).
These location related fields are updated even if you haven't marked them for "Pallet Verification Update" in the related pallet file definition. 


### Update of Produce related fields
<br/>
If the lines of a Pallet ID in the pallet verification file are validated, properly matched to an existing pallet lot number, have no compare errors and passes the CanFreightPoint, it will also update any of the fields that you have marked for "Pallet Verification Update" in the related pallet file definition.

Example of fields marked for update in the pallet file fields of a pallet file definition
![](/media/StockLogistics_PalletVerifications_FileDefinitions_UpdatePalletInformation.jpeg)  

---