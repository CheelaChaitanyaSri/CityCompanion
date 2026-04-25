# main.py - central entry point
# Combines Safety System + Security System + Community Tab

from src.safety_system.safety import check_listing, log_alert
from src.security_system.security import detect_misuse, log_event
from src.community_management.community import community_tab

def run_checks():
    """Run initial safety + security checks."""
    rental_type = input("Enter type of rental (car, house, shop, etc.): ").strip()
    price = float(input("Enter listing price: "))
    avg_price = float(input("Enter average market price: "))
    verified_input = input("Is the listing verified? (yes/no): ").strip().lower()
    verified = (verified_input == "yes")
    description = input("Enter listing description: ").strip()

    # Safety check
    score = check_listing(price, avg_price, verified)
    log_alert(rental_type, score)

    # Security check
    if detect_misuse(description):
        print("🚨 Security Alert: Misuse detected in description!")
        log_event("Misuse detected", description)
    else:
        print("✅ Description is safe.")

def main_menu():
    """Main CLI menu for City Companion."""
    while True:
        print("\n=== City Companion ===")
        print("1. Safety System")
        print("2. Security System")
        print("3. Community")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_checks()
        elif choice == "2":
            desc = input("Enter description to check misuse: ")
            if detect_misuse(desc):
                print("🚨 Security Alert: Misuse detected!")
                log_event("Misuse detected", desc)
            else:
                print("✅ Description is safe.")
        elif choice == "3":
            community_tab()   # Community tab includes posts + friends
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
