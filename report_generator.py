import os
import pandas as pd
import logging
import argparse

# Set up logging
def setup_logging(log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s')

# Load test results from CSV
def load_test_results(filepath):
    try:
        df = pd.read_csv(filepath)
        logging.info(f'Loaded test results from {filepath} successfully.')
        return df
    except Exception as e:
        logging.error(f'Failed to load test results: {e}')
        raise

# Generate the markdown report
def generate_report(df, report_path):
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    try:
        with open(report_path, 'w') as f:
            f.write("# Fluidic Process Test Report\n\n")
            f.write(f"Total tests performed: {len(df)}\n\n")
            for test_name in df['Test Name'].unique():
                subset = df[df['Test Name'] == test_name]
                passed = len(subset[subset['Status'] == 'PASS'])
                failed = len(subset[subset['Status'] == 'FAIL'])
                f.write(f"## {test_name}\n")
                f.write(f"- Passed: {passed}\n- Failed: {failed}\n\n")
            f.write("## See attached plot:\n![Measurement Plot](../results/measurement_plot.png)\n")
        logging.info(f'Report generated at {report_path}')
    except Exception as e:
        logging.error(f'Failed to generate report: {e}')
        raise

def generate_html_report(df, report_path):
    """Generate an HTML report from the test results DataFrame."""
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    try:
        html = ["<html><head><title>Fluidic Process Test Report</title></head><body>"]
        html.append("<h1>Fluidic Process Test Report</h1>")
        html.append(f"<p>Total tests performed: {len(df)}</p>")
        for test_name in df['Test Name'].unique():
            subset = df[df['Test Name'] == test_name]
            passed = len(subset[subset['Status'] == 'PASS'])
            failed = len(subset[subset['Status'] == 'FAIL'])
            html.append(f"<h2>{test_name}</h2>")
            html.append(f"<ul><li>Passed: {passed}</li><li>Failed: {failed}</li></ul>")
        html.append('<h2>See attached plot:</h2>')
        html.append('<img src="../results/measurement_plot.png" alt="Measurement Plot" style="max-width:600px;">')
        html.append("</body></html>")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html))
        logging.info(f'HTML report generated at {report_path}')
    except Exception as e:
        logging.error(f'Failed to generate HTML report: {e}')
        raise

def main():
    parser = argparse.ArgumentParser(description='Generate fluidic process test report.')
    parser.add_argument('--test-plan', type=str, default='results/test_results.csv',
                        help='Path to the test results CSV file (default: results/test_results.csv)')
    parser.add_argument('--format', type=str, default='md', choices=['md', 'html'],
                        help='Report format: md (Markdown) or html (HTML). Default is md.')
    args = parser.parse_args()

    setup_logging('results/report_log.txt')

    try:
        df = load_test_results(args.test_plan)
        if args.format == 'md':
            generate_report(df, 'reports/test_report.md')
        elif args.format == 'html':
            generate_html_report(df, 'reports/test_report.html')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
