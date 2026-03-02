#!/bin/bash
# MiniMax SVG Fixer - with auto-retry on validation failure
# Sends read.md + purpose.md + summary.md + current SVG to MiniMax M2.5
# and gets back a spec-compliant, educationally accurate fixed SVG.
# If validation fails, automatically retries with error feedback (up to 2 retries).
#
# Usage: ./minimax-fix-svg.sh <svg-path-or-topic-dir> [svg-filename]
# Requires: MINIMAX_API_KEY environment variable

set -euo pipefail

# --- Configuration ---
if [ -z "${MINIMAX_API_KEY:-}" ]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ ERROR: MINIMAX_API_KEY not set"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "To fix this, set your MiniMax API key in your terminal:"
  echo ""
  echo "  export MINIMAX_API_KEY='your-api-key-here'"
  echo ""
  echo "Or add it to your ~/.zshrc or ~/.bashrc for persistence:"
  echo ""
  echo "  echo 'export MINIMAX_API_KEY=\"your-api-key-here\"' >> ~/.zshrc"
  echo "  source ~/.zshrc"
  echo ""
  echo "Get your API key from: https://platform.minimax.io/"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 1
fi
API_KEY="sk-cp-r--6hiKCzLgU9QbQREFxR4v336s2kP0vDCeb3x7-iNJxAAdDwQeXhInB8zgfwcduBNoBtQBSj33uci2eCKcCu7q4VjmMGWDhKYHXu_lpv1fmWctproM4cAg"
API_URL="https://api.minimax.io/anthropic/v1/messages"
MODEL="MiniMax-M2.5"
MAX_TOKENS=8192
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
    SVG_PATH=$(find "$TOPIC_DIR/assets" -name "*.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  elif [ -d "$INPUT" ] && [ "$(basename "$INPUT")" = "assets" ]; then
    TOPIC_DIR="$(dirname "$INPUT")"
    SVG_PATH=$(find "$INPUT" -name "*.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  else
    TOPIC_DIR="$INPUT"
    SVG_PATH=$(find "$TOPIC_DIR/assets" -name "*.svg" -print -quit 2>/dev/null)
    SVG_NAME="$(basename "$SVG_PATH")"
  fi
fi

if [ ! -d "$TOPIC_DIR" ]; then
  echo "ERROR: Topic directory not found: $TOPIC_DIR"
  exit 1
fi

if [ -z "$SVG_PATH" ] || [ ! -f "$SVG_PATH" ]; then
  echo "ERROR: SVG not found. Looked in: $TOPIC_DIR/assets/"
  exit 1
fi

TOPIC_NAME=$(basename "$TOPIC_DIR")
# Extract subject name from directory path (topic -> topics -> module -> chapters -> subject)
SUBJECT_DIR=$(dirname "$(dirname "$(dirname "$(dirname "$TOPIC_DIR")")")")
SUBJECT_SLUG=$(basename "$SUBJECT_DIR")
# Strip course code prefix (e.g., bcs502-computer-networks -> computer-networks)
SUBJECT_NAME=$(echo "$SUBJECT_SLUG" | sed -E 's/^[a-z]{2,5}[0-9]{3}[a-z]?-//' | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')
MODULE_DIR=$(dirname "$(dirname "$TOPIC_DIR")")
MODULE_NAME=$(basename "$MODULE_DIR" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')

TMPDIR="${TMPDIR:-/tmp}"
PAYLOAD_FILE="$TMPDIR/minimax_fix_payload_$$.json"
RESPONSE_FILE="$TMPDIR/minimax_fix_response_$$.json"
ERRORS_FILE="$TMPDIR/minimax_fix_errors_$$.txt"
SYSPROMPT_FILE="$TMPDIR/minimax_fix_sysprompt_$$.txt"

trap 'rm -f "$PAYLOAD_FILE" "$RESPONSE_FILE" "$ERRORS_FILE" "$SYSPROMPT_FILE"' EXIT

echo "=== MiniMax SVG Fixer ==="
echo "Subject: $SUBJECT_NAME"
echo "Module:  $MODULE_NAME"
echo "Topic:   $TOPIC_NAME"
echo "SVG:     $SVG_PATH"
echo ""

# --- Write system prompt to temp file (avoids heredoc quoting issues) ---
python3 -c "
import sys
prompt = '''You are an expert SVG diagram creator for educational content. You fix and polish SVG diagrams used in a university study app (VTU 2022 Scheme, CSE branch).

SVG SPEC REQUIREMENTS:
- viewBox=\"0 0 800 600\", xmlns=\"http://www.w3.org/2000/svg\"
- Background: <rect width=\"800\" height=\"600\" fill=\"#f8f9fa\"/> placed OUTSIDE all step groups
- 5-7 steps as <g class=\"step\" id=\"stepN\" data-narration=\"...\"> with class=\"step\" MANDATORY. Step IDs MUST be 0-indexed: step0, step1, step2...
- data-narration: STRICTLY 20-35 words per step, conversational TTS-friendly
- Color palette: Blue #e3f2fd/#1976d2, Green #e8f5e9/#388e3c, Orange #fff3e0/#ff9800, Red #ffebee/#f44336, Purple #f3e5f5/#9c27b0
- Arrow markers in <defs>
- No fixed width/height on root <svg> (only viewBox)

MANDATORY LAYOUT PLANNING:
Before writing ANY SVG, plan the vertical layout. Canvas = 600px tall.
1. Choose 5, 6, or 7 steps (NEVER 8+)
2. step0 title: y=10-50 (40px)
3. Remaining: y=58 to y=588 = 530px for content steps
4. Budget per content step: 530 / (step_count - 1). E.g. 7 steps = 530/6 = ~88px each with 8px gaps
5. Each step outer rect height MUST contain ALL child elements

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

REFERENCE (correct 7-step Y-layout):
step0: y=10 h=40 (title)
step1: y=58 h=80 (content from y=58 to y=138)
step2: y=146 h=80 (content from y=146 to y=226)
step3: y=234 h=80 (content from y=234 to y=314)
step4: y=322 h=80 (content from y=322 to y=402)
step5: y=410 h=80 (content from y=410 to y=490)
step6: y=498 h=90 (content from y=498 to y=588)
FOLLOW THIS PATTERN. Adjust heights as needed but keep ALL content inside each step outer rect.

OUTPUT: Return ONLY the fixed SVG. No explanation, no markdown fences. Raw SVG from <svg to </svg>.'''
with open(sys.argv[1], 'w') as f:
    f.write(prompt)
" "$SYSPROMPT_FILE"

# --- Build initial payload ---
python3 -c "
import json, sys, os

import json as _json

topic_name = sys.argv[1]
svg_path = sys.argv[2]
payload_file = sys.argv[3]
model = sys.argv[4]
max_tokens = int(sys.argv[5])
sysprompt_file = sys.argv[6]
subject_name = sys.argv[7]
module_name = sys.argv[8]
topic_dir = os.path.dirname(os.path.dirname(svg_path))

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return '(File not found)'

# Read sibling topics from module _index.json
siblings_line = ''
module_dir = os.path.dirname(os.path.dirname(topic_dir))  # topics -> module
index_path = os.path.join(module_dir, '_index.json')
if os.path.exists(index_path):
    try:
        with open(index_path) as f:
            mdata = _json.load(f)
        topic_slug = os.path.basename(topic_dir)
        siblings = [t.get('title', t.get('id','')) for t in mdata.get('topics', []) if t.get('id') != topic_slug]
        if siblings:
            siblings_line = 'Other topics in this module: ' + ', '.join(siblings)
    except Exception:
        pass

read_md = read_file(os.path.join(topic_dir, 'read.md'))
purpose_md = read_file(os.path.join(topic_dir, 'purpose.md'))
summary_md = read_file(os.path.join(topic_dir, 'summary.md'))
svg_content = read_file(svg_path)

with open(sysprompt_file, 'r') as f:
    system_prompt = f.read()

siblings_ctx = f'\n{siblings_line}' if siblings_line else ''
user_message = f'''Fix this SVG diagram for the topic: \"{topic_name}\"
Subject: {subject_name}
Module: {module_name}{siblings_ctx}

IMPORTANT: This diagram must be specifically about \"{topic_name}\" in the context of \"{subject_name}\".

== FULL TOPIC CONTENT (read.md) ==
{read_md}

== LEARNING OBJECTIVE (purpose.md) ==
{purpose_md}

== KEY POINTS (summary.md) ==
{summary_md}

== CURRENT SVG TO FIX ==
{svg_content}

Fix all issues: layout overlaps, narration length (20-35 words each), containment (all elements inside their step outer rect), overflow (max y=588). Output ONLY the fixed SVG.'''

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
print(f'Payload: system ~{sys_tokens} tokens, user ~{user_tokens} tokens, total ~{sys_tokens + user_tokens} tokens (estimated)')
" "$TOPIC_NAME" "$SVG_PATH" "$PAYLOAD_FILE" "$MODEL" "$MAX_TOKENS" "$SYSPROMPT_FILE" "$SUBJECT_NAME" "$MODULE_NAME"

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
    echo "ERROR: HTTP $http_code"
    cat "$RESPONSE_FILE"
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
    print(f'ERROR: {response[\"error\"]}')
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

with open(svg_path, 'w') as f:
    f.write(svg)

usage = response.get('usage', {})
input_tokens = usage.get('input_tokens', 0)
output_tokens = usage.get('output_tokens', 0)
total = input_tokens + output_tokens
print(f'  Input tokens:  {input_tokens:>8,}')
print(f'  Output tokens: {output_tokens:>8,}')
print(f'  Total tokens:  {total:>8,}')
" "$RESPONSE_FILE" "$SVG_PATH"
}

# --- Function: validate SVG, write errors to ERRORS_FILE, return 0=pass 1=fail ---
validate_svg() {
  python3 -c "
import sys, re

svg_path = sys.argv[1]
errors_file = sys.argv[2]
elapsed = sys.argv[3]

with open(svg_path, 'r') as f:
    svg = f.read()

errors = []

has_viewbox = 'viewBox=\"0 0 800 600\"' in svg
has_background = 'fill=\"#f8f9fa\"' in svg
step_count_class = len(re.findall(r'class=\"step\"', svg))
step_count_id = len(re.findall(r'id=\"step\d+\"', svg))
step_count = max(step_count_class, step_count_id)
narrations = re.findall(r'data-narration=\"([^\"]*)\"', svg)
word_counts = [len(n.split()) for n in narrations]

print(f'\n{\"=\"*50}')
print(f'  SVG VALIDATION (API time: {elapsed}s)')
print(f'{\"=\"*50}')
print(f'  viewBox 800x600:  {\"PASS\" if has_viewbox else \"FAIL\"}')
print(f'  Background rect:  {\"PASS\" if has_background else \"FAIL\"}')
print(f'  Steps count:      {step_count} {\"PASS\" if 5 <= step_count <= 7 else \"WARN (expected 5-7)\"}')

if not has_viewbox:
    errors.append('Missing viewBox')
if not has_background:
    errors.append('Missing background rect')
if step_count > 7:
    errors.append(f'Too many steps ({step_count}). Maximum is 7.')

step_tags = re.findall(r'(<g[^>]*class=\"step\"[^>]*>.*?</g>)', svg, re.DOTALL)

for i, tag in enumerate(step_tags):
    if re.search(r'<rect[^>]*width=\"800\"[^>]*height=\"600\"', tag) or re.search(r'<rect[^>]*height=\"600\"[^>]*width=\"800\"', tag):
        msg = f'step{i} has full 800x600 rect inside step group - remove it'
        print(f'  CANVAS RESET: {msg} [FAIL]')
        errors.append(msg)

print()
for i, (n, wc) in enumerate(zip(narrations, word_counts)):
    status = 'PASS' if 20 <= wc <= 35 else ('WARN' if wc <= 40 else 'FAIL')
    print(f'  step{i} narration: {wc:>2} words [{status}]')
    if wc < 20:
        errors.append(f'step{i} narration too short ({wc} words, need 20+)')
    elif wc > 40:
        errors.append(f'step{i} narration too long ({wc} words, max 35)')

step_regions = []
for i, tag in enumerate(step_tags):
    y_values = [float(m) for m in re.findall(r'\by=\"([0-9.]+)\"', tag)]
    if y_values:
        min_y = min(y_values)
        max_y = max(y_values)
        for m in re.finditer(r'y=\"([0-9.]+)\"[^>]*height=\"([0-9.]+)\"', tag):
            max_y = max(max_y, float(m.group(1)) + float(m.group(2)))
        step_regions.append((i, min_y, max_y))

print()
overlap_found = False
for i in range(len(step_regions)):
    for j in range(i+1, len(step_regions)):
        si, s_min, s_max = step_regions[i]
        sj, t_min, t_max = step_regions[j]
        if s_min < t_max and t_min < s_max:
            msg = f'step{si} (y={s_min:.0f}-{s_max:.0f}) overlaps step{sj} (y={t_min:.0f}-{t_max:.0f})'
            print(f'  OVERLAP: {msg} [FAIL]')
            errors.append(msg)
            overlap_found = True
if not overlap_found:
    print(f'  No overlaps between steps [PASS]')

print()
containment_ok = True
for i, tag in enumerate(step_tags):
    outer_rect = re.search(r'<rect\s+[^>]*?x=\"([0-9.]+)\"[^>]*?y=\"([0-9.]+)\"[^>]*?width=\"([0-9.]+)\"[^>]*?height=\"([0-9.]+)\"', tag)
    if not outer_rect:
        continue
    outer_y = float(outer_rect.group(2))
    outer_h = float(outer_rect.group(4))
    outer_bottom = outer_y + outer_h

    child_max_y = outer_y
    for m in re.finditer(r'<rect\s+[^>]*?y=\"([0-9.]+)\"[^>]*?height=\"([0-9.]+)\"', tag):
        child_max_y = max(child_max_y, float(m.group(1)) + float(m.group(2)))
    for m in re.finditer(r'<text\s+[^>]*?y=\"([0-9.]+)\"', tag):
        child_max_y = max(child_max_y, float(m.group(1)) + 2)
    for m in re.finditer(r'<circle\s+[^>]*?cy=\"([0-9.]+)\"[^>]*?r=\"([0-9.]+)\"', tag):
        child_max_y = max(child_max_y, float(m.group(1)) + float(m.group(2)))

    if child_max_y > outer_bottom + 2:
        needed = child_max_y - outer_y + 5
        msg = f'step{i} outer rect ends at y={outer_bottom:.0f} but content goes to y={child_max_y:.0f}. Need height={needed:.0f}'
        print(f'  CONTAINMENT: {msg} [FAIL]')
        errors.append(msg)
        containment_ok = False

if containment_ok:
    print(f'  All step content contained [PASS]')

all_y_vals = [float(m) for m in re.findall(r'\by=\"([0-9.]+)\"', svg)]
all_rect_bottoms = []
for m in re.finditer(r'y=\"([0-9.]+)\"[^>]*height=\"([0-9.]+)\"', svg):
    all_rect_bottoms.append(float(m.group(1)) + float(m.group(2)))
max_y = max(all_y_vals + all_rect_bottoms) if (all_y_vals or all_rect_bottoms) else 0

if max_y > 600:
    msg = f'Content extends to y={max_y:.0f}, exceeds 600px. Reduce steps or compress.'
    print(f'  OVERFLOW: {msg} [FAIL]')
    errors.append(msg)
elif max_y > 590:
    print(f'  TIGHT FIT: max y={max_y:.0f} [WARN]')
else:
    print(f'  Bounds: max y={max_y:.0f} [PASS]')

print(f'{\"=\"*50}')

with open(errors_file, 'w') as f:
    for e in errors:
        f.write(e + '\n')

if errors:
    print(f'\n  {len(errors)} FAIL(s) detected')
    sys.exit(1)
else:
    print(f'\n  ALL CHECKS PASSED!')
    sys.exit(0)
" "$SVG_PATH" "$ERRORS_FILE" "$ELAPSED"
}

# --- Function: build retry payload with error feedback ---
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

retry_message = f'''The SVG you produced has validation errors. Fix ALL of these errors:

ERRORS:
{errors_text}

CURRENT BROKEN SVG:
{current_svg}

HOW TO FIX:
- CONTAINMENT: outer bounding rect is TOO SHORT. INCREASE its height so all inner rects (y+height) and text (y) fit inside.
- OVERLAP: steps share Y-coordinates. Each step must start AFTER the previous ends. Leave 8px gaps.
- OVERFLOW: total exceeds 600px. Use fewer steps (5 or 6) or compress content.

Output ONLY the corrected SVG.'''

payload = {
    'model': model,
    'max_tokens': max_tokens,
    'system': system_prompt,
    'messages': [
        {'role': 'user', 'content': 'Fix the SVG for this topic.'},
        {'role': 'assistant', 'content': current_svg},
        {'role': 'user', 'content': retry_message}
    ]
}

with open(payload_file, 'w') as f:
    json.dump(payload, f)

print(f'  Retry payload built with {len(errors_text.splitlines())} error(s) to fix')
" "$SVG_PATH" "$PAYLOAD_FILE" "$MODEL" "$MAX_TOKENS" "$SYSPROMPT_FILE" "$ERRORS_FILE"
}

# --- Main execution loop ---

# Initial call
call_minimax "attempt 1 of $((MAX_RETRIES + 1))"
echo ""
extract_svg
echo "  API time:      ${ELAPSED}s"
echo "  SVG written to: $SVG_PATH"

if validate_svg; then
  echo ""
  echo "Done! SVG is valid."
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
  echo "  SVG written to: $SVG_PATH"

  if validate_svg; then
    echo ""
    echo "Done! SVG passed on retry $retry."
    exit 0
  fi
done

echo ""
echo "WARNING: SVG still has issues after $MAX_RETRIES retries. Manual fix may be needed."
echo "Done."
