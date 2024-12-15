def Tax(taxable_income): # 160,0000
    taxable_income -= min(taxable_income*.5, 100000)
    taxable_income -= 60000
    if taxable_income >= 5000001:
        return ((taxable_income-5000000)*.35) + 7500 + 20000 + 37500 + 50000 + 250000 + 900000
    elif taxable_income >= 2000001:
        return ((taxable_income-2000000)*.3) + 7500 + 20000 + 37500 + 50000 + 250000
    elif taxable_income >= 1000001:
        return ((taxable_income-1000000)*.25) + 7500 + 20000 + 37500 + 50000
    elif taxable_income >= 750001:
        return ((taxable_income-750000)*.2) + 7500 + 20000 + 37500
    elif taxable_income >= 500001:
        return ((taxable_income-500000)*.15) + 7500 + 20000
    elif taxable_income >= 300001:
        return ((taxable_income-300000)*.1) + 7500
    elif taxable_income >= 1500001:
        return ((taxable_income-150000)*.05)
    elif taxable_income < 1500001:
        return 0

print(Tax(1000000))
