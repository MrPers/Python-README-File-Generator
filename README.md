# Professional README.md Generator

A powerful Python CLI tool designed to help developers quickly generate high-quality, professional `README.md` files for their GitHub repositories. Built with **InquirerPy** for interactive prompts and **Rich** for beautiful terminal output.

## Features

- **Interactive CLI:** Guided prompts for project title, description, and instructions.
- **Smart License Selection:** Dropdown menu featuring common licenses (MIT, Apache, GPL, etc.).
- **Professional Formatting:** Generates valid Markdown with automated badges and clean structures.
- **Real-time Feedback:** Uses `Rich` to provide colored success messages and error handling.

## Installation

Follow these steps to set up the environment and run the generator:
1. **Clone the repository:**
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

2. **Create and activate a virtual environment:**
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
3. **Install dependencies:**
    pip install -r requirements.txt