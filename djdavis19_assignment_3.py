# PERSONAL ACADEMIC & LIFE PORTFOLIO
# Author: D’ante
# Description: Enhanced student analytics with formatted output and expanded life data

# -------------------------------
# Data Initialization
# -------------------------------

# Strings
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
major = "Computer Science"
hometown = "Charlotte, NC"
graduation_term = "Spring 2028"
home_address = "456 Oak Street, Charlotte, NC 28202"

# Lists
credit_hours_list = [3, 3, 3, 3]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]
completed_courses_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]

# Tuples
instagram_info_tuple = ("Instagram", "@jordan_codes", 312)
twitter_info_tuple = ("Twitter", "@jordandev", 127)

# Sets
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}
career_interests_set = {"Software development", "Game development", "Web development", "Data science"}

# Dictionaries
study_hours_dict = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}

monthly_budget_dict = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
}

contact_directory_dict = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}

# -------------------------------
# Calculations
# -------------------------------

total_current_credits = sum(credit_hours_list)
cumulative_gpa = round(sum(gpa_history_list) / len(gpa_history_list), 2)
completed_courses_count = len(completed_courses_list)
total_study_hours = sum(study_hours_dict.values())
academic_load = total_current_credits + total_study_hours
monthly_budget_total = sum(monthly_budget_dict.values())
daily_food_budget = round(monthly_budget_dict["Food"] / 30, 1)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget_dict["Books"] / total_study_hours, 1)
total_followers = instagram_info_tuple[2] + twitter_info_tuple[2]
current_skills_count = len(current_skills_set)
skills_to_learn_count = len(skills_to_learn_set)
contact_count = len(contact_directory_dict)
backlog_count = len(entertainment_backlog_set)
hobby_count = len(current_skills_set)

# -------------------------------
# Output Summary
# -------------------------------

print("=" * 63)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 63)
print(f"Student: {full_name} | ")
print(f"Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_term}")
print(f"Major: {major}")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across 4 courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print("⏎\nCurrent Courses:")
print("COMP 163 - 3 credits - Prof. Rhodes - M-Eric 300")
print("MATH 150 - 3 credits - Dr. Lee - Marteena 201")
print("ENG 101 - 3 credits - Dr. Martinez - Crosby 121")
print("HIS 105 - 3 credits - Dr. Brown - Crosby 210")

print("\n=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}")

print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget_dict['Food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget_dict['Entertainment']}")
print(f"Books: ${monthly_budget_dict['Books']}")
print(f"Transportation: ${monthly_budget_dict['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}")

print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: Hannah Smith (Mom) - {contact_directory_dict['Mom']}")
print(f"Home Address: {home_address}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_count} people in directory")

print("\n=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {backlog_count} items")
print(f"Current Hobbies: {hobby_count} activities")
print("=" * 63)