#I decided not to use this class for now.


class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = "hub"
        self.delivery_time = datetime

    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, "
                f"City: {self.city}, State: {self.state}, Zip: {self.zip}, "
                f"Deadline: {self.deadline}, Weight: {self.weight}, "
                f"Status: {self.status}, Delivery Time: {self.delivery_time}")

    def update_status(self, status):
        if status == "hub" or status == "en route" or status == "delivered":
            self.status = status
        else:
            raise ValueError("Invalid status. Must be 'hub', 'en route', or 'delivered'.")
    
    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time