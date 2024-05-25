# Directory Traveler
Objective: Create a Python script to analyze all files in a specified directory, collecting metrics such as file type, size, and potential purpose. Visualize the analysis results in real-time using a web interface.

## Modules

1. Directory File Analyzer
    - Write a Python script to traverse a directory, analyze each file, and collect metrics.
    - Gather metrics like file type, size, and basic content analysis (e.g. word count for text files).
2. Parallel Processor
    - Use concurrent.futures for parallel processing.
    - Have initial component run to determine how to assign chunks to executors.
    - Implement a load-balancer that monitors processors and redistributes chunk assignment as needed.
    - Initial version will count the number of files per directory in order to determine chunk assignment.
3. Real-time Visualization
    - Use a lighweight web server (e.g. Flask) to serve real-time updates.
    - Use a library like 'plotly' to create visualizations of the analysis progress