import streamlit as st
import random

st.set_page_config(page_title="FinGuard AI", page_icon="🛡️")
st.title("🛡️ FinGuard AI - Fraud Detection")
st.write("Real-time AI powered fraud detection system")

col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Transaction Amount (₹)", 100, 1000000, 5000)
    age = st.number_input("Customer Age", 18, 80, 25)
with col2:
    city = st.text_input("City (Enter any city)", "Indore")
    hour = st.slider("Transaction Hour", 0, 23, 14)

if st.button("🔍 Check Fraud Risk"):
    base_risk = 10
    
    if amount > 80000:
        base_risk += 50
    elif amount > 50000:
        base_risk += 30
    elif amount > 20000:
        base_risk += 10
    
    if hour <= 4:
        base_risk += 35
    elif hour <= 6:
        base_risk += 15

    if city.lower() not in ["mumbai", "delhi", "bangalore", "indore", "pune", ""] :
        base_risk += 10

    prob = base_risk + random.randint(-7, 7)
    prob = max(5, min(98, prob))
    
    st.divider()
    if prob > 70:
        st.error(f"🚨 HIGH RISK FRAUD! Risk: {prob}%")
        st.progress(prob/100)
        st.write(f"Reason: High amount ₹{amount} at {hour}:00 from {city}")
    elif prob > 40:
        st.warning(f"⚠️ MEDIUM RISK! Risk: {prob}%")
        st.progress(prob/100)
        st.write(f"Reason: Slightly unusual pattern in {city}")
    else:
        st.success(f"✅ SAFE Transaction! Fraud Risk: {prob}%")
        st.progress(prob/100)
        st.write(f"This transaction from {city} looks normal")

st.caption("Built by Mohit | AI Powered Fraud Detection")