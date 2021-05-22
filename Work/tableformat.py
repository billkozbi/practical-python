# tableformat.py

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    
    raise FormatError(f'Unknown table format {fmt}')


class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


def print_table(table, columns, formatter):
    formatter.headings(columns)
    for row in table:
        row = [str(getattr(row, column)) for column in columns]
        formatter.row(row)


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for r in rowdata:
            print(f"{r:>10s}", end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    @staticmethod
    def _html_table_row(row):
        return f"<tr>{row}</tr>"

    @staticmethod
    def _html_table_header(header):
        return f"<th>{header}</th>"

    @staticmethod
    def _html_table_cell(cell):
        return f"<td>{cell}</td>"

    def headings(self, headers):
        html_header_row = self._html_table_row("".join([self._html_table_header(h) for h in headers]))
        print(html_header_row)

    def row(self, rowdata):
        html_header_row = self._html_table_row("".join([self._html_table_cell(d) for d in rowdata]))
        print(html_header_row)


