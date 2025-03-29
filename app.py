import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Systemic Resilience Simulator", layout="centered")
st.title("🧩 Systemic Resilience Simulator")
st.subheader("Module G: Universal Basic Income & Work Redistribution")

st.markdown("""
This simulation estimates the social and economic effects of UBI (Universal Basic Income)
based on various monthly support levels. Explore how financial stability can reduce stress,
increase education participation, cut healthcare costs, and boost small business creation.
""")

ubi = st.slider("Select UBI per Adult per Month ($)", min_value=0, max_value=1500, step=100, value=1000)

ubi_levels = [0, 500, 1000, 1500]
societal_stress = [100, 75, 55, 40]
education_gain = [0, 10, 25, 40]
health_cost_reduction = [0, 5, 15, 25]
small_biz_growth = [0, 5, 12, 20]

def interpolate(x_vals, y_vals, x):
    for i in range(len(x_vals)-1):
        if x_vals[i] <= x <= x_vals[i+1]:
            ratio = (x - x_vals[i]) / (x_vals[i+1] - x_vals[i])
            return y_vals[i] + ratio * (y_vals[i+1] - y_vals[i])
    return y_vals[-1] if x >= x_vals[-1] else y_vals[0]

stress = interpolate(ubi_levels, societal_stress, ubi)
edu = interpolate(ubi_levels, education_gain, ubi)
health = interpolate(ubi_levels, health_cost_reduction, ubi)
biz = interpolate(ubi_levels, small_biz_growth, ubi)

col1, col2 = st.columns(2)
col1.metric("🧠 Stress Index (Lower is Better)", f"{stress:.1f}")
col1.metric("📚 Education Uptake (%)", f"{edu:.1f}%")
col2.metric("🏥 Health Cost Reduction", f"{health:.1f}%")
col2.metric("💼 Small Biz Growth", f"{biz:.1f}%")

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ubi_levels, societal_stress, label="Stress Index", marker='o')
ax.plot(ubi_levels, education_gain, label="Education Uptake", marker='o')
ax.plot(ubi_levels, health_cost_reduction, label="Health Cost Reduction", marker='o')
ax.plot(ubi_levels, small_biz_growth, label="Small Biz Growth", marker='o')
ax.set_xlabel("UBI per Month ($)")
ax.set_ylabel("Impact (%) or Index")
ax.set_title("Simulated Societal Impacts of UBI")
ax.grid(True)
ax.legend()
st.pyplot(fig)

with st.expander("📈 Mutual Prosperity Incentive (Why This Matters)"):
    st.markdown("""
    A system that rewards businesses for lifting the baseline, not just maximizing margins:
    - 📊 **Stable customers** mean more reliable revenue streams
    - 🏥 **Healthier communities** reduce insurance and absenteeism costs
    - 🎓 **Educated populations** improve workforce readiness
    - 💡 **Co-investment opportunities** in public innovation (green tech, care work, infrastructure)

    **Taking care of people = taking care of the economy.**
    """)