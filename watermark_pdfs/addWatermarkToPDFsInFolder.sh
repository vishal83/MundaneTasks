#!/bin/bash

# Check if the watermark text is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <watermark_text>"
  exit 1
fi

# Watermark text input
WATERMARK_TEXT=$1

# Loop through all PDF files in the current directory
for file in *.pdf; do
    if [ -f "$file" ]; then
        # Extract the filename without extension
        filename="${file%.pdf}"
        
        # Output filename with "_watermarked" appended
        output_file="${filename}_watermarked.pdf"
        
        # Call the Python script to add watermark
        python3 pdf_watermark.py "$file" "$output_file" "$WATERMARK_TEXT"
        
        echo "Watermarked PDF created: $output_file"
    fi
done
