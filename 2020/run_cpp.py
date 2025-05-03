from aoc import get_input
import sys
import subprocess
import os

if len(sys.argv) != 2:
    print("Usage: python run_cpp.py <question_number>")
    sys.exit(1)

question_number = int(sys.argv[1])
data = get_input(question_number)

cpp_file = f"./{question_number}.cpp"
executable = f"ex_{question_number}"
input_file = f"./data/2020_{question_number}.txt"

# Use clang++ by default, but allow override with CXX
compiler = os.environ.get("CXX", "clang++")

# Abseil Homebrew paths (adjust if you're on Apple Silicon)
absl_include = "/usr/local/opt/abseil/include"
absl_lib = "/usr/local/opt/abseil/lib"

compile_flags = [
    "-std=c++17",
    f"-I{absl_include}",
    f"-L{absl_lib}",
    "-labsl_strings"
]

try:
    subprocess.run(
        [compiler, *compile_flags, cpp_file, "-o", executable],
        check=True
    )
    print(f"C++ code compiled successfully using {compiler}.")
except subprocess.CalledProcessError:
    print("Compilation failed. Please check your C++ code.")
    sys.exit(1)

try:
    result = subprocess.run(
        [f"./{executable}"],
        input=data,
        capture_output=True,
        text=True
    )
    print("C++ code executed successfully.")
    print(result.stdout)
except subprocess.CalledProcessError:
    print("Execution failed. Please check your C++ code.")
    sys.exit(1)
