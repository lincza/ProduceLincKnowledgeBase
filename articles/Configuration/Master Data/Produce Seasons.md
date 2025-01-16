---
grand_parent: Configuration
has_children: false
layout: default
nav_order: 21003
parent: Master Data
title: Produce Seasons
---

# Produce Seasons

### In this article

[Overview of Produce Seasons](#overview-of-produce-seasons)  
[Impact of Current field of Produce Seasons](#impact-of-current-field-of-produce-seasons)


Related Guide
<br/>
[How to set up Produce Seasons](/articles/Configuration/Master%20Data/Guides/How%20to%20set%20up%20Produce%20Seasons)

---
## Overview of Produce Seasons
<br/>
Produce Seasons allow your business to report on produce trading by season, and not just by accounting periods and financial years.

Pallet lines are associated with produce seasons based on their respective confirmation dates, commodity group code, inbound channel and outbound channel.

This produce season code is visible on pallet lines, pallet selection and pallet allocation, and also in the pallet line archive that is the main source of data for reporting on larger volumes of data.

Produce seasons are defined for combinations of Commodity Group, Inbound Channel and Outbound Channel; allowing for each combination to have different start and end dates. This is particularly useful if your business not only trades in locally produced produce but also imports produce from overseas.

**Example**:

* Grapes produced locally (inbound channel "L") and exported (outbound channel "E") could have start and end dates defined as 1st Nov 2021 to 31st May 2022 for the 2022 season grouping
* Grapes that are imported (inbound channel "I") and sold locally (outbound channel "L") for the 2022 season can have start dates from 1st May 2022 to 31st October 2022

| **Produce Season Code** | **Commodity Group Code** | **Inbound Channel Code** | **Outbound Channel Code** | **Start Date** | **End Date** |
| --- | --- | --- | --- | --- | --- |
| 2022GR-L-E | GR | L | E | 2021-11-01 | 2022-05-31 |
| 2022GR-I-L | GR | I | L | 2022-05-01 | 2022-10-31 |


---
## Impact of **Current** field of Produce Seasons
<br/>
Produce Seasons are marked as *Current* or *Non-Current*. This has the following impact on the rebuild of the pallet line archive that is used for reporting purposes.

* During the rebuild of the pallet line archive (typically via a scheduled job queue), the system first deletes all lines from the pallet line archive where **Current** is TRUE.
* Pallets that are marked **not** market as **Current**, are left in the pallet line archive with their information as is.
* The system then finds all pallet lines that are associated with current produce season codes and rebuilds these lines to the pallet line archive with their latest information.

Thus, a produce season code should only be marked as non-current in **Produce Seasons** once all transactions for the pallet have been completed; including the final payment to the producer.

