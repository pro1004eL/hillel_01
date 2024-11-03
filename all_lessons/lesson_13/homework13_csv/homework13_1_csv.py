import csv


unique_rows = set()

def read_csv_file(file):
    with open(file) as f:
        reader = list(csv.reader(f))

        global headers
        headers = reader[0]
        reader_rows = reader[1:]

        for row in reader_rows:
            unique_rows.add(tuple(row))


read_csv_file('r-m-c.csv')
read_csv_file('rmc.csv')


with open('file_without_duplicates.csv', 'w', newline='') as f_no_d:
    writer = csv.writer(f_no_d)
    writer.writerow(headers)
    for row in unique_rows:
        writer.writerow(row)

