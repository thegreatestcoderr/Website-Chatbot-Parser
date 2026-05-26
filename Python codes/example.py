import time
from contextlib import contextmanager
import functools

# 1. Generator for efficient line-by-line reading
def read_log_lines(filepath):
    """Reads a log file line by line using a generator."""
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# 2. Decorator for logging processing time
def log_processing_time(func):
    """Decorator to log the start and end time of a function's execution."""
    @functools.wraps(func)
    def wrapper(line):
        start_time = time.time()
        print(f"Processing line started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
        result = func(line)
        end_time = time.time()
        print(f"Processing line finished at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
        print(f"Processing time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# 3. A processing function that will be decorated
@log_processing_time
def process_log_line(line):
    """Simulates processing a single log line."""
    time.sleep(0.1)  # Simulate some processing time
    if "ERROR" in line:
        return f"Found an error: {line}"
    return f"Processed: {line}"

# Let's create a dummy log file for this example
def create_dummy_log(filepath, num_lines=5):
    with open(filepath, 'w') as f:
        for i in range(num_lines):
            if i == 2:
                f.write(f"Timestamp - ERROR - Something critical happened line {i+1}\n")
            else:
                f.write(f"Timestamp - INFO - This is a log message line {i+1}\n")

if __name__ == "__main__":
    log_file = "example.log"
    create_dummy_log(log_file)

    # Using the generator to iterate through the log file
    for line in read_log_lines(log_file):
        processed_output = process_log_line(line)
        if processed_output and "ERROR" in processed_output:
            print(f"Alert: {processed_output}")
        print("-" * 20)