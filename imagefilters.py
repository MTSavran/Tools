#MEHMET TUGRUL SAVRAN
# MIT 2018

#THIS IS THE PYTHON IMPLEMENTATION OF 3 USEFUL
# IMAGE FILTERS: INVERT, GAUSSIAN BLUR, AND EDGE-HIGHLIGHT
# INPUT IMAGES MUST BE GRAYSCALE

def width(image):
    return image["width"]

def height(image):
    return image["height"]

def pixel(image, x, y):
    index = x + width(image)*y
    #print index
    return image["pixels"][index]

def set_pixel(image, x, y, color):
    index = x + width(image)*y
    image["pixels"][index] = color

def make_image(width, height):
    return {"width": width, "height": height, "pixels": ([0]*width*height)}

# return a new image by applying function f to each pixel of the input image
def apply_per_pixel(image, f):
    result = make_image(width(image),height(image))
    for x in range(width(image)):
        for y in range(height(image)):
            color = pixel(image, x, y)
            set_pixel(result, x, y, f(color))
    return result
  
def invert(c):
    return abs(255-c)
    
def filter_invert(image):
    return apply_per_pixel(image, invert)

#Checks where the given pixel of the image resides and returns either True (meaning somewhere in the middle, not on edges) 
#or returns curt string codes to indicate the relative edge/corner 
def isPassable(image,x,y):
    w = width(image)
    h = height(image)

    uzunluk = w*h
    index = x + w*y

    if index <= w - 1:
        if index%w == 0:
            return "TLC"
        elif index%w == w - 1:
            return "TRC"
        else:
            return "TOP"

    if index >= uzunluk - w:
        if index%w == 0:
            return "BLC"
        elif index%w == w - 1:
            return "BRC"
        else:
            return "BOT"
    else:

        if (index)%w == 0:
            return "L"
        if (index)%w == w -1:
            return "R"
    return True

def convolve(image,kernel):
    result = make_image(width(image),height(image))
    for x in range(width(image)):
        for y in range(height(image)):
            
            if isPassable(image,x,y) == True: #IF PIXEL IS NOT IN ANY EDGE CASE
                newcolor = pixel(image,x-1,y-1)*pixel(kernel,0,0) + pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x+1,y-1)*pixel(kernel,2,0) + pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1) + pixel(image,x-1,y+1)*pixel(kernel,0,2) + pixel(image,x,y+1)*pixel(kernel,1,2) + pixel(image,x+1,y+1)*pixel(kernel,2,2)      
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "TLC":
                newcolor = pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1) + pixel(image,x,y+1)*pixel(kernel,1,2) + pixel(image,x+1,y+1)*pixel(kernel,2,2)
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "TRC":
                newcolor = pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x-1,y+1)*pixel(kernel,0,2) + pixel(image,x,y+1)*pixel(kernel,1,2)
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "BLC":
                newcolor = pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x+1,y-1)*pixel(kernel,2,0) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1)
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "BRC":
                newcolor = pixel(image,x-1,y-1)*pixel(kernel,0,0) + pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1)
                newcolor = int(round(newcolor))
                set_pixel(result,x,y,newcolor)
            if isPassable(image,x,y) =="TOP":
                newcolor = pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1) + pixel(image,x-1,y+1)*pixel(kernel,0,2) + pixel(image,x,y+1)*pixel(kernel,1,2) + pixel(image,x+1,y+1)*pixel(kernel,2,2)
                newcolor = int(round(newcolor))
                set_pixel(result,x,y,newcolor)
            if isPassable(image,x,y) == "BOT":
                newcolor = pixel(image,x-1,y-1)*pixel(kernel,0,0) + pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x+1,y-1)*pixel(kernel,2,0) + pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1) 
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "L":
                newcolor = pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x+1,y-1)*pixel(kernel,2,0) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x+1,y)*pixel(kernel,2,1) +pixel(image,x,y+1)*pixel(kernel,1,2) + pixel(image,x+1,y+1)*pixel(kernel,2,2)
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
            if isPassable(image,x,y) == "R":
                newcolor = pixel(image,x-1,y-1)*pixel(kernel,0,0) + pixel(image,x,y-1)*pixel(kernel,1,0) + pixel(image,x-1,y)*pixel(kernel,0,1) + pixel(image,x,y)*pixel(kernel,1,1) + pixel(image,x-1,y+1)*pixel(kernel,0,2) + pixel(image,x,y+1)*pixel(kernel,1,2)
                newcolor = int(round(newcolor))
                set_pixel(result, x, y, newcolor)
    return result

def filter_gaussian_blur(image):
    kernel = {
    "width":3,
    "height":3,
    "pixels": [1.0/16, 2.0/16, 1.0/16,
               2.0/16, 4.0/16, 2.0/16,
               1.0/16, 2.0/16, 1.0/16]
    }
    return convolve(image,kernel)

def filter_edge_detect(image):
    result = make_image(width(image),height(image))
    Kx = {
    "width":3,
    "height":3,
    "pixels": [-1, 0, 1,
               -2, 0, 2,
               -1, 0, 1]
    }

    Ky = {
    "width":3,
    "height":3,
    "pixels": [-1,-2,-1,
                0, 0, 0, 
                1, 2, 1]
    }
    Ox = convolve(image,Kx)
    Oy = convolve(image,Ky)
    for x in range(width(image)):
        for y in range(height(image)):
            color = min(255,int(round((pixel(Ox, x, y)**2 + pixel(Oy,x,y)**2)**0.5)))
            set_pixel(result,x,y,color)

    return result

# cen = {
#   "width": 11,
#   "height": 11,
#   "pixels": [
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 0,   255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
#     255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255
#   ]
# }
# print filter_edge_detect(cen)




# kernel = {
#     "width":3,
#     "height":3,
#     "pixels": [1.0/16, 2.0/16, 1.0/16,
#                2.0/16, 4.0/16, 2.0/16,
#                1.0/16, 2.0/16, 1.0/16]
# }



# resim = {
#     "height":1,
#     "width":4,
#     "pixels":[0,64,128,255]
# }
    
# resim2 = {
# "width": 2,
# "height": 3,
# "pixels": [ 0 ,50,
# 50 ,100,
# 100,255 ] }

# resim3 = {
# "width": 3,
# "height": 3,
# "pixels": [ 0 ,50,
# 50 ,100,
# 100,255, 210, 210, 167 ] }

# print convolve(resim3,kernel)

# if isPassable(resim3,1,2) == True:
#     print "AM"





# print apply_per_pixel(ornek,invert)

# print pixel(resim,3,0)

# any function of the form "filter_X( image ):", where X denotes the name of
# the filter, can be applied via test.py and the web UI!
# Feel free to go wild and implement your favorite filters once you are done.
# Here are some to inspire you: [GIMP filters](https://docs.gimp.org/en/filters.html)
