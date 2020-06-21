from simpleimage import SimpleImage


def main():
    # This program creates a reflection, upside down, of the selected image file.

    original = SimpleImage('my_filer.jpg')
    # shows the original image
    original.show()
    reflected = make_reflected('my_filer.jpg')
    # shows the reflected image
    reflected.show()


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    # a blank image of width as same as original and height double to original image is created
    reflection = SimpleImage.blank(width, height * 2)
    for x in range(width):
        for y in range(height):
            original = image.get_pixel(x, y)
            # the top half is created
            reflection.set_pixel(x, y, original)
            # the bottom half, containing similar pixels to top half, is created i.e. a reflection
            reflection.set_pixel(x, (height * 2) - (y + 1), original)

    return reflection


if __name__ == '__main__':
    main()
