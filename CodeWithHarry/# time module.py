#  time module
import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.strftime("%Y;%m;%d   %H:%M:%S",time.localtime()))
# print(time.gmtime())

timestamp=int(time.strftime("%H",time.localtime()))
if(timestamp<12):
    print("good morning")
elif(timestamp<16):
    print("good afternoon")
elif(timestamp<20):
    print("good evening")
else:
    print("good night")





"""
The time module in Python provides various time-related functions to work with time and date. It is part of Python's standard library and is useful for tasks like measuring execution time, pausing program execution, or working with timestamps.

Here’s a quick overview of some commonly used functions in the time module:

1. Getting the Current Time
time.time(): Returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC).
Copy the code
import time
current_time = time.time()
print("Current time in seconds since epoch:", current_time)

2. Formatting Time

time.ctime(): Converts a time expressed in seconds since the epoch to a readable string.

Copy the code
readable_time = time.ctime()
print("Readable time:", readable_time)


time.strftime(format, t): Formats a time tuple or struct_time into a string based on the specified format.

Copy the code
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("Formatted time:", formatted_time)

3. Pausing Execution
time.sleep(seconds): Suspends execution of the program for the specified number of seconds.
Copy the code
print("Waiting for 3 seconds...")
time.sleep(3)
print("Done waiting!")

4. Working with Time Tuples

time.localtime(): Returns the current local time as a struct_time object.

Copy the code
local_time = time.localtime()
print("Local time:", local_time)


time.gmtime(): Returns the current UTC time as a struct_time object.

Copy the code
utc_time = time.gmtime()
print("UTC time:", utc_time)

5. Measuring Execution Time

time.perf_counter(): Provides a high-resolution timer for measuring short durations.

Copy the code
start = time.perf_counter()
# Simulate some work
time.sleep(2)
end = time.perf_counter()
print(f"Elapsed time: {end - start} seconds")


time.process_time(): Measures CPU time used by the process.

Copy the code
start = time.process_time()
# Simulate some work
for _ in range(1000000):
    pass
end = time.process_time()
print(f"CPU time used: {end - start} seconds")

6. Parsing Time
time.strptime(string, format): Parses a string representing time into a struct_time object.
Copy the code
time_string = "2025-06-10 12:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("Parsed time:", parsed_time)


These are just a few highlights of the time module. It’s a versatile tool for handling time-related tasks in Python!
"""