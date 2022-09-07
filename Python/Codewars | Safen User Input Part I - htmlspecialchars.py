def html_special_chars(data): 
    return data.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')
