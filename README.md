# STAR Log.final.out Parser & Visualization

This project parses STAR RNA-seq `Log.final.out` files, extracts key mapping statistics, summarizes them in an Excel file, and optionally generates bar plots to visualize mapping quality across samples.

---

## Features

- Automatically reads all STAR `*_Log.final.out` files in a directory.
- Extracts key mapping metrics for each sample:
  - Total number of reads
  - Percentage of uniquely mapped reads
  - Percentage of multi-mapped reads
  - Percentage of reads unmapped due to being too short
- Saves a summary Excel file with all statistics.
- Generates a bar plot showing Unique %, Multi %, and Unmapped too short % per sample.
- Optionally displays the plot and/or saves it as a PNG file.

---

## How It Works

1. The script scans the provided directory for files ending with `_Log.final.out`.
2. Each file is parsed to extract relevant mapping statistics.
3. The data from all files is combined into a pandas DataFrame.
4. The DataFrame is saved as an Excel file (`STAR_mapping_summary.xlsx` by default).
5. If requested, a bar plot is created to visualize mapping percentages per sample.
6. The plot can be displayed on-screen and/or saved as a PNG file.

---

## Example

### Input
```text
sample1_Log.final.out
sample2_Log.final.out
sample3_Log.final.out
```

### Command
```bash
python star_mapping_summary.py STAR_logs --output_file summary.xlsx --plot_file mapping.png --show_plot
``` 

### Output
```text
summary.xlsx            # Excel file summarizing mapping statistics
mapping.png             # Optional bar plot showing mapping percentages per sample
# Plot displayed in a window if --show_plot is used
```

### Usage
```bash
python star_mapping_summary.py INPUT_DIR [--output_file OUTPUT_FILE] [--plot_file PLOT_FILE] [--show_plot]
```

### Arguments
```text
INPUT_DIR         : Directory containing STAR Log.final.out files
--output_file     : Name of the Excel file to save the summary (default: STAR_mapping_summary.xlsx)
--plot_file       : Path to save the plot as PNG (optional)
--show_plot       : Display the plot in a window (optional)
```

### Requirements
```text
Python 3.8 or higher
Python packages:
- pandas
- seaborn
- matplotlib
- openpyxl
```

### Installation
```bash
git clone https://github.com/RemyKlein/STAR-log-parser.git
cd STAR-log-parser
pip install -r requirements.txt
```

## Running the Script Step-by-Step

### 1. Open your terminal
Navigate to the folder where your script `star_mapping_summary.py` is located:

```bash
cd STAR-log-parser
```

### 2. Prepare a folder with your STAR log files
Create a folder to store your STAR *_Log.final.out files:

```bash
mkdir STAR-logs
```

Then copy or move all your STAR log files into this folder:
```text
STAR-log-parser/
│
├─ STAR-logs/
│   ├─ sample1_Log.final.out
│   ├─ sample2_Log.final.out
│   └─ sample3_Log.final.out
├─ star_mapping_summary.py
└─ README.md
```

### 3. Run the script

You can run the script in two ways:

Using a relative path (recommended):
```bash
python star_mapping_summary.py STAR-logs --output_file summary.xlsx --plot_file mapping.png --show_plot
```

Using an absolute path:
```bash
python star_mapping_summary.py "C:/path/to/your/STAR-logs" --output_file summary.xlsx --plot_file mapping.png --show_plot
```

### 4. Check the output

After running the script, you should see the following results:
```text
summary.xlsx    # Excel file with mapping statistics
mapping.png     # Bar plot (if specified)
# Plot displayed on-screen if --show_plot is used
```

### Notes / Important Considerations
```text
- Ensure that all STAR Log.final.out files are in the same directory.
- Percentages are automatically converted from strings to floats for plotting.
- The Excel file and plot file paths can be customized via command-line arguments.
- The script is designed for RNA-seq datasets aligned with STAR.
```