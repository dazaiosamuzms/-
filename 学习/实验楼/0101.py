'''
    按照point内func修改像素
'''


from PIL import Image
import os
import sys

size = (256, 256)

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + "(min2).jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            source = im.split()
            R, G, B = 0, 1, 2
            mask = source[R].point(lambda i: i < 100 and 255)
            out = source[G].point(lambda i: i * 0.7)
            source[G].paste(out, None, mask)
            im = Image.merge(im.mode, source)
            print(infile, im.format, "%d*%d" % im.size, im.mode)
            print(im.getbbox(), im.getpalette())
            # im.thumbnail(size)          # 缩略图
            im.save(outfile)
        except IOError:
            print("cannot convert", infile)


