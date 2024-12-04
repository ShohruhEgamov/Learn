# Given data for High and Low prices
highs = [2655, 2673, 2715]
lows = [2618, 2647, 2673]

# Calculating average Close prices based on (High + Low) / 2
average_closes = [(high + low) / 2 for high, low in zip(highs, lows)]
print(average_closes)