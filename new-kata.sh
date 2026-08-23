#!/usr/bin/env bash
# Usage: ./new-kata.sh two-sum
set -e

SLUG="$1"
if [ -z "$SLUG" ]; then
    echo "Usage: new-kata.sh <slug>"
    exit 1
fi

DIR="$HOME/codewars/$SLUG"
mkdir -p "$DIR"
cp "$HOME/codewars/template/solution.py" "$DIR/solution.py"
cp "$HOME/codewars/template/notes.md" "$DIR/notes.md"

cd "$HOME/codewars"
git add "$SLUG"
git commit -m "start kata: $SLUG"
git push

echo "Created $DIR"
