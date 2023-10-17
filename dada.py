import json

# Input and output file paths
input_file_path = 'backup.json'
output_file_path = 'cleaned_backup.json'

def is_utf8(s):
    try:
        s.decode('utf-8-sig')  # Use 'utf-8-sig' to handle BOM if present
        return True
    except UnicodeDecodeError:
        return False

def find_lines_with_non_utf8(input_path):
    problematic_lines = []
    with open(input_path, 'rb') as input_file:
        for line_number, line in enumerate(input_file, start=1):
            if not is_utf8(line):
                problematic_lines.append(line_number)
    return problematic_lines

def clean_json(input_path, output_path):
    problematic_lines = find_lines_with_non_utf8(input_path)
    if problematic_lines:
        print("Problematic lines with non-UTF-8 data found on lines:", problematic_lines)
        return

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        data = input_file.readlines()

    cleaned_data = [line for line in data if is_utf8(line)]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(cleaned_data)

if __name__ == '__main__':
    clean_json(input_file_path, output_file_path)
