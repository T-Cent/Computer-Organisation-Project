# Computer-Organisation-Project
# RISC-V Assembler Project

## Note:
 - The original git repository can be found at `github.com/taraash23552/Computer-Organisation-Project`; due to some unforeseen conditions, I (taraash) managed to make somehow this repository unusable as we could not push anything to it anymore. Hence, we made a new repository and tried to replicate all the premade commits added to it (using `git log --oneline`, we had all the history).
 - We believe the correct answers provided by the college are wrong; we have found multiple instances in which the given solutions fail.


## Outline

This collaborative project involves the creation of a simple RISC-V assembler with a team of four members from IIIT Delhi, India. The assembler translates RISC-V assembly code into binary machine code, implemented in Python.

## Structure and flow of project

1. **lookup.py**: Defines a lookup table containing binary encodings for RISC-V instructions.
   
   ```python
   # Highlight: Binary encodings for R-type, I-type, S-type, B-type, U-type, J-type instructions, and register mapping.
   ```

2. **suggestor.py**: Provides a suggestion module for correcting misspelt instructions or labels, along with coloured terminal output.
   
   ```python
   # Highlight: The helper module is for correction suggestions and coloured terminal output.
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
   - Developed the `suggestor.py` module for correction suggestions and colored terminal output and helped build and debug the `assembler.py`.
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
  
