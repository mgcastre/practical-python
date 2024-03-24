# fileparse.py
# Exercise 3.3 to 3.7
# M. G. Castrellon
# 24 March 2024

import csv

def parse_csv(lines, select=None, types=None,
              has_headers=True, delimiter=",",
              silence_errors=False):
    '''
    Parse a csv file into a list of records with type conversion.
    '''
    
    # Raise an exception is both select and has_headers=False
    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")

    # Read all rows in the lines
    rows = csv.reader(lines, delimiter=delimiter)

    # Read file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices 
    # for filtering and set output columns
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    
    # Create an empty list to hold the data
    records = []

    for rowno, row in enumerate(rows, 1):
        if not row: # Skip rows with no data
            continue

        # If specific column indices are selected, 
        # pick them out
        if select:
            row = [row[index] for index in indices]
        
        # Perform the type conversion for the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue
        
        # Make a dictionary or a tupple
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        
        # Append record to list of records
        records.append(record)
        
    # Return list of records
    return records