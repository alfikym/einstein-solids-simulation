import numpy as np
import matplotlib.pyplot as plt
from math import comb
import streamlit as st

def multiplicity(q, N):
    """
    Calculate the multiplicity of an Einstein solid.
    Arguments:
    q -- number of energy quanta
    N -- number of oscillators
    """
    if q < 0 or N <= 0:
        raise ValueError("Number of quanta must be non-negative and number of oscillators must be positive.")
    return comb(q + N - 1, q)

# Streamlit UI
st.title("Total Multiplicity of Two Interacting Einstein Solids")
st.write("Use the sliders below to adjust the parameters and visualize the total multiplicity of two interacting Einstein solids.")

# Sliders for input
q_total = st.slider("Total Number of Quanta (q)", min_value=1, max_value=100, value=20, step=1)
N_A = st.slider("Number of Oscillators in Solid A (N_A)", min_value=1, max_value=300, value=10, step=1)
N_B = st.slider("Number of Oscillators in Solid B (N_B)", min_value=1, max_value=300, value=10, step=1)

# Calculate multiplicities
q_A_values = np.arange(0, q_total + 1)
multiplicities = [multiplicity(q_A, N_A) * multiplicity(q_total - q_A, N_B) for q_A in q_A_values]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(q_A_values, multiplicities, color='b', alpha=0.7)
ax.set_xlabel('Energy of Solid A (q_A)')
ax.set_ylabel('Total Multiplicity (Omega_Total)')
ax.set_title('Total Multiplicity of Two Interacting Einstein Solids')
ax.grid(True, linestyle='--', alpha=0.5)

# Display plot in Streamlit
st.pyplot(fig)
