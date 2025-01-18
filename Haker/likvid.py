# Grafikni qayta yaratish uchun kodni takrorlaymiz

import matplotlib.pyplot as plt

# Diagramma uchun ma'lumotlar
price_levels = [100, 98, 95, 92, 88, 85, 88, 92, 96, 100, 104]
time = list(range(len(price_levels)))

# Grafikni yaratish
plt.figure(figsize=(10, 6))

# Narx harakati
plt.plot(time, price_levels, label="Price Action", color="blue", linewidth=2)

# Support darajasini chizish
plt.axhline(y=85, color='red', linestyle='--', label="Support Level")

# Fake breakout nuqtasi
plt.scatter(5, 85, color="red", zorder=5, label="Liquidity Sweep")

# Belgilar va chiziqlar
plt.annotate("Liquidity Sweep\n(Fake Breakout)", xy=(5, 85), xytext=(2, 87),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color="black")

plt.annotate("Price Reverses", xy=(7, 88), xytext=(8, 82),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color="green")

# Grafik nomlari
plt.title("Liquidity Sweep Strategy (Fake Breakout Example)")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
