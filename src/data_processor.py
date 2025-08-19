"""
Data processing module for fetching, processing, and exporting data
"""

import pandas as pd
from datetime import datetime
import json
import time
import random
from rich.progress import track


class DataProcessor:
    def __init__(self, console):
        self.data = None
        self.processed_data = None
        self.console = console
        
    def fetch_sample_data(self):
        """Generate sample data locally"""
        self.console.print("[bold blue]Generating sample data...[/bold blue]")
        self.generate_mock_data()
        return self.data
    
    def generate_mock_data(self):
        """Generate mock data locally"""
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
        companies = ["Tech Corp", "Global Solutions", "Innovation Inc", "Future Systems", "Data Analytics Co"]
        first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Lisa", "James", "Maria"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        
        num_records = random.randint(15, 25)
        self.data = []
        
        for i in range(1, num_records + 1):
            self.data.append({
                "id": i,
                "name": f"{random.choice(first_names)} {random.choice(last_names)}",
                "email": f"user{i}@{random.choice(['example.com', 'mail.com', 'email.org'])}",
                "address": {
                    "city": random.choice(cities),
                    "zipcode": f"{random.randint(10000, 99999)}"
                },
                "company": {
                    "name": random.choice(companies)
                }
            })
        
        self.console.print(f"[green]✓ Generated {len(self.data)} mock records[/green]")
    
    def process_data(self):
        """Process and analyze the data"""
        self.console.print("\n[bold cyan]Processing data...[/bold cyan]")
        
        df = pd.DataFrame(self.data)
        
        for _ in track(range(10), description="Analyzing..."):
            time.sleep(0.1)
        
        stats = {
            "total_records": len(df),
            "unique_cities": df.apply(lambda x: x['address']['city'] if isinstance(x['address'], dict) else 'Unknown', axis=1).nunique(),
            "unique_companies": df.apply(lambda x: x['company']['name'] if isinstance(x['company'], dict) else 'Unknown', axis=1).nunique(),
            "timestamp": datetime.now().isoformat()
        }
        
        self.processed_data = stats
        return stats
    
    def export_results(self, filename="results.json"):
        """Export results to JSON file"""
        if not self.processed_data:
            self.console.print("[red]No data to export.[/red]")
            return
        
        with open(filename, 'w') as f:
            json.dump(self.processed_data, f, indent=2)
        
        self.console.print(f"\n[green]✓ Results exported to {filename}[/green]")