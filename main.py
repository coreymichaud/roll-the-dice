import streamlit as st

# Pages

# General
home = st.Page("views/general/home.py", title = "Home")
model_selector = st.Page("views/general/model_selector.py", title = "Model Selector")
resources = st.Page("views/general/resources.py", title = "Resources")

# Random Formulas
summary_statistics = st.Page("views/random_formulas/summary_statistics.py", title = "Summary Statistics")

# Probability Distributions
normal_distribution = st.Page("views/probability_distributions/normal_distribution.py", title = "Normal Distribution")

# Analysis of Variance
one_way_anova = st.Page("views/anova/one_way_anova.py", title = "One Way ANOVA")

# Hypothesis Tests
binomial_test = st.Page("views/hypothesis_tests/binomial_test.py", title = "Binomial Test")

# Confidence Intervals
t_test = st.Page("views/confidence_intervals/t_test.py", title = "t-Test")

# Navigation
pg = st.navigation({
                   "🌐 General": [home, model_selector, resources],
                   "🧮 Random Formulas": [summary_statistics],
                   "🌊 Probability Distributions": [normal_distribution],
                   "🌌 Analysis of Variance": [one_way_anova],
                   "🧠 Hypothesis Tests": [binomial_test],
                   "💡 Confidence Intervals": [t_test],
                   })

# Page config
st.set_page_config(page_title = "Roll The Dice", page_icon = "🎲")

# Run app
pg.run()