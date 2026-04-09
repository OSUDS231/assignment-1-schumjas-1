seconds = int(input("Please enter the number of seconds: "))
print(f"{seconds} seconds = {seconds // 3600} hours, {(seconds % 3600) // 60} minutes, and {seconds % 60} seconds.")