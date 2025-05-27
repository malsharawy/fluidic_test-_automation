import yaml
import pandas as pd
import numpy as np
import random

# Load test plan
with open('test_plan.yaml') as f:
    test_plan = yaml.safe_load(f)

results = []

# Simulated experiment execution
for test in test_plan['tests']:
    for val in test['values']:
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

df = pd.DataFrame(results)
df.to_csv('results/test_results.csv', index=False)
print(df)
