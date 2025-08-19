#!/usr/bin/env python3
"""
Data Analysis and Visualization Tool
A sample Python application that demonstrates various dependencies and functionality
"""

import argparse
from datetime import datetime
from src.data_processor import DataProcessor
from src.display import create_console, display_results, display_header
from src.utils import generate_random_matrix

def main():
    parser = argparse.ArgumentParser(description="Data Analysis and Visualization Tool")
    parser.add_argument("--export", action="store_true", help="Export results to JSON")
    parser.add_argument("--matrix", action="store_true", help="Generate random matrix")
    parser.add_argument("--mock", action="store_true", help="Use mock data instead of API")
    args = parser.parse_args()
    
    console = create_console()
    display_header(console)
    
    processor = DataProcessor(console)
    
    if args.mock:
        processor.generate_mock_data()
    else:
        processor.fetch_sample_data()
    
    stats = processor.process_data()
    display_results(console, processor.processed_data)
    
    if args.matrix:
        generate_random_matrix(console)
    
    if args.export:
        processor.export_results()
    
    console.print("\n[bold green]✓ Processing complete![/bold green]")
    console.print(f"[dim]Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/dim]\n")

if __name__ == "__main__":
    main()