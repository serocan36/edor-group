import glob

old_logo = '<a href="index.html" class="logo">EDOR <span>GROUP</span></a>'
new_logo = '<a href="index.html" class="logo"><img src="assets/images/logo.png" alt="EDOR GROUP Logo" class="site-logo"></a>'

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    if old_logo in content:
        new_content = content.replace(old_logo, new_logo)
        with open(file, "w") as f:
            f.write(new_content)
        print(f"Updated logo in {file}")

