
## Creator / Dev
## tubakhxn

# Monte Carlo Stock Simulator 3D

This project simulates possible future stock prices using the Monte Carlo method and visualizes the results as an animated racing line plot. It uses real historical stock data from Yahoo Finance and demonstrates how randomness and volatility affect stock price predictions.

## What is this project?
This is a Python-based simulator that:
- Downloads historical stock price data for a given ticker
- Estimates drift and volatility from the data
- Runs 200+ Monte Carlo simulations of future price paths
- Animates the results so you can see all simulated paths "racing" into the future

## Relevant Wikipedia Links
- [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Geometric Brownian motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
- [Stock market](https://en.wikipedia.org/wiki/Stock_market)

## How to Fork and Run
1. **Fork this repository** using the GitHub interface (top right, 'Fork' button)
2. **Clone your fork** to your computer:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Monte_Carlo_Stock_Simulator_3D.git
   cd Monte_Carlo_Stock_Simulator_3D
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the simulator**:
   ```bash
   python main.py
   ```
5. A window will open showing the animated simulation plot.

## Customization
- Edit `main.py` to change the stock ticker, simulation count, or time horizon.
