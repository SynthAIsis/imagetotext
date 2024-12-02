from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_description(image_path):
    """
    Generate a description for an image using a pretrained BLIP model.
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Generate text
    outputs = model.generate(**inputs, max_length=100, num_beams=5, early_stopping=True)
    description = processor.decode(outputs[0], skip_special_tokens=True)

    return description

# Example usage
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    generated_text = generate_description(image_path)
    print("Generated Description:", generated_text)
