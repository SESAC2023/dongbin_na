score_table = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

n = 20
summary = 0
total_credit = 0

for i in range(20):
    title, credit, score = input().split(" ")
    if score == "P": continue
    credit = float(credit)
    total_credit += credit
    summary += score_table[score] * credit

print(summary / total_credit)
