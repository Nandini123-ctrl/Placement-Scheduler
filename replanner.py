import csv

def dynamic_replan(cancel_student_id=None, cancel_company_id=None, cancel_slot_id=None):
    # Load existing schedule
    schedule = []
    with open('final_schedule.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            schedule.append(row)
            
    # Load students and slots for reallocating if needed
    students = {}
    with open('students.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            students[row['StudentID']] = row
            
    print(f"Original schedule has {len(schedule)} entries.")
    
    # Track currently booked slots to avoid double-booking during replanning
    booked_slots = {(item['StudentID'], item['SlotID']) for item in schedule}
    
    new_schedule = []
    removed_count = 0
    
    # Filter out the canceled item(s)
    for item in schedule:
        is_canceled = False
        if cancel_student_id and item['StudentID'] == cancel_student_id:
            is_canceled = True
        if cancel_company_id and item['CompanyID'] == cancel_company_id:
            is_canceled = True
        if cancel_slot_id and item['SlotID'] == cancel_slot_id:
            is_canceled = True
            
        if is_canceled:
            removed_count += 1
            booked_slots.remove((item['StudentID'], item['SlotID']))
        else:
            new_schedule.append(item)
            
    print(f"Disruption applied: Removed {removed_count} interview slot(s).")
    
    # Save updated schedule
    with open('updated_schedule.csv', mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['StudentID', 'StudentName', 'CompanyID', 'CompanyName', 'SlotID', 'Day', 'Time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_schedule)
        
    print(f"Dynamic replanning complete! Updated schedule saved to 'updated_schedule.csv' with {len(new_schedule)} entries.")

if __name__ == '__main__':
    # Example simulation: Let's cancel a specific student (e.g., 'S001') to test replanning
    dynamic_replan(cancel_student_id='S001')
