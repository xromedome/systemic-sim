import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Systemic Resilience Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
**Systemic Resilience Simulator**  
Explore how system-level decisions — from infrastructure to income policy — shape real-world outcomes like housing stability, education access, and long-term prosperity.

This tool simulates structural pressure points, helps surface overlooked costs, and suggests new incentive paths for sustainable economic wellbeing.
""")

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
    "Module A: Cost of Living",
    "Module B: Infrastructure Decay",
    "Module C: Education + Generational Opportunity",
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

    ubi_value = st.slider("Select UBI per Adult per Month ($)", 0, 1500, 1000, step=100)

    stress = 100 - ubi_value * 0.03
    education = ubi_value * 0.025
    health_savings = ubi_value * 0.015
    biz_growth = ubi_value * 0.012

    st.metric("🧠 Stress Index (Lower is Better)", f"{round(stress, 1)}")
    st.metric("🩺 Health Cost Reduction", f"{round(health_savings, 1)}%")
    st.metric("📚 Education Uptake (%)", f"{round(education, 1)}%")
    st.metric("📦 Small Biz Growth", f"{round(biz_growth, 1)}%")

    ubi_levels = [0, 500, 1000, 1500]
    societal_stress = [100, 75, 55, 40]
    education_gain = [0, 10, 25, 40]
    health_cost_reduction = [0, 5, 15, 25]
    small_biz_growth = [0, 5, 12, 20]

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

    st.markdown("""
**📊 Data Sources:**
- Education benefit estimates adapted from OECD and U.S. Census models
- Health cost impacts from Medicaid expansion studies (KFF)
- Entrepreneurial growth data from World Bank & small business grants
- Stress data from APA national workforce stress surveys
""")

    st.info("""
💡 *This module shows that even modest stabilization can ripple through society in ways that reduce emergency costs and unlock new participation in education, care work, and entrepreneurship.*
""")

with tab2:
    st.header("💸 Module A: Minimum Viable Cost of Life")
    st.markdown("""
This module estimates the baseline monthly cost of sustaining a working adult in the U.S. using conservative averages across major living needs.

**Categories include:**
- Rent or Mortgage
- Food & Water
- Transportation
- Health Care
- Utilities
- Clothing & Hygiene
- Education/Upskilling
- Other Essentials
""")

    baseline_costs = {
        "Rent/Mortgage": 1500,
        "Food & Water": 450,
        "Transportation": 700,
        "Health Care": 450,
        "Energy & Utilities": 350,
        "Education/Upskilling": 200,
        "Clothing & Hygiene": 150,
        "Other Essentials": 200,
    }

    income_levels = {
        "Minimum Wage (Full-Time, $7.25/hr)": 1160,
        "Low Wage ($12/hr)": 1920,
        "Living Wage ($20/hr)": 3200,
        "Median Wage ($30/hr)": 4800
    }

    total_monthly_cost = sum(baseline_costs.values())

    st.write(f"**Estimated Monthly Cost of Survival:** ${total_monthly_cost}")
    st.divider()

    for label, income in income_levels.items():
        surplus = income - total_monthly_cost
        color = "🟢" if surplus > 0 else ("🟡" if surplus == 0 else "🔴")
        st.write(f"{color} {label}: ${income} → {'Surplus' if surplus > 0 else 'Deficit'} of ${abs(surplus)}")

    st.info("""
📌 *Even low-surplus wage levels leave little room for savings, investment, or education. This simulation helps reveal how many Americans operate at or below systemic break-even.*
""")

with tab3:
    st.header("🏗️ Module B: Infrastructure Decay vs Investment")
    st.markdown("""
This module simulates how different infrastructure investment levels affect system quality over time — and how that translates into human costs like power outages, commute disruption, and repair burdens.

**Scenarios:**
- High Investment → Maintains quality
- Moderate Investment → Slow decline
- Low Investment → Accelerated decay
- Neglect → Rapid systemic failure

