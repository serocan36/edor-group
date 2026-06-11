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


  // Preloader Logic
  window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
      preloader.classList.add('loaded');
      setTimeout(() => {
        preloader.style.display = 'none';
      }, 800);
    }
  });

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

});
