document.addEventListener('DOMContentLoaded', () => {
  // Initialize AOS
  AOS.init({
    duration: 1000,
    once: true,
    offset: 100,
    easing: 'ease-out-cubic'
  });

  // Custom Cursor
  const cursor = document.createElement('div');
  cursor.classList.add('cursor');
  document.body.appendChild(cursor);

  const cursorDot = document.createElement('div');
  cursorDot.classList.add('cursor-dot');
  document.body.appendChild(cursorDot);

  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';

    cursorDot.style.left = e.clientX + 'px';
    cursorDot.style.top = e.clientY + 'px';
  });

  // Hover effects on links and buttons for custom cursor
  const hoverElements = document.querySelectorAll('a, button, .service-card');
  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
  });

  // Sticky Header
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // Mobile Menu
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (mobileMenuBtn) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.classList.add('menu-overlay');
    document.body.appendChild(overlay);

    // Add mobile elements to navLinks if they don't exist
    if (!document.querySelector('.mobile-menu-header')) {
      const headerDiv = document.createElement('div');
      headerDiv.classList.add('mobile-menu-header');
      headerDiv.innerHTML = '<a href="index.html" class="logo"><img src="assets/images/edorlogo.png" alt="EDOR GROUP Logo" class="site-logo"></a>';
      navLinks.insertBefore(headerDiv, navLinks.firstChild);

      const footerDiv = document.createElement('div');
      footerDiv.classList.add('mobile-menu-footer');
      footerDiv.innerHTML = `
        <div class="footer-socials mobile-socials">
            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
            <a href="#"><i class="fa-brands fa-instagram"></i></a>
            <a href="#"><i class="fa-brands fa-twitter"></i></a>
        </div>
        <a href="iletisim.html" class="btn btn-outline mobile-contact-btn">Bize Ulaşın</a>
      `;
      navLinks.appendChild(footerDiv);
    }

    const toggleMenu = () => {
      mobileMenuBtn.classList.toggle('active');
      navLinks.classList.toggle('active');
      document.body.classList.toggle('menu-open');
      overlay.classList.toggle('active');
    };

    mobileMenuBtn.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);
  }

  // Counter Animation
  const counters = document.querySelectorAll('.counter-val');
  const speed = 200; // The lower the slower

  const animateCounters = () => {
    counters.forEach(counter => {
      const updateCount = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = target / speed;

        if (count < target) {
          counter.innerText = Math.ceil(count + inc);
          setTimeout(updateCount, 10);
        } else {
          counter.innerText = target;
        }
      };
      updateCount();
    });
  };

  // Trigger counters when scrolled into view
  const statsSection = document.querySelector('.stats-section');
  let animated = false;

  if (statsSection) {
    window.addEventListener('scroll', () => {
      if (animated) return;

      const rect = statsSection.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        animateCounters();
        animated = true;
      }
    });
  }

  // Scroll Progress Logic
  const scrollProgress = document.getElementById('scroll-progress');
  if (scrollProgress) {
    window.addEventListener('scroll', () => {
      const scrollPx = document.documentElement.scrollTop;
      const winHeightPx = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = `${scrollPx / winHeightPx * 100}%`;
      scrollProgress.style.width = scrolled;
    });
  }

  // Cinematic Video Slider Logic
  const heroVideos = document.querySelectorAll('.hero-video-bg');
  if (heroVideos.length > 0) {
    let currentVideoIndex = 0;
    setInterval(() => {
      heroVideos[currentVideoIndex].classList.remove('active');
      currentVideoIndex = (currentVideoIndex + 1) % heroVideos.length;
      heroVideos[currentVideoIndex].classList.add('active');

      const videoEl = heroVideos[currentVideoIndex];
      if (videoEl.paused) {
        videoEl.play().catch(e => console.log('Autoplay prevented:', e));
      }
    }, 6000); // 6 seconds per video for a 18s total loop
  }

  // Lightbox Photo Gallery Logic
  const galleries = {
    samanli: [
      "assets/images/samanli/yalovavillakapak.jpeg",
      "assets/images/samanli/yalovavilla2.jpeg",
      "assets/images/samanli/yalovavilla3.jpeg",
      "assets/images/samanli/yalovavilla4.jpeg",
      "assets/images/samanli/yalovavilla5.jpeg",
      "assets/images/samanli/yalovavilla6.jpeg",
      "assets/images/samanli/yalovavilla7.jpeg",
      "assets/images/samanli/yalovavilla8.jpeg",
      "assets/images/samanli/yalovavilla9.jpeg",
      "assets/images/samanli/yalovavilla10.jpeg",
      "assets/images/samanli/yalovavilla11.jpeg",
      "assets/images/samanli/yalovavilla12.jpeg",
      "assets/images/samanli/yalovavilla13.jpeg",
      "assets/images/samanli/yalovavilla15.jpeg",
      "assets/images/samanli/yalovavilla16.jpeg"
    ],
    ciftlikkoy: [
      "assets/images/ciftlikkoy/ciftlikkoy.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy2.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy3.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy4.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy5.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy6.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy7.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy8.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy9.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy10.jpeg",
      "assets/images/ciftlikkoy/ciftlikkoy11.jpeg"
    ],

    mercedes: [
      "assets/images/otomotiv/mercedes2.jpg",
      "assets/images/otomotiv/mercedes3.jpg",
      "assets/images/otomotiv/mercedes4.jpg"
    ],
    bmw: [
      "assets/images/otomotiv/bmw2.jpg",
      "assets/images/otomotiv/bmw3.jpg",
      "assets/images/otomotiv/bmw4.jpg"
    ],
    audi: [
      "assets/images/otomotiv/audi2.jpg",
      "assets/images/otomotiv/audi3.jpg",
      "assets/images/otomotiv/audi4.jpg"
    ],
    vw: [
      "assets/images/otomotiv/wolksvagen2.jpg",
      "assets/images/otomotiv/wolksvagen3.jpg",
      "assets/images/otomotiv/wolksvagen4.jpg"
    ]

  };

  const lightbox = document.getElementById('projectLightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');
  const lightboxCounter = document.getElementById('lightboxCounter');

  let currentGallery = [];
  let currentIndex = 0;

  function openLightbox(galleryId) {
    if (galleries[galleryId]) {
      currentGallery = galleries[galleryId];
      currentIndex = 0;
      updateLightbox();
      if (lightbox) lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeLightbox() {
    if (lightbox) lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  function updateLightbox() {
    if (lightboxImg && lightboxCounter) {
      lightboxImg.src = currentGallery[currentIndex];
      lightboxCounter.textContent = `${currentIndex + 1} / ${currentGallery.length} Fotoğraf`;
    }
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % currentGallery.length;
    updateLightbox();
  }

  function showPrev() {
    currentIndex = (currentIndex - 1 + currentGallery.length) % currentGallery.length;
    updateLightbox();
  }

  document.querySelectorAll('.btn-gallery').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const galleryId = btn.getAttribute('data-gallery');
      openLightbox(galleryId);
    });
  });

  if (lightbox) {
    lightboxClose.addEventListener('click', closeLightbox);
    lightboxNext.addEventListener('click', showNext);
    lightboxPrev.addEventListener('click', showPrev);

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') showNext();
      if (e.key === 'ArrowLeft') showPrev();
    });

    let touchStartX = 0;
    let touchEndX = 0;

    lightbox.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    lightbox.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, { passive: true });

    function handleSwipe() {
      const minSwipeDistance = 50;
      if (touchEndX < touchStartX - minSwipeDistance) showNext();
      if (touchEndX > touchStartX + minSwipeDistance) showPrev();
    }
  }

});

// Preloader Logic must be outside DOMContentLoaded or attached to window.load
window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  if (preloader) {
    preloader.classList.add('loaded');
    setTimeout(() => {
      preloader.style.display = 'none';
    }, 800);
  }
});
