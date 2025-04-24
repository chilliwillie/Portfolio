
# Smart Energy Manager

This project simulates a household energy management system using Python classes. It calculates energy consumption from appliances, energy generation from solar panels, and evaluates overall savings and usage metrics. The results are also visualized using pandas and matplotlib.

## 🔧 Features

- Track multiple appliances (name, power usage, daily hours)
- Track multiple solar panels (output watts, daily sun hours)
- Compute:
  - Daily kWh consumption
  - Monthly cost for appliances
  - Daily solar generation
  - Monthly savings from solar panels
  - Net energy and cost balance
- Visualize:
  - Bar chart of daily usage per appliance

## 🧪 Tools Used

- Python (classes, loops, lists)
- pandas
- matplotlib

## 🚀 How to Use

1. Clone the repo.
2. Run the script in any Python environment.
3. Modify the list of appliances and panels to match your use case.
4. Outputs include printed summaries, pandas DataFrames, and plots.

---

## 📁 Code

```

import pandas as pd
import matplotlib.pyplot as plt

class Appliance:
    def __init__(self, name, watts, hours_per_day):
        self.name = name
        self.watts = watts
        self.hours_per_day = hours_per_day

    def daily_usage(self):
        return (self.watts * self.hours_per_day) / 1000

    def cost(self, price_per_kwh):
        return price_per_kwh * self.daily_usage() * 30

class SolarPanel:
    def __init__(self, panel_id, watts, sun_hours):
        self.panel_id = panel_id
        self.watts = watts
        self.sun_hours = sun_hours

    def daily_generation(self):
        return (self.watts * self.sun_hours) / 1000

    def monthly_generation(self):
        return self.daily_generation() * 30

    def savings(self, price_per_kwh):
        return price_per_kwh * self.monthly_generation()

class Home:
    def __init__(self, appliances, panels):
        self.appliances = appliances
        self.panels = panels

    def total_usage(self):
        return sum([a.daily_usage() for a in self.appliances])

    def total_generation(self):
        return sum([p.daily_generation() for p in self.panels])

    def net_energy(self):
        return self.total_generation() - self.total_usage()

    def net_savings(self, price_per_kwh):
        total_cost = sum([a.cost(price_per_kwh) for a in self.appliances])
        total_savings = sum([p.savings(price_per_kwh) for p in self.panels])
        return total_savings - total_cost

# Example data
appliances = [
    Appliance('Fan', 10, 8),
    Appliance('Fridge', 150, 24),
    Appliance('Light', 5, 12)
]

panels = [
    SolarPanel('SP1', 300, 8),
    SolarPanel('SP2', 400, 6),
    SolarPanel('SP3', 250, 7)
]

home = Home(appliances, panels)

# Print summary
print("----- Home Energy Summary -----")
print("Total Daily Usage:", home.total_usage(), "kWh")
print("Total Daily Generation:", home.total_generation(), "kWh")
print("Net Daily Energy:", home.net_energy(), "kWh")
print("Net Monthly Savings at 0.22 €/kWh:", home.net_savings(0.22), "€")

# Create DataFrames
appliance_df = pd.DataFrame({
    "Appliance": [a.name for a in appliances],
    "Watts": [a.watts for a in appliances],
    "Hours/Day": [a.hours_per_day for a in appliances],
    "Daily kWh": [a.daily_usage() for a in appliances],
    "Monthly Cost (€)": [a.cost(0.22) for a in appliances]
})

panel_df = pd.DataFrame({
    "Panel ID": [p.panel_id for p in panels],
    "Watts": [p.watts for p in panels],
    "Sun Hours": [p.sun_hours for p in panels],
    "Daily Generation (kWh)": [p.daily_generation() for p in panels],
    "Monthly Savings (€)": [p.savings(0.22) for p in panels]
})

# Show data
print(appliance_df)
print(panel_df)

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(appliance_df["Appliance"], appliance_df["Daily kWh"], color="skyblue")
plt.title("Daily Energy Use by Appliance")
plt.xlabel("Appliance")
plt.ylabel("Daily kWh")
plt.grid(True)
plt.tight_layout()
plt.show()

```