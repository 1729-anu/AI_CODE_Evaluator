from app.evaluator import evaluate_versions

if __name__ == "__main__":
    print("AI Code Evaluator Interface")
    version_1 = input("Enter AI-generated Code Version 1:\n")
    version_2 = input("Enter AI-generated Code Version 2:\n")
    feedback = evaluate_versions(version_1, version_2)
    print("\nEvaluation Result:")
    print(feedback)
