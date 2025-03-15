# Makefile for Ubuntu
# Updated for GCC 9.3.0 and later
# Note: The -fipa-modref flag (not supported) was removed and the variable CXX is used for the C++ compiler
#       (ensuring that the standard library is linked).
#       The inclusion of <x86intrin.h> is forced so that __rdtsc is declared.

# C++ Compiler (you can override it by running: make CXX=g++-10)
CXX ?= g++

# Compiler flags (optimized for performance)
CFLAGS = -include x86intrin.h -std=c++17 -Ofast -funroll-loops -ftree-vectorize -fstrict-aliasing \
         -fno-semantic-interposition -fvect-cost-model=unlimited -fno-trapping-math \
         -fipa-ra -flto -fassociative-math -fopenmp -mavx2 -mbmi2 -madx

# Linker flags
LDFLAGS = -fopenmp

# Source files
SOURCES = Cyclone.cpp SECP256K1.cpp Int.cpp IntGroup.cpp IntMod.cpp Point.cpp \
          ripemd160_avx2.cpp p2pkh_decoder.cpp sha256_avx2.cpp Timer.cpp Random.cpp

# Object files
OBJECTS = $(SOURCES:.cpp=.o)

# Final executable
TARGET = Cyclone

# Default target: build the executable
all: $(TARGET)

# Rule to compile .cpp files into .o files
%.o: %.cpp
	$(CXX) $(CFLAGS) -c $< -o $@

# Rule to link object files and generate the final executable
$(TARGET): $(OBJECTS)
	$(CXX) $(CFLAGS) $(OBJECTS) -o $@ $(LDFLAGS)

# Clean up generated files
clean:
	rm -f $(TARGET) $(OBJECTS)
