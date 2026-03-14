import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import yfinance as yf

# Parameters
TICKER = 'AAPL'  # Change to your preferred stock
SIMULATIONS = 200
DAYS = 252  # 1 year of trading days

# Download historical data
data = yf.download(TICKER, period='3y', interval='1d')
if data.empty:
    raise ValueError(f"No data found for ticker {TICKER}")
if 'Adj Close' in data.columns:
    prices = data['Adj Close'].dropna()
elif 'Close' in data.columns:
    prices = data['Close'].dropna()
else:
    raise ValueError(f"Neither 'Adj Close' nor 'Close' found in data for ticker {TICKER}")

# Calculate log returns
daily_returns = np.log(prices / prices.shift(1)).dropna()
mu = daily_returns.mean()
sigma = daily_returns.std()
if isinstance(mu, pd.Series):
    mu = mu.values[0]
if isinstance(sigma, pd.Series):
    sigma = sigma.values[0]

dt = 1  # 1 day
last_price = prices.iloc[-1]
def extract_scalar(val):
    if isinstance(val, pd.Series):
        return float(val.values.flatten()[0])
    if isinstance(val, np.ndarray):
        return float(val.flatten()[0])
    return float(val)
S0 = extract_scalar(last_price)

# Monte Carlo simulation
simulations = np.zeros((SIMULATIONS, DAYS))
historical_prices = prices.values.flatten()
for sim in range(SIMULATIONS):
    price_path = np.zeros(DAYS)
    # Start from a random historical price
    price_path[0] = np.random.choice(historical_prices)
    for t in range(1, DAYS):
        drift = (mu - 0.5 * sigma**2) * dt
        shock = sigma * np.random.normal() * np.sqrt(dt)
        prev_price = extract_scalar(price_path[t-1])
        exp_val = np.exp(drift + shock)
        price_path[t] = prev_price * exp_val
    simulations[sim, :] = price_path



# Animated 3D Line Plot: Each simulation is a line that "races" forward in time

# 2D Animated Racing Line Plot
import matplotlib.animation as animation


fig, ax = plt.subplots(figsize=(12, 8))
X = np.arange(DAYS)
lines = []
for i in range(SIMULATIONS):
    (line,) = ax.plot([], [], alpha=0.7, linewidth=1)
    lines.append(line)

ax.set_xlim(0, DAYS)
ax.set_ylim(np.min(simulations), np.max(simulations))
ax.set_title(f"Monte Carlo Stock Price Simulation for {TICKER}")
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Stock Price ($)')
ax.grid(True)
plt.tight_layout()

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    if frame == 0:
        for line in lines:
            line.set_data([], [])
    else:
        for i, line in enumerate(lines):
            line.set_data(X[:frame], simulations[i, :frame])
    return lines

ani = animation.FuncAnimation(
    fig, update, frames=DAYS, init_func=init, interval=30, blit=True, repeat=False
)
plt.show()
