from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
)

PACKS = [
    {"name": "5,000 Carats", "price": 69.99, "carats": 5000},
    {"name": "2,500 Carats", "price": 33.99, "carats": 2500},
    {"name": "1,500 Carats", "price": 20.99, "carats": 1500},
    {"name": "700 Carats", "price": 9.99, "carats": 700},
    {"name": "350 Carats", "price": 5.99, "carats": 350},
    {"name": "210 Carats", "price": 2.99, "carats": 210},
    {"name": "60 Carats", "price": 0.99, "carats": 60},
]

WEB_STORE_PACKS = [
    {"name": "5,500 Carats", "price": 69.99, "carats": 5500, "limit": 100},
    {"name": "2,750 Carats", "price": 33.99, "carats": 2750, "limit": 100},
    {"name": "1,650 Carats", "price": 20.99, "carats": 1650, "limit": 100},
    {"name": "770 Carats", "price": 9.99, "carats": 770, "limit": 100},
    {"name": "385 Carats", "price": 5.99, "carats": 385, "limit": 100},
    {"name": "231 Carats", "price": 2.99, "carats": 231, "limit": 100},
    {"name": "66 Carats", "price": 0.99, "carats": 66, "limit": 100},
]

WEB_STORE_PACKS_LIMITED = [
    {"name": "8,250 Carats (Limited)", "price": 69.99, "carats": 5000, "limit": 3},
    {"name": "1,650 Carats (Limited)", "price": 13.99, "carats": 1650, "limit": 2},
    {"name": "5,500 Carats", "price": 69.99, "carats": 5500, "limit": 100},
    {"name": "2,750 Carats", "price": 33.99, "carats": 2750, "limit": 100},
    {"name": "1,650 Carats", "price": 20.99, "carats": 1650, "limit": 100},
    {"name": "770 Carats", "price": 9.99, "carats": 770, "limit": 100},
    {"name": "385 Carats", "price": 5.99, "carats": 385, "limit": 100},
    {"name": "231 Carats", "price": 2.99, "carats": 231, "limit": 100},
    {"name": "66 Carats", "price": 0.99, "carats": 66, "limit": 100},
]

#Optimizer using Greedy-By-Density to Determine Best Combination for Most Carats by Ratio
#in the In-Game Shop
@app.get("/optimize/ratio/standard")
def optimize(budget: float):
    sorted_packs = sorted(PACKS, key=lambda x: x['carats'] / x['price'], reverse=True)
    remaining = budget
    selection = []
    total_carats = 0

    for pack in sorted_packs:
        count = int(remaining // pack['price'])
        if count > 0:
            selection.append({
                "name": pack['name'],
                "count": count,
                "sub_price": round(pack['price'] * count, 2),
                "sub_carats": count * pack['carats']
            })
            total_carats += (pack['carats'] * count)
            remaining -= (pack['price'] * count)

    return {
        "best_combo": selection,
        "total_carats": total_carats,
        "remaining_budget": round(remaining, 2)
    }

def calc_final(pack, tax_rate):
    return pack['price'] * (1 + tax_rate)

#Optimizer using Greedy-By-Density to Determine Best Combination for Most Carats by Ratio
#in the Web Store with Limited Packs
@app.get("/optimize/ratio/limited")
def optimize(budget: float, tax_rate: float = 0.07):
    sorted_packs = sorted(
        WEB_STORE_PACKS_LIMITED, key=lambda x: x['carats'] / calc_final(x, tax_rate), reverse=True
    )
    remaining = budget
    selection = []
    total_carats = 0

    for pack in sorted_packs:
        count = int(remaining // calc_final(pack, tax_rate))
        to_buy = min(count, pack['limit'])
        if count > 0:
            selection.append({
                "name": pack['name'],
                "count": to_buy,
                "sub_price": round(to_buy * calc_final(pack, tax_rate), 2),
                "sub_carats": to_buy * pack['carats']
            })
            total_carats += (pack['carats'] * to_buy)
            remaining -= (calc_final(pack, tax_rate) * to_buy)

    return {
        "best_combo": selection,
        "total_carats": total_carats,
        "remaining_budget": round(remaining, 2)
    }

#Web Optimizer Minus Limited Packs
@app.get("/optimize/ratio/web")
def optimize(budget: float, tax_rate: float = 0.07):
    sorted_packs = sorted(
        WEB_STORE_PACKS, key=lambda x: x['carats'] / calc_final(x, tax_rate), reverse=True
    )
    remaining = budget
    selection = []
    total_carats = 0

    for pack in sorted_packs:
        count = int(remaining // calc_final(pack, tax_rate))
        to_buy = min(count, pack['limit'])
        if count > 0:
            selection.append({
                "name": pack['name'],
                "count": to_buy,
                "sub_price": round(to_buy * calc_final(pack, tax_rate), 2),
                "sub_carats": to_buy * pack['carats']
            })
            total_carats += (pack['carats'] * to_buy)
            remaining -= (calc_final(pack, tax_rate) * to_buy)

    return {
        "best_combo": selection,
        "total_carats": total_carats,
        "remaining_budget": round(remaining, 2)
    }

#Carats/$USD Ratios for Packs in In-Game Shop
@app.get("/data/ratios/standard")
def get_ratios():
    ratios = []
    for p in PACKS:
        pack_ratio = p['carats'] / p['price']
        ratios.append({
            "name": p['name'],
            "ratio": round(pack_ratio, 2),
            "carats": p['carats'],
            "price": p['price'],
        })

    return sorted(ratios, key=lambda x: x["ratio"], reverse=True)

#Carats/$USD Ratios for Packs in Cygames ID Web Store
@app.get("/data/ratios/limited")
def get_ratios(tax_rate: float = 0.07):
    ratios = []
    for p in WEB_STORE_PACKS:
        pack_ratio = p['carats'] / calc_final(p, tax_rate)
        ratios.append({
            "name": p['name'],
            "ratio": round(pack_ratio, 2),
            "carats": p['carats'],
            "price": p['price'],
            "taxed_price": round(calc_final(p, tax_rate), 2)
        })

    return sorted(ratios, key=lambda x: x["ratio"], reverse=True)