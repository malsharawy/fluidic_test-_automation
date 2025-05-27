import pandas as pd
import logging

logging.basicConfig(filename='results/report_log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

try:
    df = pd.read_csv('results/test_results.csv')
    logging.info('Loaded test results successfully.')
except Exception as e:
    logging.error(f'Failed to load test results: {e}')
    raise

try:
    with open('reports/test_report.md', 'w') as f:
        f.write("# Fluidic Process Test Report\n\n")
        f.write(f"Total tests performed: {len(df)}\n\n")
        for test_name in df['Test Name'].unique():
            subset = df[df['Test Name'] == test_name]
            passed = len(subset[subset['Status'] == 'PASS'])
            failed = len(subset[subset['Status'] == 'FAIL'])
            f.write(f"## {test_name}\n")
            f.write(f"- Passed: {passed}\n- Failed: {failed}\n\n")
        f.write("## See attached plot:\n![Measurement Plot](../results/measurement_plot.png)\n")
    logging.info('Report generated at reports/test_report.md')
except Exception as e:
    logging.error(f'Failed to generate report: {e}')
