#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${MINIMAX_ENV_FILE:-$ROOT_DIR/.minimax.env}"

if [[ -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  source "$ENV_FILE"
fi

if [[ -z "${MINIMAX_API_KEY:-}" ]]; then
  echo "ERROR: MINIMAX_API_KEY is not set." >&2
  exit 1
fi

if [[ -z "${MINIMAX_API_HOST:-}" ]]; then
  MINIMAX_API_HOST="https://api.minimax.io"
fi

export MINIMAX_API_KEY
export MINIMAX_API_HOST

exec uvx minimax-coding-plan-mcp -y

