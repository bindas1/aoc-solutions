from aoc import get_input
import sys
import subprocess

if len(sys.argv) != 2:
    print("Usage: python run_cpp.py <question_number>")
    sys.exit(1)

question_number = int(sys.argv[1])
data = get_input(question_number)

# Compile the C++ code
cpp_file = f"./{question_number}.cpp"
executable = f"ex_{question_number}"

try:
    subprocess.run(["g++", cpp_file, "-o", executable], check=True)
    print("C++ code compiled successfully.")
except subprocess.CalledProcessError:
    print("Compilation failed. Please check your C++ code.")
    sys.exit(1)

# run the compiled C++ code with the input data
input_file = f"./data/2020_{question_number}.txt"

try:
    result = subprocess.run([f"./{executable}"], input=data, capture_output=True, text=True)
    print("C++ code executed successfully.")
    print(result.stdout)
except subprocess.CalledProcessError:
    print("Execution failed. Please check your C++ code.")
    sys.exit(1)