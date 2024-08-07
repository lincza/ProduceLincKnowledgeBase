# Overview: Salesperson Code

When pallets are allocated for sales, the system automatically assigns the Salesperson Code. The Salesperson code is part of the grouping logic of Produce Trades and is shown on the Produce Trade header and Produce Trade list page. Salesperson Code indicates who is responsible for the commercial deal and is useful for sales analysis and reporting, and also for managing produce trades and potential customer claims.

  


On pallet allocation and redirect of pallets to an Allocated Delivery Point, the Salesperson Code is first derived from the related Customer record, then from the User Setup of the allocation user, and last from Produce Trade Defaults. The last Salesperson Code found in either of the above is the value that is ultimately assigned to the pallet line. This allows for Salesperson Codes to be defined on the Customer record only and with no corresponding rule in User Setup and Produce Trade Defaults, for cases where the same Salesperson should be assigned irrespective of the user allocating the pallets or the Commodity Group of the allocated pallets.

  


For more information, see [Produce Trade Defaults](https://linc.freshdesk.com/en/support/solutions/articles/8000097808)

  


  


  


