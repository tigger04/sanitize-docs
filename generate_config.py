import csv
import json
from pathlib import Path

def generate_config(csv_file, output_file):
    """
    Generate a JSON configuration file for anonymization rules from a CSV file.
    """
    rules = []

    # Open and read the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            entry_type = row['type']
            value = row['value']
            translation = row['translation']
            
            # Build the regex pattern and replacement
            if entry_type == 'first_name':
                # Add case-sensitive patterns for first names
                rules.append({"pattern": f"\\b{value}\\b", "replacement": translation})
                rules.append({"pattern": f"\\b{value.lower()}\\b", "replacement": translation.lower()})
            elif entry_type == 'surname':
                # Add case-sensitive patterns for surnames
                rules.append({"pattern": f"\\b{value}\\b", "replacement": translation})
                rules.append({"pattern": f"\\b{value.lower()}\\b", "replacement": translation.lower()})
            elif entry_type == 'company':
                # Add case-sensitive patterns for company names
                rules.append({"pattern": f"\\b{value}\\b", "replacement": translation})
            elif entry_type == 'tld':
                # Add patterns for TLDs
                rules.append({"pattern": f"{value}\\b", "replacement": translation})

    # Write rules to the JSON file
    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump({"rules": rules}, json_file, indent=4)

    print(f"Config file generated: {output_file}")

# Specify input and output paths
csv_file = "data.csv"
output_file = "config.json"

# Generate the config file
generate_config(csv_file, output_file)
