# TCL Preprocessing Script

This project provides a Python script to preprocess TCL files by handling multiline commands and combining them into single-line commands. It also checks for unexpected line breaks in square brackets `[]` or parentheses `()`.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.x

## Installation

1. **Clone the repository or download the script files.**

2. **Install required Python libraries:**
   ```sh
   pip install re argparse json
   ```

## Usage

### Configuration File

Create a JSON configuration file that lists the TCL files you want to process. For example, `config.json`:

```json
{
    "file_list": [
        "input1.tcl",
        "input2.tcl"
    ]
}
```

### Running the Script

Use the following command to run the script, passing the path to your configuration file as an argument:

```sh
python tcl_line_processing.py config.json
```

### Example

Assuming you have a configuration file named `config.json` and TCL files `input1.tcl` and `input2.tcl`:

```sh
python tcl_line_processing.py config.json
```

### Output

For each input file, the script will generate:
- An intermediate file after handling backslashes: `<filename>_intermediate1.tcl`
- An intermediate file after handling braces: `<filename>_intermediate2.tcl`
- A final output file with combined single-line commands: `<filename>_output.tcl`

If there are any errors such as unexpected line breaks, the script will print an error message and continue processing the next file.

### Error Handling

If a file is not found or there are issues reading a file, the script will print an error message and skip processing that file.

## Example Directory Structure

```
project/
│
├── tcl_line_processing.py
├── config.json
├── input1.tcl
├── input2.tcl
├── input1_intermediate1.tcl
├── input1_intermediate2.tcl
├── input1_output.tcl
├── input2_intermediate1.tcl
├── input2_intermediate2.tcl
└── input2_output.tcl
```

## Contributing

If you would like to contribute to this project, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to contact [your contact information].
