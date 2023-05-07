""" This class extracts from an inputted notation string."""
# nonogram notation 1.
'2, 1,. 2, 1, 3,. 7,. 1, 3,. 2, 1... 2,. 2, 1,. 1, 1,. 3,. 1, 1,. 1, 1,. 2,. 1, 1,. 1, 2,. 2, ...'

""" each value ends with a comma. Each group (column or row) ends with a period. 
    All COLUMNS are listed first, and then an ellipses (three periods), then all ROWS are listed 
    End with three periods. """


class Notation:

    def __init__(self, notation):
        self.notation = notation

    def all_columns(self):
        """ return a list of all columns. From the notation. """
        pass

    def all_rows(self):
        """return a list of all rows. From the notation. """
        pass
