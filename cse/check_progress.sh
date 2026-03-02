#!/bin/bash
# Quick progress check for SVG regeneration

LOG_FILE="/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/svg_regeneration.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found. Regeneration may not have started."
    exit 1
fi

echo "================================"
echo "SVG REGENERATION PROGRESS"
echo "================================"
echo ""

# Extract stats
TOTAL=$(grep "Need regeneration:" "$LOG_FILE" | head -1 | awk '{print $NF}')
REGENERATED=$(grep -c "✓ Regenerated" "$LOG_FILE")
FAILED=$(grep -c "✗" "$LOG_FILE")
PROGRESS=$((REGENERATED + FAILED))

echo "Total to regenerate: $TOTAL"
echo "Completed: $PROGRESS"
echo "  ✓ Success: $REGENERATED"
echo "  ✗ Failed: $FAILED"
echo ""

if [ "$TOTAL" -gt 0 ]; then
    PERCENT=$((100 * PROGRESS / TOTAL))
    echo "Progress: $PERCENT%"

    # Calculate ETA
    if [ "$REGENERATED" -gt 0 ]; then
        # Get start time from log
        START_LINE=$(grep "CSE SVG REGENERATION" "$LOG_FILE" -n | head -1 | cut -d: -f1)
        END_LINE=$(tail -1 "$LOG_FILE" -n | head -1 | cut -d: -f1)

        # Estimate based on current rate
        REMAINING=$((TOTAL - PROGRESS))
        echo "Remaining: $REMAINING SVGs"
        echo ""
        echo "Recent activity:"
        tail -10 "$LOG_FILE" | grep -E "(✓|✗|Generating)" | tail -5
    fi
fi

echo ""
echo "Last updated: $(date)"
echo ""
echo "To monitor live: tail -f $LOG_FILE"
