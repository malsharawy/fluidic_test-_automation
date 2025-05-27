import pandas as pd

df = pd.read_csv('results/test_results.csv')

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
