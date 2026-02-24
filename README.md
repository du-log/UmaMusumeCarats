# Carat Pack API for Ratios and Greedy Optimizing
This is a basic API in Python that provides the ratios of each carat pack in the Uma Musume in-game shop and Cygames ID Web Store.
The calculations are primarily for the English version of Uma Musume where we simply divide the amount of carats per pack by their dollar value.
For the Web Store calculation, there is an additional tax rate we need to factor in to determine the ratio of the packs.

The API also provides endpoints for calculating the most optimal combination of packs that can provide the most amount of carats within a given budget.
For the web store, there are two endpoints depending on if the limited packs are available or not.
The calculation for the in-game shop optimizer assumes that the player is on Android where, as of February 2026, there is no digital tax applied when purchasing through Google Play.
Additional assumption is if the player is located in Georgia, US.

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
