import pandas as pd

score_board = {
    "students": [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
    ],
    "scores": [85, 92, 78, 88, 91, 76, 94, 83, 79, 87],
}


data = pd.DataFrame(score_board)
print(data)

# create a CSV file !
data.to_csv('student_scoreboard.csv')