from rembg import remove
from PIL import Image

input_path = "10_BG_Remover/ben10.jpg"
output_path = "10_BG_Remover/output.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)