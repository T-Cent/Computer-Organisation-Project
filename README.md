"# Computer-Organisation-Project" 
# RISC-V Assembler Project

## Outline

This collaborative project involves the creation of a simple RISC-V assembler with a team of four members from IIIT Delhi, India. The assembler translates RISC-V assembly code into binary machine code and is implemented in Python.

## Structure and flow of project

1. **lookup.py**: Defines a lookup table containing binary encodings for RISC-V instructions.
   
   ```python
   # Highlight: Binary encodings for R-type, I-type, S-type, B-type, U-type, J-type instructions, and register mapping.
   ```

2. **suggestor.py**: Provides a suggestion module for correcting misspelled instructions or labels, along with colored terminal output.
   
   ```python
   # Highlight: Helper module for correction suggestions and colored terminal output.
   ```

3. **assembler.py**: Implements the RISC-V assembler, utilizing the lookup table and suggestion module to convert assembly code to binary, and it also contains the execution of the assembler. It is the main file of the project.
   
   ```python
   # Highlight: Binary conversion, label handling, error checking, and correction suggestions.
   # Highlight: Main logic for file input, reading assembly code, and writing binary output.
   ```




## Contributors and Contributions

1. Taraash Mittal(2023552):
    - Implemented the initial version of the RISC-V assembler.
    - Worked on the design and structure of the `suggestor.py` file.
    - Contributed to the implementation of the assembler's error-checking functionality.
    - Contributed to error handling and correction suggestions.

2. Mitul Aggarwal(2023322):
   - Developed the `suggestor.py` module for correction suggestions and colored terminal output and helped in building and debugging the `assembler.py`.
   - Contributed to error handling and correction suggestions.
   - Assisted in refining the overall code structure.

3. Namandeep Singh(2023339):
   - Collaborated on the `assembler.py` file, focusing on binary conversion and label handling.
   - Contributed to the lookup table design and validation logic.
   - Assisted in optimizing and refining code for better performance.

4. Parth Goyal(2023371):
   - Worked on the `assembler.py` and `lookup.py` file, handling file input, and executing the assembler.
   - Wrote the README documentation.
   - Assisted in integrating individual contributions and ensuring a smooth project work throughout.
  
## How to Use

1. **Clone the Repository:**
   ```
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Run the Assembler:**
   ```
   python assembler.py <input_file.txt> <output_file.txt>
   ```

   Replace `<input_file.txt>` with your RISC-V assembly code file and `<output_file.txt>` with the desired binary output file.

3. **Check for Errors:**
   The assembler will display any errors or suggestions for corrections in the terminal. If there are no errors, it will confirm the successful creation of the binary file.

## Example

```bash
python assembler.py sample_code.txt binary_output.txt
```

