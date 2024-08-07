# Overview: Pallet Editor Rules

The rules/conditions under which a field on the pallet may be edited are not the same across all pallet fields. Some fields are subjected to stricter rules than others - especially where these fields have an impact on financial entries or grouping logic for produce trades and produce bills.

  


The table below lists the editable fields - each with a link to a specific *Scenario* that specifies the conditions under which editing of the field will not be allowed. 

  




| PALLET LINE FIELD | SCENARIO RULE SET |
| --- | --- |
| Brand Code | Scenario 3 |
| Class Code | Scenario 5 |
| Color Code | Scenario 1 |
| Commodity Code | Scenario 5 |
| Commodity Group Code | Scenario 5 |
| Country of Origin | Scenario 3 |
| External Purchase Reference | Scenario 1 |
| External Sales Reference | Scenario 2 |
| GGN | Scenario 1 |
| Harvest Date | Scenario 4 |
| Inbound Channel Code | Scenario 7 |
| Inner Pack Code | Scenario 3 |
| Inspection Date | Scenario 4 |
| Inspection Point | Scenario 1 |
| Intake Date | Scenario 4 |
| Intake Freight Point | Scenario 3 |
| Intended Purchase Comment | Scenario 1 |
| Intended Sales Comment | Scenario 1 |
| Lot Billing Type | Indirectly edited through re-applying of lot billing defaults. Scenario 6 rules apply. |
| Lot Billing Party No. | Indirectly edited through re-applying of lot billing defaults. Scenario 6 rules apply. |
| Outbound Channel Code | Scenario 7 |
| Outer Pack Code | Scenario 5 |
| Pack Date | Scenario 4 |
| Packhouse Code | Scenario 3 |
| Packhouse Lot No. | Scenario 1 |
| Pallet Edit Reason | A reason code must be provided when editing any field |
| Phyto Data | Scenario 1 |
| Producer Code | Scenario 4 |
| Producer Lot No. | Scenario 1 |
| Producer Site Code | Scenario 1 |
| Quality Grade Code | No editing restrictions |
| Quality Grade Remark | No editing restrictions |
| Rejection Reason Code | No editing restrictions |
| Size Code | Scenario 5 |
| Target Country Code | Scenario 3 |
| Target Market Code | Scenario 3 |
| Target Region Code | Scenario 3 |
| Target Retailer Code | Scenario 3 |
| Variety Code | Scenario 5 |
| Variety Group Code | Scenario 5 |
| Verified Gross Weight | Scenario 1 |

  


### SCENARIO 1

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)

  


### SCENARIO 2

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- Pallet is on an Active Produce Trade

  


### SCENARIO 3

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- The status of the related Cost Produce Bill of the pallet lot is not *Open*

  


### SCENARIO 4

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- Pallet is on a Produce Bill (irrespective of the purpose of the produce bill)

  


### SCENARIO 5

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- The sum of the posted trade amounts is not zero  
- The status of the related Cost Produce Bill of the pallet lot is not *Open*  
- The posted Advance Produce Bill amounts are not zero  
- The posted Cost Produce Bill amounts are not zero

  


### SCENARIO 6

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- Produce Trade entries exist  
- Produce Bill entries exist (postings were processed from advance or cost produce bills)  
- Pallet is on a Produce Bill (irrespective of the purpose of the produce bill)

  


### SCENARIO 7

Pallet field cannot be edited if  
- Final Payment Status of the pallet is *Processed* (i.e. if the pallet has been *Final Paid*)  
- The sum of the posted trade amounts (SCY and LCY) is not zero  
- The posted Advance Produce Bill amounts (PCY and LCY) are not zero  
- The posted Cost Produce Bill Amounts (PCY and LCY) are not zero  
- Pallet is on a Produce Bill (irrespective of the purpose of the produce bill)

