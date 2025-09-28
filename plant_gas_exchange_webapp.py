import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Plant Gas Exchange Simulation", layout="centered")
st.title("🌿 Plant Gas Exchange Simulation")
st.markdown("""
This interactive simulation shows how plants release or absorb gases under different conditions.
Select the environment, light intensity, and duration to observe the net change in Oxygen (O₂) and Carbon Dioxide (CO₂).
""")

environment = st.selectbox("Environment", ["Light", "Dark"])
light_intensity = st.selectbox("Light Intensity", ["Low", "Medium", "High"])
duration = st.slider("Duration (hours)", 1, 6, 1)

def simulate_gas_exchange(env, intensity, hours):
    if env == "Light":
        intensity_factor = {"Low": 2, "Medium": 4, "High": 6}[intensity]
        oxygen_change = intensity_factor * hours
        co2_change = -intensity_factor * 0.6 * hours
    else:
        oxygen_change = -2 * hours
        co2_change = 4 * hours
    return oxygen_change, co2_change

oxygen, co2 = simulate_gas_exchange(environment, light_intensity, duration)

st.subheader("Simulation Results")
st.write(f"**Oxygen (O₂) Net Change:** {oxygen:.1f}")
st.write(f"**Carbon Dioxide (CO₂) Net Change:** {co2:.1f}")

fig, ax = plt.subplots()
gases = ['Oxygen (O₂)', 'Carbon Dioxide (CO₂)']
values = [oxygen, co2]
colors = ['green' if v >= 0 else 'red' for v in values]
ax.bar(gases, values, color=colors)
ax.set_ylabel("Net Change")
ax.set_title("Gas Exchange Result")
st.pyplot(fig)

st.markdown("---")
st.markdown("Designed for middle school science education. 🌱")
