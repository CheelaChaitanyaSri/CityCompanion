import json
def run_smart_assistant():
    with open("CityCompanion/city_data.json", "r") as file:   # FIXED path
        data = json.load(file)
    print("Welcome to CityCompanion Assistant!")
    print("Ask anything about hospitals, transport, routes, police, or helplines.")
    print("Type 'exit' to stop.\n")
    while True:
        user_input = input("Ask: ").lower().strip()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "":
            continue
        elif "hospital" in user_input:
            print("\nHospitals:")
            for h in data["hospitals"]:
                print(h["name"], "-", h["address"])
                print("Phone:", h["contact"])
                print("Map:", h["map_link"])
                print("Timings: 24/7 (assumed)")
                print()
        elif "rule" in user_input:
            print("\nCity Rules:")
            for r in data["city_rules"]:
                print("-", r)
        elif ("bus" in user_input or
              "way" in user_input or
              "go" in user_input or
              "how to" in user_input):
            found = False
            clean_input = user_input.replace("-", "").replace(" ", "")
            for route in data.get("transport_routes", []):
                destination = route["to"].lower().replace("-", "").replace(" ", "")
                if destination in clean_input:
                    print("\nRoute Found:")
                    print("From:", route["from"])
                    print("To:", route["to"])
                    print("Bus Numbers:", ", ".join(route["bus_numbers"]))
                    found = True
                    break
            if not found:
                print("Sorry, I don't have info yet.")
        elif "transport" in user_input:
            print("\nTransport Info:")
            for t in data["transport_info"]:
                print("-", t)
        elif "police" in user_input:
            print("\nPolice Stations:")
            for p in data["police_stations"]:
                print(p["name"], "-", p["address"])
                print("Phone:", p["contact"])
                print("Map:", p["map_link"])
                print()
        elif "helpline" in user_input or "number" in user_input:
            print("\nHelplines:")
            for h in data["helplines"]:
                print(h["service"], "-", h["number"])
        elif any(word in user_input for word in data["faqs"]):
            for key, value in data["faqs"].items():
                if key in user_input:
                    print("\n", value)
        elif "city" in user_input:
            print("\nYou can travel using buses or metro.")
            print("Check 'transport' for more details.")
        else:
            print("Sorry, I don't have info yet.")
if __name__ == "__main__":
    run_smart_assistant()