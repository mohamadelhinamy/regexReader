import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)
    
    f = open(args.file, "r")
    text = f.read()
    pattern=re.finditer("[123\+\-*\/.=]{2,4}",text)
    pattern = [m.group(0) for m in pattern]
    
    f = open("task_1_4_result.txt", "w")
    for m in pattern: 
      print(m)
      f.write(m)
      f.write("\n")
      
    f.close()
    print(pattern)