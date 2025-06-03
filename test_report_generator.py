import unittest
import pandas as pd
import os
from report_generator import load_test_results, generate_report

# Unit tests for the report generator module
class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame and test file paths for use in tests
        self.df = pd.DataFrame({
            'Test Name': ['Test A', 'Test A', 'Test B'],
            'Status': ['PASS', 'FAIL', 'PASS'],
            'Set Value': [1, 2, 3],
            'Measured Value': [1.1, 1.9, 3.0],
            'Unit': ['unit', 'unit', 'unit']
        })
        self.test_report_path = 'reports/test_report_unittest.md'
        os.makedirs('reports', exist_ok=True)

    def test_load_test_results_valid(self):
        # Test that load_test_results correctly loads a valid CSV file
        test_csv = 'results/test_results_unittest.csv'
        os.makedirs('results', exist_ok=True)
        self.df.to_csv(test_csv, index=False)
        df_loaded = load_test_results(test_csv)
        self.assertEqual(len(df_loaded), 3)  # Should load 3 rows
        self.assertIn('Test Name', df_loaded.columns)  # Should have 'Test Name' column

    def test_generate_report(self):
        # Test that generate_report creates a markdown report with expected content
        generate_report(self.df, self.test_report_path)
        self.assertTrue(os.path.exists(self.test_report_path))  # Report file should exist
        with open(self.test_report_path, 'r') as f:
            content = f.read()
            self.assertIn('Fluidic Process Test Report', content)  # Report title present
            self.assertIn('Test A', content)  # Test names present
            self.assertIn('Test B', content)

    def tearDown(self):
        # Clean up any files created during tests
        if os.path.exists(self.test_report_path):
            os.remove(self.test_report_path)
        test_csv = 'results/test_results_unittest.csv'
        if os.path.exists(test_csv):
            os.remove(test_csv)

if __name__ == '__main__':
    unittest.main()
