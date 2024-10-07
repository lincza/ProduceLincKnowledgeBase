---
grand_parent: Reporting
has_children: false
layout: default
nav_order: 61001
parent: Profitability Reporting
title: Pallet line archive - Reporting on income, costs, and gross profit
---

# Pallet line archive - Reporting on income, costs, and gross profit
<br/>
The pallet line archive contains a vast number of fields, including various amount fields. To simplify reporting on income, costs, commission and gross profit we have included the summaries of these amounts in a list of easily identifiable reporting fields.

- Reporting Income (LCY)
- Reporting Income Status
- Reporting Cost (LCY)
- Reporting Commission (LCY)
- Reporting Produce Cost (LCY)
- Reporting Gross Profit (LCY)
- Reporting Produce Bill Purpose
- Reporting Produce Bill No.
- Reporting Produce Bill Status


Here is how to interpret these values:

## Reporting Income (LCY) and Reporting Income Status
Several factors impact how the Reporting Income and Reporting Status is calculated. These include things such as whether income from the produce trade was posted as final or not final, whether the pallet is on a forecast or cost produce bill, the status of the produce bill and the trade exchange rate rule that is used for the produce bill. 

Here is the logic: 

### Pallet is not on a forecast or cost produce bill. Income from the produce trade was posted as NOT final

- _Reporting Income (LCY)_ is calculated as the _Posted Trade Amount (LCY)_ + _Outstanding Amount (LCY)_ - _Income Charges (LCY)_
- _Reporting Income Status_ is _Intended Income_


### Pallet is not on a forecast or cost produce bill. Income from the produce trade was posted as final
  
- _Reporting Income (LCY)_ is calculated as the _Posted Trade Amount (LCY)_ - _Income Charges (LCY)_
- _Reporting Income Status_ is _Final Income_


### Pallet is on a forecast produce bill

The _Net Trade Amount (LCY)_ of the forecast bill line is shown in the _Reporting Income (LCY)_. This means that the forecast produce bill must have gone through a charge calculation, during which the Net Trade Amount (LCY) is calculated. The conditions of the trade posting (final or not final) as well as the chosen Trade Exchange Rate Rule of the produce bill have an impact on how the Net Trade Amount (LCY) - and by extension Reporting Income (LCY) - is calculated.

Here is the logic:

Income from the produce trade was posted as NOT final

- Net Trade Amount (LCY) is calculated as the (Posted Trade Amount + Outstanding Amount - Income Charges) x exch. rate as per the Trade Exchange Rate Rule selected for the produce bill
- _Reporting Income Status_ is _Intended Income_


Income from the produce trade was posted as final

- Net Trade Amount (LCY) is calculated as the (Posted Trade Amount - Income Charges) x exch. rate as per the Trade Exchange Rate Rule selected for the produce bill
- _Reporting Income Status_ is _Final Income_


### Pallet is on a cost produce bill

The _Net Trade Amount (LCY)_ of the cost bill line is shown as the _Reporting Income (LCY)_. This means that the cost produce bill must have gone through a charge calculation, during which the Net Trade Amount (LCY) is calculated. The chosen Trade Exchange Rate Rule of the produce bill have an impact on how the Net Trade Amount (LCY) - and by extension Reporting Income (LCY) - is calculated. Note that on a cost produce bill the final/not final posted state of the produce trade income has no impact and only the real posted trade amounts and income charges are used for the calculation of Net Trade Amount (LCY).

Here is the logic:

- Net Trade Amount (LCY) is calculated as the (Posted Trade Amount - Income Charges) x exch. rate as per the Trade Exchange Rate Rule selected for the produce bill
- _Reporting Income Status_ is _Final Income_


*\* see footnote for reporting income on production pallets*



## Reporting Charges (LCY)

_Reporting Charges (LCY)_ refer to the cost of the pallet but excludes the produce cost itself. It comes from the prioritised charges of the pallet line's related bill line. This means that the pallet line must be on either a forecast or cost produce bill, and that the produce bill must have gone through a charge calcualtion, during which the charges are calculated and prioritised. 

- _Reporting Charges (LCY)_ in the pallet line archive is then shown as the sum of the prioritised charges, but excludes any recharges and pallet charges with treatment "Commission".



## Reporting Commission (LCY)

_Reporting Commission (LCY)_ come from the prioritised commission charges of the pallet line. This means that the pallet line must be on either a forecast or cost produce bill and that the produce bill must have gone through a charge calculation for values to show in this field.

- _Reporting Commission (LCY)_ in the pallet line archive is then shown as the sum of the prioritised charges for those pallet charge codes that are set up in your master data with treatment _Commission_.




## Reporting Produce Cost (LCY)

_Reporting Produce Cost (LCY)_ refers to the cost of the produce itself, and is calculated using the bill amounts of the pallet line. This means that the pallet line must be on either an invoice, forecast or cost produce bill. If the pallet is on an invoice produce bill, then that bill must either have posting amounts entered for the pallet line or must have already been posted. If the pallet is on a forecast or cost produce bill, the bill must have at least gone through a _Bill Calculation_ or have already been posted for amounts to show in Reporting Produce Cost (LCY).

_Reporting Produce Cost (LCY)_ is then simply calculated as the _Posting Amount (LCY)_ + _Posted Bill Amount (LCY)_ of the bill line.

In essence the value is the sum of all invoice and cost bill amounts that have already been posted, plus any additional values that you are about to post (posting amounts).




## Reporting Gross Profit (LCY)

For lot billing type **Consignment** the _Reporting Commission LCY_ is simply shown in _Reporting Gross Profit (LCY)_ since this is your business' income for the pallet.


For lot billing type **Purchase** the _Reporting Gross Profit (LCY)_ is calculated as Reporting Income (LCY) - Reporting Charges (LCY) - Reporting Produce Cost (LCY)





## Reporting Produce Bill No.

The actual no. of the Forecast or Cost Produce Bill is shown in this field. This provides easy traceability in cases where values and status of the produce bill must be further investigated.




## Reporting Produce Bill Purpose

This field indicates whether the pallet is on a forecast or cost produce bill.




## Reporting Produce Bill Status

The status of the relevant forecast or cost produce bill is shown in this field. This is a useful when interpreting the values of the Reporting fields. For example: the Reporting Produce Cost shows no value, but the pallet is on a cost produce bill. The Reporting Produce Bill Status may indicate the status of the bill as "Open" or "Charges Calculated" - which could explain why there are not posting or posted bill amounts to use for calculating Reporting Produce Cost.

<br/>

## \* Production Pallets

- An output pallet that was also used as an input pallet will show zero values in the 'Reporting' amount fields, since these pallets were neither sold to a customer, nor does it get paid to lot billing parties.

- Output pallets carry their own income, since these are the pallets that are 'sold and invoiced' to customers. But the total prioritised costs sits against the related input pallet lot. Thus, to allow for reporting from a 'sales perspective by eg. customer' on these pallets, the Prioritised Charges, Prioritised Commission and Produce Costs (all in LCY) of the input pallet is 'apportioned' to the output lot purely for reporting purposes. These apportioned values are then shown in _Reporting Charges (LCY)_, _Reporting Commission (LCY)_ and _Reporting Produce Cost (LCY)_ in the pallet line arcive for the production output pallets.

- If your business uses pallet production, it is important to ensure that you include and exclude production pallets appropriately when reporting. This depends on the desired perspective. If your intention is to report on the total income and costs for your business, you should exclude production output pallet lines from such report views since the income and costs of production output pallets are already apportioned to their related input pallet lines (the original intake pallets) during calculations of the production produce bills.