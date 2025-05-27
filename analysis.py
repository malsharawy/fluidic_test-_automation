import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(filename='results/analysis_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

try:
    df = pd.read_csv('results/test_results.csv')
    logging.info('Loaded test results successfully.')
except Exception as e:
    logging.error(f'Failed to load test results: {e}')
    raise

try:
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Set Value', y='Measured Value', hue='Test Name')
    plt.title('Fluidic Test Measurements')
    plt.savefig('results/measurement_plot.png')
    plt.show()
    logging.info('Measurement plot saved to results/measurement_plot.png')
except Exception as e:
    logging.error(f'Error during plotting: {e}')

try:
    print(df.groupby(['Test Name', 'Status']).size())
    logging.info('Printed test summary by Test Name and Status.')
except Exception as e:
    logging.error(f'Error during summary print: {e}')
