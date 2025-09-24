student_name = 'Dante Davis'
# Define starting stats
current_gpa = 3.2         # Float between 1.0 and 4.0
study_hours = 25          # Integer (e.g., hours per week)
social_points = 50        # Integer (e.g., social engagement score)
stress_level = 70         # Integer between 0 and 100

# Display welcome message with stats (Copilot supported code)
print(" Welcome to your Academic Wellness Tracker!")
print("Here are your starting stats:")
print(f"• Current GPA: {current_gpa}")
print(f"• Weekly Study Hours: {study_hours}")
print(f"• Social Points: {social_points}")
print(f"• Stress Level: {stress_level}/100")


course_load = input("Enter your choice (Calm/Chill/Time to lock in): ").strip().lower()

if course_load == "calm":
    if current_gpa >= 3.0:
        study_hours -= 5
        stress_level -= 10
    else:
        study_hours -= 2
        stress_level -= 5
elif course_load == "chill":
    if current_gpa >= 3.0:
        study_hours += 0
        stress_level += 5
    else:
        study_hours += 3
        stress_level += 10
elif course_load == "time to lock in":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 15
    else:
        study_hours += 15
        stress_level += 25
else:
    print("❌ Invalid input. Please choose Calm, Chill, or Time to lock in.")
    exit()