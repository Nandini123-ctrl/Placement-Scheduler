import csv
import random

# 1. Generate Students Data
departments = ['CSE', 'ECE', 'EEE', 'Mechanical', 'Civil']
first_names = ['Aarav', 'Ananya', 'Rohan', 'Priya', 'Vikram', 'Neha', 'Arjun', 'Sneha', 'Karan', 'Pooja']
last_names = ['Sharma', 'Verma', 'Patel', 'Reddy', 'Iyer', 'Gupta', 'Kumar', 'Das', 'Mehta', 'Nair']

students = []
for student_id in range(1, 101):  # 100 students
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    dept = random.choice(departments)
    cgpa = round(random.uniform(6.0, 10.0), 2)
    students.append([f"S{student_id:03d}", name, dept, cgpa])

with open('students.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['StudentID', 'Name', 'Department', 'CGPA'])
    writer.writerows(students)

# 2. Generate Companies Data
company_names = ['TechCorp', 'InnoSoft', 'DataVantage', 'AlphaSolutions', 'NextGen Systems', 'CodeCraft']
companies = []
for i, comp_name in enumerate(company_names, start=1):
    comp_id = f"C{i:02d}"
    cgpa_cutoff = round(random.uniform(6.5, 8.0), 1)
    max_slots = random.randint(15, 30)
    target_dept = random.choice(departments)
    companies.append([comp_id, comp_name, cgpa_cutoff, max_slots, target_dept])

with open('companies.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['CompanyID', 'CompanyName', 'CGPACutoff', 'MaxSlots', 'TargetDepartment'])
    writer.writerows(companies)

# 3. Generate Time Slots Data
slots = []
slot_id = 1
for day in range(1, 4):  # 3 days of placements
    for hour in range(9, 17):  # 9 AM to 5 PM
        if hour == 13: # Lunch break
            continue
        start_time = f"{hour:02d}:00"
        end_time = f"{hour+1:02d}:00"
        slots.append([f"SL{slot_id:03d}", f"Day {day}", start_time, end_time])
        slot_id += 1

with open('slots.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['SlotID', 'Day', 'StartTime', 'EndTime'])
    writer.writerows(slots)

print("Dataset generated successfully: students.csv, companies.csv, slots.csv created!")
