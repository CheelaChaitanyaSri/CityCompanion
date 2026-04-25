# safety.py - Safety & Trust System (Anti-Scam Shield)

import datetime

def safety_score(price, avg_price, verified=False):
    """
    Calculate a safety score for a listing.
    - price: actual price of the listing
    - avg_price: average market price
    - verified: whether the listing is verified
    """
    score = 50
    if verified:
        score += 30
    if price <= avg_price * 1.2:
        score += 20
    return min(score, 100)

def check_listing(price, avg_price, verified):
    """
    Check a listing and print an alert based on its safety score.
    """
    score = safety_score(price, avg_price, verified)
    if score < 50:
        print("🚨 Risky listing detected!")
    elif score < 80:
        print("⚠️ Proceed with caution.")
    else:
        print("✅ Safe listing.")
    return score

def log_alert(listing_type, score):
    """
    Log the safety check result into a file for transparency.
    """
    with open("security_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {listing_type} – Score: {score}\n")

if __name__ == "__main__":
    # Example test run
    score = check_listing(price=12000, avg_price=10000, verified=False)
    log_alert("Rental Listing", score)
