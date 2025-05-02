---
grand_parent: Stock and Logistics
has_children: false
layout: default
nav_order: 42003
parent: Produce Orders
title: Limit vendors to specific currencies
---

# Limit vendors to specific currencies

### In this article
[The business case](#the-business-case)  
[Limit certain vendors to a specific currency](#limit-certain-vendors-to-a-specific-currency)  
[How currency and prices are converted for vendors with limited currency](#how-currency-and-prices-are-converted-for-vendors-with-limited-currency)  

---
## The business case
<br/>
When pallets are allocated to outbound produce order lines, ProduceLinc updates the _Intended Purchase Currency_ and _Intended Purchase Price_ for those pallets using the values from the related produce order line.
But what if some of the vendors (lot billing parties) for those allocated pallets may only be paid in a specific currency, and the intended purchase currency of the order line is different?

Let's say a user creates a produce order line with USD intended purchase currency and price, and then allocates 10 pallets to the order line. But the vendor for 3 of the 10 pallets may only be paid in LCY (local currency). This user is likely a member of the marketing or logistics department and unaware that this vendor may not be paid in USD. But you need these 3 pallets to end up with _Intended Purchase Currency_ as LCY (local currency), and of course not with the USD _Intended Purchase Price_ the user entered on the produce order line.


---
## Limit certain vendors to a specific currency
<br/>
You can limit a vendor to a specific currency by enabling _Limit Purchase Currency_ on the vendor card. If this is enabled, the intended purchase currency for the vendor's pallets must match the default currency code on the vendor card. 

ProduceLinc will ensure that such a vendor's pallets end up with the correct _Intended Purchase Currency Code_ and take care of converting the _Intended Purchase Price_. Read the next section for more information. 

![](/media/StockLog_ProduceOrders_ConvertPurchCurr_1._LimitVendor.png)  


---
## How currency and prices are converted for vendors with limited currency
<br/>
When pallets are allocated to produce order lines the _Intended Purchase Currency_ for allocation pallets for vendors with _Limit Purchase Currency_ will automatically be updated to match the currency of the vendor card. At the same time the _Intended Purchase Price_ for these pallets will be converted from the produce order line's intended purchase price to a price in the vendor's currency.


### Example conversion and logic:
<br/>
Let's illustrate with an example and the following setup:

Exchange rate for USD = 17
Exchange rate for EUR = 20

Available pallets for the order line include pallets from three Vendors

- PVEN014 - the purchase currency for this vendor is NOT limited
- PVEN015 - purchase currency is limited to USD
- PVEN042 - purchase currency is limited to LCY (blank value on the vendor card)

Produce Order Line's Intended Purchase Currency is EUR, Intended Purchase Price is 10 and Minimum Guarantee Purchase Price is 8.

Here's the order line before the allocation

![](/media/StockLog_ProduceOrders_ConvertPurchCurr_2._OrderLine.png)  

Here are the available pallets where the intended currencies and prices have not yet been updated.

![](/media/StockLog_ProduceOrders_ConvertPurchCurr_3._PalletsBeforeAllocation.png)  

**Thus:**

- for PVEN014 the intended purchase currency and price should be as per the order line (in EUR)
- for PVEN015 the intended purchase currency must be USD with prices converted from the order line's EUR prices
- for PVEN042 the intended purchase currency must be LCY (blank) with prices converted from the order line's EUR prices

Here's how the intended purchase currencies and prices look like after the pallets were allocated to the order line.

![](/media/StockLog_ProduceOrders_ConvertPurchCurr_4._ConvertedCurrAndPrices.png)  

**What is the conversion logic for the prices?**  

The order line's intended prices are first converted to LCY based on the latest exchange rate
If the vendor's currency must then be something else, eg. USD, the LCY values that were calculated in the previous step are then converted using the latest exchange rate for the 'final' currency.
Thus, based on the exchange rates for this example:

For vendor PVEN015 that we must pay in USD the conversion logic is this:

> _Order Line Intended Purchase Price: EUR 10 x exch. rate of 20 = LCY 200_  
  > _LCY 200 divided by USD exch. rate of 17 = USD 11.76_  


> _Order Line Purchase MGP: EUR 8 x exch. rate of 20 = LCY 160_  
  > _LCY 160 divided by USD exch. rate of 17 = USD 9.41_  
  
For vendor PVEN042 that must be paid in LCY the conversion logic is this:

> _Order Line Intended Purchase Price: EUR 10 x exch. rate of 20 = LCY 200_   
> _Order Line Purchase MGP: EUR 8 x exch. rate of 20 = LCY 160_