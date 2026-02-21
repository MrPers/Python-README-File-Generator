import sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

def generate_markdown(data):
    """
    Constructs the Markdown string based on user input.
    """
    # Create a dynamic license badge using Shields.io
    license_name = data['license']
    badge_url = f"https://img.shields.io/badge/license-{license_name.replace(' ', '_')}-blue.svg"
    
    markdown_text = f"""# {data['title']}

![License]({badge_url})

## Description
{data['description']}

## Installation
```bash
{data['installation']}
```

## Usage
{data['usage']}

## License
This project is distributed under the {data['license']}.

## Author
Created by {data['author']}.
Contact: {data['contact']}
"""
    return markdown_text

def main():
    print("--- Welcome to the Professional README Generator ---")

    try:
        # Collecting data from the user via CLI prompts
        user_data = {
            "title": inquirer.text(
                message="Project Title:",
                validate=lambda x: len(x) > 0,
                invalid_message="Title is required!"
            ).execute(),

            "description": inquirer.text(message="Short description:").execute(),

            "installation": inquirer.text(
                message="Installation command:",
                default="pip install -r requirements.txt"
            ).execute(),

            "usage": inquirer.text(message="Usage instructions:").execute(),

            "license": inquirer.select(
                message="Select a license:",
                choices=[
                    Choice("MIT", name="MIT License"),
                    Choice("Apache 2.0", name="Apache 2.0"),
                    Choice("GPL v3", name="GNU GPL v3"),
                    Choice("Unlicense", name="Unlicense (Public Domain)"),
                ],
                default="MIT"
            ).execute(),

            "author": inquirer.text(message="Author Name:").execute(),

            "contact": inquirer.text(message="Contact Info (Email/Link):").execute(),
        }

        # Generate the final string
        final_output = generate_markdown(user_data)

        # Save to file
        with open("GENERATED_README.md", "w", encoding="utf-8") as f:
            f.write(final_output)

        print("\n[SUCCESS] Your README has been generated as 'GENERATED_README.md'!")

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n[EXIT] Program stopped by user.")
        sys.exit(0)
    except Exception as e:
        # General error handling for safety
        print(f"\n[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()