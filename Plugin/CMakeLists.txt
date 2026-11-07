cmake_minimum_required(VERSION 3.20)
project(JVPLEY_ETS2_Plugin LANGUAGES CXX)

if(NOT WIN32 OR NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
  message(FATAL_ERROR "JVPLEY ETS2 plugin requires Windows x64.")
endif()

add_library(JVPLEY_ETS2 SHARED src/plugin.cpp)
target_compile_features(JVPLEY_ETS2 PRIVATE cxx_std_17)
target_compile_definitions(JVPLEY_ETS2 PRIVATE WIN32_LEAN_AND_MEAN NOMINMAX)
set_target_properties(JVPLEY_ETS2 PROPERTIES PREFIX "" OUTPUT_NAME "JVPLEY_ETS2")
