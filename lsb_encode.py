from PIL import Image

def makeEven(image):
    pixels = list(image.getdata())
    evenPixels = [(r>>1<<1, g>>1<<1, b>>1<<1) for (r,g,b) in pixels]
    image_after = Image.new("RGB", image.size)
    image_after.putdata(evenPixels)
    return image_after

def getBinary(pixels):
    bin_pixels_string = []
    for i in range(len(pixels)):
        (r, g, b) = pixels[i]
        bin_pixels_string.append(str('%08d' % int(bin(r)[2:])))
        bin_pixels_string.append(str('%08d' % int(bin(g)[2:])))
        bin_pixels_string.append(str('%08d' % int(bin(b)[2:])))
    bin_pixels = []
    for j in range(len(bin_pixels_string)):
        for k in range(len(bin_pixels_string[j])):
            bin_pixels.append(int(list(bin_pixels_string[j])[k]))
    return bin_pixels

def encode(image, small_img):
    even_img = makeEven(image)
    even_pixels = list(even_img.getdata())
    small_pixels = list(small_img.getdata())
    bin_small_pixels = getBinary(small_pixels)
    encoded_pixels = []
    if len(bin_small_pixels) > len(even_pixels) * 3:
        raise Exception("Error")
    index = 0
    for i in range(len(even_pixels)):
        if index * 3 + 2 < len(bin_small_pixels):
            encoded_pixels.append((even_pixels[i][0] + int(bin_small_pixels[index * 3 + 0]),
                             even_pixels[i][1] + int(bin_small_pixels[index * 3 + 1]),
                             (even_pixels[i][2] + int(bin_small_pixels[index * 3 + 2]))))
            index += 1
        else:
            encoded_pixels.append((even_pixels[i][0], even_pixels[i][1], even_pixels[i][2]))
    encoded_img = Image.new("RGB", even_img.size)
    encoded_img.putdata(encoded_pixels)
    images = str(raw_input('Please input your preferred file path and file name of the encoded image (e.g. d:/fudan_encoded.bmp):\n'))
    encoded_img.save(images)
    return encoded_img

images = str(raw_input('Please input the file path of a big image and a small one (e.g. d:/fudan.bmp d:/cxk.bmp):\n'))
picture = images.split(' ')
image = Image.open(picture[0])
small_img = Image.open(picture[1])
encoded_img = encode(image, small_img)