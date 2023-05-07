""" This module extracts nonogram data from an inputted notation string."""
# nonogram notation 1.
'2, 1,, 2, 1, 3,, 7,, 1, 3,, 2, 1.: 2,, 2, 1,, 1, 1,, 3,, 1, 1,, 1, 1,, 2,, 1, 1,, 1, 2,, 2,;'

""" each value ends with a comma. Each group (column or row) ends with a double-comma. 
    All COLUMNS are listed first, and then a colon, then all ROWS are listed 
    
    Can count how many periods are before each semicolon to know how many rows/columns are in the picross grid."""


def all_columns(notation):
    """ return a list of all columns. From the notation.
    [ [2, 1], [2, 1, 3], [7], [1, 3], [2, 1] ]"""
    column_data = notation.replace(' ', '').split(':')[0]
    column_data = column_data.split(',,')

    column_list = []
    for each_column in column_data:
        new_column = each_column.split(',')
        for index in range(0, len(new_column)):
            new_column[index] = int(new_column[index])

        column_list.append(new_column)

    return column_list


def all_rows(notation):
    """ return a list of all rows. From the notation.
    [ [2], [2, 1], [1, 1], [3], [1, 1], [1, 1], [2], [1, 1], [1, 2], [2] ]"""
    row_data = notation.replace(' ', '').split(':')[1]
    row_data = row_data.split(',,')

    row_list = []
    for each_row in row_data:
        new_row = each_row.split(',')
        for index in range(0, len(new_row)):
            new_row[index] = int(new_row[index])

        row_list.append(new_row)

    return row_list
