import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.load import load
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

# Initialize Rich Console
console = Console()

# 1. Load the local .env file residing in this folder
load_dotenv(override=True)

# Verify API key is present
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY not found in the local .env file.")
    sys.exit(1)

# 2. Initialize the chat model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 3. Define options data
papers = [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
]

styles = ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]

lengths = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)",
]

def display_menu(title: str, options: list[str]):
    """Helper to display a numbered table menu using Rich"""
    table = Table(title=title, title_style="bold cyan", border_style="blue")
    table.add_column("No.", justify="right", style="bold yellow", width=6)
    table.add_column("Option", style="green")

    for idx, option in enumerate(options, 1):
        table.add_row(str(idx), option)

    console.print(table)

def get_user_choice(max_val: int) -> int:
    """Prompt the user for a valid choice number"""
    while True:
        try:
            choice = console.input(
                f"[bold green]Select an option (1-{max_val}) ➜ [/bold green] "
            ).strip()
            if choice.lower() in ["exit", "quit", "q"]:
                console.print(
                    "\n[bold yellow]Exiting Research Explainer. Goodbye![/bold yellow]"
                )
                sys.exit(0)

            val = int(choice)
            if 1 <= val <= max_val:
                return val - 1  # Return zero-indexed position
            console.print(
                f"[bold red]Please enter a valid number between 1 and {max_val}.[/bold red]"
            )
        except ValueError:
            console.print(
                "[bold red]Invalid input. Please enter a number.[/bold red]"
            )

console.print(
       Align.center(
        Panel.fit(
            "[bold cyan]📚 AI Research Paper Explainer[/bold cyan]\n[dim]Interactive CLI Tool[/dim]",
            border_style="blue",
        )
    )
)

# Step 1: Select Paper
console.print()
display_menu("Research Papers", papers)
paper_idx = get_user_choice(len(papers))
selected_paper = papers[paper_idx]

# Step 2: Select Style
console.print()
display_menu("Explanation Styles", styles)
style_idx = get_user_choice(len(styles))
selected_style = styles[style_idx]

# Step 3: Select Length
console.print()
display_menu("Explanation Lengths", lengths)
length_idx = get_user_choice(len(lengths))
selected_length = lengths[length_idx]

# Summary of selection
console.print(
    Panel(
        f"[bold]Paper:[/bold] {selected_paper}\n"
        f"[bold]Style:[/bold] {selected_style}\n"
        f"[bold]Length:[/bold] {selected_length}",
        title="[cyan]Your Selections[/cyan]",
        border_style="green",
    )
)

current_dir = Path(__file__).resolve().parent
file_path = current_dir / "template.json"

console.print(f"[cyan]Loading template from: {file_path}[/cyan]")

# 2. Open the JSON file and deserialize it using langchain_core.load.load
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    prompt = load(data, allowed_objects="core")

formatted_prompt = prompt.invoke({
        'paper_input': selected_paper, 
        'style_input': selected_style, 
        'length_input': selected_length
})

console.print("\n[bold magenta]💡 Generating explanation...[/bold magenta]\n")
response = model.invoke(formatted_prompt)
console.print("[bold blue]AI ➜ [/bold blue] ", end="")
console.print(Markdown(response.content))