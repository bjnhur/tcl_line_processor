import re
import os
import json
import argparse


def remove_multiline(file_path):
    base_name, _ = os.path.splitext(file_path)
    intermediate1_path = f"{base_name}_intermediate1.tcl"
    intermediate2_path = f"{base_name}_intermediate2.tcl"
    output_path = f"{base_name}_output.tcl"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return False, None, None, None
    except Exception as e:
        print(f"Error: Unable to read file {file_path} - {e}")
        return False, None, None, None

    # Step 1: Handle backslashes and ignore lines with only spaces or tabs
    combined_lines = []
    buffer = ""
    line_number = 0

    for line in lines:
        line_number += 1
        stripped_line = line.rstrip()

        if stripped_line.endswith("\\"):
            buffer += stripped_line[:-1] + " "
        elif re.match(r"^[ \t]*$", stripped_line):
            buffer += " "
        else:
            buffer += stripped_line
            combined_lines.append(buffer)
            buffer = ""

    # Write intermediate result after backslash handling
    with open(intermediate1_path, "w") as file:
        for line in combined_lines:
            file.write(line + "\n")

    # Step 2: Handle nested braces and combine multiline contents
    single_line_script = []
    buffer = ""
    inside_braces = 0

    for line in combined_lines:
        stripped_line = line.strip()

        if "{" in stripped_line:
            inside_braces += stripped_line.count("{")
        if "}" in stripped_line:
            inside_braces -= stripped_line.count("}")

        buffer += stripped_line + " "

        if inside_braces == 0:
            single_line_script.append(buffer.strip())
            buffer = ""

    # Write intermediate result after brace handling
    with open(intermediate2_path, "w") as file:
        for line in single_line_script:
            file.write(line + "\n")

    # Step 3: Check for unexpected line breaks in [] or ()
    for i, line in enumerate(single_line_script):
        if ("[" in line and "]" not in line) or ("(" in line and ")" not in line):
            print(f"Error: Unexpected line break at {file_path}:{i+1}")
            return False, None, None, None

    # Remove multiple spaces
    single_line_script = [re.sub(r"\s+", " ", line) for line in single_line_script]

    with open(output_path, "w") as file:
        for line in single_line_script:
            file.write(line + "\n")

    return True, intermediate1_path, intermediate2_path, output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process TCL files based on a JSON configuration.")
    parser.add_argument("config_file", type=str, help="Path to the JSON configuration file")
    args = parser.parse_args()

    try:
        with open(args.config_file, "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found - {args.config_file}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in the configuration file - {args.config_file}")
        exit(1)
    except Exception as e:
        print(f"Error: Unable to read configuration file {args.config_file} - {e}")
        exit(1)

    file_list = config.get("file_list", [])

    if not file_list:
        print("No files to process. Please provide a list of files in the configuration.")
        exit(1)

    for input_file in file_list:
        print(f"Processing {input_file}...")
        success, intermediate1_file, intermediate2_file, output_file = remove_multiline(input_file)
        if success:
            print(f"Processed script has been saved to {output_file}")
            print(f"Intermediate results saved to {intermediate1_file} and {intermediate2_file}")
        else:
            print(f"Processing failed for {input_file} due to unexpected line breaks or file errors.")
