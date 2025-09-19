import streamlit as st
import pandas as pd

st.title("📊 Forex Trading Analytics Dashboard")

# store trades for your session
if "trades" not in st.session_state:
    st.session_state.trades = []

with st.form("trade_form"):
    date = st.date_input("Date")
    trader = st.text_input("Trader")
    instrument = st.text_input("Instrument")
    entry = st.number_input("Entry Price", format="%.4f")
    sl = st.number_input("Stop Loss", format="%.4f")
    target = st.number_input("Target Price", format="%.4f")
    outcome = st.selectbox("Outcome", ["Win", "Loss", "Break-even"])
    result = st.selectbox("Result", ["Profit", "Loss"])
    submitted = st.form_submit_button("Add Trade")
    if submitted:
        st.session_state.trades.append({
            "Date": date,
            "Trader": trader,
            "Instrument": instrument,
            "Entry": entry,
            "SL": sl,
            "Target": target,
            "Outcome": outcome,
            "Result": result
        })

df = pd.DataFrame(st.session_state.trades)
st.write("### Trades Table")
st.dataframe(df)

if not df.empty:
    st.write("### Profit vs Loss")
    st.bar_chart(df["Result"].value_counts())
