class TravelManagementSystem:
    def __init__(self, budget):
        """Initializes the travel management system with a given budget."""
        self.budget = budget
        self.expenses = 0
        self.travel_plan = {
            "destination": None,
            "flight": None,
            "car_rental": None,
            "tours": [],
        }

    def check_budget(self):
        """Checks if there is enough budget left."""
        return self.budget - self.expenses

    def choose_travel(self):
        """Choose a travel destination."""
        destinations = ["Paris", "London", "America", "Europe"]
        print("Available Destinations: Paris, London, America, Europe")
        destination = input("Enter your travel destination: ")
        if destination in destinations:
            self.travel_plan["destination"] = destination
            print(f"Destination chosen: {destination}")
        else:
            print("Invalid destination. Please choose from the available options.")

    def book_flights(self):
        """Books a flight if it's within the budget."""
        flight_options = {
            "Air India": 600,
            "Indigo": 400,
            "British Airways": 700
        }
        print("Available Flights: Air India, Indigo, British Airways")
        flight_choice = input("Choose your flight (Air India, Indigo, British Airways): ")

        if flight_choice in flight_options:
            flight_cost = flight_options[flight_choice]
            if self.check_budget() >= flight_cost:
                self.travel_plan["flight"] = flight_choice
                self.expenses += flight_cost
                print(f"Flight booked with {flight_choice}! Cost: ${flight_cost}")
            else:
                print("Insufficient budget for flight.")
        else:
            print("Invalid flight choice. Please choose from the available options.")

    def book_car_rental(self):
        """Books a car rental if it's within the budget."""
        car_rental_options = {
            "Economy": 50,
            "SUV": 100,
            "Luxury": 150
        }
        print("Available Car Rentals: Economy, SUV, Luxury")
        car_choice = input("Choose your car rental (Economy, SUV, Luxury): ")

        if car_choice in car_rental_options:
            rental_cost = car_rental_options[car_choice]
            if self.check_budget() >= rental_cost:
                self.travel_plan["car_rental"] = car_choice
                self.expenses += rental_cost
                print(f"Car rental booked: {car_choice}. Cost: ${rental_cost}")
            else:
                print("Insufficient budget for car rental.")
        else:
            print("Invalid car rental choice. Please choose from the available options.")

    def book_tour(self):
        """Books a tour if it's within the budget."""
        tour = input("Enter the tour you'd like to book (e.g., Guided Tour, Night Tour): ")
        tour_cost = float(input(f"Enter the cost for '{tour}': $"))
        if self.check_budget() >= tour_cost:
            self.travel_plan["tours"].append((tour, tour_cost))
            self.expenses += tour_cost
            print(f"Tour '{tour}' booked! Cost: ${tour_cost}")
        else:
            print("Insufficient budget for this tour.")

    def add_money(self):
        """Adds extra money to the budget."""
        amount = float(input("Enter the amount you'd like to spend extra: $"))
        self.budget += amount
        print(f"${amount} saved! New budget: ${self.budget}")

    def display_plan(self):
        """Displays the full travel plan and expenses."""
        print("\n--- Travel Plan ---")
        print(f"Destination: {self.travel_plan['destination']}")
        print(f"Flight: {self.travel_plan['flight'] if self.travel_plan['flight'] else 'Not booked yet'}")
        print(f"Car Rental: {self.travel_plan['car_rental'] if self.travel_plan['car_rental'] else 'Not booked yet'}")
        print("Tours:")
        for tour, cost in self.travel_plan["tours"]:
            print(f"  - {tour}: ${cost}")
        print(f"Total Expenses: ${self.expenses}")
        print(f"Remaining Budget: ${self.check_budget()}")
        print("---------------------")


# Main function to run the travel system
def main():
    print("Welcome to the Travel Management System!")
    initial_budget = float(input("Enter your initial budget: $"))

    travel_system = TravelManagementSystem(budget=initial_budget)

    while True:
        print("\nPlease choose an option:")
        print("1. Choose travel destination")
        print("2. Book flight")
        print("3. Book car rental")
        print("4. Book tour")
        print("5. add extra money")
        print("6. Display travel plan")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            travel_system.choose_travel()
        elif choice == "2":
            travel_system.book_flights()
        elif choice == "3":
            travel_system.book_car_rental()
        elif choice == "4":
            travel_system.book_tour()
        elif choice == "5":
            travel_system.add_money()
        elif choice == "6":
            travel_system.display_plan()
        elif choice == "7":
            print("Thank you for using the Travel Management System!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
