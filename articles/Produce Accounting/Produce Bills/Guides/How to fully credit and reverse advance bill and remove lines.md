---
grand_parent: Produce Bills
has_children: false
layout: default
nav_order: 52903
parent: Guides
title: How to fully credit and reverse advance bill and remove lines
---

# How to fully credit and reverse advance bill and remove lines

<br/>
**Step 1:** If the Advance Produce Bill is in "Posted' status, reopen the bill. The advance produce bill will now be in _Open_ status
<br/>
<br/>
**Step 2:** Calculate the Charges
<br/>
<br/>
**Step 3:** Calculate the Bill. Status of the advance bill will now be _Bill Calculated_
<br/>
<br/>
**Step 4:** Now change the _Posting Amount (PCY)_ on the lines for which you want to fully reverse the advance. This can either be on all the lines or only some of the lines. Fill in the _Posting Amount (PCY)_ with the full negative of what was posted as an advance. If _Posted Adv. Amount (PCY)_ is eg. 10,0000.00 for the line, enter -10,000.00 in _Posting Amount (PCY)_.
<br/>
<br/>
**Step 5:** Check that the _Posting Amount (LCY)_ is also the full negative of _Posted Adv. Amount (LCY)_. If they are not, then you are likely using a different exchange rate for the reversal than the exchange rate that was used for the initial posting. You can re-open the bill again, change the currency factor to match that of the initial posting and repeat step 2 to step 3 again.
<br/>
<br/>
**Step 6:** Remember to supply a _Posting Credit Reason Code_ for the lines for which you want to post the credit.
<br/>
<br/>
**Step 7:** Release and Post the advance bill. The lines for which you entered full reversal amounts should now have zero under _Posted Adv. Amount (PCY)_.
<br/>
<br/>
**Step 8:** Reopen the bill again. (The produce bill must be in _Open_ status to allow you to delete lines.)
<br/>
<br/>
**Step 9:** Delete the relevant lines from the advance bill (the ones you fully reversed).
<br/>
<br/>
**Step 10:** Release and Post the Bill. This last action is not to post further amounts, but simply to put the advance produce bill in a _Posted_ status again.