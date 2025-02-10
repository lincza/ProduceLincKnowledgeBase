---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 33002
parent: Pallet Verification
title: Pallet Verifications for stock reconciliation
---
# Pallet Verifications for stock reconciliation


### In this article
[Required setup to perform stock reconciliations](#required-setup-to-perform-stock-reconciliations)  
[What happens during stock reconciliation](#what-happens-during-stock-reconciliation  )


Related Articles
<br/>
[Pallet Verifications overview](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20overview)  
[How to interpret Pallet Verification Results for stock reconciliations](/articles/Stock%20and%20Logistics/Pallet%20Verification/Guides/How%20to%20interpret%20Pallet%20Verification%20Results)  

---
## Required setup to perform stock reconciliations
<br/>

Some initial setup must be done to ensure that ProduceLinc can automatically perform stock reconciliations.

**Pallet File Definitions:** The system needs the 'location' of each stock file to be in the 'header' of the pallet file entry. Thus, ensure you define the current freight point for the PS file definition(s) as the "Verification Freight Point".

![](/media/StockLogistics_PalletVerification_PalletFIleDefinition_VerificationFreightPoint.jpeg)  

**Pallet File Purpose Mapping:** The files you want to use for stock reconciliation must be mapped for Pallet Verification in Pallet File Purpose Mapping. These will typically be the PS files from the various locations. The field for _Automatically Confirm Lines_ must also be checked.

![](/media/StockLogistics_PalletVerification_PalletFilePurposeMapping.jpeg)  

**Job queue entry:** A job queue entry for codeunit 85038 SnapshotFPointVer_FRP_LINC must be set up, and have the word **_VERIFY_** in the parameter string. This parameter string is what tells the system to process the pallet verification files (stock files) for stock reconciliation.
Set up this job queue to run once a day (for example early in the morning) or at more regular intervals throughout the day - depending on your business principles.

![](/media/StockLogistics_PalletVerification_JobQueue_Snapshot_StockRecon.jpeg)  

**Point Mappings for locations:** Ensure that all the locations for which you will receive and process PS files are defined in Point Mappings with **Mapping Type** as _Location_.

![](/media/StockLogistics_PalletVerification_PointMappingsLocations.jpeg)



## What happens during stock reconciliation

When the job queue entry for SnapshotFPointVer_FRP_LINC with **VERIFY** in the parameter string runs, it
- finds the **latest** pallet verification file (stock file) for each location in the system
- updates the Verification Snapshot DateTime for each of these last files, based on the date and time that the job queue entry executes
- performs the comparison between the stock file's pallet IDs and the system's Pallet IDs that are available and in stock for the location.
   - _ProduceLinc takes all pallets that are NOT yet in an outbound freight container into consideration when comparing the system stock to the location's file_

The results of the comparison can be viewed in the **_Pallet Verifications_** page. This page is filtered to show
- the **last** verification results for each location
- where the Verification Snapshot DateTime is up to and including the current date and time (when you opened the page), but not older than 30 days

The verification results are classified into 4 groups
- System and Freight Point File
- Only in System
- Only in Freight Point File
- Incomplete Transfer

Here's an example of what you can see in the Pallet Verifications page
![](/media/StockLogistics_PalletVerification_StockRecon_PalletVerificationResults_Example.jpeg)  

See [How to interpret Pallet Verification Results](/articles/Stock%20and%20Logistics/Pallet%20Verification/Guides/How%20to%20Interpret%20Pallet%20Verification%20Results)