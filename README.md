# GenAI App - AI Code Reviewer

## Overview

The **GenAI App** is an AI-powered code reviewer built using Python and OpenAI's GPT-3.5 model. It allows users to submit their Python code for analysis and receive detailed feedback on potential bugs, errors, and optimization suggestions. The app is built using **Streamlit**, providing a simple and interactive user experience.

## Features

- **User-friendly Interface:** Built with **Streamlit** for easy interaction.
- **AI-Powered Code Review:** Utilizes **OpenAI's GPT-3.5** model to analyze Python code.
- **Bug Detection & Fixes:** Identifies errors and suggests potential fixes.
- **Code Optimization:** Provides recommendations for improving efficiency and readability.
- **Quick Feedback:** Instant analysis with a simple code submission.
- **Secure API Integration:** Uses OpenAI's API for processing code securely.

## Demo

Click the image below to watch the demonstration video:

[![Watch the video](Screenshot%202024-04-16%20080220.png)](https://drive.google.com/file/d/1wSTvgl5APoICxDhBwRDK-uUS9FjY4ahu/view?usp=sharing)

## Installation & Setup

### Prerequisites
- **Python 3.8+**
- **pip** (Python package manager)
- **OpenAI API Key** (Required to use the AI-powered review feature)

### Steps to Install & Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Swastik-Dubey/GenAI_App_AI_Code_Reviewer.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd GenAI_App_AI_Code_Reviewer
   ```
3. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set Up OpenAI API Key**
   - Create a `.env` file in the project directory and add:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Alternatively, set the API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key_here  # Linux/macOS
     set OPENAI_API_KEY=your_openai_api_key_here  # Windows
     ```

6. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in a browser (it will launch automatically upon running the command).
2. Enter your Python code in the text area.
3. Click the **"Generate"** button.
4. View the AI-generated review, including detected errors and improvement suggestions.

## Example Output

Upon entering the following Python snippet:
```python
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))
```

The AI might provide feedback such as:
- **Code Quality:** The function is well-structured.
- **Optimization:** Consider adding type hints (`def add_numbers(a: int, b: int) -> int`).
- **Readability:** Docstrings can be added for better documentation.

## Troubleshooting

- **Issue:** `ModuleNotFoundError: No module named 'streamlit'`
  - **Solution:** Run `pip install streamlit` and try again.
- **Issue:** `streamlit: command not found`
  - **Solution:** Ensure that Python and pip are installed and correctly added to the system path.
- **Issue:** OpenAI API Key Error
  - **Solution:** Check if the API key is correctly set in the `.env` file or as an environment variable.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



Happy Coding! 🚀

