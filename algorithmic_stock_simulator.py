import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- Step 1: Initializing Financial Math Simulation Models ---")

total_trading_days = 100
initial_stock_price = 150.0
volatility_coefficient = 0.02

np.random.seed(42)
daily_market_returns = np.random.normal(loc=0.001, scale=volatility_coefficient, size=total_trading_days)

simulated_prices = np.zeros(total_trading_days)
simulated_prices[0] = initial_stock_price

print("Running progressive mathematical matrix compounding iterations...")

for day in range(1, total_trading_days):
    simulated_prices[day] = simulated_prices[day-1] * (1 + daily_market_returns[day])

market_dictionary = {
    "Trading_Day": np.arange(1, total_trading_days + 1),
    "Live_Share_Price": np.round(simulated_prices, 2)
}
df = pd.DataFrame(market_dictionary)

df["10_Day_Moving_Average"] = df["Live_Share_Price"].rolling(window=10).mean()

print("\nInitial Financial Matrix Log Preview:")
print(df.head(12))  

print("\n--- Step 2: Generating Elite Multi-Line Financial Trend Chart ---")
plt.figure(figsize=(10, 5))


plt.plot(df["Trading_Day"], df["Live_Share_Price"], color="#228B22", label="Simulated Live Share Price", linewidth=2)
plt.plot(df["Trading_Day"], df["10_Day_Moving_Average"], color="#DC143C", label="10-Day Trendline Moving Average", linewidth=2.5, linestyle="--")


plt.title("Algorithmic Stock Market Trend Simulation & Moving Average Analysis", fontsize=11, fontweight="bold")
plt.xlabel("Trading Timeline (Days)", fontsize=10)
plt.ylabel("Stock Share Price Valuation ($)", fontsize=10)
plt.grid(axis='both', linestyle='--', alpha=0.5)
plt.legend(loc="lower left")
plt.tight_layout()

print("Force rendering layout financial charts...")
plt.show(block=True)
