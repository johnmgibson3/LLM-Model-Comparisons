LLM Model Comparisons ￼

This project benchmarks and compares the outputs of multiple Large Language Models (LLMs) using the Ollama ↗ API. It runs a set of diverse prompts through several open-source models—including Llama 3, Mistral, Phi-3, Gemma, and Qwen—and collects their responses. The results are rendered into an HTML report for easy side-by-side analysis.

Features:
 • Runs a suite of reasoning, math, code, and creative prompts across multiple LLMs.
 • Uses the Ollama Python API for local or remote model inference.
 • Outputs results to a clean, readable HTML file using Jinja2 templating.
 • Easily extensible: add more prompts or models as needed.

Requirements:
 • Python 3.8+
 • Ollama Python package ↗
 • Jinja2 ↗

Usage:
 1. Install dependencies:
‎`pip install ollama jinja2`
 2. Ensure Ollama is running and the desired models are available.
  `ollama pull {model-name}`
 3. Run the script:
‎`python your_script.py`
 4. Open ‎`ollama_comparison.html` to view the results.
