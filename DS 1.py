import numpy as np

# Fixed dataset: 32 students, 4 subjects
# For demonstration, I’ll repeat the earlier 4-student block 8 times
student_scores = np.array([
    [85, 78, 92, 74],  # Student 1
    [88, 82, 79, 85],  # Student 2
    [90, 76, 88, 80],  # Student 3
    [70, 85, 84, 90],  # Student 4
] * 8)  # Repeat 8 times to make 32 students

# Calculate average score per subject (column-wise)
averages = np.mean(student_scores, axis=0)

# Identify subject with highest average
subjects = ["Math", "Science", "English", "History"]
max_index = np.argmax(averages)

# Display results
print("Average scores per subject:")
for subj, avg in zip(subjects, averages):
    print(f"{subj}: {avg:.2f}")

print("\nSubject with highest average:", subjects[max_index])
