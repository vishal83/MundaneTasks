import argparse
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from PyPDF2 import PdfReader, PdfWriter

def create_watermark(text, output_pdf, opacity=0.5):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    
    # Set the color with opacity (0-1 range)
    c.setFillColor(Color(1, 0, 0, opacity))  # Red color with specified opacity

    # Dynamically adjust font size based on text length and page width
    max_width = width * 0.5  # Max width the text should occupy (50% of the page width)
    font_size = 60  # Start with a medium-large font size
    c.setFont("Helvetica", font_size)
    
    # Reduce font size until the text fits within the max width
    while c.stringWidth(text, "Helvetica", font_size) > max_width and font_size > 12:
        font_size -= 1
        c.setFont("Helvetica", font_size)

    # Define the number of rows and columns for the grid
    rows = 5
    cols = 2

    # Calculate spacing between watermarks
    x_spacing = width / (cols + 1)
    y_spacing = height / (rows + 1)

    # Draw watermarks in an orderly grid layout
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            # Calculate the exact position for the watermark
            x_position = col * x_spacing - max_width / 2
            y_position = row * y_spacing
            
            # Rotate the canvas for diagonal watermark
            c.saveState()  # Save the current state of the canvas
            c.translate(x_position, y_position)  # Move the canvas origin to the calculated position
            c.rotate(45)  # Apply rotation for diagonal watermark

            # Draw the watermark text
            c.drawString(0, 0, text)  # Drawing at origin (0, 0) because we moved the canvas

            c.restoreState()  # Restore the original canvas state for the next watermark

    # Save the canvas as a PDF
    c.save()

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    watermark = PdfReader(watermark_pdf)
    original = PdfReader(input_pdf)
    writer = PdfWriter()
    
    for page in original.pages:
        page.merge_page(watermark.pages[0])
        writer.add_page(page)

    with open(output_pdf, 'wb') as f:
        writer.write(f)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Add watermark to a PDF file.')
    parser.add_argument('input_pdf', help='Path to the input PDF file')
    parser.add_argument('output_pdf', help='Path to save the output PDF file')
    parser.add_argument('watermark_text', help='Text for the watermark')
    parser.add_argument('--opacity', type=float, default=0.3, help='Opacity of the watermark (0 to 1)')
    
    args = parser.parse_args()

    watermark_pdf = 'watermark.pdf'

    # Create the watermark PDF with opacity
    create_watermark(args.watermark_text, watermark_pdf, opacity=args.opacity)

    # Add the watermark to the input PDF
    add_watermark(args.input_pdf, watermark_pdf, args.output_pdf)
    print(f'Watermark "{args.watermark_text}" added to {args.output_pdf}')

if __name__ == "__main__":
    main()
