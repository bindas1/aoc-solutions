#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

std::vector<int> read_lines() {
    std::string input;
    std::vector<int> inputs;

    while (std::getline(std::cin, input)) {
        // std::cout << input << std::endl;
        inputs.push_back(std::stoi(input));
    }

    return inputs;
}

void find_product_of_two_sum(std::vector<int>& numbers, int target_sum=2020) {
    std::set<int> seen;

    for (int number : numbers) {
        int complement = target_sum - number;
        if (seen.count(complement) == 1) {
            std::cout << "Found: " << number << " and " << complement << std::endl;
            std::cout << "Product: " << number * complement << std::endl;
            return;
        }
        seen.insert(number);
    }
}

void find_product_of_three_sum(std::vector<int>& numbers, int target_sum=2020) {
    // find the product of three numbers that sum to 2020
    std::sort(numbers.begin(), numbers.end());
    size_t size = numbers.size();

    for (size_t i=0; i<size; ++i) {
        // use two pointers technique to find the two complementary numbers
        int remaining_sum = target_sum - numbers[i];
        int l = i + 1, r = size - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] == remaining_sum) {
                std::cout << "Found: " << numbers[i] << ", " << numbers[l] << " and " << numbers[r] << std::endl;
                std::cout << "Product: " << numbers[i] * numbers[l] * numbers[r] << std::endl;
                return;
            }
            else if (numbers[l] + numbers[r] < remaining_sum) {
                ++l;
            }
            else {
                --r;
            }
        }
    }
    return;
}

int main() {
    std::vector<int> inputs = read_lines();
    find_product_of_two_sum(inputs);
    find_product_of_three_sum(inputs);

    return 0;
}