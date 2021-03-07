import argparse 
import csv 

class Server: 

    def __init__(self):
        self.current_task = None
        self.time_remaining = 0


class Request: 

    def __init__(self, request_time, file_name, duration):
        self.request_time = request_time
        self.file_name = file_name
        self.duration = duration 


def simulateOneServer(filename):
    
    with open(filename, newline='') as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        for line in data_reader:
            new_request = Request(line[0], line[1], line[2])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="csv file path", type=str, required=True)
    parser.add_argument("--servers", help="simulate multiple servers", type=str)
    args = parser.parse_args()
    
    simulateOneServer(args.file)