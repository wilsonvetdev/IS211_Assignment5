import argparse 
import csv 

class Server: 

    def greet(self):
        print('hello')

class Request: 

    def __init__(self, request_time, file_name, duration):
        self.request_time = request_time
        self.file_name = file_name
        self.duration = duration 

def process_data(filename):
    
    with open(filename, newline='') as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        for line in data_reader:
            print(line)
            new_request = Request(line[0], line[1], line[2])
            print(new_request.request_time, new_request.file_name, new_request.duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="csv file path", type=str, required=True)
    parser.add_argument("--servers", help="simulate multiple servers", type=str)
    args = parser.parse_args()

    print(args.file)
    process_data(args.file)