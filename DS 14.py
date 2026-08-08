import matplotlib.pyplot as plt

study_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.scatter(study_time, exam_scores, color='purple')
plt.title("Study Time vs Exam Scores")
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.show()
