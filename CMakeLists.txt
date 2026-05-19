cmake_minimum_required(VERSION 3.15...3.27)

project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

if (NOT SKBUILD)
    message(WARNING "This project must be built via pip/scikit-build-core, not raw CMake.")
endif()

find_package(Python 3.9 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(bionify_ext src/bionify_ext.cpp)

install(TARGETS bionify_ext
    LIBRARY DESTINATION bionify
    RUNTIME DESTINATION bionify
    ARCHIVE DESTINATION bionify
)

install(FILES
    src/bionify/__init__.py
    src/bionify/_core.py
    src/bionify/hook.py
    DESTINATION bionify
)