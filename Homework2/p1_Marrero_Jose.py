# Name: Jose Marrero
# Z Number = Z23816617


# Step A

def line_number(in_file: str, out_file: str):
    """
    The function reads the first file and saves a copy in the
    second file, adding a number at the beginning of each line.
    """
    try:
        input_file = open(in_file, 'r')
        output_file = open(out_file, 'w')

        line_count_int = 1
        for line_str in input_file:
            output_file.write(f"{line_count_int}. {line_str}")
            line_count_int += 1

        input_file.close()
        output_file.close()

    except FileNotFoundError:
        print("The input file does not exist.")
        raise


# Step B

def parse_functions(filename: str):
    """The function takes a Python filename and reads it to find the functions defined inside.
    It returns a tuple of tuples, each containing the function’s starting line number,
    name, parameter list as text, and full code as text with empty lines and comments removed.
    """
    try:
        with open(filename, 'r') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print("The input file does not exist.")
        raise

    parsed_f = []
    i = 0
    total = len(lines)

    while i < total:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("def ") and "(" in stripped and ":" in stripped:
            start = i + 1
            indent = len(line) - len(line.lstrip())

            def_pos = line.find("def ")
            paren_start = line.find("(", def_pos)
            paren_end = line.rfind(")")

            f_name = line[def_pos +4:paren_start].strip()
            params = line[paren_start +1:paren_end].strip()

            code_ls = []
            j = i 
            while j < total:
                current_line = lines[j]
                current_stripped = current_line.strip()

                if j > i and current_stripped:
                    current_indent = len(current_line) - len(current_line.lstrip())
                    if current_indent <= indent:
                        break 

                if current_stripped and not current_stripped.startswith("#"):
                    code_ls.append(current_line.rstrip())

                j += 1

            final_code = "\n".join(code_ls)
            parsed_f.append((start, f_name, params, final_code))
            i = j - 1

        i += 1 
    parsed_f.sort(key=lambda item: item[1])
    return tuple(parsed_f)

def main():
    in_str = "p1_Marrero_Jose.py"
    out_str = "p1_Marrero_Jose.py.txt"

    line_number(in_str, out_str)

    functions = parse_functions(in_str)

    print(f"Parsed {len(functions)} function(s):")
    for func in functions:
        print(func)

if __name__ == "__main__":
    main()