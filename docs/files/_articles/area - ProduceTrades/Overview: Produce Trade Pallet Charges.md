# Overview: Produce Trade Pallet Charges

Overseas and account sale costs - as charged by the customer - can be posted directly from the produce trade by defining the costs in the *Pallet Charge Assignment* section of the produce trade.

  


Before posting a produce trade, the sum of the posting amount of the pallet charge assignments associated with the produce trade is added to the sum of the posting amount of the pallet lines and if the nett is positive, an invoice will be posted, else a credit memo.

  


It is possible to post pallet charges on produce trades without also posting trade amounts for the produce pallets.

  


Post manual Pallet Charges
--------------------------

* Choose the **Assignment Level** as either *Produce Trade*, *Pallet* or *Pallet Lot*. To assign and spread the posting amount across all pallets in the produce trade, select *Produce Trade* in **Assignment Level**, and select the freight container code in the **Assignment Target** field. If the Assignment Level is selected as *Pallet*, the posting amount will assign and spread to all pallet lines of the Pallet ID that is selected in **Assignment Target**. If *Pallet Lot* is selected as the Assignment level, the posting amount will be assigned and allocated only to the pallet lot number that is specified in the Assignment Target.
* Select the appropriate pallet charge in the **Pallet Charge Code** field. The list of available pallet charges that can be selected is limited to pallet charge codes where the treatment is *Income*.
* Enter the amount in the **Posting Amount** field. Negative amounts will reduce income; positive amounts will increase income.
* Multiple pallet charge assignment lines can be entered on the produce trade.
* When the produce trade is posted, the Posting Amount field will clear - ready for additional posting amounts of subsequent postings. The sum of the posted pallet charges for a line will be displayed in the **Amount** and **Amount (LCY)** fields.

  


Post Standard Pallet Charges
----------------------------

* Standard rates for Pallet Charges of treatment type *Income* can be defined in **Pallet Charge Standard Rates**. These will be added to the pallet charge assignment lines during the create/update step of a produce trade and will always be applied at the pallet lot no. level.

 

