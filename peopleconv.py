import argparse
import os

# A dictionary that contains the allowed children for each tag
allowed_map = {
    'person': ['T', 'A', 'F'],
    'family': ['T', 'A'],
    'people': ['P'],
    'address': [],
    'phone': [],
}

# Maps the tag to the XML tag
tag_map = {
    'P': 'person',
    'T': 'phone',
    'A': 'address',
    'F': 'family',
}

# Maps the tag to the data fields
field_map = {
    'P': ['firstname', 'lastname'],
    'T': ['mobile', 'landline'],
    'A': ['street', 'city', 'postcode'],
    'F': ['name', 'born'],
}

def convert_people_file(filepath, output, force=False):
    if not force and os.path.exists(output):
        print(f'Output file already exists: {output}! Use --force to overwrite')
        return
    
    # The file will always start with a <people> tag
    xml_lines = ['<people>']
    # Stack keeps track of the current open tags
    stack = ['people']
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                line_data = line.split('|')
                line_key = line_data[0].strip()
                
                if line_key not in tag_map.keys():
                    raise ValueError(f'Unexpected start of line: {line_key}')
                
                # Close tags until the current tag is allowed
                while stack and line_key not in allowed_map[stack[-1]]:
                    xml_lines.append(f'</{stack.pop()}>')
                    
                # If the stack is empty, the file is invalid (eg. a phone number without a person)
                if not stack:
                    raise ValueError(f'Unexpected start of line: {line_key}')
                
                open_tag = tag_map[line_key]
                xml_lines.append(f'<{open_tag}>')
                stack.append(open_tag)

                for i, field in enumerate(field_map[line_key], start=1):
                    if len(line_data) > i:
                        xml_lines.append(f'<{field}>{line_data[i].strip()}</{field}>')
           
        # Close all open tags
        while stack:
            xml_lines.append(f'</{stack.pop()}>')
        
        # Write the XML to the output file
        with open(output, 'w') as file:
            file.write('\n'.join(xml_lines))
            file.write('\n')
    
    except FileNotFoundError:
        print(f'File not found: {filepath}')
    except IOError as e:
        print(f'Error reading file: {e}')

def main():
    parser = argparse.ArgumentParser(
        prog='PeopleFileConverter',
        description='Converts a line-separated file of people to an XML file',
    )
    
    parser.add_argument('filepath', help='The path to the file to convert')
    parser.add_argument('--output', help='The path to the output file', default='people.xml')
    parser.add_argument('--force', help='Overwrite the output file if it exists', action='store_true')
    args = parser.parse_args()
    convert_people_file(args.filepath, args.output, args.force)
    
if __name__ == '__main__':
    main()