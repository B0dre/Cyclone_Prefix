#!/usr/bin/python3

import random
import subprocess

puzzle = 68
add = "1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ"
start_prefix = "D" # 8,9,a,b,c,d,e,f
prefix_length = 10

# Constants
LOWER_BOUND = 2 ** (puzzle - 1)
UPPER_BOUND = (2**puzzle) - 1
BIT_GAP = 2**30  # 30-bit gap (1,077,958,656 in decimal)

count = 0

while True:
    # Generate the first random number within the valid range
    first_number = random.randrange(LOWER_BOUND, UPPER_BOUND - BIT_GAP)
  
    # Calculate the second number with a 30-bit gap
    second_number = first_number + BIT_GAP
  
    # Ensure the second number is within the upper bound
    if second_number > UPPER_BOUND:
        second_number = UPPER_BOUND  # Set second_number to UPPER_BOUND if it exceeds

    # Format both numbers as hexadecimal strings without leading zeros and replace the first character with the prefix
    first_hex = start_prefix + f"{first_number:X}"[1:]
    second_hex = start_prefix + f"{second_number:X}"[1:]
  
    # Prepare the command with the generated random values and nuevo argumento -p (valor 3)
    command = [
        "./Cyclone",
        "-a", f"{add}",
        "-r", f"{first_hex}:{second_hex}",
        "-p", f"{prefix_length}"
    ]
  
    # Print the generated numbers
    print(f"Iteration {count + 1}:")
    print(f"First Number (Hex): {first_hex}")
    print(f"Second Number (Hex): {second_hex}")
    print("Executing Cyclone command...")
    print("-" * 50)
  
    # Execute the command and stream output/error to the terminal in real-time
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
  
    found_match = False
    lines_to_save = []  # Lista para almacenar todas las líneas del bloque de match
  
    # Lee la salida en tiempo real
    while True:
        stdout_line = process.stdout.readline()
        if stdout_line:
            print(stdout_line, end="")  # Imprime la salida en tiempo real
            if "FOUND MATCH!" in stdout_line:
                found_match = True
            if found_match:
                lines_to_save.append(stdout_line)
        else:
            break
  
    # Tras finalizar la lectura de stdout
    process.wait()
  
    if found_match:
        # Guarda todas las líneas capturadas en el archivo de coincidencia
        with open("found_match.txt", "w") as file:
            file.writelines(lines_to_save)
        print("================== FOUND MATCH! ==================")
        break  # Sale del script tras encontrar un match
  
    # En caso de fallo en la ejecución del proceso
    if process.returncode != 0:
        # Lee lo que haya en stderr y lo imprime
        error_output = process.stderr.read()
        print(error_output)
        print(f"Cyclone command failed with return code: {process.returncode}")
    else:
        print("Cyclone command completed successfully.")
  
    # Incrementa el contador
    count += 1
