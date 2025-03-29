import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Systemic Resilience Simulator", layout="wide")

st.title("🧠 Systemic Resilience Simulator")

# Intro Section
st.markdown("""
> **What does it really cost to be alive in modern society?**
>
> This interactive tool explores the hidden strain on individuals and communities — from housing, food, and transportation, to decaying infrastructure and underfunded education. Instead of assigning blame, we use data-driven models to ask:
>
> **What if we restructured society to reduce suffering and unlock human potential for everyone?**

**This simulator lets you:**
- Estimate the minimum viable cost of living
- See how infrastructure investments affect human outcomes
- Explore the economic ripple effects of supporting non-working populations
- Test reforms like income stabilization and public investment incentives

**Our goal:** To inspire citizens, policymakers, and businesses to reimagine prosperity — not just as GDP, but as shared human flourishing.

🛠️ _Taking care of people is not a burden — it's the engine of a stable and thriving society._
""")

# Tabs for different modules
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Module G: Stability & Redistribution",
    "Module A: Cost of Living (Coming Soon)",
    "Module B: Infrastructure Decay (Coming Soon)",
    "Module C: Education + Generational Opportunity (Coming Soon)",
    "Module D: Food System Capacity (Coming Soon)",
    "Module E: Debt + Wealth Lock-in (Coming Soon)",
    "Module F: Knowledge Attrition (Coming Soon)"
])

with tab1:
    st.header("📊 Stability & Work Redistribution")
    st.markdown("""
This module simulates the effects of income stabilization on societal stress, economic participation,
and long-term productivity. It explores how supporting non-working populations can lead to net gains
in innovation, health, education, and economic resilience.

**Key assumptions:**
- Stabilization amount per adult per month
- Reduction in healthcare/emergency costs
- Increase in education participation and small business creation
- Corporate gains from healthier, more creative society
""")

    st.markdown("""
**📊 Data Sources:**
- Education benefit estimates adapted from OECD and U.S. Census models
- Health cost impacts from Medicaid expansion studies (KFF)
- Entrepreneurial growth data from World Bank & small business grants
- Stress data from APA national workforce stress surveys
""")

    ubi_levels = [0, 500, 1000, 1500]
    societal_stress = [100, 75, 55, 40]  # Index (lower is better)
    education_gain = [0, 10, 25, 40]     # % increase
    health_cost_reduction = [0, 5, 15, 25]  # % reduction
    small_biz_growth = [0, 5, 12, 20]    # % growth

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(ubi_levels, societal_stress, marker='o', label="Societal Stress Index (↓ good)")
    ax.plot(ubi_levels, education_gain, marker='o', label="Education Participation (%)")
    ax.plot(ubi_levels, health_cost_reduction, marker='o', label="Emergency Health Cost Reduction (%)")
    ax.plot(ubi_levels, small_biz_growth, marker='o', label="Small Business Growth (%)")

    ax.set_title("Impacts of Monthly Stability Support on Social & Economic Health")
    ax.set_xlabel("Monthly Stabilization Amount per Adult ($)")
    ax.set_ylabel("Systemic Outcomes (% or Index)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.info("""
💡 *This module shows that even modest stabilization can ripple through society in ways that reduce emergency costs and unlock new participation in education, care work, and entrepreneurship.*
""")

with tab2:
    st.write("🛠️ Module A coming soon: Minimum Viable Cost of Life Simulator")
with tab3:
    st.write("🛠️ Module B coming soon: Infrastructure Investment vs Decay")
with tab4:
    st.write("🛠️ Module C coming soon: Education Access and Generational Outcomes")
with tab5:
    st.write("🛠️ Module D coming soon: Agricultural Efficiency vs Labor Needs")
with tab6:
    st.write("🛠️ Module E coming soon: Debt Systems, Wealth Lock-in, and Social Mobility")
with tab7:
    st.write("🛠️ Module F coming soon: Knowledge Attrition, Inheritance, and Collapse Prevention")
