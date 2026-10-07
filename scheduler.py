import csv

def load_data():
    # Load Students
    students = []
    with open('students.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['CGPA'] = float(row['CGPA'])
            students.append(row)
            
    # Load Companies
    companies = []
    with open('companies.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['CGPACutoff'] = float(row['CGPACutoff'])
            row['MaxSlots'] = int(row['MaxSlots'])
            companies.append(row)
            
    # Load Slots
    slots = []
    with open('slots.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slots.append(row)
            
    return students, companies, slots

def generate_schedule():
    students, companies, slots = load_data()
    
    schedule = []
    student_booked_slots = set() # Keeps track of student schedules to prevent overlapping conflicts (e.g., ("S001", "SL001"))
    
    slot_index = 0
    
    print("Processing scheduling algorithm...")
    
    for company in companies:
        comp_id = company['CompanyID']
        comp_name = company['CompanyName']
        cutoff = company['CGPACutoff']
        target_dept = company['TargetDepartment']
        max_slots = company['MaxSlots']
        
        assigned_count = 0
        
        for student in students:
            if assigned_count >= max_slots:
                break # Company slots are full
                
            student_id = student['StudentID']
            
            # Check eligibility: CGPA match and Department match
            if student['CGPA'] >= cutoff and student['Department'] == target_dept:
                
                # Find an available time slot for this student
                while slot_index < len(slots):
                    current_slot = slots[slot_index]
                    slot_id = current_slot['SlotID']
                    
                    # Conflict check: ensure student is free in this slot
                    conflict_key = (student_id, slot_id)
                    if conflict_key not in student_booked_slots:
                        # Book the slot
                        student_booked_slots.add(conflict_key)
                        schedule.append({
                            'StudentID': student_id,
                            'StudentName': student['Name'],
                            'CompanyID': comp_id,
                            'CompanyName': comp_name,
                            'SlotID': slot_id,
                            'Day': current_slot['Day'],
                            'Time': f"{current_slot['StartTime']} - {current_slot['EndTime']}"
                        })
                        assigned_count += 1
                        break
                    
                    slot_index += 1
                    
        # Reset slot index slightly for the next company to distribute interviews fairly if needed
        slot_index = max(0, slot_index - len(students) // 2)

    # Save final schedule to a CSV file
    with open('final_schedule.csv', mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['StudentID', 'StudentName', 'CompanyID', 'CompanyName', 'SlotID', 'Day', 'Time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(schedule)
        
    print(f"Scheduling complete! Successfully generated {len(schedule)} interviews. Saved to 'final_schedule.csv'.")

if __name__ == '__main__':
    generate_schedule()
