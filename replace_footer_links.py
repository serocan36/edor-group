import glob

full_footer = """    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <a href="index.html" class="logo">EDOR <span>GROUP</span></a>
                    <p>Gayrimenkul, otomotiv ve inşaat sektörlerinde öncü, güvenilir ve yenilikçi çözümler sunan kurumsal yapı.</p>
                    <div class="footer-socials">
                        <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                    </div>
                </div>
                
                <div class="footer-links">
                    <h3 class="footer-title">Hızlı Menü</h3>
                    <ul>
                        <li><a href="index.html">Ana Sayfa</a></li>
                        <li><a href="gayrimenkul.html">Gayrimenkul</a></li>
                        <li><a href="otomotiv.html">Otomotiv</a></li>
                        <li><a href="insaat.html">İnşaat</a></li>
                        <li><a href="iletisim.html">İletişim</a></li>
                    </ul>
                </div>
                
                <div class="footer-links">
                    <h3 class="footer-title">Kurumsal</h3>
                    <ul>
                        <li><a href="hakkimizda.html">Hakkımızda</a></li>
                        <li><a href="vizyonumuz.html">Vizyonumuz</a></li>
                        <li><a href="misyonumuz.html">Misyonumuz</a></li>
                        <li><a href="degerlerimiz.html">Değerlerimiz</a></li>
                        <li><a href="insan-kaynaklari.html">İnsan Kaynakları</a></li>
                    </ul>
                </div>
                
                <div class="footer-contact">
                    <h3 class="footer-title">İletişim</h3>
                    <ul>
                        <li>
                            <i class="fa-solid fa-location-dot"></i>
                            <span>Levent Mah. Büyükdere Cad. No: 123<br>Şişli / İstanbul</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-phone"></i>
                            <span>+90 (212) 555 00 00</span>
                        </li>
                        <li>
                            <i class="fa-solid fa-envelope"></i>
                            <span>info@edorgroup.com.tr</span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 EDOR GROUP. Tüm hakları saklıdır. Design & Code by <a href="https://serhatmazak.com/" target="_blank" class="footer-credit">Serhat MAZAK</a></p>
            </div>
        </div>
    </footer>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    start_idx = content.find("<!-- Footer -->")
    end_idx = content.find("</footer>") + len("</footer>")
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + full_footer + content[end_idx:]
        with open(file, "w") as f:
            f.write(new_content)
        print(f"Updated {file}")
