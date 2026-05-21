import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
asdasdasda
# Population dynamics simulation
def logistic_growth(t, P0, r, K):
    """
    Logistic population growth model
    P(t) = K / (1 + ((K - P0) / P0) * e^(-r*t))
    
    Parameters:
    t: time
    P0: initial population
    r: intrinsic growth rate
    K: carrying capacity
    """
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

def exponential_growth(t, P0, r):
    """Exponential population growth"""
    return P0 * np.exp(r * t)

# Create figure with subplots
fig = plt.figure(figsize=(15, 12))

# ============ SUBPLOT 1: Logistic Growth ============
ax1 = plt.subplot(2, 3, 1)
time = np.linspace(0, 50, 500)
P0 = 100  # Initial population
r = 0.15  # Growth rate
K = 10000  # Carrying capacity

population = logistic_growth(time, P0, r, K)
ax1.plot(time, population, 'b-', linewidth=2.5, label='Population')
ax1.axhline(y=K, color='r', linestyle='--', linewidth=2, label=f'Carrying Capacity (K={K})')
ax1.fill_between(time, 0, population, alpha=0.3)
ax1.set_xlabel('Time (years)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Population', fontsize=11, fontweight='bold')
ax1.set_title('Logistic Growth Model', fontsize=12, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()

# ============ SUBPLOT 2: Exponential vs Logistic ============
ax2 = plt.subplot(2, 3, 2)
exp_pop = exponential_growth(time[:200], P0, 0.1)
log_pop = logistic_growth(time, P0, 0.15, K)

ax2.plot(time[:200], exp_pop, 'r-', linewidth=2.5, label='Exponential Growth')
ax2.plot(time, log_pop, 'b-', linewidth=2.5, label='Logistic Growth (K=10000)')
ax2.set_xlabel('Time (years)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Population', fontsize=11, fontweight='bold')
ax2.set_title('Growth Models Comparison', fontsize=12, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_ylim([0, 12000])

# ============ SUBPLOT 3: Different Growth Rates ============
ax3 = plt.subplot(2, 3, 3)
growth_rates = [0.05, 0.10, 0.15, 0.20]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

for rate, color in zip(growth_rates, colors):
    pop = logistic_growth(time, P0, rate, K)
    ax3.plot(time, pop, linewidth=2.5, label=f'r={rate}', color=color)

ax3.axhline(y=K, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
ax3.set_xlabel('Time (years)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Population', fontsize=11, fontweight='bold')
ax3.set_title('Effect of Growth Rate (r)', fontsize=12, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)

# ============ SUBPLOT 4: Population Age Distribution ============
ax4 = plt.subplot(2, 3, 4)
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']
population_dist = [1800, 1200, 3500, 1200, 1300]
colors_dist = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#96CEB4']

bars = ax4.bar(age_groups, population_dist, color=colors_dist, edgecolor='black', linewidth=1.5)
ax4.set_ylabel('Population (millions)', fontsize=11, fontweight='bold')
ax4.set_title('Age Distribution', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}M',
             ha='center', va='bottom', fontweight='bold')

# ============ SUBPLOT 5: Birth and Death Rates ============
ax5 = plt.subplot(2, 3, 5)
time_bd = np.linspace(0, 50, 500)
birth_rate = 25 - 0.2 * time_bd  # Declining birth rate
death_rate = 10 + 0.1 * time_bd  # Rising death rate

ax5.plot(time_bd, birth_rate, 'g-', linewidth=2.5, label='Birth Rate', marker='o', markersize=3, markevery=20)
ax5.plot(time_bd, death_rate, 'r-', linewidth=2.5, label='Death Rate', marker='s', markersize=3, markevery=20)
ax5.fill_between(time_bd, death_rate, birth_rate, alpha=0.2, color='blue')
ax5.set_xlabel('Time (years)', fontsize=11, fontweight='bold')
ax5.set_ylabel('Rate (per 1000)', fontsize=11, fontweight='bold')
ax5.set_title('Birth vs Death Rates Over Time', fontsize=12, fontweight='bold')
ax5.legend()
ax5.grid(True, alpha=0.3)
ax5.set_ylim([5, 30])

# ============ SUBPLOT 6: Population Projection ============
ax6 = plt.subplot(2, 3, 6)
years = np.array([2000, 2010, 2020, 2030, 2040, 2050, 2060])
population_hist = np.array([6.1, 6.8, 7.8, 8.5, 9.0, 9.2, 9.1])
population_future = np.array([8.5, 9.0, 9.2, 9.1, 8.8, 8.5])
years_future = np.array([2030, 2040, 2050, 2060, 2070, 2080])

ax6.plot(years, population_hist, 'bo-', linewidth=2.5, markersize=8, label='Historical Data')
ax6.plot(years_future, population_future, 'r--s', linewidth=2.5, markersize=8, label='Projected (Low Fertility)')
ax6.axvline(x=2020, color='gray', linestyle=':', alpha=0.7, linewidth=2)
ax6.fill_between(years, 0, population_hist, alpha=0.2, color='blue')
ax6.fill_between(years_future, 0, population_future, alpha=0.2, color='red')
ax6.set_xlabel('Year', fontsize=11, fontweight='bold')
ax6.set_ylabel('Population (Billions)', fontsize=11, fontweight='bold')
ax6.set_title('World Population Projection', fontsize=12, fontweight='bold')
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_ylim([5, 10])

# Main title
fig.suptitle('Population Dynamics Analysis', fontsize=16, fontweight='bold', y=0.995)

plt.tight_layout()
plt.savefig('population_plot.png', dpi=300, bbox_inches='tight')
print("✓ Population plot saved as 'population_plot.png'")

plt.show()

# Print statistics
print("\n" + "="*60)
print("POPULATION DYNAMICS STATISTICS")
print("="*60)
print(f"\nLogistic Growth Model (P0={P0}, r=0.15, K={K}):")
print(f"  Time to reach 50% of carrying capacity: {np.argmax(population >= K/2) * 50/500:.1f} years")
print(f"  Time to reach 90% of carrying capacity: {np.argmax(population >= 0.9*K) * 50/500:.1f} years")
print(f"  Final population: {population[-1]:.0f}")
print(f"\nExponential Growth (first 10 years):")
print(f"  Initial population: {P0}")
print(f"  Population after 10 years: {exponential_growth(10, P0, 0.1):.0f}")
print(f"  Doubling time: {np.log(2) / 0.1:.1f} years")
print(f"\nGlobal Population Data:")
print(f"  Current (2020): 7.8 billion")
print(f"  Projected (2050): 9.2 billion (+18.0%)")
print(f"  Projected (2080): 8.5 billion (-7.7%)")
print("="*60)
