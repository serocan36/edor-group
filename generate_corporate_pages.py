import os

template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="EDOR GROUP - {title}">
    <title>{title} | EDOR GROUP</title>
    
    <!-- CSS -->
    <link rel="stylesheet" href="assets/css/style.css">
    
    <!-- AOS Animation -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        .page-header {{
            height: 60vh;
            background: linear-gradient(to bottom, rgba(5,5,5,0.4) 0%, rgba(5,5,5,1) 100%), url('{bg_img}') center/cover no-repeat;
            display: flex;
            align-items: flex-end;
            padding-bottom: 4rem;
        }}
        
        .corp-content {{
            max-width: 900px;
            margin: 0 auto;
            text-align: center;
        }}
        
        .corp-content p {{
            font-size: 1.2rem;
            line-height: 1.8;
            margin-bottom: 2rem;
            color: var(--text-secondary);
        }}
        
        .highlight-text {{
            font-family: var(--font-heading);
            font-size: 2.5rem;
            color: var(--accent-gold);
            margin-bottom: 2rem;
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header class="header">
        <div class="container nav-container">
            <a href="index.html" class="logo">EDOR <span>GROUP</span></a>
            
            <nav class="nav-links">
                <a href="index.html">Ana Sayfa</a>
                <a href="gayrimenkul.html">Gayrimenkul</a>
                <a href="otomotiv.html">Otomotiv</a>
                <a href="insaat.html">İnşaat</a>
                <a href="iletisim.html">İletişim</a>
            </nav>

            <button class="mobile-menu-btn">
                <div class="hamburger"></div>
            </button>
        </div>
    </header>

    <!-- Page Header -->
    <section class="page-header">
        <div class="container" data-aos="fade-up">
            <span class="hero-subtitle">{subtitle}</span>
            <h1 class="hero-title" style="font-size: 4rem; margin-bottom: 0;">{title}</h1>
        </div>
    </section>

    <!-- Content Section -->
    <section class="section">
        <div class="container">
            <div class="corp-content" data-aos="fade-up">
                <div class="highlight-text">"{quote}"</div>
                {content}
            </div>
        </div>
    </section>

    <!-- Footer -->
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
    </footer>

    <!-- Scripts -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>"""

pages = {
    "vizyonumuz.html": {
        "title": "Vizyonumuz",
        "subtitle": "Geleceğe Bakışımız",
        "bg_img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=2071&auto=format&fit=crop",
        "quote": "Sektörde küresel bir değer yaratmak.",
        "content": "<p>Faaliyet gösterdiğimiz tüm alanlarda öncü kimliğimizle kalıcı eserler bırakmak, sürdürülebilir teknolojik gelişmeleri yatırımlarımıza entegre ederek küresel çapta tanınan bir dünya markası olmaktır.</p><p>Gelecek nesillere ilham veren, güven inşa eden ve sektörel standartları daima bir adım ileriye taşıyan büyük bir holding yapısı olmak en büyük hedefimizdir.</p>"
    },
    "misyonumuz.html": {
        "title": "Misyonumuz",
        "subtitle": "Amacımız ve Hedeflerimiz",
        "bg_img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=2070&auto=format&fit=crop",
        "quote": "Değer katan, güvenilir yatırımlar sunmak.",
        "content": "<p>Müşterilerimize ve iş ortaklarımıza en yüksek kalite standartlarında, güvenilir ve modern çözümler sunmak. Çevreye ve insana duyarlı projeler geliştirerek sürdürülebilir bir ekosisteme katkı sağlamak.</p><p>Değişen pazar koşullarına hızla adapte olan dinamik yapımızla, ülkemiz ekonomisine katma değer sağlamak ve çalışanlarımızın potansiyelini en üst seviyeye çıkarmaktır.</p>"
    },
    "degerlerimiz.html": {
        "title": "Değerlerimiz",
        "subtitle": "Temel Prensiplerimiz",
        "bg_img": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=2070&auto=format&fit=crop",
        "quote": "Güven, Kalite, Yenilik, İnsan Odaklılık.",
        "content": """
            <div class="services-grid" style="margin-top: 3rem; text-align: left;">
                <div class="service-card" style="padding: 2rem;">
                    <i class="fa-solid fa-handshake service-icon"></i>
                    <h3>Güven</h3>
                    <p>Attığımız her adımda şeffaflık, dürüstlük ve güvenilirlik esastır.</p>
                </div>
                <div class="service-card" style="padding: 2rem;">
                    <i class="fa-solid fa-gem service-icon"></i>
                    <h3>Kalite</h3>
                    <p>Sıfır hata prensibiyle, uluslararası standartlarda lüks ve kalite üretiyoruz.</p>
                </div>
                <div class="service-card" style="padding: 2rem;">
                    <i class="fa-solid fa-lightbulb service-icon"></i>
                    <h3>Yenilikçilik</h3>
                    <p>Teknolojiyi takip eden değil, teknolojiye yön veren projeler geliştiriyoruz.</p>
                </div>
            </div>
        """
    },
    "insan-kaynaklari.html": {
        "title": "İnsan Kaynakları",
        "subtitle": "Kariyer & Kültür",
        "bg_img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop",
        "quote": "En büyük sermayemiz, insan kaynağımızdır.",
        "content": "<p>EDOR GROUP'un başarısının temelinde, farklı yeteneklere sahip, takım çalışmasına inanan ve kendini sürekli geliştiren uzman kadromuz yatmaktadır.</p><p>Çalışanlarımıza eşit fırsatlar sunan, onların profesyonel gelişimlerini destekleyen modern ve yenilikçi bir çalışma ortamı sağlamak en öncelikli vizyonumuzdur.</p><a href='iletisim.html' class='btn btn-primary' style='margin-top: 2rem;'>Açık Pozisyonlar ve Başvuru</a>"
    }
}

for filename, data in pages.items():
    html_content = template.format(**data)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Created {filename}")

