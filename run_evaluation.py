from app.evaluator import run_evaluation

print("Running Model A...")
run_evaluation("openrouter/auto")

print("Running Model B...")
run_evaluation("openai/gpt-3.5-turbo")