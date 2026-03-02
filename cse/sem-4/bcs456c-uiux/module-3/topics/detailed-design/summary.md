# Detailed Design in UI/UX - Summary

## Key Definitions and Concepts

- **Design System**: A comprehensive collection of reusable components, standards, and documentation that enables consistent design across applications
- **Design Tokens**: Fundamental values (colors, spacing, typography) that serve as building blocks
- **Type Scale**: Mathematical ratios used to determine font sizes hierarchically
- **Grid System**: Structural framework using columns, rows, and gutters for consistent layout
- **Visual Hierarchy**: Arrangement of elements to indicate importance and guide user attention

## Important Formulas and Theorems

- **Contrast Ratio**: WCAG requires minimum 4.5:1 for normal text, 3:1 for large text
- **Touch Target Size**: Minimum 44×44 pixels for accessible interactive elements
- **Line Height**: Body text 1.4-1.6, Headings 1.2-1.3
- **Spacing Multiplier**: 4px base unit (4, 8, 16, 24, 32, 48, 64px scale)
- **Type Scale Ratio**: Common ratios include 1.25 (minor third), 1.414 (augmented fourth)

## Key Points

- Design systems ensure consistency and reduce design debt across projects
- Limit typography to 2-3 font families maximum for visual coherence
- Color palettes should include primary, secondary, neutral, and semantic colors
- The 8-point grid system creates consistent spacing throughout interfaces
- All interactive elements require defined states: default, hover, active, focus, disabled
- Responsive design uses fluid grids, flexible images, and media queries
- Accessibility requires 4.5:1 contrast ratio and 44px minimum touch targets

## Common Mistakes to Avoid

- Using too many font families and sizes creates visual clutter
- Inconsistent spacing breaks visual rhythm and confuses users
- Ignoring accessibility standards leads to exclusion of users with disabilities
- Using color alone to convey information (also need text/icons)
- Neglecting disabled states in interactive components
- Not testing designs at multiple screen sizes

## Revision Tips

- Practice creating design specifications for common UI components
- Memorize standard color values and their psychological associations
- Review WCAG accessibility requirements before examinations
- Understand the difference between wireframes, prototypes, and detailed designs
- Practice calculating grid layouts and spacing values
- Study real-world design systems like Material Design for reference
