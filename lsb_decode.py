from PIL import Image

def decode(image, decode_size):
    # get (r, g, b) of encoded image
    encoded_pixels = list(image.getdata())
    # decode_size is a tuple, multiply both parameter to get the number of pixels
    size = decode_size[0] * decode_size[1]
    # int_pixels stores the binary bits of each (r, g, b); decode_pixels stores the integer form
    int_pixels, decoded_pixels = [], []
    # each parameter(r/g/b) has 8 binary bits, so the total bits is (size * 8)
    for i in range(size * 8):
        (r, g, b) = encoded_pixels[i]
        # if modified, the bit is 1; otherwise it is 0
        if r >> 1 << 1 != r:
            int_pixels.append(int(1))
        else:
            int_pixels.append(int(0))
        if g >> 1 << 1 != g:
            int_pixels.append(int(1))
        else:
            int_pixels.append(int(0))
        if b >> 1 << 1 != b:
            int_pixels.append(int(1))
        else:
            int_pixels.append(int(0))
    # index is the number of tuples in encoded_pixels
    index = len(int_pixels) % 8
    if index != 0:
        print 'Error!'
    loop = len(int_pixels) / 8
    for j in range(loop / 3 - 1):
        r = int("".join(map(str,int_pixels[j*24 + 0 : j*24 + 8])),2)
        g = int("".join(map(str,int_pixels[j*24 + 8 : j*24 + 16])),2)
        b = int("".join(map(str,int_pixels[j*24 + 16 : j*24 + 24])),2)
        decoded_pixels.append((r, g, b))
    # create a new image and put the pixels in
    decoded_img = Image.new("RGB", decode_size)
    decoded_img.putdata(decoded_pixels)
    images = str(raw_input(
        'Please input your preferred file path and file name of the decoded image (e.g. d:/decoded.bmp):\n'))
    decoded_img.save(images)
    return decoded_img

images = str(raw_input('Please input the file path of an encoded image that you want to decode (e.g. d:/fudan_encoded.bmp):\n'))
encoded = Image.open(images)
decode_width = int(raw_input('Please input width of the decoded image (make sure you know the size of the decoded image):\n'))
decode_height = int(raw_input('Please input height of the decoded image:\n'))
print 'Size: ' + str(decode_width) + ' * ' + str(decode_height) + '\n'
decode_size = (decode_width, decode_height) # pixels
decode(encoded, decode_size)
