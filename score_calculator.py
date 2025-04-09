# features/score_calculator.py

def compute_average_score(scores):
    """Computes the average score from a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

if __name__ == "__main__":
    student_scores = [85, 90, 78, 92, 88]
    average = compute_average_score(student_scores)
    print(f"The average score is: {average}")

    empty_scores = []
    average_empty = compute_average_score(empty_scores)
    print(f"The average of an empty list is: {average_empty}")
