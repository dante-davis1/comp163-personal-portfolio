# Step 1: Foundation Setup
student_name = "Dante Davis"  # Replace with your name
current_gpa = 3.2             # Float between 1.0-4.0
study_hours = 25              # Integer
social_points = 50            # Integer
stress_level = 40             # Integer 0-100


# Welcome message
print(f"\n Welcome, {student_name}, to your Academic Wellness Tracker!")
print("Starting Stats:")
print(f"• GPA: {current_gpa}")
print(f"• Weekly Study Hours: {study_hours}")
print(f"• Social Points: {social_points}")
print(f"• Stress Level: {stress_level}/100")

# Step 2: Course Planning Decision
print("\nChoose your course load:")
print("A) Calm (12 credits)")
print("B) Chill (15 credits)")
print("C) Locked in (18 credits)")
course_choice = input("Your choice: ").upper() # AI Generated

if course_choice == "A":
    if current_gpa >= 3.5:
        study_hours = study_hours - 3
        stress_level = stress_level - 5
    else:
        study_hours = study_hours - 1
        stress_level = stress_level - 2
elif course_choice == "B":
    if current_gpa >= 3.0:
        study_hours = study_hours + 2
        stress_level = stress_level + 5
    else:
        study_hours = study_hours + 4
        stress_level = stress_level + 8
elif course_choice == "C":
    if current_gpa >= 3.5:
        study_hours = study_hours + 5
        stress_level = stress_level + 10
    else:
        study_hours = study_hours + 8
        stress_level = stress_level + 15
else:
    print("Invalid course load choice.")
    exit()

# Step 3: Study Strategy Decision
study_options = ["Programming", "Math", "English", "History"]
print("\nChoose your study focus:", ", ".join(study_options))
chosen_subject = input("Your choice: ").title() # AI Generated

if chosen_subject not in study_options:
    print("Invalid study choice. Exiting program.")
    exit()
else:
    if (chosen_subject == "Programming" and current_gpa >= 3.0) or (chosen_subject == "Math" and social_points < 40):
        current_gpa = current_gpa + 0.1
        social_points = social_points - 5
    elif chosen_subject == "English" and current_gpa < 3.0:
        current_gpa = current_gpa + 0.05
        social_points = social_points + 3
    elif chosen_subject == "History" or stress_level > 60:
        current_gpa = current_gpa + 0.07
        social_points = social_points + 5
    else:
        print("No major change for this study choice.")

# Step 4: Final Semester Assessment
# Type checking using identity operators
if type(current_gpa) is not float or type(study_hours) is not int:
    print("Type error: GPA must be float and study_hours must be int.")
    exit()

# Nested logic for multiple endings
if current_gpa >= 3.5:
    if study_hours >= 30 and stress_level <= 60:
        ending = " Outstanding! Dean’s List potential."  # AI generated
    elif stress_level > 80:
        ending = " Excellent GPA but stress is high. Self-care needed."  # AI generated
    else:
        ending = "Strong academic performance, keep balanced."  # AI generated
elif current_gpa >= 2.5:
    if study_hours < 20 and social_points > 60:
        ending = " Social butterfly! Moderate GPA."  # AI generated
    elif stress_level > 70:
        ending = " Moderate GPA with high stress. Refocus required."  # AI generated
    else:
        ending = " Steady progress, maintain effort."  # AI generated
else:
    if study_hours < 15 or stress_level > 85:
        ending = " Academic risk zone. Seek support!"  # AI generated
    else:
        ending = " Recovery mode: potential is there, stay consistent."  # AI generated

# Final statistics display
print("\nFinal Statistics:")
print(f"• GPA: {current_gpa:.2f}")
print(f"• Study Hours: {study_hours}")
print(f"• Social Points: {social_points}")
print(f"• Stress Level: {stress_level}/100")
print(f"\n🏁 Outcome: {ending}")


