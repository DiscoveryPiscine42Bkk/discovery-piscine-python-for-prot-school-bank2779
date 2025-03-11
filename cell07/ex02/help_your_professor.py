def average(scores):
    if not scores:
        return 0  # Handle case with no students
    return sum(scores.values()) / len(scores)

# Dictionaries with student scores
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Display the average scores
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
