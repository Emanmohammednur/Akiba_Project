student_name = input("Enter Student Name: ")
python_score = float(input("Enter Python Score: "))
english_score = float(input("Enter English Score: "))
mathematics_score = float(input("Enter Mathematics Score: "))

average = (python_score + english_score + mathematics_score) / 3

print("==================================================")
print("                  STUDENT RESULT                  ")
print("==================================================\n")

print(f"Student: {student_name}\n")

print(f"Python:       {python_score}")
print(f"English:      {english_score}")
print(f"Mathematics:  {mathematics_score}\n")

print("---------------------------------------")
print(f"Average:      {average}")
print("==================================================")

