import glob

favicon_tag = '    <link rel="icon" href="assets/images/favicon.png" type="image/png">\n'

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        lines = f.readlines()
    
    # Check if already has favicon to avoid duplicates
    if any("favicon.png" in line for line in lines):
        continue
        
    for i, line in enumerate(lines):
        if "<title>" in line:
            lines.insert(i + 1, favicon_tag)
            break
            
    with open(file, "w") as f:
        f.writelines(lines)
    print(f"Added favicon to {file}")

