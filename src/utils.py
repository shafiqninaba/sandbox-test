"""
Utility functions for data analysis
"""

import numpy as np
import pandas as pd


def generate_random_matrix(console):
    """Generate and display a random matrix using numpy"""
    console.print("\n[bold yellow]Generating random matrix...[/bold yellow]")
    matrix = np.random.rand(5, 5)
    
    df = pd.DataFrame(matrix, 
                      columns=[f"Col {i+1}" for i in range(5)],
                      index=[f"Row {i+1}" for i in range(5)])
    
    console.print("\n[cyan]Random Matrix (5x5):[/cyan]")
    console.print(df.round(3).to_string())
    
    console.print(f"\n[green]Matrix Statistics:[/green]")
    console.print(f"  Mean: {matrix.mean():.3f}")
    console.print(f"  Std Dev: {matrix.std():.3f}")
    console.print(f"  Min: {matrix.min():.3f}")
    console.print(f"  Max: {matrix.max():.3f}")