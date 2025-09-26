import ollama
from jinja2 import Template

prompts = [
    'A farmer has 17 sheep. All but 9 run away. How many sheep does the farmer still have?',
    'What is 7 mod 2?',
    'Explain the Monty Hall problem and why switching doors increases your chances.',
    'Write a short, polite email to a professor asking for an extension on a project due to illness.',
    'List three key differences between Python and VBA.',
    'Write a Python function that takes a list of numbers and returns the average, ignoring any None values.',
    'You are a sarcastic assistant.  What’s the best way to study for finals?',
    'Explain recursion using only words that start with the letter R.',
    'When did C. Shane Reese become president of BYU?',
    'Write a short poem about a creature that doesn’t exist.'
]

models = [
    "llama3", 
    "mistral", 
    "phi3",
    "gemma3",
    "gemma3:270m",
    'qwen:0.5b'
]

def run_prompt(model_name, prompt_text):
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt_text}])
    return response['message']['content']

results = []

for prompt in prompts:
    for model in models:
        print(f'Model {model}, prompt {prompt}')
        output = run_prompt(model, prompt)
        results.append({
            "model": model,
            "prompt": prompt,
            "output": output
        })

template = Template("""
<html>
<head><title>Ollama Model Comparison</title></head>
<body>
<h1>Model Comparison Results</h1>
{% for item in results %}
  <h2>{{ item.prompt }}</h2>
  <p><strong>Model:</strong> {{ item.model }}</p>
  <p><strong>Output:</strong> {{ item.output }}</p>
  <hr>
{% endfor %}
</body>
</html>
""")

with open("ollama_comparison.html", "w", encoding="utf-8") as f:
    f.write(template.render(results=results))

