import csv
from collections import Counter

def show_dashboard():
    schedule = []
    try:
        with open('final_schedule.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                schedule.append(row)
    except FileNotFoundError:
        print("Error: 'final_schedule.csv' not found. Please run scheduler.py first!")
        return

    print("==========================================")
    print("      PLACEMENT COORDINATOR DASHBOARD     ")
    print("==========================================")
    print(f"Total Interviews Scheduled: {len(schedule)}\n")

    # Count interviews per company
    companies = [item['CompanyName'] for item in schedule]
    company_counts = Counter(companies)
    
    print("--- Interviews per Company ---")
    for comp, count in company_counts.items():
        print(f"  {comp}: {count} interviews")

    # Count interviews per day
    days = [item['Day'] for item in schedule]
    day_counts = Counter(days)
    
    print("\n--- Interviews per Day ---")
    for day, count in day_counts.items():
        print(f"  {day}: {count} interviews")
    print("==========================================")

if __name__ == '__main__':
    show_dashboard()
