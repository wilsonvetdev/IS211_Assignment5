import argparse 
import csv 

class Server: 

    def greet(self):
        print('hello')

class Request: 

    def greet(self):
        print('hello')

def process_data(filename):
    
    with open(filename, newline='') as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',')
        for line in data_reader:
            print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="csv file path", type=str, required=True)
    parser.add_argument("--servers", help="simulate multiple servers", type=str)
    args = parser.parse_args()

    print(args.file)
    process_data(args.file)

    server = Server()
    server.greet()
    request = Request()
    request.greet()