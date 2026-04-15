# Email Generation Assistant

## Project Overview

This project implements an AI-powered Email Generation Assistant that generates professional emails based on structured user inputs:

- **Intent** – Purpose of the email (e.g., follow-up, request, apology)
- **Key Facts** – Important details to include
- **Tone** – Style of communication (formal, casual, empathetic, etc.)

The system uses a Large Language Model (LLM) with advanced prompt engineering techniques to ensure high-quality, structured, and contextually accurate outputs.

---

## Key Features

- Email generation using LLM
- Role-based prompting
- Few-shot learning for improved quality
- Streamlit-based user interface
- Custom evaluation metrics
- Automated evaluation on 10 test scenarios
- Model comparison (Few-shot vs No Few-shot)
- CSV-based evaluation results

---
## 🏗️ Project Structure

```
email-generator-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Streamlit UI
│   ├── generator.py         # Email generation logic
│   ├── prompts.py           # Prompt templates
│   ├── evaluator.py         # Evaluation logic
│   ├── metrics.py           # Custom metrics
│   ├── test_data.py         # Test scenarios
│
├── outputs/
│   └── evaluation_results.csv
│
├── run_evaluation.py        # Script to run evaluation
├── requirements.txt
├── README.md
├── .env (not included in repo)
```
---

## Setup Instructions

### 1. Clone the Repository

git clone <your-repository-link>
cd email-generator-assistant

---

### 2. Create Virtual Environment

#### Windows:

python -m venv venv
venv\Scripts\activate

#### Mac/Linux:

python3 -m venv venv
source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Add API Key

Create a `.env` file in the root folder:

OPENROUTER_API_KEY=your_api_key_here

---

## Running the Application

Run the Streamlit app:

python -m streamlit run app/main.py

Then open:

http://localhost:8501

---

## Running Evaluation

Run the evaluation script:

python run_evaluation.py

This will:

- Run all 10 test scenarios
- Generate emails using the model
- Calculate evaluation metrics
- Save results in:

outputs/evaluation_results.csv

---

## Custom Evaluation Metrics

### 1. Fact Recall Score

Measures how many input facts are correctly included in the generated email.

**Logic:**

- Compare each fact with generated email
- Score = matched facts / total facts

---

### 2. Tone Accuracy Score

Evaluates whether the generated email matches the requested tone.

**Logic:**

- Uses tone-specific keywords (e.g., "Dear", "Hi", "Sorry")
- Checks presence of appropriate tone indicators

---

### 3. Conciseness Score

Ensures the email is neither too long nor too short.

**Logic:**

- 80–150 words → Ideal (Score = 1.0)
- Slight deviation → Score = 0.7
- Too short/long → Score = 0.4

---

## 🔍 Model Comparison

Two approaches were evaluated:

### Model A:

- Role-based prompting
- Few-shot examples

### Model B:

- No few-shot prompting

### Result:

Model A performed better across all metrics:

- Higher fact inclusion
- Better tone consistency
- More structured output

---

## Example Output

Subject: Request for Leave

Hi Team,

I would like to inform you that I will be on leave next week for five days.
I have completed all necessary handovers to ensure a smooth workflow.

Please let me know if anything urgent arises.

Best regards,
[Your Name]

---

## Technologies Used

- Python
- Streamlit
- OpenRouter API (LLM access)
- Pandas

---

## Important Notes

- `.env` file is not included in the repository
- Do not share your API key publicly

---

## Future Improvements

- LLM-based evaluation (LLM-as-a-Judge)
- Personalization of emails
- Multi-language support
- Better tone detection using NLP models

---
