# STAR Log.final.out Parser & Visualization

A Python script to parse STAR RNA-seq mapping log files, summarize key statistics, and visualize mapping quality.

## Description

This script is designed for researchers and bioinformaticians working with RNA-seq data.  
It parses STAR `Log.final.out` files, extracts essential mapping statistics, saves a summary Excel file, and optionally generates a visualization of mapping percentages for each sample.

Key statistics extracted:
- Total number of reads
- Percentage of uniquely mapped reads
- Percentage of multi-mapped reads
- Percentage of reads unmapped due to being too short

---

## Features

- Automatically reads all STAR `*_Log.final.out` files in a directory
- Extracts key mapping metrics for each sample
- Saves a summary in an Excel file
- Generates a bar plot showing Unique %, Multi %, and Unmapped too short % per sample
- Optionally displays the plot and/or saves it as a PNG file

---

## Requirements

- Python 3.8 or higher
- Required Python packages:
```bash
pip install pandas seaborn matplotlib openpyxl
