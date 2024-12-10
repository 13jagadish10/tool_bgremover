import os
from rembg import remove
from PIL import Image
import io
 
input_dir = 'E:\\_learning\\playground\\Python\\projects\\bg_remover\\input'  
output_dir = 'E:\\_learning\\playground\\Python\\projects\\bg_remover\\output'  
print("starting the process...") 
os.makedirs(output_dir, exist_ok=True)
 
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'): 
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
 
        with open(input_path, 'rb') as f:
            input_image = f.read()
 
        output_image = remove(input_image)
 
        output_pil_image = Image.open(io.BytesIO(output_image))
 
        output_pil_image.save(output_path, 'WEBP')
        print(filename," is done.") 

print('All files saved successfully!')
