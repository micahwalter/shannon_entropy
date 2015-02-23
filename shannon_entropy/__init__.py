import Image
import math

####### calculate the shannon entropy for an image ###############

def shannon_entropy(img):

    histogram = img.histogram()
    histogram_length = sum(histogram)

    samples_probability = [float(h) / histogram_length for h in histogram]

    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])


####### calculate the shannon entropy for small slices of an image

def focalpoint(img):
    
    w = img.size[0]
    h = img.size[1]
    dims = [ w,h ]
    
    crop_size = 300
    slice_size = 100
    
    tiles = []
    max_ent = 0
    
    for y in range(0,h,slice_size):
        for x in range(0,w,slice_size):
            mx = min(x+slice_size, w)
            my = min(y+slice_size, h)

            buff = Image.new("RGB", [slice_size, slice_size], (255, 255, 255)) 
            tile = img.crop((x, y, mx, my))
            buff.paste(tile, (0, 0))

            ent = entropy(buff)

            data = {'entropy':ent, 'x':x, 'y':y}

            if ent > max_ent:
                max_ent = ent
                tiles = data

    if tiles['x'] > slice_size:
        tiles['x'] -= slice_size
        
    if tiles['y'] > slice_size:
        tiles['y'] -= slice_size

    if (tiles['x'] + crop_size) > w:
        tiles['x'] = w - crop_size

    if (tiles['y'] + crop_size) > h:
        tiles['y'] = h - crop_size

    tiles['w'] = w
    tiles['h'] = h

    return tiles
