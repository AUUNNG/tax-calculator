def Tax(value): # 160,0000
    value -= min(value*.5, 100000)
    value -= 60000 + 30000 + 30000
    if value >= 5000001:
        return ((value-5000000)*.35) + 0 + 7500 + 20000 + 37500 + 50000 + 250000 + 900000
    elif value >= 2000001:
        return ((value-2000000)*.3) + 0 + 7500 + 20000 + 37500 + 50000 + 250000
    elif value >= 1000001:
        return ((value-2000000)*.25) + 0 + 7500 + 20000 + 37500 + 50000
    elif value >= 750001:
        return ((value-2000000)*.2) + 0 + 7500 + 20000 + 37500
    elif value >= 500001:
        return ((value-2000000)*.15) + 0 + 7500 + 20000
    elif value >= 300001:
        return ((value-2000000)*.1) + 0 + 7500
    elif value >= 1500001:
        return ((value-2000000)*.05) + 0
    elif value < 1500001:
        return 0

print(Tax(250000))
