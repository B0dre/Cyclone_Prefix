# This Makefile has been tested on macOS.
# Compiler to use (GCC 14 installed via Homebrew)
# Coded by @B0dre
CC = g++-14

# Detect system architecture (Intel or Apple Silicon)
ARCH := $(shell uname -m)

# Set paths based on architecture
ifeq ($(ARCH),arm64)
  # Apple Silicon paths
  LIBOMP_PATH = /opt/homebrew/opt/libomp
else
  # Intel Mac paths
  LIBOMP_PATH = /usr/local/opt/libomp
endif

# Compiler flags
CFLAGS = -std=c++17 -Ofast -funroll-loops -ftree-vectorize -fstrict-aliasing \
         -fno-semantic-interposition -fvect-cost-model=unlimited -fno-trapping-math \
         -fipa-ra -fipa-modref -flto -fassociative-math -fopenmp -mavx2 -mbmi2 -madx \
         -I$(LIBOMP_PATH)/include

# Linker flags
LDFLAGS = -L$(LIBOMP_PATH)/lib -lomp

# Source files - including Timer.cpp and Random.cpp
SOURCES = Cyclone.cpp SECP256K1.cpp Int.cpp IntGroup.cpp IntMod.cpp Point.cpp \
          ripemd160_avx2.cpp p2pkh_decoder.cpp sha256_avx2.cpp Timer.cpp Random.cpp

# Object files
OBJECTS = $(SOURCES:.cpp=.o)

# Target executable name
TARGET = Cyclone

# Default target
all: $(TARGET)

# Rule to build object files
%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

# Rule to build the target
$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $@ $(LDFLAGS)

# Clean up
clean:
	rm -f $(TARGET) $(OBJECTS)
