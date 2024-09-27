class Reservation:
    def __init__(self, name, phone, email, gender, payment_method):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.payment_method = payment_method
        self.hotel_booking = None  # Store hotel booking details

    def add_hotel_booking(self, hotel_name, nights, price_per_night):
        self.hotel_booking = {
            "hotel_name": hotel_name,
            "nights": nights,
            "price_per_night": price_per_night,
            "total_cost": nights * price_per_night
        }

    def display_details(self):
        details = (f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\n"
                   f"Gender: {self.gender}\nPayment Method: {self.payment_method}")
        if self.hotel_booking:
            details += (f"\n\nHotel Booking Details:\nHotel: {self.hotel_booking['hotel_name']}\n"
                        f"Nights: {self.hotel_booking['nights']}\nTotal Cost: Rs.{self.hotel_booking['total_cost']}")
        return details


class AthleticFieldReservationSystem:
    def __init__(self):
        self.slots = {}  # To hold slot reservations
        self.offers = ["10% off for groups of 5 or more", "Free water bottle with every reservation"]

    def show_slots(self):
        print("Available Slots:")
        for slot, reservation in self.slots.items():
            if reservation is None:
                print(slot)
        print("Special Offers:")
        for offer in self.offers:
            print(offer)

    def reserve_slot(self, slot):
        if slot in self.slots and self.slots[slot] is None:
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            gender = input("Enter your gender: ")
            payment_method = input("Enter your payment method: ")
            
            reservation = Reservation(name, phone, email, gender, payment_method)
            self.slots[slot] = reservation
            
            # Ask for hotel booking
            self.offer_hotel_booking(reservation)

            print("Reservation details:")
            print(reservation.display_details())
            confirm = input("Are these details correct? (yes/no): ")
            if confirm.lower() == 'yes':
                print("Slot reserved successfully!")
            else:
                print("Reservation canceled.")
                self.slots[slot] = None
        else:
            print("Slot is already reserved or does not exist.")

    def cancel_reservation(self, slot):
        if slot in self.slots and self.slots[slot] is not None:
            self.slots[slot] = None
            print(f"Reservation for slot {slot} has been canceled.")
        else:
            print("No reservation found for this slot.")

    def modify_reservation(self, slot):
        if slot in self.slots and self.slots[slot] is not None:
            reservation = self.slots[slot]
            print("Current Reservation Details:")
            print(reservation.display_details())
            new_slot = input("Enter new slot: ")
            if new_slot in self.slots and self.slots[new_slot] is None:
                self.slots[new_slot] = reservation
                self.slots[slot] = None
                print(f"Reservation has been moved to {new_slot}.")
            else:
                print("New slot is not available.")
        else:
            print("No reservation found for this slot.")

    def show_reservation_details(self, slot):
        if slot in self.slots and self.slots[slot] is not None:
            print("Reservation Details:")
            print(self.slots[slot].display_details())
        else:
            print("No reservation found for this slot.")

    def show_hotel_reservation(self):
        print("Hotel Reservation Options:")
        print("1. Hotel A - Rs.1500/night")
        print("2. Hotel B - Rs.1100/night")
        print("3. Hotel C - Rs.1800/night")

    def offer_hotel_booking(self, reservation):
        book_hotel = input("Would you like to book a hotel along with your reservation? (yes/no): ")
        if book_hotel.lower() == 'yes':
            self.show_hotel_reservation()
            hotel_choice = input("Choose a hotel (1/2/3): ")

            if hotel_choice == '1':
                hotel_name = "Hotel A"
                price_per_night = 1500
            elif hotel_choice == '2':
                hotel_name = "Hotel B"
                price_per_night = 1100
            elif hotel_choice == '3':
                hotel_name = "Hotel C"
                price_per_night = 1800
            else:
                print("Invalid choice, no hotel booked.")
                return

            nights = int(input("How many nights would you like to book? "))
            reservation.add_hotel_booking(hotel_name, nights, price_per_night)
            print(f"Hotel {hotel_name} booked successfully for {nights} nights at Rs.{price_per_night}/night.")

def main():
    system = AthleticFieldReservationSystem()
    system.slots = {
        "2024-09-30 10:00": None,
        "2024-09-30 12:00": None,
        "2024-09-30 15:00": None,
        "2024-09-30 18:00": None,
        "2024-09-30 21:00": None,
    }

    while True:
        print("\nWelcome to the Athletic Field Reservation System")
        print("1. Show Slots")
        print("2. Reserve Slot")
        print("3. Cancel Reservation")
        print("4. Modify Reservation")
        print("5. Show Reservation Details")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            system.show_slots()
        elif choice == '2':
            slot = input("Enter the slot you want to reserve (e.g., 2024-09-30 10:00): ")
            system.reserve_slot(slot)
        elif choice == '3':
            slot = input("Enter the slot you want to cancel: ")
            system.cancel_reservation(slot)
        elif choice == '4':
            slot = input("Enter the current slot you want to modify: ")
            system.modify_reservation(slot)
        elif choice == '5':
            slot = input("Enter the slot to show details: ")
            system.show_reservation_details(slot)
        elif choice == '6':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
