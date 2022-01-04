# IMAGE ENCRYPTION PROJECT  

# Step-1 : Read the image by adding image location as first parameter , and Reading mode as second!
file = open('dencrypted.jpg', "rb")
image = file.read()
file.close()

# Steo-2 : Convert the image file into a ByteArray
image = bytearray(image)

#print(image)

# Step-3 : Choose the key for Encryption/Decryption
key = 2


# Final Step : The Bytearray image is manupulated based on the Key the user given

for i,j in enumerate(image):
    image[i] = j^key


# The final encrypted/Decrpted image will be saved in the folder/workspace in which the source code is saved!
file = open("endencrypted.jpg", "wb")
file.write(image)
file.close()
