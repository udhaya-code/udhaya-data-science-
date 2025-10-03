import pandas as uk
import matplotlib.pyplot as ud
uh = uk.read_csv('gender_submission.csv')
print(uk)
Total_Pass = uh["Survived"].value_counts()
total = len(uh)
non_survivors = Total_Pass[0]  # Assuming 0 = non-survivor
perc = (non_survivors / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind='bar', color=["green", "red"])
ud.xlabel("Survival Status (0 = No, 1 = Yes)")
ud.ylabel("Number of People")
ud.title("Titanic survival")
ud.xticks(rotation=0)
ud.show()