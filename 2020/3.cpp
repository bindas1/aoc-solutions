#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> read_lines() {
    std::string input;
    std::vector<std::string> inputs;

    while (std::getline(std::cin, input)) {
        inputs.push_back(input);
    }

    return inputs;
}

size_t count_trees(std::vector<std::string>& inputs, const int move_right=3, const int move_down=1) {
    if (inputs.empty()) {
        return 0;
    }
    
    size_t curr_right = 0, curr_down = 0;
    const size_t max_right = inputs[0].size(), max_down = inputs.size();
    size_t trees = 0;

    while (curr_down < max_down) {
        if (inputs[curr_down][curr_right] == '#') {
            ++trees;
        }

        curr_right = (curr_right + move_right) % max_right;
        curr_down += move_down;
    }

    return trees;
}

int main() {
    std::vector<std::string> inputs = read_lines();
    std::cout << count_trees(inputs) << std::endl;
    size_t multiplied_results = 
        count_trees(inputs, 1, 1) * 
        count_trees(inputs, 3, 1) * 
        count_trees(inputs, 5, 1) * 
        count_trees(inputs, 7, 1) * 
        count_trees(inputs, 1, 2);
    std::cout << multiplied_results << std::endl;
    return 0;
}