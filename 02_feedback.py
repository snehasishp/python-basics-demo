# Collecting user feedback
feedback = ["Great service", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Adding duplicate feedback
feedback.append("Very satisfied")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")

# Remove duplicate feedback
feedback.remove("Very satisfied")

# Counting positive feedback
positive_feeback_count = sum(1 for comment in feedback if "great" in comment.lower()
                             or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feeback_count}")

# Printing all feedback
print("Updated User Feedback:")
for comment in feedback:
    print(f"- {comment}")
