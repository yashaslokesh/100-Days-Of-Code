import time

print("Press S to start stopwatch, and press Enter to lap... Press Ctrl+C to quit")
start = input()

if start.strip().lower() == "s":
    start_time = time.time()
    most_recent_time = time.time() # Initialize to be the starting time

    laps = 1

    try:
        while True:
            lap_key = input()
            if lap_key.strip().lower() == "l":
                lap_time = time.time() - most_recent_time
                total = time.time() - start_time
                print(f"Lap {laps} lasted for {lap_time} seconds and {total} seconds have elapsed so far") 
                laps += 1
                most_recent_time = time.time() # Set to the time once lap is signalled
    except KeyboardInterrupt:
        total = time.time() - start_time
        print(f"The stopwatch lasted for {total} seconds and had {laps} laps")
