#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${MINIMAX_ENV_FILE:-$ROOT_DIR/.minimax.env}"
ENDPOINT="${MINIMAX_ENDPOINT:-https://api.minimax.io/v1/text/chatcompletion_v2}"
MODEL="${MINIMAX_MODEL:-MiniMax-M2}"

if [[ -z "${MINIMAX_API_KEY:-}" && -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$ENV_FILE"
fi

if [[ -z "${MINIMAX_API_KEY:-}" ]]; then
  echo "ERROR: MINIMAX_API_KEY is not set. Add it to $ENV_FILE or export it." >&2
  exit 1
fi

if [[ $# -gt 0 ]]; then
  PROMPT="$*"
elif [[ ! -t 0 ]]; then
  PROMPT="$(cat)"
else
  echo "Usage: $0 \"your prompt\"" >&2
  echo "   or: echo \"your prompt\" | $0" >&2
  exit 1
fi

REQ_BODY="$(node -e 'const prompt=process.argv[1]; const model=process.argv[2]; console.log(JSON.stringify({model, messages:[{role:"user", content:prompt}]}));' "$PROMPT" "$MODEL")"
RESP_FILE="$(mktemp)"
HTTP_STATUS="$(
  curl -sS -m 45 -o "$RESP_FILE" -w "%{http_code}" \
    -X POST "$ENDPOINT" \
    -H "Authorization: Bearer $MINIMAX_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$REQ_BODY"
)"

BODY="$(cat "$RESP_FILE")"
rm -f "$RESP_FILE"

if [[ "$HTTP_STATUS" != "200" ]]; then
  echo "HTTP $HTTP_STATUS" >&2
  echo "$BODY" >&2
  exit 1
fi

node -e '
const body = process.argv[1];
let parsed;
try {
  parsed = JSON.parse(body);
} catch {
  console.error("ERROR: Non-JSON response from MiniMax:");
  console.error(body);
  process.exit(1);
}

const code = parsed?.base_resp?.status_code ?? 0;
const msg = parsed?.base_resp?.status_msg ?? "ok";
if (code !== 0) {
  console.error(`MiniMax error ${code}: ${msg}`);
  process.exit(1);
}

let out = "";
if (typeof parsed.reply === "string" && parsed.reply.length > 0) out = parsed.reply;
if (!out && parsed?.choices?.[0]?.message?.content) out = parsed.choices[0].message.content;
if (!out && parsed?.choices?.[0]?.text) out = parsed.choices[0].text;

if (!out) {
  console.log(JSON.stringify(parsed, null, 2));
  process.exit(0);
}

console.log(out);
' "$BODY"

