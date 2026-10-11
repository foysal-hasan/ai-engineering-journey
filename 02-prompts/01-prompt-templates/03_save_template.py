import json
from pathlib import Path
from langchain_core.load import dumpd
from langchain_core.prompts import PromptTemplate
from rich.console import Console

console = Console()

template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
        1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
        2. Analogies:
            - Use relatable analogies to simplify complex ideas. If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.

    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
)

console.print("[cyan]Saving template to current folder...[/cyan]")

# Serialize the prompt template into a JSON-compatible dictionary using dumpd
template_dict = dumpd(template)

current_dir = Path(__file__).resolve().parent
file_path = current_dir / "template.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(template_dict, f, indent=2)

console.print("[bold green]Completed! Saved as template.json[/bold green]")