import streamlit as st
import pandas as pd

st.set_page_config(page_title="Forex Trading Analytics Dashboard", layout="wide")

# ---- Sidebar ----
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Dashboard", "Settings"])

if menu == "Dashboard":
    st.title("📊 Forex Trading Analytics Dashboard")

    # ---- Top Cards ----
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Trades", "124", "↑ 8")
    col2.metric("Win Rate", "65%", "↑ 2%")
    col3.metric("Avg Profit", "$342", "↑ $15")
    col4.metric("Loss Rate", "35%", "↓ 2%")

    st.markdown("---")

    # ---- Instruments with Hover Suggestions ----
    st.subheader("💹 Instruments")
    st.caption("Hover to see suggestions (example only)")
    with st.expander("Instrument List & Suggestions"):
        st.write(
            """
            - **EUR/USD** – click to trade  
            - **GBP/USD** – suggested range strategy  
            - **USD/JPY** – momentum signals active  
            - **XAU/USD** – watch for breakout
            """
        )

    # ---- Recent Trades Table ----
    st.subheader("📒 Recent Trades")
    trade_data = pd.DataFrame(
        {
            "Instrument": ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"],
            "Direction": ["Buy", "Sell", "Buy", "Sell"],
            "Entry Price": [1.0932, 1.2710, 149.50, 1928.3],
            "Exit Price": [1.0970, 1.2650, 150.05, 1912.4],
            "P/L ($)": [380, -420, 550, -260],
        }
    )
    st.dataframe(trade_data, use_container_width=True)

    # ---- Notes / Comments ----
    st.subheader("📝 Trader Notes")
    st.text_area("Write your observations here:")

elif menu == "Settings":
    st.title("⚙️ Settings")
    st.write("Adjust user preferences here.")
    st.slider("Refresh Rate (seconds)", 5, 60, 15)
    st.color_picker("Theme Color", "#2c3e50")
