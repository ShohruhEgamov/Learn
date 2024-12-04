# import matplotlib.pyplot as plt

# # Data points for an illustrative example of BTC/USD
# # Assume these are the high, low, and close prices for 3 days
# days = ["kun 20", "kun 21", "kun 22"]
# yuqori_narxlar = [99000, 98500, 98800]
# past_narxlar = [97000, 96000, 96500]
# previous_close_prices = [97500, 98500, 97000]

# # Calculate |Low - Previous Close| for each day
# low_prev_close_diff = [abs(low - prev_close) for low, prev_close in zip(past_narxlar, previous_close_prices)]

# # Plotting the data
# plt.figure(figsize=(10, 6))

# # Plot High, Low, and Previous Close Prices
# plt.plot(days, yuqori_narxlar, label="High Prices", marker="o")
# plt.plot(days, past_narxlar, label="Low Prices", marker="o")
# plt.plot(days, previous_close_prices, label="Previous Close Prices", marker="o")

# # Highlighting the difference |Low - Previous Close|
# plt.bar(days, low_prev_close_diff, alpha=0.5, color="orange", label="|Low - Previous Close|")

# # Adding details
# plt.title("BTC/USD Analysis: High, Low, Previous Close and Differences")
# plt.xlabel("Days")
# plt.ylabel("Price (USD)")
# plt.legend()
# plt.grid()

# # Show the plot
# plt.tight_layout()
# plt.show()



# def calculate_atr(highs, lows, closes, period=14):
#     """
#     ATR (Average True Range) hisoblash
#     :param highs: Maksimal narxlar ro'yxati
#     :param lows: Minimal narxlar ro'yxati
#     :param closes: Yopilish narxlari ro'yxati
#     :param period: ATRni hisoblash uchun period (standart 14)
#     :return: ATR qiymati
#     """
#     true_ranges = []
#     for i in range(1, len(highs)):
#         tr = max(
#             highs[i] - lows[i],
#             abs(highs[i] - closes[i - 1]),
#             abs(lows[i] - closes[i - 1]),
#         )
#         true_ranges.append(tr)

#     atr = sum(true_ranges[-period:]) / period
#     return atr


# def trading_decision(price, atr, sl_multiplier=1.5, tp_multiplier=3):
#     """
#     Savdo qarorini aniqlash
#     :param price: Joriy narx
#     :param atr: Hisoblangan ATR qiymati
#     :param sl_multiplier: Stop Loss masofasini aniqlash uchun koeffitsient
#     :param tp_multiplier: Take Profit masofasini aniqlash uchun koeffitsient
#     :return: SL, TP, va savdo qarori (Buy/Sell)
#     """
#     sl = price - atr * sl_multiplier
#     tp = price + atr * tp_multiplier
#     return sl, tp


# # Foydalanuvchi kiritmalari
# print("Narxlarni kiritish uchun yo'riqnomaga rioya qiling:")
# highs = list(map(float, input("Maksimal narxlar (vergul bilan ajrating): ").split(',')))
# lows = list(map(float, input("Minimal narxlar (vergul bilan ajrating): ").split(',')))
# closes = list(map(float, input("Yopilish narxlari (vergul bilan ajrating): ").split(',')))
# current_price = float(input("Joriy narxni kiriting: "))

# # ATRni hisoblash
# atr = calculate_atr(highs, lows, closes)
# print(f"ATR (14 period): {atr:.2f}")

# # Savdo qarorini aniqlash
# sl, tp = trading_decision(current_price, atr)
# print(f"Stop Loss (SL): {sl:.2f}")
# print(f"Take Profit (TP): {tp:.2f}")

# # Savdo tavsiyasi
# if current_price < sl:
#     print("Tavsiya: SELL")
# elif current_price > tp:
#     print("Tavsiya: BUY")
# else:
#     print("Tavsiya: Kuzatishda davom eting")




import matplotlib.pyplot as plt

# Example data for High, Low, Close prices
days = ["Day 1", "Day 2", "Day 3"]
highs = [2655, 2673, 2715]
lows = [2618, 2647, 2673]
closes = [2620, 2650, 2680]

# Plotting the High, Low, and Close prices
plt.figure(figsize=(10, 6))
plt.plot(days, highs, label="High Prices", marker="o", color="red")
plt.plot(days, lows, label="Low Prices", marker="o", color="blue")
plt.plot(days, closes, label="Close Prices", marker="o", color="green")

# Adding labels and title
plt.title("High, Low, and Close Prices Over 3 Days", fontsize=14)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)

# Display the graph
plt.show()
