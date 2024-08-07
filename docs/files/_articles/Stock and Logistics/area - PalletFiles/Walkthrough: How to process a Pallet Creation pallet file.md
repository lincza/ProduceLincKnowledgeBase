# Walkthrough: How to process a Pallet Creation pallet file

What does it do?

* Creates new pallets (intakes)

  


How do I process a pallet creation file?

* Resolve validation errors (correct values on the lines/add master data/create pallet file translation rule/ add missing pallet packing setup rules) For more information, see [Walkthrough: How to resolve errors and confirm pallet lines](https://linc.freshdesk.com/en/support/solutions/articles/8000097826)
* Resolve ‘blank’ Lot Billing Default Type and Lot Billing Party No. issues by ensuring that rules exist in Lot Billing Defaults (file lines cannot be confirmed if the lot billing information is ‘blank’)
* Resolve issue where fields are not allowed to be blank by entering the necessary values
* Lines in “Validated” status with zero errors can be confirmed
* The “Confirm” action creates the pallet in the system and essentially puts it into stock
