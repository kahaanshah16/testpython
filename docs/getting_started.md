# Getting Started

This guide will help you get started with the Python project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository** (after setting up Git):
   ```bash
   git clone <your-repository-url>
   cd my-python-project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### Basic Usage

Run the main module:
```bash
python src/main.py
```

### Running Tests

Run all tests:
```bash
python -m pytest tests/
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=src
```

### Development Tools

Format code with Black:
```bash
black src/ tests/
```

Check code style with flake8:
```bash
flake8 src/ tests/
```

Type checking with mypy:
```bash
mypy src/
```

## Project Structure

- `src/`: Source code
- `tests/`: Test files
- `docs/`: Documentation
- `requirements.txt`: Python dependencies
- `setup.py`: Package configuration
- `.gitignore`: Git ignore rules

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License. 