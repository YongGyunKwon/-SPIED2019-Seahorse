cmake_minimum_required(VERSION 3.15.19080502-MSVC_2)
project(CheckCUDA CUDA)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/result.cmake"
  "set(CMAKE_CUDA_COMPILER \"${CMAKE_CUDA_COMPILER}\")\n"
  "\n"
  )