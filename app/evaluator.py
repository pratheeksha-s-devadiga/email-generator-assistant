import pandas as pd
from app.generator import generate_email
from app.metrics import fact_recall_score, conciseness_score, tone_score_llm
from app.test_data import TEST_SCENARIOS


def run_evaluation(model_name):
    results = []

    for scenario in TEST_SCENARIOS:
        generated = generate_email(
            scenario["intent"],
            scenario["facts"],
            scenario["tone"],
            model=model_name
        )

        # ✅ ADD THIS BLOCK RIGHT HERE
        if isinstance(generated, str) and generated.startswith("❌"):
            print(f"Skipping due to API error for intent: {scenario['intent']}")
            continue

        # Metrics calculation
        fact_score = fact_recall_score(scenario["facts"], generated)
        conc_score = conciseness_score(generated)
        tone_score = tone_score_llm(generated, scenario["tone"])

        results.append({
            "intent": scenario["intent"],
            "fact_score": fact_score,
            "conciseness": conc_score,
            "tone": tone_score
        })

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Save CSV
    df.to_csv("outputs/evaluation_results.csv", index=False)

    # Print averages
    print("\n📊 AVERAGE SCORES:")
    print("Fact Recall:", round(df["fact_score"].mean(), 2))
    print("Conciseness:", round(df["conciseness"].mean(), 2))
    print("Tone:", round(df["tone"].mean(), 2))