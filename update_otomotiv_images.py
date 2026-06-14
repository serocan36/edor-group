import os

html_path = 'otomotiv.html'
js_path = 'assets/js/main.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace BMW cover
html_content = html_content.replace(
    '<img src="https://images.unsplash.com/photo-1555215695-3004980ad54e?q=80&w=2070&auto=format&fit=crop" alt="BMW" loading="lazy">',
    '<img src="assets/images/otomotiv/bmwkapak.jpg" alt="BMW" loading="lazy">'
)

# Replace VW cover
html_content = html_content.replace(
    '<img src="https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?q=80&w=2070&auto=format&fit=crop" alt="Volkswagen" loading="lazy">',
    '<img src="assets/images/otomotiv/wolksvagenkapak.jpg" alt="Volkswagen" loading="lazy">'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)


with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_car_galleries = """
    mercedes: [
      "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?q=80&w=2070&auto=format&fit=crop",
      "assets/images/otomotiv/mercedes2.jpg",
      "assets/images/otomotiv/mercedes3.jpg",
      "assets/images/otomotiv/mercedes4.jpg"
    ],
    bmw: [
      "assets/images/otomotiv/bmwkapak.jpg",
      "assets/images/otomotiv/bmw2.jpg",
      "assets/images/otomotiv/bmw3.jpg",
      "assets/images/otomotiv/bmw4.jpg"
    ],
    audi: [
      "https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a?q=80&w=2069&auto=format&fit=crop",
      "assets/images/otomotiv/audi2.jpg",
      "assets/images/otomotiv/audi3.jpg",
      "assets/images/otomotiv/audi4.jpg"
    ],
    vw: [
      "assets/images/otomotiv/wolksvagenkapak.jpg",
      "assets/images/otomotiv/wolksvagen2.jpg",
      "assets/images/otomotiv/wolksvagen3.jpg",
      "assets/images/otomotiv/wolksvagen4.jpg"
    ]
"""

import re
# We need to replace the existing mercedes, bmw, audi, vw blocks in main.js
# Since it's easier to use regex
pattern = r'mercedes: \[.*?vw: \[[^\]]*\]'
js_content = re.sub(pattern, new_car_galleries.strip(), js_content, flags=re.DOTALL)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Images updated in HTML and JS.")
