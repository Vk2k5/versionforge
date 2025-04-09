# features/feedback_entry.py

def collect_feedback():
    """Collects student feedback."""
    feedback = {}
    student_id = input("Enter your student ID: ")
    feedback['student_id'] = student_id
    feedback['subject'] = input("Enter the subject name: ")
    feedback['comments'] = input("Enter your feedback/comments: ")
    # You might want to add more specific questions here, e.g., ratings for different aspects.
    # For simplicity, we are just collecting general comments.
    print("Thank you for your feedback!")
    return feedback

if __name__ == "__main__":
    student_feedback = collect_feedback()
    print("Collected feedback:", student_feedback)
