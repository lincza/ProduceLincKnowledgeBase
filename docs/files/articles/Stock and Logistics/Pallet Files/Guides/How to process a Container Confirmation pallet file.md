---
grand_parent: Pallet Files
has_children: false
layout: default
nav_order: 31909
parent: Guides
title: How to process a Container Confirmation pallet file
---

How to process a Container Confirmation pallet file

What does it do?

* Does not create new pallets
* Can compare and/or update fields on the matched pallet ID and pallet lot with values from the file line – for fields that are marked for compare and/or update in the related pallet file definition
* Can compare and/or update fields on the related container – eg. External container number, Seal no., Temptale ID, booking reference, container external document no., etc.
* Compares the file with the relevant container and shows any discrepancies (pallets in the container but not in the file, pallets in the file but not in the container).



How do I process a container confirmation file?

* Choose the container confirmation purpose in the pallet file header (Outbound / Transfer / Inbound)
* Resolve normal validation errors first. For more information, see:  [# How to resolve errors and confirm pallet lines](https://linc.freshdesk.com/en/support/solutions/articles/8000097826)
* Once lines are validated, the system tries to find a Matched Pallet ID and Matched Pallet Lot No. (just like it would do for a pallet verification file, since a container confirmation file can also compare and update fields on the pallets in the system)
* Compare errors are generated (if any exist) as it would for a pallet verification file. Fix the values on the lines or ignore the errors.
* Once ALL lines in the file are validated and have a Matched Pallet ID and Matched Pallet Lot No. the system will try to find the trip leg and container for each pallet and auto-populate these values in the Compare Freight Trip Leg and Compare Freight Container fields. It searches only in trip legs and containers for the Container Confirmation Purpose you have chosen in the header. Thus, if you chose ‘Outbound’, it would ignore transfer and inbound legs, etc.
* The system then performs a file compare. This means that it checks that all the pallets for a given External container number are in the same internal container (Compare Freight Container) – and that all pallets in an internal container (Compare Freight Container) have the same external container no. (thus, were stuffed into the container as per your load instruction). Mismatches/discrepancies are clearly identified and must be resolved before you can confirm the container.
* Once all compare errors and file compare discrepancies have been resolved – thus, ALL lines validated with matched pallet ID and pallet lot no., correct values in Compare Freight Trip Leg and Compare Freight Container and no errors on the lines, confirm the container by selecting a single line of the container and choose “Confirm selected Lines”.