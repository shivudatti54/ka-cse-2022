#!/bin/bash
# MiniMax SVG Rich Fixer - Creates ENHANCED step-based SVGs with CSS animations
# Generates NEW -rich.svg files (doesn't overwrite originals)
# Updates visual.json to include both old and new SVGs
#
# Usage: ./minimax-fix-svg-rich.sh <svg-path-or-topic-dir> [svg-filename]
# Requires: MINIMAX_API_KEY environment variable

set -euo pipefail

# --- Configuration ---
# Hardcoded API key (can be overridden by MINIMAX_API_KEY environment variable)
DEFAULT_API_KEY="sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
API_KEY="${MINIMAX_API_KEY:-$DEFAULT_API_KEY}"

if [ -z "$API_KEY" ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ ERROR: No API key available"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 1
fi
API_URL="https://api.minimax.io/anthropic/v1/messages"
MODEL="MiniMax-M2.5"
MAX_TOKENS=12000
CURL_TIMEOUT=300
MAX_RETRIES=2

# --- Input validation & smart path resolution ---
if [ $# -lt 1 ]; then
  echo "Usage: $0 <svg-path-or-topic-dir> [svg-filename]"
  exit 1
fi

if [ $# -ge 2 ]; then
  TOPIC_DIR="$1"
  SVG_NAME="$2"
  SVG_PATH="$TOPIC_DIR/assets/$SVG_NAME"
else
  INPUT="$1"
  if [[ "$INPUT" == *.svg ]]; then
    SVG_PATH="$INPUT"
    SVG_NAME="$(basename "$SVG_PATH")"
    TOPIC_DIR="$(dirname "$(dirname "$SVG_PATH")")"
  elif [ -d "$INPUT/assets" ]; then
    TOPIC_DIR="$INPUT"
    SVG_PATH=$(find "$TOPIC_DIR/assets" -name "*.svg" ! -name "*-rich.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  elif [ -d "$INPUT" ] && [ "$(basename "$INPUT")" = "assets" ]; then
    TOPIC_DIR="$(dirname "$INPUT")"
    SVG_PATH=$(find "$INPUT" -name "*.svg" ! -name "*-rich.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  else
    TOPIC_DIR="$INPUT"
    SVG_PATH=$(find "$TOPIC_DIR/assets" -name "*.svg" ! -name "*-rich.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  fi
fi

if [ ! -d "$TOPIC_DIR" ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ ERROR: Topic directory not found"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "   Path: $TOPIC_DIR"
  echo ""
  exit 1
fi

if [ -z "$SVG_PATH" ] || [ ! -f "$SVG_PATH" ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ ERROR: SVG file not found"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "   Looked in: $TOPIC_DIR/assets/"
  echo "   Expected: ${SVG_NAME:-*.svg}"
  echo ""
  exit 1
fi

# Generate output path with -rich suffix
SVG_BASENAME="${SVG_NAME%.svg}"
RICH_SVG_NAME="${SVG_BASENAME}-rich.svg"
RICH_SVG_PATH="$TOPIC_DIR/assets/$RICH_SVG_NAME"

TOPIC_NAME=$(basename "$TOPIC_DIR")
# Extract subject name from directory path (topic -> topics -> module -> chapters -> subject)
SUBJECT_DIR=$(dirname "$(dirname "$(dirname "$(dirname "$TOPIC_DIR")")")")
SUBJECT_SLUG=$(basename "$SUBJECT_DIR")
# Strip course code prefix (e.g., bcs502-computer-networks -> computer-networks)
SUBJECT_NAME=$(echo "$SUBJECT_SLUG" | sed -E 's/^[a-z]{2,5}[0-9]{3}[a-z]?-//' | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')
MODULE_DIR=$(dirname "$(dirname "$TOPIC_DIR")")
MODULE_NAME=$(basename "$MODULE_DIR" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')

TMPDIR="${TMPDIR:-/tmp}"
PAYLOAD_FILE="$TMPDIR/minimax_rich_payload_$$.json"
RESPONSE_FILE="$TMPDIR/minimax_rich_response_$$.json"
ERRORS_FILE="$TMPDIR/minimax_rich_errors_$$.txt"
SYSPROMPT_FILE="$TMPDIR/minimax_rich_sysprompt_$$.txt"
USERMSG_FILE="$TMPDIR/minimax_rich_usermsg_$$.txt"

trap 'rm -f "$PAYLOAD_FILE" "$RESPONSE_FILE" "$ERRORS_FILE" "$SYSPROMPT_FILE" "$USERMSG_FILE"' EXIT

echo "=== MiniMax SVG RICH Fixer ==="
echo "Subject: $SUBJECT_NAME"
echo "Module:  $MODULE_NAME"
echo "Topic:   $TOPIC_NAME"
echo "Input:   $SVG_PATH"
echo "Output:  $RICH_SVG_PATH"
echo "Context: Using visual.json + read.md for contextual accuracy"
echo ""

# --- Enhanced system prompt with CSS animations ---
python3 -c "
import sys
prompt = '''You are an expert SVG diagram creator for educational content. You create RICH, ANIMATED step-based SVG diagrams for a university study app (VTU 2022 Scheme, CSE branch).

MANDATORY STEP FORMAT (every step MUST use this EXACT format):
<g class=\"step\" id=\"stepN\" data-narration=\"Your 20-35 word narration text here\">
  ...step content...
</g>

CRITICAL: The data-narration attribute is REQUIRED on EVERY step. Steps without data-narration are INVALID and will be rejected. This is used for text-to-speech in the app.

EXAMPLE of CORRECT step:
<g class=\"step\" id=\"step0\" data-narration=\"Welcome to our exploration of this topic. Let us begin by understanding the fundamental concepts and their importance.\">
  <rect x=\"10\" y=\"10\" width=\"780\" height=\"40\" rx=\"8\" fill=\"#e3f2fd\"/>
  <text x=\"400\" y=\"35\" text-anchor=\"middle\" font-size=\"16\" fill=\"#1976d2\">Topic Title</text>
</g>

SVG SPEC REQUIREMENTS - COMPREHENSIVE EDUCATIONAL DESIGN:
- viewBox=\"0 0 800 HEIGHT\" (HEIGHT: 600-2000px based on content needs)
- Background: <rect width=\"800\" height=\"HEIGHT\" fill=\"#f8f9fa\"/> placed OUTSIDE all step groups
- 7-20 steps, each as <g class=\"step\" id=\"stepN\" data-narration=\"20-35 word narration\">
- Step IDs MUST be 0-indexed: step0, step1, step2...
- GOAL: Create a complete visual explanation that helps students deeply understand the topic
- Color palette: Blue #e3f2fd/#1976d2, Green #e8f5e9/#388e3c, Orange #fff3e0/#ff9800, Red #ffebee/#f44336, Purple #f3e5f5/#9c27b0
- Arrow markers in <defs>
- No fixed width/height on root <svg> (only viewBox)

CSS ANIMATIONS - MANDATORY FOR RICH SVGS:
Add a <style> block inside <svg> with these animations:

@keyframes fadeInSlide {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.85); }
  to { opacity: 1; transform: scale(1); }
}

@keyframes textReveal {
  from { opacity: 0; transform: translateX(-10px); }
  to { opacity: 1; transform: translateX(0); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

Apply animations (IMPORTANT: use semicolons correctly):
.step { animation: fadeInSlide 0.6s ease-out; }
.step rect {
  animation: scaleIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  transform-origin: center;
}
.step text { animation: textReveal 0.4s ease-out 0.2s backwards; }

Use gradients for visual richness (<linearGradient> in <defs>).

VERTICAL STACKING LAYOUT - NO OVERLAPS:
1. Choose step count: 7-20 steps based on topic complexity
2. Calculate canvas height: HEIGHT = 60 + (step_count * 100)
   - For 10 steps: HEIGHT = 1060px
   - For 15 steps: HEIGHT = 1560px
   - For 20 steps: HEIGHT = 2060px
3. step0 title: y=10-50 (40px header)
4. Content steps STACK VERTICALLY:
   - step1: y=60 (height ~90px)
   - step2: y=160 (height ~90px)
   - step3: y=260 (height ~90px)
   - Continue pattern: each step starts where previous ended + 10px gap
5. CRITICAL: Each step must have UNIQUE Y position
6. NO overlapping - all elements visible simultaneously when all steps shown

CONTAINMENT RULE (THE #1 BUG):
Every step MUST have an outer bounding <rect> as FIRST child. ALL other elements MUST fit inside it.
If outer rect is y=58 height=85 (bottom = 143):
- ALL inner <rect y=Y height=H> must have Y+H <= 143
- ALL <text y=Y> must have Y <= 143
- If content overflows, INCREASE outer rect height or REMOVE content

LAYOUT RULES:
- Steps are CUMULATIVE (not slides). Each step ADDS to diagram. NO step reuses Y-coordinates of earlier steps.
- NEVER put a background rect (width=800 height=600) inside a step group
- ALL content must fit within viewBox. Max y for any element = 588
- Use diverse layouts: side-by-side boxes, pipelines, comparison columns, grids
- Compact fonts: titles 12-13px, body 9-10px, labels 8px. Min 8px gap between steps.

VISUAL RICHNESS:
- Use rounded rectangles (rx="8" ry="8")
- Add subtle shadows with filters
- Use gradient fills for depth
- Add connecting arrows between concepts
- Make it visually appealing and professional

LAYOUT EXAMPLE (14-step layout for HEIGHT=1500):
step0: y=10 h=40 (title at top)
step1: y=60 h=90 (first content step)
step2: y=160 h=90
step3: y=260 h=90
step4: y=360 h=90
... (continue stacking)
step13: y=1360 h=90 (last step at bottom)

WRONG (causes overlapping):
step1: y=60
step2: y=160
step8: y=60  ← NO! This overlaps with step1

RIGHT (vertical stacking):
step1: y=60
step2: y=160
step8: y=760 ← YES! Unique Y position

Think of it like a LONG vertical scroll, not overlapping layers.

REMINDER: data-narration is REQUIRED on EVERY step group. Example:
<g class=\"step\" id=\"step5\" data-narration=\"Now we examine how this algorithm processes each element in the array, comparing adjacent values.\">

OUTPUT: Return ONLY the RICH animated SVG. No explanation, no markdown fences. Raw SVG from <svg to </svg>.'''
with open(sys.argv[1], 'w') as f:
    f.write(prompt)
" "$SYSPROMPT_FILE"

# --- Extract sibling topics from module _index.json ---
SIBLINGS_LINE=""
MODULE_INDEX_DIR=$(dirname "$(dirname "$TOPIC_DIR")")
if [ -f "$MODULE_INDEX_DIR/_index.json" ]; then
  SIBLINGS_LINE=$(python3 -c "
import json, sys, os
try:
    with open('$MODULE_INDEX_DIR/_index.json') as f:
        data = json.load(f)
    slug = os.path.basename('$TOPIC_DIR')
    siblings = [t.get('title', t.get('id','')) for t in data.get('topics', []) if t.get('id') != slug]
    if siblings:
        print('Other topics in this module: ' + ', '.join(siblings))
except Exception:
    pass
" 2>/dev/null)
fi

# --- Build user message from context files ---
cat > "$USERMSG_FILE" << EOFUSER
You are an expert educational content designer. Your task: Create ONE comprehensive animated SVG that helps students deeply understand this topic.

Subject: $SUBJECT_NAME
Module: $MODULE_NAME
Topic: $TOPIC_NAME
$SIBLINGS_LINE

IMPORTANT: This SVG must be specifically about "$TOPIC_NAME" in the context of "$SUBJECT_NAME". Do not confuse with similarly named topics from other subjects.
EOFUSER

echo "" >> "$USERMSG_FILE"
echo "== 📚 COMPLETE TOPIC CONTENT (read.md) ==" >> "$USERMSG_FILE"
cat "$TOPIC_DIR/read.md" >> "$USERMSG_FILE" 2>/dev/null || echo "(read.md not found)" >> "$USERMSG_FILE"

echo "" >> "$USERMSG_FILE"
echo "== 🎯 VISUAL SPECIFICATION (if available) ==" >> "$USERMSG_FILE"
if [ -f "$TOPIC_DIR/visual.json" ]; then
  python3 -c "
import json
with open('$TOPIC_DIR/visual.json') as f:
    data = json.load(f)
visuals = data.get('visuals', [])
for v in visuals:
    print('Title:', v.get('title', ''))
    print('Description:', v.get('description', ''))
diagrams = data.get('diagrams', [])
if diagrams:
    print('Diagram elements:')
    for d in diagrams[:1]:
        for n in d.get('content', {}).get('nodes', []):
            print(' -', n.get('label', ''))
" >> "$USERMSG_FILE" 2>/dev/null || echo "(visual.json not parsed)" >> "$USERMSG_FILE"
else
  echo "(visual.json not available)" >> "$USERMSG_FILE"
fi

echo "" >> "$USERMSG_FILE"
echo "== 🎓 LEARNING OBJECTIVE ==" >> "$USERMSG_FILE"
cat "$TOPIC_DIR/purpose.md" >> "$USERMSG_FILE" 2>/dev/null || echo "(purpose.md not found)" >> "$USERMSG_FILE"

echo "" >> "$USERMSG_FILE"
echo "== 📝 KEY SUMMARY ==" >> "$USERMSG_FILE"
cat "$TOPIC_DIR/summary.md" >> "$USERMSG_FILE" 2>/dev/null || echo "(summary.md not found)" >> "$USERMSG_FILE"

cat >> "$USERMSG_FILE" << 'EOFUSER'

YOUR DESIGN TASK:
1. **Read and understand the ENTIRE topic** - all sections, formulas, concepts, examples
2. **Identify the core learning objectives** - what must students understand?
3. **Design a THREE-SECTION visual explanation**:

   SECTION 1 - INTRODUCTION (Steps 0-2): Overview & motivation
   - Use y=60-260 for these 3 steps
   - Each step gets ~90px height with 10px gap
   - Brief intro cards, key concepts preview

   SECTION 2 - DEEP DIVE (Steps 3-N): Detailed explanation
   - Continue from y=270 onwards (NO OVERLAP with Section 1)
   - Each step gets ~90-120px height depending on complexity
   - Progressive reveal of formulas, graphs, proofs
   - Include all important concepts from read.md

   SECTION 3 - SUMMARY (Last 2 steps): Wrap-up & key takeaways
   - Continue from where Section 2 ends (NO OVERLAP)
   - Clean summary with main points
   - Full-width summary cards

4. **CRITICAL: NO OVERLAPPING ELEMENTS**:
   - Every step MUST have unique Y coordinates
   - Steps are cumulative - they stack vertically
   - Calculate layout: step_y = 60 + (step_number * 100)
   - NEVER reuse Y coordinates between steps
   - Each step adds to the diagram, building up vertically

4. **For each step, include:**
   - Clear visual representation (shapes, graphs, diagrams)
   - Formulas with proper notation
   - Annotations and labels
   - SMIL animations (draw paths, build formulas, plot graphs)
   - 20-35 word narration explaining the concept

5. **Canvas flexibility:**
   - viewBox="0 0 800 HEIGHT" where HEIGHT can be 600-2000
   - Adjust height based on content needs
   - Ensure proper spacing between steps (80-100px per step)

6. **Animation richness (make it feel like a video lecture):**
   - Use SMIL for drawing effects (<animate>, <animateMotion>)
   - CSS for smooth section transitions
   - Coordinate timing for visual storytelling
   - Make formulas build piece-by-piece (like writing on blackboard)
   - Make graphs/curves draw themselves (like plotting in real-time)
   - Add transition effects between sections (fade out/in)
   - Use motion along paths for dynamic illustrations
   - Make it feel like watching an animated educational video

PRESENTATION STYLE - Think like a video lecturer:
- SECTION 1: Hook the student with "Why does this matter?"
- SECTION 2: Teach thoroughly with building blocks
- SECTION 3: Tie it together with "What did we learn?"

LAYOUT RULES - CRITICAL TO PREVENT OVERLAPPING:
- All steps stack vertically like slides in a presentation
- Each step occupies its own vertical space (y=60, y=160, y=260, etc.)
- NEVER place elements from different steps at the same Y coordinate
- When all steps are visible, nothing should overlap
- Think: vertical scrolling comic strip, not layered slides

ANIMATION PACING - Match narration timing:
- Quick intro animations (0.3-0.5s)
- Detailed drawing/plotting (1-2s for graphs)
- Formula building (0.5s per term)
- Smooth transitions between sections (0.5s fade)

FOCUS: Create a video-like animated lecture that students will love watching.
Make it engaging, clear, and comprehensive. Don't worry about constraints - focus on pedagogical impact.

FINAL CHECKLIST before outputting:
- Every <g class="step"> has id="stepN" (0-indexed) ✓
- Every <g class="step"> has data-narration="..." with 20-35 words ✓
- Steps stack vertically with no overlap ✓
- viewBox height matches content ✓

Output ONLY the rich animated SVG (no markdown, no explanation).
EOFUSER

# --- Build initial payload ---
python3 -c "
import json, sys

payload_file = sys.argv[1]
model = sys.argv[2]
max_tokens = int(sys.argv[3])
sysprompt_file = sys.argv[4]
usermsg_file = sys.argv[5]

with open(sysprompt_file, 'r') as f:
    system_prompt = f.read()

with open(usermsg_file, 'r') as f:
    user_message = f.read()

payload = {
    'model': model,
    'max_tokens': max_tokens,
    'system': system_prompt,
    'messages': [{'role': 'user', 'content': user_message}]
}

with open(payload_file, 'w') as f:
    json.dump(payload, f)

sys_tokens = len(system_prompt) // 4
user_tokens = len(user_message) // 4
print('Payload: system ~{} tokens, user ~{} tokens, total ~{} tokens (estimated)'.format(sys_tokens, user_tokens, sys_tokens + user_tokens))
" "$PAYLOAD_FILE" "$MODEL" "$MAX_TOKENS" "$SYSPROMPT_FILE" "$USERMSG_FILE"

# --- Function: call MiniMax API ---
call_minimax() {
  local attempt_label="$1"
  echo ""
  echo "Sending to MiniMax M2.5 ($attempt_label)..."
  local start_time end_time http_code
  start_time=$(date +%s)

  http_code=$(curl -s -o "$RESPONSE_FILE" -w "%{http_code}" -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -H "x-api-key: ${API_KEY}" \
    -H "anthropic-version: 2023-06-01" \
    -d @"$PAYLOAD_FILE" \
    --max-time "$CURL_TIMEOUT")

  end_time=$(date +%s)
  ELAPSED=$((end_time - start_time))

  if [ "$http_code" != "200" ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "❌ API ERROR: HTTP $http_code"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "   Topic: $TOPIC_NAME"
    echo "   SVG: $SVG_NAME"
    echo "   Attempt: $attempt_label"
    echo ""
    echo "Response body:"
    cat "$RESPONSE_FILE" | head -20
    echo ""
    if [ "$http_code" = "401" ]; then
      echo "💡 Hint: Check your API key is valid"
    elif [ "$http_code" = "429" ]; then
      echo "💡 Hint: Rate limit exceeded, try reducing parallel workers"
    elif [ "$http_code" = "500" ] || [ "$http_code" = "502" ] || [ "$http_code" = "503" ]; then
      echo "💡 Hint: MiniMax server error, will retry if attempts remaining"
    fi
    echo ""
    exit 1
  fi
}

# --- Function: extract SVG from response ---
extract_svg() {
  python3 -c "
import json, sys, re

response_file = sys.argv[1]
svg_path = sys.argv[2]

with open(response_file, 'r') as f:
    response = json.load(f)

if 'error' in response:
    error_msg = response.get('error', {})
    if isinstance(error_msg, dict):
        error_type = error_msg.get('type', 'unknown')
        error_message = error_msg.get('message', str(error_msg))
        print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'❌ API RESPONSE ERROR: {error_type}')
        print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'   {error_message}')
        print()
    else:
        print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'❌ API RESPONSE ERROR')
        print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(f'   {error_msg}')
        print()
    sys.exit(1)

text = ''
for block in response.get('content', []):
    if block.get('type') == 'text':
        text = block['text']
        break

svg = text.strip()
fence = chr(96) * 3
if svg.startswith(fence):
    svg = re.sub(r'^' + fence + r'\w*\n?', '', svg)
    svg = re.sub(r'\n?' + fence + r'$', '', svg)
svg = svg.strip()

if not svg.startswith('<svg'):
    print(f'ERROR: Response does not start with <svg>')
    print(f'First 300 chars: {svg[:300]}')
    sys.exit(1)

# Auto-fix common issues
# 1. Escape unescaped < and > in attribute values (fixes XML parsing errors)
import html
svg = re.sub(r'data-narration=\"([^\"]*?)\"', lambda m: 'data-narration=\"' + html.escape(m.group(1), quote=False) + '\"', svg)

# 2. Remove incomplete opening tags at the end (caused by token limit cutoff)
# Find last complete element by looking for last properly closed tag
lines = svg.split('\\n')
last_valid = len(lines)
for i in range(len(lines) - 1, -1, -1):
    line = lines[i].strip()
    # If we find an incomplete opening tag (starts with < but doesn't end with > or />)
    if line.startswith('<') and not (line.endswith('>') or line.endswith('/>')):
        last_valid = i
        print(f'  ⚠️  Removing incomplete element at line {i}: {line[:50]}...')
        break
svg = '\\n'.join(lines[:last_valid])

# 3. Fix incomplete SVG (add closing tags if missing)
if not svg.endswith('</svg>'):
    print('  ⚠️  SVG appears truncated, attempting to close tags...')
    # Count open and close tags
    open_g = svg.count('<g ')
    close_g = svg.count('</g>')
    if open_g > close_g:
        # Add missing closing tags
        for _ in range(open_g - close_g):
            svg += '\\n  </g>'
    if not svg.rstrip().endswith('</svg>'):
        svg += '\\n</svg>'

with open(svg_path, 'w') as f:
    f.write(svg)

usage = response.get('usage', {})
input_tokens = usage.get('input_tokens', 0)
output_tokens = usage.get('output_tokens', 0)
total = input_tokens + output_tokens
print(f'  Input tokens:  {input_tokens:>8,}')
print(f'  Output tokens: {output_tokens:>8,}')
print(f'  Total tokens:  {total:>8,}')
" "$RESPONSE_FILE" "$RICH_SVG_PATH"
}

# --- Function: validate SVG ---
validate_svg() {
  python3 -c "
import sys, re

svg_path = sys.argv[1]
errors_file = sys.argv[2]
elapsed = sys.argv[3]

with open(svg_path, 'r') as f:
    svg = f.read()

errors = []

# Check for flexible viewBox (800 x HEIGHT where HEIGHT is 600-2000)
viewbox_match = re.search(r'viewBox=\"0 0 (\d+) (\d+)\"', svg)
has_viewbox = viewbox_match is not None
viewbox_valid = False
if has_viewbox:
    width = int(viewbox_match.group(1))
    height = int(viewbox_match.group(2))
    viewbox_valid = width == 800 and 600 <= height <= 2000

has_background = 'fill=\"#f8f9fa\"' in svg
has_style = '<style>' in svg
has_animations = '@keyframes' in svg
step_count = len(re.findall(r'class=\"step\"', svg))
narrations = re.findall(r'data-narration=\"([^\"]*)\"', svg)
word_counts = [len(n.split()) for n in narrations]

viewbox_str = f'0 0 {width} {height}' if has_viewbox else 'MISSING'
print(f'\n{\"=\"*50}')
print(f'  RICH SVG VALIDATION (API time: {elapsed}s)')
print(f'{\"=\"*50}')
print(f'  viewBox:          {viewbox_str} {\"PASS\" if viewbox_valid else \"FAIL (need 800 x 600-2000)\"}')
print(f'  Background rect:  {\"PASS\" if has_background else \"FAIL\"}')
print(f'  CSS <style>:      {\"PASS\" if has_style else \"FAIL\"}')
print(f'  CSS animations:   {\"PASS\" if has_animations else \"FAIL\"}')
print(f'  Steps count:      {step_count} {\"PASS\" if 7 <= step_count <= 20 else \"WARN (expected 7-20)\"}')

if not viewbox_valid:
    errors.append('Invalid viewBox (need 800 x 600-2000)')
if not has_background:
    errors.append('Missing background rect')
if not has_style:
    errors.append('Missing <style> block')
if not has_animations:
    errors.append('Missing CSS @keyframes animations')
if step_count < 7:
    errors.append(f'Too few steps: {step_count} (need at least 7)')
narration_count = len(narrations)
if narration_count == 0:
    errors.append(f'Missing ALL data-narration attributes ({step_count} steps but 0 narrations)')
elif narration_count < step_count:
    errors.append(f'Missing narrations: {narration_count} narrations for {step_count} steps')

print(f'  Narrations:       {narration_count}/{step_count} {\"PASS\" if narration_count == step_count else \"FAIL\"}')
for i, (n, wc) in enumerate(zip(narrations, word_counts)):
    status = 'PASS' if 20 <= wc <= 35 else 'WARN'
    print(f'  step{i} narration: {wc:>2} words [{status}]')

print(f'{\"=\"*50}')

with open(errors_file, 'w') as f:
    for e in errors:
        f.write(e + '\n')

if errors:
    print(f'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'❌ VALIDATION FAILED: {len(errors)} issue(s) detected')
    print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    for e in errors:
        print(f'   • {e}')
    print()
    sys.exit(1)
else:
    print(f'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'✅ SUCCESS: Rich SVG created and validated!')
    print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print()
    sys.exit(0)
" "$RICH_SVG_PATH" "$ERRORS_FILE" "$ELAPSED"
}

# --- Function: build retry payload ---
build_retry_payload() {
  python3 -c "
import json, sys

svg_path = sys.argv[1]
payload_file = sys.argv[2]
model = sys.argv[3]
max_tokens = int(sys.argv[4])
sysprompt_file = sys.argv[5]
errors_file = sys.argv[6]

with open(sysprompt_file, 'r') as f:
    system_prompt = f.read()
with open(svg_path, 'r') as f:
    current_svg = f.read()
with open(errors_file, 'r') as f:
    errors_text = f.read().strip()

retry_message = f'''The rich SVG has validation errors. Fix ALL of these:

ERRORS:
{errors_text}

CURRENT SVG:
{current_svg}

Fix and output ONLY the corrected rich SVG with CSS animations.'''

payload = {
    'model': model,
    'max_tokens': max_tokens,
    'system': system_prompt,
    'messages': [
        {'role': 'user', 'content': 'Create rich SVG.'},
        {'role': 'assistant', 'content': current_svg},
        {'role': 'user', 'content': retry_message}
    ]
}

with open(payload_file, 'w') as f:
    json.dump(payload, f)

print(f'  Retry payload built with {len(errors_text.splitlines())} error(s)')
" "$RICH_SVG_PATH" "$PAYLOAD_FILE" "$MODEL" "$MAX_TOKENS" "$SYSPROMPT_FILE" "$ERRORS_FILE"
}

# --- Main execution ---
call_minimax "attempt 1 of $((MAX_RETRIES + 1))"
echo ""
extract_svg
echo "  API time:      ${ELAPSED}s"
echo "  Rich SVG written to: $RICH_SVG_PATH"

if validate_svg; then
  echo ""
  echo "✅ Rich SVG created successfully!"
  echo "   Old: $SVG_NAME"
  echo "   New: $RICH_SVG_NAME"
  exit 0
fi

# Retry loop
for retry in $(seq 1 $MAX_RETRIES); do
  echo ""
  echo "=================================================="
  echo "  AUTO-RETRY $retry of $MAX_RETRIES"
  echo "=================================================="

  build_retry_payload
  call_minimax "retry $retry of $MAX_RETRIES"
  echo ""
  extract_svg
  echo "  API time:      ${ELAPSED}s"

  if validate_svg; then
    echo ""
    echo "✅ Rich SVG passed on retry $retry!"
    exit 0
  fi
done

echo ""
echo "⚠️  SVG has issues after $MAX_RETRIES retries. Removing bad SVG."
rm -f "$RICH_SVG_PATH"
echo "   Deleted: $RICH_SVG_PATH"
echo "Done."
exit 1
