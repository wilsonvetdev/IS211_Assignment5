import argparse 
import csv 



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="csv file path", type=str, required=True)
    parser.add_argument("--servers", help="simulate multiple servers", type=str)
    args = parser.parse_args()
    print(args.file)

