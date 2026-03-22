#!/bin/bash

declare -A PACKAGES
PACKAGES=(["flask"]="flask" ["flask_cors"]="flask-cors")
MISSING=()

for import_name in "${!PACKAGES[@]}"; do
    python -c "import $import_name" 2>/dev/null || MISSING+=("${PACKAGES[$import_name]}")
done

if [ ${#MISSING[@]} -gt 0 ]; then
    echo "Missing dependencies: ${MISSING[*]}"
    read -p "Install them? [y/N] " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        pip3 install "${MISSING[@]}"
    else
        exit 1
    fi
fi

python main.py "$@"
