#!/usr/bin/env python3
"""
Generate step-based animated SVG diagrams with TTS narration for AI-ML Semester 6 topics.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

BASE_PATH = Path("/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/ai-ml/sem-6")

# Color schemes by purpose
COLORS = {
    "concept": {"primary": "#4A90E2", "secondary": "#E8F4FF", "accent": "#2E5C8A"},
    "process": {"primary": "#50C878", "secondary": "#E8F8EE", "accent": "#2E7D4F"},
    "architecture": {"primary": "#9B59B6", "secondary": "#F4E8F8", "accent": "#6B3A86"},
    "algorithm": {"primary": "#E67E22", "secondary": "#FDF2E7", "accent": "#B85E16"},
    "data": {"primary": "#3498DB", "secondary": "#EBF5FB", "accent": "#21618C"},
    "network": {"primary": "#1ABC9C", "secondary": "#E8F8F5", "accent": "#117864"},
    "security": {"primary": "#E74C3C", "secondary": "#FDEDEC", "accent": "#B03A2E"},
}

def get_topic_color_scheme(topic_name: str, module: str) -> Dict[str, str]:
    """Determine color scheme based on topic and module."""
    topic_lower = topic_name.lower()

    if any(word in topic_lower for word in ["architecture", "structure", "framework", "model"]):
        return COLORS["architecture"]
    elif any(word in topic_lower for word in ["algorithm", "learning", "training", "optimization"]):
        return COLORS["algorithm"]
    elif any(word in topic_lower for word in ["process", "flow", "pipeline", "steps"]):
        return COLORS["process"]
    elif any(word in topic_lower for word in ["network", "distributed", "node", "blockchain"]):
        return COLORS["network"]
    elif any(word in topic_lower for word in ["security", "crypto", "authentication", "key"]):
        return COLORS["security"]
    elif any(word in topic_lower for word in ["data", "analysis", "statistics", "dataset"]):
        return COLORS["data"]
    else:
        return COLORS["concept"]

def create_nlp_bigram_svg() -> str:
    """Generate SVG for Bigram topic."""
    return '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .step { opacity: 0; }
      .step.active { opacity: 1; transition: opacity 0.5s; }
      text { font-family: Arial, sans-serif; }
      .title { font-size: 24px; font-weight: bold; fill: #2C3E50; }
      .label { font-size: 16px; fill: #34495E; }
      .sublabel { font-size: 14px; fill: #7F8C8D; }
    </style>
  </defs>

  <g class="step" data-step="1" data-narration="A bigram is a sequence of two consecutive words used in natural language processing to model word relationships.">
    <text x="400" y="50" class="title" text-anchor="middle">Bigram Model in NLP</text>
    <rect x="300" y="150" width="200" height="80" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="5"/>
    <text x="400" y="195" class="label" text-anchor="middle">Input Text</text>
  </g>

  <g class="step" data-step="2" data-narration="First, the input text is tokenized into individual words by splitting on whitespace and punctuation.">
    <rect x="300" y="280" width="200" height="80" fill="#E8F8EE" stroke="#50C878" stroke-width="2" rx="5"/>
    <text x="400" y="325" class="label" text-anchor="middle">Tokenization</text>
    <path d="M 400 230 L 400 280" stroke="#2E5C8A" stroke-width="2" marker-end="url(#arrowhead)"/>
  </g>

  <g class="step" data-step="3" data-narration="The tokenized words are then processed to extract all consecutive word pairs, forming bigrams.">
    <rect x="150" y="410" width="150" height="60" fill="#FDF2E7" stroke="#E67E22" stroke-width="2" rx="5"/>
    <text x="225" y="445" class="label" text-anchor="middle">Bigram 1</text>
    <rect x="325" y="410" width="150" height="60" fill="#FDF2E7" stroke="#E67E22" stroke-width="2" rx="5"/>
    <text x="400" y="445" class="label" text-anchor="middle">Bigram 2</text>
    <rect x="500" y="410" width="150" height="60" fill="#FDF2E7" stroke="#E67E22" stroke-width="2" rx="5"/>
    <text x="575" y="445" class="label" text-anchor="middle">Bigram 3</text>
    <path d="M 400 360 L 225 410" stroke="#2E7D4F" stroke-width="2"/>
    <path d="M 400 360 L 400 410" stroke="#2E7D4F" stroke-width="2"/>
    <path d="M 400 360 L 575 410" stroke="#2E7D4F" stroke-width="2"/>
  </g>

  <g class="step" data-step="4" data-narration="Each bigram is counted to determine its frequency in the corpus, creating a probability distribution.">
    <rect x="100" y="510" width="100" height="40" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="3"/>
    <text x="150" y="535" class="sublabel" text-anchor="middle">Count: 5</text>
    <rect x="250" y="510" width="100" height="40" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="3"/>
    <text x="300" y="535" class="sublabel" text-anchor="middle">Count: 8</text>
    <rect x="400" y="510" width="100" height="40" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="3"/>
    <text x="450" y="535" class="sublabel" text-anchor="middle">Count: 3</text>
    <rect x="550" y="510" width="100" height="40" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="3"/>
    <text x="600" y="535" class="sublabel" text-anchor="middle">Count: 6</text>
  </g>

  <g class="step" data-step="5" data-narration="The resulting bigram model can predict the next word given the current word, useful for text generation and language modeling.">
    <rect x="250" y="100" width="300" height="120" fill="none" stroke="#9B59B6" stroke-width="3" stroke-dasharray="5,5" rx="10"/>
    <text x="400" y="80" class="label" text-anchor="middle" fill="#9B59B6">Bigram Language Model</text>
  </g>

  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E5C8A"/>
    </marker>
  </defs>
</svg>'''

def create_ml_types_svg() -> str:
    """Generate SVG for Machine Learning Types."""
    return '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .step { opacity: 0; }
      .step.active { opacity: 1; transition: opacity 0.5s; }
      text { font-family: Arial, sans-serif; }
      .title { font-size: 24px; font-weight: bold; fill: #2C3E50; }
      .label { font-size: 16px; fill: #34495E; }
      .sublabel { font-size: 13px; fill: #7F8C8D; }
    </style>
  </defs>

  <g class="step" data-step="1" data-narration="Machine learning can be categorized into three main types based on how the algorithm learns from data.">
    <text x="400" y="40" class="title" text-anchor="middle">Types of Machine Learning</text>
  </g>

  <g class="step" data-step="2" data-narration="Supervised learning uses labeled training data where both input features and desired outputs are provided to the algorithm.">
    <rect x="50" y="100" width="200" height="140" fill="#E8F4FF" stroke="#4A90E2" stroke-width="3" rx="8"/>
    <text x="150" y="130" class="label" text-anchor="middle" font-weight="bold">Supervised</text>
    <text x="150" y="155" class="sublabel" text-anchor="middle">Labeled Data</text>
    <circle cx="120" cy="190" r="8" fill="#50C878"/>
    <text x="135" cy="195" class="sublabel">Input → Output</text>
    <text x="150" y="220" class="sublabel" text-anchor="middle">Examples:</text>
    <text x="150" y="235" class="sublabel" text-anchor="middle">Classification</text>
  </g>

  <g class="step" data-step="3" data-narration="Unsupervised learning works with unlabeled data, finding hidden patterns and structure without predefined outputs.">
    <rect x="300" y="100" width="200" height="140" fill="#E8F8EE" stroke="#50C878" stroke-width="3" rx="8"/>
    <text x="400" y="130" class="label" text-anchor="middle" font-weight="bold">Unsupervised</text>
    <text x="400" y="155" class="sublabel" text-anchor="middle">Unlabeled Data</text>
    <circle cx="370" cy="190" r="8" fill="#E67E22"/>
    <text x="385" cy="195" class="sublabel">Find Patterns</text>
    <text x="400" y="220" class="sublabel" text-anchor="middle">Examples:</text>
    <text x="400" y="235" class="sublabel" text-anchor="middle">Clustering</text>
  </g>

  <g class="step" data-step="4" data-narration="Reinforcement learning trains an agent through trial and error, receiving rewards or penalties based on its actions.">
    <rect x="550" y="100" width="200" height="140" fill="#FDF2E7" stroke="#E67E22" stroke-width="3" rx="8"/>
    <text x="650" y="130" class="label" text-anchor="middle" font-weight="bold">Reinforcement</text>
    <text x="650" y="155" class="sublabel" text-anchor="middle">Reward-Based</text>
    <circle cx="620" cy="190" r="8" fill="#9B59B6"/>
    <text x="635" cy="195" class="sublabel">Agent ↔ Env</text>
    <text x="650" y="220" class="sublabel" text-anchor="middle">Examples:</text>
    <text x="650" y="235" class="sublabel" text-anchor="middle">Game AI</text>
  </g>

  <g class="step" data-step="5" data-narration="Supervised learning includes regression for continuous outputs and classification for discrete categories.">
    <rect x="50" y="280" width="90" height="50" fill="#D6EAF8" stroke="#3498DB" stroke-width="2" rx="5"/>
    <text x="95" y="310" class="sublabel" text-anchor="middle">Regression</text>
    <rect x="160" y="280" width="90" height="50" fill="#D6EAF8" stroke="#3498DB" stroke-width="2" rx="5"/>
    <text x="205" y="305" class="sublabel" text-anchor="middle">Classification</text>
    <path d="M 150 240 L 95 280" stroke="#4A90E2" stroke-width="2"/>
    <path d="M 150 240 L 205 280" stroke="#4A90E2" stroke-width="2"/>
  </g>

  <g class="step" data-step="6" data-narration="Unsupervised learning includes clustering to group similar data and dimensionality reduction to simplify complex datasets.">
    <rect x="300" y="280" width="90" height="50" fill="#D5F4E6" stroke="#1ABC9C" stroke-width="2" rx="5"/>
    <text x="345" y="310" class="sublabel" text-anchor="middle">Clustering</text>
    <rect x="410" y="280" width="90" height="50" fill="#D5F4E6" stroke="#1ABC9C" stroke-width="2" rx="5"/>
    <text x="455" y="303" class="sublabel" text-anchor="middle">Dimension</text>
    <text x="455" y="318" class="sublabel" text-anchor="middle">Reduction</text>
    <path d="M 400 240 L 345 280" stroke="#50C878" stroke-width="2"/>
    <path d="M 400 240 L 455 280" stroke="#50C878" stroke-width="2"/>
  </g>

  <g class="step" data-step="7" data-narration="Reinforcement learning uses value-based methods to estimate action quality and policy-based methods to learn optimal strategies.">
    <rect x="550" y="280" width="90" height="50" fill="#FADBD8" stroke="#E74C3C" stroke-width="2" rx="5"/>
    <text x="595" y="310" class="sublabel" text-anchor="middle">Value-Based</text>
    <rect x="660" y="280" width="90" height="50" fill="#FADBD8" stroke="#E74C3C" stroke-width="2" rx="5"/>
    <text x="705" y="310" class="sublabel" text-anchor="middle">Policy-Based</text>
    <path d="M 650 240 L 595 280" stroke="#E67E22" stroke-width="2"/>
    <path d="M 650 240 L 705 280" stroke="#E67E22" stroke-width="2"/>
  </g>

  <g class="step" data-step="8" data-narration="Each learning type suits different problems: supervised for prediction, unsupervised for exploration, and reinforcement for sequential decision-making.">
    <rect x="150" y="380" width="500" height="180" fill="#F4E8F8" stroke="#9B59B6" stroke-width="2" rx="10"/>
    <text x="400" y="410" class="label" text-anchor="middle" font-weight="bold">Key Differences</text>
    <text x="170" y="440" class="sublabel">Supervised: Known outcomes, predictive tasks</text>
    <text x="170" y="465" class="sublabel">Unsupervised: Unknown structure, exploratory analysis</text>
    <text x="170" y="490" class="sublabel">Reinforcement: Sequential decisions, goal-oriented</text>
    <text x="170" y="525" class="sublabel" fill="#9B59B6">Choose based on: data availability, problem type, goal</text>
  </g>
</svg>'''

def create_blockchain_consensus_svg() -> str:
    """Generate SVG for Blockchain Consensus."""
    return '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .step { opacity: 0; }
      .step.active { opacity: 1; transition: opacity 0.5s; }
      text { font-family: Arial, sans-serif; }
      .title { font-size: 24px; font-weight: bold; fill: #2C3E50; }
      .label { font-size: 16px; fill: #34495E; }
      .sublabel { font-size: 13px; fill: #7F8C8D; }
    </style>
  </defs>

  <g class="step" data-step="1" data-narration="Consensus is the process by which nodes in a distributed blockchain network agree on a single version of truth.">
    <text x="400" y="40" class="title" text-anchor="middle">Blockchain Consensus</text>
  </g>

  <g class="step" data-step="2" data-narration="Multiple nodes in the network each maintain a copy of the blockchain ledger.">
    <circle cx="200" cy="150" r="40" fill="#E8F8F5" stroke="#1ABC9C" stroke-width="3"/>
    <text x="200" y="155" class="label" text-anchor="middle">Node 1</text>
    <circle cx="400" cy="150" r="40" fill="#E8F8F5" stroke="#1ABC9C" stroke-width="3"/>
    <text x="400" y="155" class="label" text-anchor="middle">Node 2</text>
    <circle cx="600" cy="150" r="40" fill="#E8F8F5" stroke="#1ABC9C" stroke-width="3"/>
    <text x="600" y="155" class="label" text-anchor="middle">Node 3</text>
  </g>

  <g class="step" data-step="3" data-narration="When a new transaction occurs, it must be validated and agreed upon by the network.">
    <rect x="330" y="230" width="140" height="60" fill="#FDEDEC" stroke="#E74C3C" stroke-width="2" rx="5"/>
    <text x="400" y="255" class="label" text-anchor="middle">New</text>
    <text x="400" y="275" class="label" text-anchor="middle">Transaction</text>
    <path d="M 200 190 L 360 230" stroke="#1ABC9C" stroke-width="2" stroke-dasharray="5,5"/>
    <path d="M 400 190 L 400 230" stroke="#1ABC9C" stroke-width="2" stroke-dasharray="5,5"/>
    <path d="M 600 190 L 440 230" stroke="#1ABC9C" stroke-width="2" stroke-dasharray="5,5"/>
  </g>

  <g class="step" data-step="4" data-narration="Consensus mechanisms ensure agreement through four key properties: validity, agreement, termination, and integrity.">
    <rect x="50" y="340" width="150" height="80" fill="#E8F4FF" stroke="#4A90E2" stroke-width="2" rx="5"/>
    <text x="125" y="370" class="label" text-anchor="middle">Agreement</text>
    <text x="125" y="390" class="sublabel" text-anchor="middle">All nodes reach</text>
    <text x="125" y="405" class="sublabel" text-anchor="middle">same decision</text>

    <rect x="225" y="340" width="150" height="80" fill="#E8F8EE" stroke="#50C878" stroke-width="2" rx="5"/>
    <text x="300" y="370" class="label" text-anchor="middle">Validity</text>
    <text x="300" y="390" class="sublabel" text-anchor="middle">Result is valid</text>
    <text x="300" y="405" class="sublabel" text-anchor="middle">per protocol</text>

    <rect x="425" y="340" width="150" height="80" fill="#FDF2E7" stroke="#E67E22" stroke-width="2" rx="5"/>
    <text x="500" y="370" class="label" text-anchor="middle">Termination</text>
    <text x="500" y="390" class="sublabel" text-anchor="middle">Process must</text>
    <text x="500" y="405" class="sublabel" text-anchor="middle">eventually end</text>

    <rect x="600" y="340" width="150" height="80" fill="#F4E8F8" stroke="#9B59B6" stroke-width="2" rx="5"/>
    <text x="675" y="370" class="label" text-anchor="middle">Integrity</text>
    <text x="675" y="390" class="sublabel" text-anchor="middle">Honest nodes</text>
    <text x="675" y="405" class="sublabel" text-anchor="middle">decide once</text>
  </g>

  <g class="step" data-step="5" data-narration="Popular consensus algorithms include Proof of Work, Proof of Stake, and Byzantine Fault Tolerance mechanisms.">
    <rect x="100" y="460" width="140" height="50" fill="#D6EAF8" stroke="#3498DB" stroke-width="2" rx="5"/>
    <text x="170" y="490" class="label" text-anchor="middle">Proof of Work</text>

    <rect x="280" y="460" width="140" height="50" fill="#D5F4E6" stroke="#1ABC9C" stroke-width="2" rx="5"/>
    <text x="350" y="490" class="label" text-anchor="middle">Proof of Stake</text>

    <rect x="460" y="460" width="140" height="50" fill="#FADBD8" stroke="#E74C3C" stroke-width="2" rx="5"/>
    <text x="530" y="485" class="label" text-anchor="middle">Byzantine FT</text>
  </g>

  <g class="step" data-step="6" data-narration="Once consensus is reached, the new block is added to all copies of the blockchain, maintaining network consistency.">
    <rect x="150" y="540" width="500" height="40" fill="#E8F8F5" stroke="#1ABC9C" stroke-width="3" rx="5"/>
    <text x="400" y="565" class="label" text-anchor="middle">Blockchain Updated Across Network</text>
  </g>
</svg>'''

def generate_generic_svg(topic_name: str, module: str, visual_data: dict) -> str:
    """Generate a generic educational SVG based on topic information."""
    colors = get_topic_color_scheme(topic_name, module)

    # Extract information from visual_data
    title = visual_data.get("title", topic_name.replace("-", " ").title())
    description = visual_data.get("description", "")
    elements = visual_data.get("elements", [])
    viz_type = visual_data.get("type", "diagram")

    # Generate SVG structure
    svg_header = f'''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .step {{ opacity: 0; }}
      .step.active {{ opacity: 1; transition: opacity 0.5s; }}
      text {{ font-family: Arial, sans-serif; }}
      .title {{ font-size: 24px; font-weight: bold; fill: #2C3E50; }}
      .label {{ font-size: 16px; fill: #34495E; }}
      .sublabel {{ font-size: 13px; fill: #7F8C8D; }}
    </style>
  </defs>

  <g class="step" data-step="1" data-narration="This diagram illustrates the key concepts of {title.lower()}.">
    <text x="400" y="40" class="title" text-anchor="middle">{title}</text>
  </g>
'''

    steps = []
    y_pos = 120

    # Generate steps based on number of elements
    if elements and len(elements) > 0:
        for idx, element in enumerate(elements[:8], start=2):  # Max 8 elements
            narration = f"Step {idx-1}: {element}"
            if idx == 2:
                narration = f"Understanding {element} as the foundational component of this concept."
            elif idx == len(elements) + 1:
                narration = f"Finally, {element} completes the overall process and delivers the result."
            else:
                narration = f"The next step involves {element}, which builds upon the previous components."

            step_svg = f'''  <g class="step" data-step="{idx}" data-narration="{narration}">
    <rect x="200" y="{y_pos}" width="400" height="60" fill="{colors['secondary']}" stroke="{colors['primary']}" stroke-width="2" rx="5"/>
    <text x="400" y="{y_pos + 38}" class="label" text-anchor="middle">{element}</text>'''

            if idx > 2:
                step_svg += f'''
    <path d="M 400 {y_pos - 20} L 400 {y_pos}" stroke="{colors['accent']}" stroke-width="2" marker-end="url(#arrowhead)"/>'''

            step_svg += "\n  </g>\n"
            steps.append(step_svg)
            y_pos += 80
    else:
        # Generate generic steps if no elements provided
        generic_steps = [
            ("Introduction", "This concept is fundamental to understanding the topic."),
            ("Core Principle", "The main principle defines how this concept operates."),
            ("Key Components", "Multiple components work together to form the complete system."),
            ("Process Flow", "The process follows a logical sequence of operations."),
            ("Output Result", "The final output demonstrates the practical application."),
        ]

        for idx, (step_title, narration) in enumerate(generic_steps[:6], start=2):
            step_svg = f'''  <g class="step" data-step="{idx}" data-narration="{narration}">
    <rect x="200" y="{y_pos}" width="400" height="60" fill="{colors['secondary']}" stroke="{colors['primary']}" stroke-width="2" rx="5"/>
    <text x="400" y="{y_pos + 38}" class="label" text-anchor="middle">{step_title}</text>'''

            if idx > 2:
                step_svg += f'''
    <path d="M 400 {y_pos - 20} L 400 {y_pos}" stroke="{colors['accent']}" stroke-width="2" marker-end="url(#arrowhead)"/>'''

            step_svg += "\n  </g>\n"
            steps.append(step_svg)
            y_pos += 80

    svg_footer = '''
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E5C8A"/>
    </marker>
  </defs>
</svg>'''

    return svg_header + "".join(steps) + svg_footer

def process_topic(visual_json_path: Path, count: int) -> Tuple[bool, str]:
    """Process a single topic and generate its SVG."""
    try:
        # Read visual.json
        with open(visual_json_path, 'r') as f:
            visual_data = json.load(f)

        topic_dir = visual_json_path.parent
        topic_name = topic_dir.name
        module_dir = topic_dir.parent.parent
        module = module_dir.name

        # Create assets directory
        assets_dir = topic_dir / "assets"
        assets_dir.mkdir(exist_ok=True)

        # Determine SVG filename
        topic_id = visual_data.get("topicId", topic_name)
        svg_filename = f"{topic_id}.svg"
        svg_path = assets_dir / svg_filename

        # Skip if SVG already exists
        if svg_path.exists():
            return False, f"Skipped (exists): {topic_name}"

        # Generate appropriate SVG
        if "bigram" in topic_name.lower():
            svg_content = create_nlp_bigram_svg()
        elif "types-of-machine-learning" in topic_name.lower():
            svg_content = create_ml_types_svg()
        elif "consensus" in topic_name.lower():
            svg_content = create_blockchain_consensus_svg()
        else:
            svg_content = generate_generic_svg(topic_name, module, visual_data)

        # Write SVG file
        with open(svg_path, 'w') as f:
            f.write(svg_content)

        return True, f"Generated: {topic_name}"
    except Exception as e:
        return False, f"Error in {visual_json_path.name}: {str(e)}"

def main():
    """Main function to generate all SVGs."""
    print("=" * 80)
    print("Generating AI-ML Semester 6 SVG Diagrams")
    print("=" * 80)

    # Find all visual.json files
    visual_files = sorted(BASE_PATH.rglob("visual.json"))
    total = min(len(visual_files), 236)  # Process up to 236

    print(f"\nFound {len(visual_files)} topics, processing first {total}...")
    print()

    generated = 0
    skipped = 0
    errors = 0

    for idx, visual_path in enumerate(visual_files[:total], start=1):
        success, message = process_topic(visual_path, idx)

        if success:
            generated += 1
        elif "Skipped" in message:
            skipped += 1
        else:
            errors += 1

        # Report every 20 topics
        if idx % 20 == 0:
            print(f"\n{'='*80}")
            print(f"Progress Report: {idx}/{total} topics processed")
            print(f"{'='*80}")
            print(f"Generated: {generated} | Skipped: {skipped} | Errors: {errors}")
            print(f"Success Rate: {(generated/(idx-skipped)*100):.1f}%")
            print()

    # Final summary
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    print(f"Total Processed: {total}")
    print(f"Generated: {generated}")
    print(f"Skipped (existed): {skipped}")
    print(f"Errors: {errors}")
    print(f"Success Rate: {(generated/(total-skipped)*100 if total > skipped else 0):.1f}%")
    print("=" * 80)

if __name__ == "__main__":
    main()
