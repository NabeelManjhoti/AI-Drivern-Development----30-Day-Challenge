# tests/integration/test_cli.py
import subprocess
import sys
import pytest

# Define the path to the main script
MAIN_SCRIPT = "src.main"

def run_cli_command(num1, operator, num2):
    command = [
        sys.executable,
        "-m", MAIN_SCRIPT,
        "--num1", str(num1),
        "--operator", operator,
        "--num2", str(num2)
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def test_cli_addition_valid():
    stdout, stderr, returncode = run_cli_command(5, "+", 3)
    assert returncode == 0
    assert stdout == "8.0"
    assert stderr == ""

def test_cli_subtract_valid():
    stdout, stderr, returncode = run_cli_command(10, "-", 4)
    assert returncode == 0
    assert stdout == "6.0"
    assert stderr == ""

def test_cli_multiply_valid():
    stdout, stderr, returncode = run_cli_command(7, "*", 2)
    assert returncode == 0
    assert stdout == "14.0"
    assert stderr == ""

def test_cli_divide_valid():
    stdout, stderr, returncode = run_cli_command(10, "/", 2)
    assert returncode == 0
    assert stdout == "5.0"
    assert stderr == ""

def test_cli_divide_by_zero():
    stdout, stderr, returncode = run_cli_command(10, "/", 0)
    assert returncode == 0 # The program handles the error and exits gracefully
    assert stdout == "Error: Division by zero is not allowed"
    assert stderr == ""

def test_cli_invalid_operator():
    stdout, stderr, returncode = run_cli_command(5, "^", 3)
    assert returncode == 0 # The program handles the error and exits gracefully
    assert stdout == "Error: Invalid operator '^'. Supported operators are +, -, *, /"
    assert stderr == ""

def test_cli_non_numeric_input_num1():
    stdout, stderr, returncode = run_cli_command("hello", "+", 3)
    assert returncode == 2 # argparse exits with code 2 for invalid arguments
    assert stdout == ""
    assert "argument --num1: invalid float value: 'hello'" in stderr

def test_cli_non_numeric_input_num2():
    stdout, stderr, returncode = run_cli_command(5, "+", "world")
    assert returncode == 2 # argparse exits with code 2 for invalid arguments
    assert stdout == ""
    assert "argument --num2: invalid float value: 'world'" in stderr
