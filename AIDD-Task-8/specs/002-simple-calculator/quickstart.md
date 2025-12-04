# Quickstart: Simple Calculator CLI

This document provides instructions on how to quickly set up and use the Simple Calculator CLI.

## Prerequisites

- Python 3.10+ installed on your system.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2.  **Navigate to the feature branch**:
    ```bash
    git checkout 002-simple-calculator
    ```

## Usage

The calculator is a command-line application that takes two numbers and an operator as input.

### Examples

**Addition**:
```bash
python src/main.py --num1 5 --operator + --num2 3
# Expected output: 8
```

**Subtraction**:
```bash
python src/main.py --num1 10 --operator - --num2 4
# Expected output: 6
```

**Multiplication**:
```bash
python src/main.py --num1 7 --operator * --num2 2
# Expected output: 14
```

**Division**:
```bash
python src/main.py --num1 10 --operator / --num2 2
# Expected output: 5.0
```

**Division by Zero Error**:
```bash
python src/main.py --num1 5 --operator / --num2 0
# Expected output: Error: Division by zero is not allowed
```

**Invalid Operator Error**:
```bash
python src/main.py --num1 5 --operator ^ --num2 3
# Expected output: Error: Invalid operator. Supported operators are +, -, *, /
```

**Non-numeric Input Error**:
```bash
python src/main.py --num1 hello --operator + --num2 world
# Expected output: Error: Non-numeric input provided. Please enter valid numbers.
```
