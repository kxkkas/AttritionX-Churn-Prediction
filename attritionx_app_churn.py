
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("customer_data.csv")

# Display basic statistics
print("Total Customers:", len(data))
print("Churned Customers:", data['Churn'].sum())
print("Active Customers:", len(data) - data['Churn'].sum())

# Pie chart for churn distribution
labels = ['Active', 'Churned']
sizes = [len(data) - data['Churn'].sum(), data['Churn'].sum()]
explode = (0, 0.1)
colors = ['lightgreen', 'lightcoral']

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Customer Churn Distribution')
plt.axis('equal')
plt.tight_layout()
plt.savefig("churn_pie_chart.png")
plt.show()

# Bar plot of churn vs features (example: Gender)
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', hue='Churn', data=data)
plt.title('Churn Count by Gender')
plt.savefig("churn_by_gender.png")
plt.show()
