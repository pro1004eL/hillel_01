import csv


def read_csv_file(file):
    with open(file) as f:
        reader = list(csv.reader(f))
        header = reader[0]
        return header, reader[1:]


unique_rows = set()
header, data = read_csv_file('r-m-c.csv')
unique_rows.update(set(tuple(row) for row in data))
header_2, data_2 = read_csv_file('rmc.csv')
unique_rows.update(set(tuple(row) for row in data_2))


with open('file_without_duplicates.csv', 'w', newline='') as f_no_d:
    writer = csv.writer(f_no_d)
    writer.writerow(header)
    for row in unique_rows:
        writer.writerow(row)

