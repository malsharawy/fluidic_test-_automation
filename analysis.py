import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('results/test_results.csv')

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Set Value', y='Measured Value', hue='Test Name')
plt.title('Fluidic Test Measurements')
plt.savefig('results/measurement_plot.png')
plt.show()

print(df.groupby(['Test Name', 'Status']).size())
