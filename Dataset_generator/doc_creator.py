from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Function to create a PDF with the layout of an existing document and the provided data
def create_pdf_with_layout(new_data, output_pdf_path):
    pdf = canvas.Canvas(output_pdf_path, pagesize=letter)
    # Set up the font and font size for the PDF
    pdf.setFont("Times-Roman", 12)

    # Center alignment
    def draw_centered_string(y, text):
        text_width = pdf.stringWidth(text, "Times-Roman", 12)
        x = (letter[0] - text_width) / 2
        # print(letter[0])
        # print(text,"=",x)
        if x < 0:
            words = text.split(' ')
            # print(words)
            # print(len(words))
            index = 0
            while (index<len(words)):
                new_line = ""
                while(pdf.stringWidth(new_line, "Times-Roman", 12)<=390 and index<len(words)):
                    new_line += words[index] + " "
                    # print(new_line)
                    index += 1
                    # print(index)
                pdf.drawString((letter[0] - pdf.stringWidth(new_line, "Times-Roman", 12))/2+35, y, new_line)
                if index<len(words):
                    y -= 15  # Adjust vertical position for each line
        else:
            pdf.drawString(x, y, text)
        return y

    # Add new data in the same layout
    y = letter[1]
    # print(y)
    for data in new_data:
        if data.startswith("Logo-") and len(data.split('-')) == 2:  # Check if it is an image
            image_file = data.split('-')[1].strip()
            # print(image_file)
            try:
                pdf.drawInlineImage(image_file, (letter[0]-250)/2, y-100, width=215, height=100)
            except Exception as e:
                print(f"Failed to add image: {e}")
            y -= 100  # Adjust vertical position for each line
        elif data.startswith("Speaker-"):
            image_file = data.split('-')[1].strip()
            try:
                pdf.drawInlineImage(image_file, (letter[0]-500)/2, y-60, width=65, height=65)
            except Exception as e:
                print(f"Failed to add image: {e}")
        else:  
            for line in data.split('\n'):
                y = draw_centered_string(y, line)
                y -= 15  # Adjust vertical position for each line
    pdf.save()