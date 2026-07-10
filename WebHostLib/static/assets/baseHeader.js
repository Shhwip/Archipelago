window.addEventListener('load', () => {
  // Mobile menu handling
  const menuButton = document.getElementById('base-header-mobile-menu-button');
  const mobileMenu = document.getElementById('base-header-mobile-menu');

  menuButton.addEventListener('click', (evt) => {
    evt.preventDefault();
    evt.stopPropagation();

    if (!mobileMenu.style.display || mobileMenu.style.display === 'none') {
      return mobileMenu.style.display = 'flex';
    }

    mobileMenu.style.display = 'none';
  });

  window.addEventListener('resize', () => {
    mobileMenu.style.display = 'none';
  });

  // Popover handling
  const popoverText = document.getElementById('base-header-popover-text');
  const popoverMenu = document.getElementById('base-header-popover-menu');

  popoverText.addEventListener('click', (evt) => {
    evt.preventDefault();
    evt.stopPropagation();

    if (!popoverMenu.style.display || popoverMenu.style.display === 'none') {
      return popoverMenu.style.display = 'flex';
    }

    popoverMenu.style.display = 'none';
  });

  document.body.addEventListener('click', () => {
    mobileMenu.style.display = 'none';
    popoverMenu.style.display = 'none';
  });

  // Dark mode toggle
  const root = document.documentElement;
  const toggles = document.querySelectorAll('.theme-toggle');

  const effectiveTheme = () => {
    const explicit = root.getAttribute('data-theme');
    if (explicit === 'dark' || explicit === 'light') {
      return explicit;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const renderToggles = () => {
    // Show the glyph for the theme the button switches *to*.
    const goingDark = effectiveTheme() === 'light';
    toggles.forEach((toggle) => {
      toggle.textContent = goingDark ? '☽' : '☀'; // ☽ moon / ☀ sun
      toggle.setAttribute('aria-label', goingDark ? 'Switch to dark mode' : 'Switch to light mode');
    });
  };

  const applyTheme = (theme) => {
    root.setAttribute('data-theme', theme);
    try {
      localStorage.setItem('theme', theme);
    } catch (e) { /* localStorage unavailable — theme resets next load */ }
    renderToggles();
  };

  toggles.forEach((toggle) => {
    toggle.addEventListener('click', (evt) => {
      evt.preventDefault();
      evt.stopPropagation();
      applyTheme(effectiveTheme() === 'dark' ? 'light' : 'dark');
    });
  });

  // Keep buttons in sync if the OS preference changes while no explicit choice is set.
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', renderToggles);

  renderToggles();
});
