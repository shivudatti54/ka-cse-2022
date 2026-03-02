#!/bin/bash
# Install fix_svg command
# This creates an alias in your shell configuration

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIX_SVG_SCRIPT="$SCRIPT_DIR/minimax-fix-svg.sh"

# Make sure the script is executable
chmod +x "$FIX_SVG_SCRIPT"

# Detect shell
SHELL_CONFIG=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    echo "Unknown shell. Please add this alias manually to your shell config:"
    echo "  alias fix_svg='$FIX_SVG_SCRIPT'"
    exit 1
fi

# Check if alias already exists
if grep -q "alias fix_svg=" "$SHELL_CONFIG" 2>/dev/null; then
    echo "✓ fix_svg alias already exists in $SHELL_CONFIG"
    echo "  Current: $(grep "alias fix_svg=" "$SHELL_CONFIG")"
    echo ""
    read -p "Do you want to update it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
    # Remove old alias
    sed -i.bak '/alias fix_svg=/d' "$SHELL_CONFIG"
fi

# Add alias
echo "" >> "$SHELL_CONFIG"
echo "# SVG Fixer - MiniMax SVG Quality Fix" >> "$SHELL_CONFIG"
echo "alias fix_svg='$FIX_SVG_SCRIPT'" >> "$SHELL_CONFIG"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✓ fix_svg command installed!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Added to: $SHELL_CONFIG"
echo ""
echo "To use it now, run:"
echo "  source $SHELL_CONFIG"
echo ""
echo "Or start a new terminal session."
echo ""
echo "Usage examples:"
echo "  fix_svg /path/to/topic/directory"
echo "  fix_svg /path/to/file.svg"
echo "  fix_svg ./assets/diagram.svg"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
