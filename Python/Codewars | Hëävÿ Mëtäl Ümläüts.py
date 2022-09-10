def heavy_metal_umlauts(boring_text):
    tab = str.maketrans('AEIOUYaeiouy', 'ÄËÏÖÜŸäëïöüÿ')
    return boring_text.translate(tab)
