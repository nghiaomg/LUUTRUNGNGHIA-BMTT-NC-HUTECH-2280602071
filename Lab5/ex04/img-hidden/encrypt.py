import sys
from PIL import Image

def encode_image(image_path, message):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    w, h = img.size
    binary_msg = ''.join(format(ord(char), '08b') for char in message)
    binary_msg += '1111111111111110' 

    data_index = 0
    binary_msg_length = len(binary_msg)
    
    img = img.convert("RGB")
    pixels = img.load()

    for row in range(h):
        for col in range(w):
            px = list(pixels[col, row])

            for color_channel in range(3): 
                if data_index < binary_msg_length:
                    px[color_channel] = (px[color_channel] & 0xFE) | int(binary_msg[data_index])
                    data_index += 1

            pixels[col, row] = tuple(px)
            if data_index >= binary_msg_length:
                break
        if data_index >= binary_msg_length:
            break
    
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()