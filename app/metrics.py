import re

def fact_recall_score(facts, generated_email):
    facts_list = [f.strip().lower() for f in facts.split(";")]
    match_count = sum(1 for f in facts_list if f in generated_email.lower())
    return match_count / len(facts_list)


def conciseness_score(email):
    word_count = len(email.split())
    if word_count < 80:
        return 1.0
    elif word_count < 150:
        return 0.7
    else:
        return 0.4


def tone_score_llm(email, expected_tone):
    # Simplified heuristic (FREE alternative)
    if expected_tone.lower() in email.lower():
        return 1.0
    return 0.6