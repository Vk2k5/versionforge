def summarize_feedback(feedback_data):

    top_scores = sorted(feedback_data, key=lambda x: x[2], reverse=True)[:5]

    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for _, _, score in feedback_data:
        if score >= 90:
            grade_count["A"] += 1
        elif score >= 80:
            grade_count["B"] += 1
        elif score >= 70:
            grade_count["C"] += 1
        elif score >= 60:
            grade_count["D"] += 1
        else:
            grade_count["F"] += 1

    return top_scores, grade_count
