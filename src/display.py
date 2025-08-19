"""
Display and formatting utilities
"""

from rich.console import Console
from rich.table import Table


def create_console():
    """Create and return a Rich console instance"""
    return Console()


def display_results(console, processed_data):
    """Display processed results in a formatted table"""
    if not processed_data:
        console.print("[red]No data to display. Please process data first.[/red]")
        return
    
    table = Table(title="Data Analysis Results", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    
    for key, value in processed_data.items():
        table.add_row(key.replace("_", " ").title(), str(value))
    
    console.print("\n")
    console.print(table)


def display_header(console):
    """Display application header"""
    console.print("[bold magenta]═══════════════════════════════════════════[/bold magenta]")
    console.print("[bold magenta]   Data Analysis and Visualization Tool    [/bold magenta]")
    console.print("[bold magenta]═══════════════════════════════════════════[/bold magenta]\n")