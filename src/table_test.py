def write_table_to_file(data, filename):
    """Write data in a table-like format to a text file."""
    with open(filename, 'w') as file:
        # Write the header row
        header = ['Name', 'Age', 'Country']
        file.write('{:<15}{:<10}{:<15}\n'.format(*header))

        # Write the data rows
        for row in data:
            file.write('{:<15}{:<10}{:<15}\n'.format(*row))


if __name__ == '__main__':
    data = [
        ['John', '25', 'USA'],
        ['Emily', '30', 'Canada'],
        ['Michael', '28', 'Australia']
    ]
    write_table_to_file(data, 'table.txt')
