import re
import json
import sys
from pathlib import Path

def load_config(config_path):
    """Load the regex and translation configuration from a JSON file."""
    with open(config_path, 'r') as file:
        return json.load(file)

def sanitize_and_translate(input_text, config):
    """Sanitize and translate the input text based on the regex configuration."""
    for rule in config['rules']:
        pattern = rule['pattern']
        replacement = rule['replacement']
        input_text = re.sub(pattern, replacement, input_text)
    return input_text

def process_file(input_file, output_file, config):
    """Process the input file to sanitize and translate content."""
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()
    
    sanitized_text = sanitize_and_translate(input_text, config)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(sanitized_text)

def main():
    """Main function to handle input arguments and process files."""
    if len(sys.argv) < 4:
        print("Usage: python sanitize_script.py <config.json> <input_file> <output_file>")
        sys.exit(1)

    config_path = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    # Check if input and config files exist
    if not Path(config_path).is_file():
        print(f"Config file not found: {config_path}")
        sys.exit(1)

    if not Path(input_file).is_file():
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    # Load configuration and process the file
    config = load_config(config_path)
    process_file(input_file, output_file, config)
    print(f"Sanitized and translated content written to {output_file}")

if __name__ == "__main__":
    main()
