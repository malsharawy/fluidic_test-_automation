import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
from report_generator import setup_logging, load_test_results, generate_report, generate_html_report

def run_report(test_plan_path, report_format):
    setup_logging('results/report_log.txt')
    try:
        df = load_test_results(test_plan_path)
        if report_format == 'md':
            generate_report(df, 'reports/test_report.md')
        elif report_format == 'html':
            generate_html_report(df, 'reports/test_report.html')
        return True, f"Report generated in 'reports/' as {report_format.upper()}"
    except Exception as e:
        return False, str(e)

def browse_file(entry):
    filename = filedialog.askopenfilename(
        title='Select Test Results CSV',
        filetypes=[('CSV Files', '*.csv'), ('All Files', '*.*')]
    )
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def main():
    root = tk.Tk()
    root.title('Fluidic Test Report Generator')
    root.geometry('400x200')

    tk.Label(root, text='Test Results CSV:').pack(pady=(10,0))
    file_frame = tk.Frame(root)
    file_frame.pack()
    entry = tk.Entry(file_frame, width=40)
    entry.pack(side=tk.LEFT, padx=5)
    tk.Button(file_frame, text='Browse', command=lambda: browse_file(entry)).pack(side=tk.LEFT)

    tk.Label(root, text='Report Format:').pack(pady=(10,0))
    format_var = tk.StringVar(value='md')
    tk.Radiobutton(root, text='Markdown', variable=format_var, value='md').pack()
    tk.Radiobutton(root, text='HTML', variable=format_var, value='html').pack()

    def on_generate():
        test_plan_path = entry.get()
        report_format = format_var.get()
        if not os.path.isfile(test_plan_path):
            messagebox.showerror('Error', 'Please select a valid CSV file.')
            return
        success, msg = run_report(test_plan_path, report_format)
        if success:
            messagebox.showinfo('Success', msg)
        else:
            messagebox.showerror('Error', msg)

    tk.Button(root, text='Generate Report', command=on_generate).pack(pady=15)
    root.mainloop()

if __name__ == '__main__':
    main()
