This document details the AI tools and prompts used for the Week 1 genome assembly deliverable. All AI assistance was used for educational purposes and to accelerate the learning process.

AI Tools Used

Chat Gpt 
Purpose: Code conversion from Python to Codon, debugging, and algorithm explanation
Version: ChatGPT-4
Usage Context: Help with Codon syntax, type annotations, and troubleshooting

Prompt 1: Initial Setup Assistance
I need to set up a bioinformatics project structure with the following directory layout:
.github/workflows/
week1/{code,data,test}
week2/
How should I organize this and set up GitHub CI/CD?

Prompt 2: Genome Assembler Understanding
I have this Python genome assembler code from a Chinese GitHub repository. Can you help me understand how to run it and what the main components do?

I need to create a Bash script that:
1. Runs Python genome assembler on datasets data1-data4
2. Runs Codon version on the same datasets
3. Measures runtime and extracts N50 values
4. Outputs a comparison table

Can you help me create this evaluation script?

Here are my results:
Python: data1=11s, data2=22s, data3=25s, data4=765s
Codon: data1=3s, data2=3s, data3=3s, data4=13s

How should I interpret these results and what conclusions can I draw?
