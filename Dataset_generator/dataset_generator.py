from pdf2image import convert_from_path
import content_generator as cg
import doc_creator as dc

# Step 1: Generate Multiple Sets of Content
def generate_multiple_sets(number_of_sets):
    sets_of_content = []
    for _ in range(number_of_sets):
        sets_of_content.append(cg.random_data())
    return sets_of_content

# Step 3: Convert PDF to JPG
def convert_pdf_to_jpg(pdf_path, output_jpg_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f"{output_jpg_path}_{i}.jpg", "JPEG")

# Generate flyers
n = int(input('Enter the number of images to make: '))
new_content_sets = generate_multiple_sets(n)  # Generate n set of new content
for i in range(n):
    output_pdf_path = "dataset/pdfs/output_"+str(i)+".pdf"
    print(new_content_sets[i])
    # Step 2: Arrange Content in the required Layout and create PDF
    dc.create_pdf_with_layout(new_content_sets[i], output_pdf_path)
    convert_pdf_to_jpg(output_pdf_path, "dataset/images/image"+str(i))
    print("created image"+str(i))

# The resulting JPG images will be saved as output_image_0.jpg, output_image_1.jpg, and so on.