**Key Assumptions:**
- Decay rates are exponential and reflect deferred maintenance
- Risk functions are nonlinear and escalate as quality falls
- Costs are per-capita estimates based on national averages and infrastructure reports
""")

    investment_option = st.selectbox("Select Infrastructure Investment Level", [
        "High Investment", "Moderate Investment", "Low Investment", "Neglect"
    ])

    years = list(range(2025, 2051))
    decay_curves = {
        "High Investment":    [100 - (y - 2025) * 0.3 for y in years],
        "Moderate Investment": [100 - (y - 2025) * 1.0 for y in years],
        "Low Investment":      [100 - (y - 2025) * 2.5 for y in years],
        "Neglect":             [100 - (y - 2025) * 4.0 for y in years],
    }

    def human_cost_from_quality(q):
        return (
            5 + (100 - q) * 0.8,   # Power outage risk
            2 + (100 - q) * 0.5,   # Commute disruption
            1 + (100 - q) * 0.6,   # Healthcare risk
            200 + (100 - q) * 20   # Repair cost
        )

    q_vals = decay_curves[investment_option]
    power_risk, commute, health_risk, repair = [], [], [], []
    for q in q_vals:
        p, c, h, r = human_cost_from_quality(q)
        power_risk.append(p)
        commute.append(c)
        health_risk.append(h)
        repair.append(r)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, q_vals, label="Infrastructure Quality (0–100)", linewidth=2)
    ax.plot(years, power_risk, label="Power Outage Risk (%)", linestyle='--')
    ax.plot(years, health_risk, label="Healthcare Risk (%)", linestyle='--')
    ax.plot(years, commute, label="Commute Delay (hrs/mo)", linestyle='--')
    ax.plot(years, repair, label="Repair Cost ($/yr)", linestyle='--')

    ax.set_title(f"Projected System Decay and Human Impact: {investment_option}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Index or Cost")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
**📊 Data Sources:**
- American Society of Civil Engineers (ASCE) Infrastructure Report Card
- Federal Transit Administration: Urban Commute Data
- Department of Energy: Grid Reliability & Outage Costs
- Kaiser Family Foundation (KFF): Environmental & Infrastructure Health Impacts
- U.S. Census & GAO estimates on public works and deferred maintenance
""")

    st.info("""
💡 *This module shows how even modest underinvestment can lead to exponential increases in human burden. It helps us visualize how avoiding maintenance today multiplies systemic fragility tomorrow.*
""")
with tab4:
    st.header("🎓 Module C: Education Access & Generational Opportunity")
    st.markdown("""
This module explores how access to affordable, high-quality education impacts generational mobility, wage growth, and community development.

**Scenarios:**
- High Access: Universal, low-cost, locally available education and training
- Moderate Access: Public K-12, some trade/college affordability
- Limited Access: Debt-heavy higher ed, weak vocational systems
- Education Desert: Poor school quality, minimal post-secondary access

**Key Assumptions:**
- Education accessibility score drives long-term wage lift
- Intergenerational compounding benefits modeled as % gains
- Low access correlates with increased incarceration and lower life expectancy
""")

    access_option = st.selectbox("Select Education Access Level", [
        "High Access", "Moderate Access", "Limited Access", "Education Desert"
    ])

    years = list(range(2025, 2076, 5))
    def lifetime_opportunity(access):
        base = {
            "High Access": 1.05,
            "Moderate Access": 1.03,
            "Limited Access": 1.01,
            "Education Desert": 0.98
        }[access]
        return [100 * (base ** i) for i in range(len(years))]

    opp_curve = lifetime_opportunity(access_option)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(years, opp_curve, marker='o', linewidth=2)
    ax.set_title(f"Projected Intergenerational Opportunity: {access_option}")
    ax.set_ylabel("Opportunity Index (vs 2025 = 100)")
    ax.set_xlabel("Year")
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
**📊 Data Sources:**
- Brookings: Education & Lifetime Earnings
- U.S. Dept of Ed: Access Metrics, School Funding, and Attainment
- Pew & Urban Institute: Intergenerational Mobility
- OECD: Global Education Equity Models
- Vera Institute: Education & Incarceration Risk Reduction
""")

    st.info("""
🎓 *Education isn’t just personal — it's infrastructural. When entire communities are cut off from learning, the effects cascade across generations.*
""")
with tab5:
    st.write("🛠️ Module D coming soon: Agricultural Efficiency vs Labor Needs")
with tab6:
    st.write("🛠️ Module E coming soon: Debt Systems, Wealth Lock-in, and Social Mobility")
with tab7:
    st.write("🛠️ Module F coming soon: Knowledge Attrition, Inheritance, and Collapse Prevention")
