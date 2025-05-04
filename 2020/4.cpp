#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include "absl/strings/str_split.h"

std::vector<std::string> read_lines() {
    std::string input;
    std::vector<std::string> inputs;

    while (std::getline(std::cin, input)) {
        if (input == "")
            std::cout << "----------------";
        std::cout << input << std::endl;
        inputs.push_back(input);
    }

    return inputs;
}

bool check_passport(std::vector<std::string>& current_passport_fields) {
    const std::unordered_set<std::string> REQUIRED_FIELDS = {
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    };
    
    std::unordered_set<std::string> present_fields(current_passport_fields.begin(), current_passport_fields.end());
    
    for (const std::string& field : REQUIRED_FIELDS) {
        if (present_fields.count(field) == 0) {
            return false;
        }
    }
    
    return true;
}

// TODO PART 2 - map strings to vals and use match case to check conditions
bool check_passport() {    
    return true;
}

size_t count_valid_passports() {
    size_t valid_passports = 0;
    std::string current_line;
    std::vector<std::string> current_passport_fields = {};

    while (std::getline(std::cin, current_line)) {
        if (current_line== "") {
            valid_passports += check_passport(current_passport_fields) ? 1 : 0;
            current_passport_fields = {};
        }
        else {
            for (absl::string_view part : absl::StrSplit(current_line, ' ')) {
                current_passport_fields.push_back(std::string(part.substr(0, 3)));
            }
        }
    }
    
    // Check the last passport if input doesn't end with an empty line
    if (!current_passport_fields.empty()) {
        valid_passports += check_passport(current_passport_fields) ? 1 : 0;
    }

    return valid_passports;
}

int main() {
    std::cout << count_valid_passports() << std::endl;
    return 0;
}