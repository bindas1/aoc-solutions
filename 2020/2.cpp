#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include "absl/strings/str_split.h"

std::vector<std::string> read_lines() {
    std::string input;
    std::vector<std::string> inputs;

    while (std::getline(std::cin, input)) {
        inputs.push_back(input);
    }

    return inputs;
}

std::tuple<int, int, char, std::string> parse_line(std::string line) {
    std::vector<std::string> parts = absl::StrSplit(line, ' ');
    std::vector<std::string> range = absl::StrSplit(parts[0], '-');

    int min = std::stoi(range[0]);
    int max = std::stoi(range[1]);
    char letter = parts[1][0];
    std::string password = parts[2];

    return std::make_tuple(min, max, letter, password);
}

size_t count_valid(std::vector<std::string> inputs) {
    size_t count = 0;
    
    for (const std::string& line : inputs) {
        auto [min, max, letter, password] = parse_line(line);

        int letter_count = std::count(password.begin(), password.end(), letter);
        if (letter_count >= min && letter_count <= max) {
            count++;
        }
    }

    return count;
}

size_t count_valid_2(std::vector<std::string> inputs) {
    size_t count = 0;
    
    for (const std::string& line : inputs) {
        auto [min, max, letter, password] = parse_line(line);

        if (password[min-1] == letter ^ password[max-1] == letter) {
            count++;
        }
    }
    
    return count;
}

int main() {
    std::vector<std::string> inputs = read_lines();
    std::cout << "Res 1: " << count_valid(inputs) << std::endl;
    std::cout << "Res 2: " << count_valid_2(inputs);
    return 0;
}