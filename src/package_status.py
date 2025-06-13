def package_status(package_table):
    while True:
        try:
            package_id = int(input("Enter a package ID to check its status (1-40) or 0 to exit: "))
            if package_id == 0:
                print("Exiting program.")
                break
            if 1 <= package_id <= 40:
                package = package_table.search(package_id)
                try:
                    input_time = input("Enter a time to check the package status (format: HH:MM AM/PM, e.g., 10:00 AM): ")
                    input_time = datetime.strptime(input_time, "%I:%M %p")
                    if input_time < package[11]:
                        status = "at hub"
                    elif input_time < package[6]:
                        status = "en route"
                    else:
                        status = "delivered"
                    print(f"Package ID: {package[0]}, Status: {status}, Delivery Time: {package[6].strftime('%I:%M %p')}")
                except ValueError:
                    print("Invalid time format. Please enter the time in the format HH:MM AM/PM.")
                    continue
            else:
                print("Invalid package ID. Please enter a number between 1 and 40.")
        except ValueError:
            print("Invalid input. Please enter a valid package ID.")