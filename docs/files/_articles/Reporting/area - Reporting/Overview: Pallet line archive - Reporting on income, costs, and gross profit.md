# Overview: Pallet line archive - Reporting on income, costs, and gross profit

The pallet line archive contains a vast number of fields, including various amount fields. To simplify reporting on income, costs, commission and gross profit we have included the summaries of these amounts in a list of easily identifiable reporting fields.

  


* Reporting Income (LCY)
* Reporting Income Status
* Reporting Cost (LCY)
* Reporting Commission (LCY)
* Reporting Produce Cost (LCY)
* Reporting Gross Profit (LCY)
* Reporting Produce Bill Purpose
* Reporting Produce Bill No.
* Reporting Produce Bill Status

  


Here is how to interpret these values:

  


**Reporting Income (LCY)**

* If the pallet has non-final postings from the produce trade, then "Reporting Income (LCY)" is the Intended Sales Amount in LCY less any Income Charges (LCY) that was already posted from the produce trade.

  


* If the pallet has final postings from the produce trade, but is not on a cost or forecast produce bill, then "Reporting Income (LCY)" is the Posted Trade Amount LCY less the Income Charges LCY that was posted from the produce trade.

  


* If the pallet is on a cost or forecast produce bill, then "Reporting Income (LCY) is the "Net Trade Amount (LCY)" from the produce bill line [essentially the same as Posted Trade Amount (LCY) less Income Charges (LCY)]

  


*\* see footnote for reporting on production pallets*

  


  


**Reporting Income Status**

* If the pallet has a final posting from a produce trade, then the "Reporting Income Status" = Final Income

  


* If the pallet has no postings from a produce trade or if only non-final postings (i.e. customer advances) were processed from the produce trade, then "Reporting Income Status" = Intended Income

  


**Reporting Charges (LCY)**

* The total prioritised charges (LCY) excluding Recharges and "Commission" pallet charges

  


  


**Reporting Commission (LCY)**

* The total prioritised commission in LCY

  


  


**Reporting Produce Cost (LCY)**

* The total produce cost (bill amounts) in LCY - i.e. the 'fruit' portion, NOT the charges

  


**Reporting Gross Profit (LCY)**

* For lot billing type 'Consignment', this is the "Reporting Commission (LCY)" - i.e. your business' income

  


* For lot billing type 'Purchase', this is the "Reporting Income (LCY)" less "Reporting Charges (LCY) less "Reporting Produce Cost (LCY)

  


  


**Reporting Produce Bill No.**

* The actual no. of the cost or forecast produce bill

  


**Reporting Produce Bill Purpose**

* Indicates if the pallet line is on a forecast produce bill or cost produce bill

  


**Reporting Produce Bill Status**

* The actual "Status" field of the related cost/forecast produce bill

  


  


  


  


**\* Production Pallets:**

* An output pallet that was also used as an input pallet will show zero values in the 'Reporting' amount fields, since these pallets were neither sold to a customer, nor does it get paid to lot billing parties.

  


* Output pallets carry their own income, since these are the pallets that are 'sold and invoiced' to customers. But the total prioritised costs sits against the related input pallet lot. Thus, to allow for reporting from a 'sales perspective by eg. customer' on these pallets, the Prioritised Charges, Prioritised Commission and Produce Costs (all in LCY) of the input pallet is 'apportioned' to the output lot purely for reporting purposes. This is done in "Reporting Charges (LCY)","Reporting Commission (LCY)" and "Reporting Produce Cost (LCY)" fields on the pallet line archive.

  


  


  


