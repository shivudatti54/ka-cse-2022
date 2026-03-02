#!/bin/bash
# Monitor SVG regeneration progress

LOG_FILE="/Users/ggoudar/Documents/GitHub/smalltools/clawdBot/study-app-template/content-packs/vtu-2022-scheme/cse/svg_regeneration.log"

echo "SVG Regeneration Monitor"
echo "========================"
echo ""

while true; do
    if [ -f "$LOG_FILE" ]; then
        clear
        echo "=== SVG REGENERATION PROGRESS ==="
        echo ""

        # Count regenerated
        REGENERATED=$(grep -c "✓ Regenerated" "$LOG_FILE" 2>/dev/null || echo "0")
        FAILED=$(grep -c "✗" "$LOG_FILE" 2>/dev/null || echo "0")

        # Get latest lines
        echo "Status:"
        echo "  Regenerated: $REGENERATED"
        echo "  Failed: $FAILED"
        echo ""

        echo "Recent activity:"
        tail -20 "$LOG_FILE"

        echo ""
        echo "Last updated: $(date)"
        echo ""
        echo "Press Ctrl+C to stop monitoring"
    else
        echo "Waiting for log file..."
    fi

    sleep 5
done
