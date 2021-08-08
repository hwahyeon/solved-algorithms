from PIL import ImageColor

def hex_string_to_RGB(hex_string): 
    r, g, b =ImageColor.getcolor(hex_string, "RGB")
    return {'r': r, 'g': g, 'b': b}
