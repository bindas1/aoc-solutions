#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> read_lines() {
    std::string input;
    std::vector<std::string> inputs;

    while (std::getline(std::cin, input)) {
        std::cout << input << std::endl;
        inputs.push_back(input);
    }
}

int main() {
    std::vector<std::string> inputs = read_lines();
    std::cout << "Total lines: " << inputs.size() << std::endl;
    return 0;
}