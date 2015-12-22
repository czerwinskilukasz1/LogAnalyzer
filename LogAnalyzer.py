#!/usr/bin/python
import re
import sys

patterns = []
log_file = 0
log_file_name = None
patterns_ignore_file_name = "patterns_ignore.txt"

def read_patterns():
  global patterns_ignore_file_name
  global patterns

  print ("Pattern file name: " + patterns_ignore_file_name)
  patterns_ignore = open(patterns_ignore_file_name, 'r')
  for pattern in patterns_ignore:
    pattern = pattern.rstrip('\n')
    if pattern == '':
      continue
    print("Pattern: " + pattern)	
    compiled = re.compile(pattern)
    patterns.append(compiled)
  print("Read " + str(len(patterns)) + " pattern(s)")


def open_log_file():
  global log_file
  log_file = open(log_file_name, 'r')

def display_log_file():
  global log_file
  global patterns
  print ("Check patterns: " + str(patterns))

  pattern_non_matches = 0
  pattern_matches = 0
  consecutive_pattern_matches = 0

  for line in log_file:
    line_matched = False
    for pattern in patterns:
      reg = pattern.match(line)
      # print("reg: " + str(reg))
      if reg != None:
        line_matched = True
        pattern_matches += 1
        consecutive_pattern_matches += 1
        # print("          <matched line>")
        break
    if not line_matched:
      pattern_non_matches += 1
      if consecutive_pattern_matches > 0:
        print("       <matched " + str(consecutive_pattern_matches) + " lines>")
        consecutive_pattern_matches = 0
      print(line),
  
  if consecutive_pattern_matches > 0:
    print("       <matched " + str(consecutive_pattern_matches) + " lines>")
    consecutive_pattern_matches = 0

  print("----- END OF LOG FILE -----")

  print("Total matches: " + str(pattern_matches))
  print("Total non-matches: " + str(pattern_non_matches))
        
def usage(argv):
  print("Usage: " + argv[0] + " [ [log file name] [patterns-to-ignore file name] ]")
  
def main(argv):
  global log_file_name
  global patterns_ignore_file_name

  print("Hello!")
  
  if len(argv) != 2 and len(argv) != 3:
    usage(argv)
    exit(0)

  log_file_name = argv[1]
  print("Log file name: " + log_file_name)

  if len(argv) > 2:
    patterns_ignore_file_name = argv[2]

  try:
    read_patterns()
    open_log_file()
    display_log_file()
  except Exception as e: 
    # e = sys.exc_info()[0]
    print("ERROR occured: " + str(e))
  
if __name__ == "__main__":
    main(sys.argv)

