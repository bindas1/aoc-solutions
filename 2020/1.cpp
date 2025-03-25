#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string input;
    std::cout << "Input line by line" << std::endl;
    std::vector<std::string> inputs;

    while (std::getline(std::cin, input)) {
        std::cout << input << std::endl;
        inputs.push_back(input);
    }

    std::cout << "Total lines: " << inputs.size() << std::endl;
    return 0;
}