import yaml
import pandas as pd
import numpy as np
import random
import logging

# Configure logging
logging.basicConfig(filename='results/test_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

try:
    # Load test plan
    with open('test_plan.yaml') as f:
        test_plan = yaml.safe_load(f)
    logging.info('Loaded test plan successfully.')
except Exception as e:
    logging.error(f'Failed to load test plan: {e}')
    raise

results = []

# Simulated experiment execution
for test in test_plan['tests']:
    for val in test['values']:
        try:
            measured = val + random.uniform(-5, 5)
            status = 'PASS' if test['expected_range'][0] <= measured <= test['expected_range'][1] else 'FAIL'
            results.append({
                'Test Name': test['name'],
                'Variable': test['variable'],
                'Set Value': val,
                'Measured Value': round(measured, 2),
                'Unit': test['units'],
                'Status': status
            })
            logging.info(f"{test['name']} | Set: {val} | Measured: {measured:.2f} | Status: {status}")
        except Exception as e:
            logging.error(f"Error during test '{test['name']}' at value {val}: {e}")
            continue

df = pd.DataFrame(results)
try:
    df.to_csv('results/test_results.csv', index=False)
    logging.info('Test results saved to results/test_results.csv')
except Exception as e:
    logging.error(f'Failed to save test results: {e}')

print(df)
