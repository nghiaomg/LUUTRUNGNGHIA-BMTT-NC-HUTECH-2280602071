import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except FileNotFoundError:
        print("Error: Encoded image file not found.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

    w, h = img.size
    binary_message = ""

    for row in range(h):
        for col in range(w):
            px = img.getpixel((col, row))

            for color_channel in range(3): 
                binary_message += str(px[color_channel] & 1)

    end_marker = "1111111111111110"
    end_index = binary_message.find(end_marker)
    if end_index != -1:
        binary_message = binary_message[:end_index] 

    message = "".join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    
    if decoded_message:
        print("Decoded message:", decoded_message)
    else:
        print("No hidden message found.")

if __name__ == "__main__":
    main()