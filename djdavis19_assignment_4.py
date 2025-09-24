student_name = 'Dante Davis'
# Define starting stats
# GPA input (float)
current_gpa = float(input("Enter your current GPA (1.0 - 4.0): "))

# Study hours input (int)
study_hours = int(input("Enter your weekly study hours: "))

# Social points input (int)
social_points = int(input("Enter your social points: "))

# Stress level input (int)
stress_level = int(input("Enter your stress level (0 - 100): "))



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
    print(" Invalid input. Please choose Calm, Chill, or Time to lock in.")
    exit()

# Starting stats
current_gpa = 3.2
social_points = 50

# List of valid study options
study_options = ["Programming", "Math", "English", "History"]

# Show options to user
print(" Choose a study focus from the following:")
print(", ".join(study_options))

# Get user input / CoPilot supported
chosen_subject = input("Enter your study focus: ").strip().title()

# Validate choice using membership operator
if chosen_subject in study_options:
    print(f"\n You chose: {chosen_subject}")

    # Apply logic based on subject and GPA
    if chosen_subject == "Programming" and current_gpa >= 3.0:
        current_gpa = current_gpa + 0.1
        social_points =  social_points - 5
    elif chosen_subject == "Math" and (current_gpa < 3.0 or social_points < 40):
        current_gpa = current_gpa + 0.2
        social_points = social_points - 10
    elif chosen_subject == "English" and not current_gpa < 2.5:
        current_gpa = current_gpa + 0.05
        social_points = social_points + 5
    elif chosen_subject == "History" and current_gpa >= 3.5 and social_points >= 60:
        current_gpa = current_gpa + 0.15
        social_points = social_points + 10
    else:
        print(" No major stat change for this combo.")
else:
    print("\n Invalid choice. Please select a valid subject from the list.")
    exit()

# Clamp GPA to max 4.0
if current_gpa > 4.0:
    current_gpa = 4.0

# Display updated stats
print("\n Updated Stats:")
print(f"• Current GPA: {current_gpa:.2f}")
print(f"• Social Points: {social_points}")