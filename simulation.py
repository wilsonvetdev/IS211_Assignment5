import argparse 
import csv 

class Server: 

    def __init__(self, requests = []):
        self.current_request = None
        self.requests = requests
        self.time_remaining = 0

    def tick(self, request):
        if self.current_request != None:
            self.time_remaining = self.time_remaining - request.duration
            if self.time_remaining <= 0:
                self.current_request = None 
    
    def busy(self):
        if self.current_request != None:
            return True 
        else:
            return False 
    
    def start_next(self, new_request):
        self.current_request = new_request
        self.time_remaining = new_request.duration

class Request: 

    def __init__(self, request_time, file_name, duration):
        self.request_time = request_time
        self.file_name = file_name
        self.duration = duration 


def simulateOneServer(filename):

    server = Server()

    with open(filename) as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        for line in data_reader:
            new_request = Request(line[0], line[1], line[2])
            server.requests.append(new_request)

    while len(server.requests) != 0:
        server.current_request = server.requests.pop(0)
        print(server.current_request.request_time, server.current_request.file_name, server.current_request.duration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="csv file path", type=str, required=True)
    parser.add_argument("--servers", help="simulate multiple servers", type=str)
    args = parser.parse_args()
    
    simulateOneServer(args.file)