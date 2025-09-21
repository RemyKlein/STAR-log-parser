#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
STAR Log.final.out Parser & Visualization
Author: Rémy Klein
Description: This script parses STAR mapping log files, extracts key statistics
             (Total Reads, Unique %, Multi %, Unmapped too short %), saves a summary
             Excel file, and optionally visualizes the mapping percentages.
"""

import os
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Functions
# -------------------------------
def parse_star_file(file_path):
    """
    Parse a STAR Log.final.out file and extract relevant statistics.
    Returns a dictionary with simplified column names.
    """
    dict_part = {
        "Number of input reads": "Total Reads",
        "Uniquely mapped reads %": "Unique (%)",
        "% of reads mapped to multiple loci": "Multi (%)",
        "% of reads unmapped: too short": "Unmapped too short (%)"
    }
    stats = {}
    with open(file_path, "r") as f:
        for line in f:
            if "|" in line:
                key, value = [x.strip() for x in line.strip().split("|")]
                if key in dict_part:
                    stats[dict_part[key]] = value
    return stats

def load_star_logs(input_dir):
    """
    Load all STAR Log.final.out files from the given directory
    and return a pandas DataFrame summarizing the results.
    """
    all_files = [f for f in os.listdir(input_dir) if f.endswith("_Log.final.out")]
    data = []
    for file_name in all_files:
        sample_name = file_name.replace("_Log.final.out", "")
        file_path = os.path.join(input_dir, file_name)
        stats = parse_star_file(file_path)
        stats["Sample"] = sample_name
        data.append(stats)
    df = pd.DataFrame(data)
    # Convert percentage strings to float
    for col in ["Unique (%)", "Multi (%)", "Unmapped too short (%)"]:
        df[col] = df[col].str.rstrip('%').astype(float)
    return df

def plot_mapping_summary(df, show_plot=True, save_path=None):
    """
    Create a bar plot showing Unique %, Multi %, and Unmapped too short % per sample.
    """
    df_melt = df.melt(id_vars="Sample",
                      value_vars=["Unique (%)", "Multi (%)", "Unmapped too short (%)"],
                      var_name="Mapping Category",
                      value_name="Percentage")
    plt.figure(figsize=(12,6))
    sns.barplot(x="Sample", y="Percentage", hue="Mapping Category", data=df_melt)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Percentage (%)")
    plt.xlabel("Sample")
    plt.title("STAR Mapping Summary per Sample")
    plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    if show_plot:
        plt.show()
    plt.close()

# -------------------------------
# Main
# -------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Parse STAR Log.final.out files, save a summary Excel file, and optionally plot mapping statistics."
    )
    
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory containing STAR Log.final.out files to process."
    )

    parser.add_argument(
        "--output_file",
        type=str,
        default="STAR_mapping_summary.xlsx",
        help="Name of the Excel file to save the summary. Default: STAR_mapping_summary.xlsx"
    )

    parser.add_argument(
        "--plot_file",
        type=str,
        default=None,
        help="Full path including filename (e.g., C:\\path\\to\\plot.png) to save the plot as PNG. Optional."
    )

    parser.add_argument(
        "--show_plot",
        action="store_true",
        help="Display the plot in a window. Use this flag to visualize the mapping percentages."
    )

    args = parser.parse_args()

    # Load and process STAR logs
    df = load_star_logs(args.input_dir)

    # Save summary Excel file
    output_path = os.path.join(args.input_dir, args.output_file)
    df.to_excel(output_path, index=False)
    print(f"Summary saved to: {output_path}")

    # Plot mapping summary
    plot_mapping_summary(df, show_plot=args.show_plot, save_path=args.plot_file)
    if args.plot_file:
        print(f"Plot saved to: {args.plot_file}")

if __name__ == "__main__":
    main()