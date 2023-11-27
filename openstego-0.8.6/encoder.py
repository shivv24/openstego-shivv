from PIL import Image

# Creating an image object
org_img = Image.open('moon.jpg')

# Loading pixel values of the original image, each entry is a pixel value i.e., RGB values as a sublist
org_pixelMap = org_img.load()

# Creating a new image object with the image mode and dimensions as that of the original image
enc_img = Image.new(org_img.mode, org_img.size)
enc_pixelsMap = enc_img.load()

# Reading the message to be encrypted from the user
key=input("Enter key to edit(Security Key):")
msg = input("Enter the message:\t")
msg_index = 0

# Finding the length of the message
msg_len = len(msg)

# Traversing through the pixel values
for row in range(org_img.size[0]):
    for col in range(org_img.size[1]):

        # Fetching RGB value a pixel to sublist
        pixel_list = org_pixelMap[row, col]
        r = pixel_list[0]  # R value
        g = pixel_list[1]  # G value
        b = pixel_list[2]  # B value

        if row == 0 and col == 0:  # 1st pixel is used to store the length of the message
            ascii_val = msg_len
            enc_pixelsMap[row, col] = (ascii_val, g, b)
        elif msg_index < msg_len:  # Hiding our message inside the R values of the pixels
            c = msg[msg_index]
            ascii_val = ord(c)
            enc_pixelsMap[row, col] = (ascii_val, g, b)
            msg_index += 1
        else:  # Assigning the pixel values of the old image to the new image
            enc_pixelsMap[row, col] = (r, g, b)

org_img.close()

# Display the image
enc_img.show()

# Save the image
enc_img.save("encrypted_image.png")
enc_img.close()

# Creating an Image Object
enc_img = Image.open('encrypted_image.png')
key1=input("\nRe-enter key to extract text:")

# Loading pixel values of the original image, each entry is a pixel value i.e., RGB values as a sublist
enc_pixelMap = enc_img.load()

# Creating an empty string for our hidden message
msg = ""
msg_index = 0
if key==key1:
# Traversing through the pixel values
    for row in range(enc_img.size[0]):
        for col in range(enc_img.size[1]):

        # Fetching RGB value a pixel to sublist
            pixel_list = enc_pixelMap[row, col]
            r = pixel_list[0]  # R value

            if col == 0 and row == 0:  # 1st pixel was used to store the length of the message
                msg_len = r
            elif msg_len > msg_index:  # Reading the message from the R value of the pixel
                msg += chr(r)  # Converting to character
                msg_index += 1
    print("The hidden message is:\n\n")
    print(msg)
else:
    print("Password is in valid")
enc_img.close()
