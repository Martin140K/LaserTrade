import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data
from indicators import add_indicators
from model import train_model
import pandas as pd

# st.title("LaserTrade – Predikce trhu")

st.markdown("<h1 style='color:rgb(110,0,140); font-size:60px; font-family:Courier; text-align:center;'>"
    "LaserTrade"
    "</h1>",
    unsafe_allow_html=True)

st.markdown("<h2 style='color:white; font-family:Courier; text-align:center;'>"
    "Predikce trhu"
    "</h2>",
    unsafe_allow_html=True)

# Populární trhy
markets = {
    "Akcie USA": ["AAPL", "NVDA", "MSFT", "GOOGL", "AMZN", "TSLA"],
    "Kryptoměny": ["BTC-USD", "ETH-USD", "SOL-USD", "ADA-USD"],
    "Forex": ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X"],
    "Komodity": ["GC=F (zlato)", "CL=F (ropa)", "SI=F (stříbro)"]
}

df_markets = pd.DataFrame([
    {"Trh": key, "Tickery": ", ".join(value)} for key, value in markets.items()
])
st.subheader("Populární trhy a tickery")
html_table = df_markets.to_html(index=False)
html_table = html_table.replace('<th>', '<th style="text-align:center">')

st.markdown(html_table, unsafe_allow_html=True)

ticker = st.text_input("Zadej ticker (např. AAPL, BTC-USD):", "AAPL")

# Načtení dat

df = load_data(ticker)
df = add_indicators(df)
df, model, acc = train_model(df)

st.write(f"📊 Přesnost modelu: {acc*100:.2f} %")

# Vizualizace


import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(12,6))
fig.patch.set_facecolor("black")   # celé plátno
ax.set_facecolor("#111111")        # oblast grafu
# ax.plot(df.index, df['Close'], color="#1454d0", label="Close")
# ax.plot(df.index, df['EMA_20'], color="orange", label="EMA 20")

# plt.figure(figsize=(12,6))

# # Close a EMA
plt.plot(df['Date'], df['Close'], label='Close', color='blue')
plt.plot(df['Date'], df['EMA_20'], label='EMA 20', color='orange')

plt.scatter(df['Date'][df['Prediction']==1], df['Close'][df['Prediction']==1], label='Predicted Up', color='green', marker='^')
plt.scatter(df['Date'][df['Prediction']==0], df['Close'][df['Prediction']==0], label='Predicted Down', color='red', marker='v')

# osa - barvy
for spine in ax.spines.values():
    spine.set_color("white")

ax.tick_params(axis='x', colors="white")
ax.tick_params(axis='y', colors="white")

ax.set_xlabel("Datum", color="white")
ax.set_ylabel("Cena v USD", color="white")

# data
# ax.plot(df.index, df['Close'], label="Close", color="white")
# ax.plot(df.index, df['EMA_20'], label="EMA 20", color="orange")

# ax.legend()



# Predikce posledního dne
last_row = df.iloc[[-1]]
features = ['Close', 'EMA_20', 'RSI', 'Volume']
X_last = last_row[features]
pred = model.predict(X_last)[0]

if pred == 1:
    prediction_text = "TRH PŮJDE NAHORU ↑"
    color = "green"
else:
    prediction_text = "TRH PŮJDE DOLŮ ↓"
    color = "red"

# Text pod graf (souřadnice 0.5 = střed, 0.0 = úplně dole)
plt.figtext(0.5, -0.05, prediction_text, fontsize=14, color=color, ha='center')
plt.ylim(bottom=0)

plt.legend()
st.pyplot(plt) 
