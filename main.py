from PIL import Image
from color import Color
from octree_quantizer import OctreeQuantizer


def main():
    image = Image.open('rainbow.png')
    pixels = image.load()
    width, height = image.size

    octree = OctreeQuantizer()

    # add colors to the octree
    for j in range(height):
        for i in range(width):
            octree.add_color(Color(*pixels[i, j]))

    # 256 colors for 8 bits per pixel output image
    palette = octree.make_palette(512)

    # create palette for 256 color max and save to file
    palette_image = Image.new('RGB', (32, 32))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        print(i//16," Separadpos ",i%16,color.red)
        palette_pixels[i % 32, i // 32] = (int(color.red), int(color.green), int(color.blue))
    palette_image.save('rainbow_palette.png')

    # save output image
    out_image = Image.new('RGB', (width, height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (color.red, color.green, color.blue)
    out_image.save('rainbow_out.png')


if __name__ == '__main__':
    main()