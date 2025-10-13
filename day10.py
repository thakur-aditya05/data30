import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "sales": [1200, 1500, 1800, 2200, 2100, 2400, 2600, 2500, 2300, 2000, 1800, 1600]
}
df = pd.DataFrame(data)

# If month is string, plotting is fine; 
# optionally sort by month order or convert to categorical with correct order.

plt.figure(figsize=(10, 6))

plt.plot(df["month"], df["sales"], marker='o', linestyle='-', color='b', linewidth=2)

# Customizing title and axis labels
plt.title("Monthly Sales Growth", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=14)
plt.ylabel("Sales (in USD)", fontsize=14)

# Customize x-ticks (rotate if many months so labels don’t overlap)
# plt.xticks(rotation=45)

# Optionally add grid
plt.grid(True, linestyle='--', alpha=0.5)

# Optionally annotate data points
for x, y in zip(df["month"], df["sales"]):
    plt.text(x, y + 50, str(y), ha='center', fontsize=10)

plt.tight_layout()  # To avoid clipping of labels
plt.show()
