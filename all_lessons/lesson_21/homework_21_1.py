from datetime import datetime, timedelta


def analyze_heartbeat_log():

    with open('hblog.txt', 'r') as file:
        rows = file.readlines()

    filtered_log = []
    for row in rows:
        if 'TSTFEED0300|7E3E|0400' in row:
            filtered_log.append(row)

    timestamps = []
    for line in filtered_log:
        ts_index = line.find('Timestamp')

        if ts_index != -1:
            ts_str = line[ts_index + 10:ts_index + 18]

            try:
                timestamps.append(datetime.strptime(ts_str, "%H:%M:%S"))

            except ValueError:
                print(f"Error matching timestamp '{ts_str}' in line: {line.strip()}")

    timestamps.sort()  # обовязково сортуємо timestamps!!!, щоб забезпечити хронологічний порядок


    with open('hb_test.log', 'w') as log_file:
        for i in range(1, len(timestamps)):
            diff = timestamps[i] - timestamps[i - 1]
            diff_seconds = diff.total_seconds()

            if 31 < diff_seconds < 33:
                log_file.write(f"{timestamps[i].time()} heartbeat is {diff_seconds} seconds: WARNING\n")

            elif diff_seconds >= 33:
                log_file.write(f"{timestamps[i].time()} heartbeat is {diff_seconds} seconds: ERROR\n")

    print('Results written to hb_test.log file.')


analyze_heartbeat_log()
