import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records

    :param select: list of column names to select
    :param types: list of type conversion functions
    :param has_headers: tell the function if file has headers
    :param delimiter: delimiter character
    :param silence_errors: print or do not print errors 
    '''

    if select and not has_headers:
        raise RuntimeError("If there are no headers in the data you cannot use select.")

    def log(s): 
        if not silence_errors: 
            print(s)

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=delimiter)

        if has_headers:
            headers = next(csv_reader)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = [headers[i] for i in indices]
        
        records = []
        for row_number, row in enumerate(csv_reader, start=1):
            if not row:
                continue

            if select:
                local_row = [row[i] for i in indices]
            else:
                local_row = row

            if types:
                try:
                    local_row = [f(v) for v, f in zip(local_row, types)]
                except ValueError as e:
                    log(f"[Row {row_number}] couldn't convert: {local_row}")
                    log(f"[Row {row_number}] reason: {e}")
                    continue

            if has_headers:
                record = dict(zip(headers, local_row))
            else:
                record = tuple(local_row)

            records.append(record)
        
        return records
        


