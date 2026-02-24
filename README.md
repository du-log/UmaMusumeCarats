# Carat Pack API for Ratios and Greedy Optimizing
This is a basic local host API in Python that provides the ratios of each carat pack in the Uma Musume in-game shop and Cygames ID Web Store. The calculations are primarily for the English version of Uma Musume where we simply divide the amount of carats per pack by their dollar value. For the Web Store calculation, there is an additional tax rate we need to factor in to determine the ratio of the packs.

The API also provides endpoints for calculating the most optimal combination of packs that can provide the most amount of carats within a given budget. For the web store, there are two endpoints depending on if the limited packs are available or not. The calculation for the in-game shop optimizer assumes that the player is on Android where, as of February 2026, there is no digital tax applied when paying through Google Play. Additional assumption is if the player is located in Georgia, US.

Not included is the Daily Carats Pack as the calculations for total carats overall are assuming the player buys all of the carats at once rather than waiting the full 30 days to get all 1,500 free carats. However, for light spenders it is absolutely recommended to buy the daily pack as it gives the best ratio of carats/$.

## In-Game Shop Ratios (Not All)
### Carats, Price, Ratio (/$)
- 5,000, $69.99, ~71.44 Carats
- 2,500, $33.99, ~73.55 Carats
- 1,500, $20.99, ~71.46 Carats

## Cygames Web Shop Ratios (Not All)
### Carats, Sub-Price (Price + 7% Tax), Taxed Ratio (/$)
- 1,650 (Limited), $13.99 ($14.97), ~110.23 Carats
- 2,750, $33.99 ($36.37), ~75.61 Carats
- 5,500, $69.99 ($74.89), ~73.44 Carats

## Greedy-By-Weight
For the moment, I utilized a greedy algorithm that focuses first on the carat pack with the best ratio. Most, if not all, calculations will end up excluding the packs with 5,000 carats or 5,500 carats due to the cost of the pack. Within the code, the dictionary for the limited web store contains a limit variable as the 1,650 carat and 8,250 carat packs are only sold x amount of times and only restock on special occasions, likely anniversaries and/or holidays. Additional limits are set on the non-limited packs as well, but this can be modified to your liking.

All endpoints for calculating optimal pack combinations will take in a **budget** float variable. Endpoints for the web store take in a **tax_rate** float variable preset to 0.07, but can be changed if a different value is passed.

### Example Budgets and Combinations
**Disclaimer: All costs are assumed an estimate, and as such while they reflect the total cost at my location, they may not be as accurate for other locations.**
#### Budget: $200  
In-Game Shop:
- 2,500 Carats x 5
- 1,500 Carats x 1
- 210 Carats x 3
- Total Carats: 14,630  
- Cost: $199.91

Web Store (7% Tax):
- 2,750 Carats x 5
- 231 Carats x 5
- 66 Carats x 2
- Total Carats: 15,037
- Cost: $199.96

Web Store + Limited (7% Tax):
- 1,650 Carats (Limited) x 2
- 2,750 Carats x 4
- 1,650 Carats x 1
- 66 Carats x 2
- Total Carats: 16,082
- Cost: $199.99
#### Budget: $500
In-Game Shop:
- 2,500 Carats x 14
- 1,500 Carats x 1
- 210 Carats x 1
- Total Carats: 36,710
- Cost: $499.84

Web Store (7% Tax):
- 2,750 Carats x 13
- 1,650 Carats x 1
- 231 Carats x 1
- 66 Carats x 1
- Total Carats: 37,697
- Cost: $499.52

Web Store + Limited (7% Tax):
- 1,650 Carats (Limited) x 2
- 2,750 Carats x 12
- 1,650 Carats x 1
- 231 Carats x 3
- 66 Carats x 1
- Total Carats: 38,709
- Cost: $499.49
