cmake_minimum_required(VERSION 3.15...3.27)

project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

if (NOT SKBUILD)
    message(WARNING "This project must be built via pip/scikit-build-core, not raw CMake.")
endif()

find_package(Python 3.9 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(fovea_ext src/fovea_ext.cpp)

# Robust installation directives covering all operating systems and output artifacts
install(TARGETS fovea_ext
    LIBRARY DESTINATION fovea
    RUNTIME DESTINATION fovea
    ARCHIVE DESTINATION fovea
)

# Ensure the Python source code is explicitly bundled alongside the compiled binary
install(FILES
    src/fovea/__init__.py
    src/fovea/_core.py
    src/fovea/hook.py
    DESTINATION fovea
)