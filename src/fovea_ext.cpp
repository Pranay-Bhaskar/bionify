#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>

#include <string>
#include <cctype>
#include <cmath>

namespace nb = nanobind;

std::string format_bionic_text(const std::string &input,
                               double intensity,
                               const std::string &prefix,
                               const std::string &suffix) {
    std::string output;
    size_t i = 0;
    const size_t n = input.size();

    while (i < n) {
        // Skip existing ANSI escape codes
        if (input[i] == '\033' && i + 1 < n && input[i + 1] == '[') {
            size_t ansi_start = i;
            i += 2;
            while (i < n && input[i] != 'm') i++;
            if (i < n) i++;
            output.append(input, ansi_start, i - ansi_start);
            continue;
        }

        // Pass through whitespace
        if (std::isspace(static_cast<unsigned char>(input[i]))) {
            output += input[i++];
            continue;
        }

        // Extract the next token (word)
        size_t start = i;
        while (i < n &&
               !std::isspace(static_cast<unsigned char>(input[i])) &&
               !(input[i] == '\033' && i + 1 < n && input[i + 1] == '[')) {
            i++;
        }
        std::string token = input.substr(start, i - start);

        // FEATURE 4: Hyperlink & Path Protection
        // If the token looks like a URL or an absolute Windows path, skip formatting
        if (token.find("://") != std::string::npos || token.find(":\\") != std::string::npos) {
            output += token;
            continue;
        }

        // Calculate word length (alphanumeric only)
        size_t word_len = 0;
        for (char c : token) {
            if (std::isalnum(static_cast<unsigned char>(c))) word_len++;
        }

        // Apply Bionic Formatting
        if (word_len > 0) {
            size_t fixation_len = static_cast<size_t>(std::ceil(word_len * intensity));
            if (fixation_len == 0) fixation_len = 1;
            if (fixation_len > word_len) fixation_len = word_len;

            output += prefix;
            output += token.substr(0, fixation_len);
            output += suffix;
            output += token.substr(fixation_len);
        } else {
            output += token;
        }
    }

    return output;
}

NB_MODULE(fovea_ext, m) {
    m.doc() = "High-performance C++ backend for Fovea.";

    m.def("format_bionic_text",
          &format_bionic_text,
          nb::arg("input"),
          nb::arg("intensity") = 0.5,
          nb::arg("prefix") = "\033[1;96m",
          nb::arg("suffix") = "\033[0m");
}