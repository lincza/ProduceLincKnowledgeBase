---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 33001
parent: Pallet Verification
title: Pallet Verifications overview
---

# Pallet Verifications overview


### In this article
[Introduction to Pallet Verification](#introduction-to-pallet-verification)  
[Stock Reconciliation](#stock-reconciliation)  
[Update of Pallet Information](#update-of-pallet-information)  
[How ProduceLinc knows when to auto-process a pallet verification file for stock reconciliation or for update of pallet information](#how-producelinc-knows-when-to-auto-process-a-pallet-verification-file-for-stock-reconciliation-or-for-update-of-pallet-information) 


Related articles
<br/>
[Pallet Verifications for stock reconciliation](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20for%20stock%20reconciliation)  
[How to interpret Pallet Verification Results for stock reconciliations](/articles/Stock%20and%20Logistics/Pallet%20Verification/Guides/How%20to%20Interpret%20Pallet%20Verification%20Results)  
[Pallet Verifications for update of pallet information](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20for%20update%20of%20pallet%20information)  


---
## Introduction to Pallet Verification
<br/>
When a pallet file is imported, ProduceLinc assigns a **purpose** to the pallet file (based on your pallet file purpose mapping or the purpose you selected when doing a manual import of the file).
One such purpose is **Pallet Verification**. 

It is typically the PS files (stock files) from cold stores that are imported for pallet verification purpose. 

Files with this purpose can perform two main actions:

- Perform a stock reconciliation between the available pallets in the system and the stock as per the location's latest stock file (Pallet Verification for stock reconciliation)
- Update information on existing pallet lines (Pallet Verification for pallet information updates)

---
## Stock Reconciliation
<br/>
It is common practice for businesses in produce marketing to process a full reconciliation between the system's available stock and the various locations' stock files at least once a day (**_Stock Reconciliation_**). This is often done before or at the start of each business day. For this **_stock reconciliation_** you want to compare the location's latest stock file with the system stock on a pallet ID level. 

The staff member that is tasked with this daily stock recon will identify any discrepancies between the locations' stock files and the available stock in the system. This may include - among other things - identifying some missing intake files and PO files, and ensuring that pallets that are no longer in the location's stock file are also not shown as available stock in the system. 

Since we're reconciling stock on a pallet ID level, the file lines for a **_stock reconciliation_** file do not need to be validated, matched to a specific existing pallet lot or confirmed. The system is simply comparing Pallet ID to Pallet ID. 

  
---
## Update of Pallet Information
<br/>
The Stock recon takes care of comparing a location's stock file to the system's available stock on a Pallet ID level, but as stock files (PS files) are imported throughout the day, you may also want these files to update certain fields on the existing pallet IDs and pallet lines in the system. The fields that are updated from pallet verification files fall into two main "categories":
- Location related fields (fields that tell you at which location the pallet ID is)
- Produce related fields (fields that tell you what the specifications of the pallet ID and its pallet lines are, eg. the variety code, producer code, inspection date, etc.)

---
## How ProduceLinc knows when to auto-process a pallet verification file for stock reconciliation or for update of pallet information
<br/>
The processing of pallet verification files are handled by two job queue entries that you must set up. Both entries must be set up for **Codeunit 85038 SnapshotFPoint_Ver_FRP_LINC**, but with different parameter strings.

### Job Queue Entry for stock reconciliation
<br/>
The job queue entry for this codeunit 85038 with parameter string **VERIFY** is used to run the stock reconciliation that compares stock files to system stock on pallet ID level.

![](/media/StockLogistics_PalletVerification_JobQueue_Snapshot_StockRecon.jpeg)

It does the following:
- Finds the **latest** pallet verification file for each location
- Gives it a Verification DateTime stamp (the date and time when the job queue runs)
- Performs the stock reconciliation and produces a verification result
- Will also try to validate the file lines and auto-match them to existing pallet lot numbers. For file lines that are validated, matched and error-free in this latest pallet verification file, the system will also update the information on the pallet lines.

See [Pallet Verifications for stock reconciliation](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20for%20stock%20reconciliation) for more detailed information.  
Also visit our guide on [How to interpret Pallet Verification Results](/articles/Stock%20and%20Logistics/Pallet%20Verification/Guides/How%20to%20interpret%20Pallet%20Verification%20Results)  
   
### Job Queue Entry for update of pallet information from stock files
<br/>
The job queue entry for this codeunit 85038 with a **blank value** in the parameter string is used to run the stock update action on existing pallet IDs and pallet lines.

![](/media/StockLogistics_PalletVerification_JobQueue_Snapshot_PalletUpdate.jpeg)

It does not perform a stock reconciliation, but does the following:
- Finds the **latest** pallet verification file for each location
- Tries to validate the file lines, auto-match them to existing pallet lot numbers and performs other checks (like ensuring that there are no compare errors and that the location fields of existing pallets may in fact be updated)
- Confirms validated and matched file lines and updates the existing pallet lines in the system with the latest information.

See [Pallet Verifications for update of pallet information](/articles/Stock%20and%20Logistics/Pallet%20Verification/Pallet%20Verifications%20for%20update%20of%20pallet%20information) for more detailed information.  

---