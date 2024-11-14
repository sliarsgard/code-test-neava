# PeopleFileConverter

`PeopleFileConverter` is a command-line tool that converts a line based text file of people data into an XML format.

## Installation
Download the executable file `peopleconv.exe` in `/dist`.

## Usage
```
peopleconv.exe <filepath> [--output OUTPUT] [--force]
```

### Arguments
* `<filepath>`: The path to the input file.
* `--output OUTPUT`: (Optional) The path to the output XML file. Defaults to `people.xml`.
* `--force`: (Optional) Overwrites the output file if it already exists.

## Input File Format
The input file should follow a format where each line starts with a tag followed by pipe-separated (`|`) fields.
The following tags are supported:
- `P` (Person): Can include fields `firstname` and `lastname`
- `T` (Phone): Can include fields `mobile` and `landline`
- `A` (Address): Can include fields `street`, `city` and `postcode`
- `F` (Family): Can include fields `name` and `born`

### Sample Input File
```
P|Carl Gustaf|Bernadotte
T|0768-101801|08-101801
A|Drottningholms slott|Stockholm|10001
F|Victoria|1977
```

### Sample Output XML
```xml
<people>
    <person>
        <firstname>Carl Gustaf</firstname>
        <lastname>Carl Gustaf</lastname>
        <phone>
            <mobile>0768-101801</mobile>
            <landline>08-101801</landline>
        </phone>
        <address>
            <street>Drottningholms slott</street>
            <city>Stockholm</city>
            <postcode>10001</postcode>
        </address>
        <family>
            <name>Victoria</name>
            <born>1977</born>
        </family>
    </person>
</people>
```
