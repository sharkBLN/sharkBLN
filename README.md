<!-- ================================================================================= -->
<!--                          NIL Digital Empire – Pride Edition                       -->
<!-- ================================================================================= -->

<div align="center">

<!-- ==================== 1) Haupt-Banner ==================== -->
<svg viewBox="0 0 1200 400" xmlns="http://www.w3.org/2000/svg" aria-label="NIL Digital Empire – Pride Edition Banner" width="100%">
  <defs>
    <!-- Glow-Filter -->
    <filter id="glow-filter">
      <feGaussianBlur stdDeviation="3" result="blurred"/>
      <feMerge>
        <feMergeNode in="blurred"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- Text-Schatten-Filter -->
    <filter id="textshadow-filter">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.5"/>
    </filter>
    <!-- Regenbogen-Gradient -->
    <linearGradient id="rainbow-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#e40303" class="rainbow-stop"/>
      <stop offset="16%"  style="stop-color:#ff8c00" class="rainbow-stop"/>
      <stop offset="33%"  style="stop-color:#ffed00" class="rainbow-stop"/>
      <stop offset="50%"  style="stop-color:#008018" class="rainbow-stop"/>
      <stop offset="66%"  style="stop-color:#0078d4" class="rainbow-stop"/>
      <stop offset="83%"  style="stop-color:#732982" class="rainbow-stop"/>
      <stop offset="100%" style="stop-color:#e40303" class="rainbow-stop"/>
      <!-- Animation via CSS keyframes in Markdown context: -->
      <animate attributeName="stop-color" values="
        #e40303;#ff8c00;#ffed00;#008018;#0078d4;#732982;#e40303
      " dur="3s" repeatCount="indefinite"/>
    </linearGradient>
    <!-- Wave-Gradient -->
    <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   style="stop-color:#e40303"/>
      <stop offset="16.66%" style="stop-color:#ff8c00"/>
      <stop offset="33.33%" style="stop-color:#ffed00"/>
      <stop offset="50%"  style="stop-color:#008c26"/>
      <stop offset="66.66%" style="stop-color:#004cff"/>
      <stop offset="83.33%" style="stop-color:#722f37"/>
      <stop offset="100%" style="stop-color:#e40303"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 100 0; 0 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <!-- Cyber-Glow für Wave-Top -->
    <filter id="cyberglow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5" result="blurred"/>
      <feMerge>
        <feMergeNode in="blurred"/>
        <feMergeNode in="blurred"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Hintergrund -->
  <rect width="1200" height="400" fill="#0a0a0a"/>

  <!-- Regenbogen-Rahmen -->
  <rect x="10" y="10" width="1180" height="380" rx="15"
        fill="none" stroke="url(#rainbow-grad)" stroke-width="6" filter="url(#glow-filter)">
    <animate attributeName="stroke-width" values="6;8;6" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Terminal-Header -->
  <rect x="30" y="30" width="1140" height="40" fill="#1a1a1a" rx="5"/>
  <circle cx="60" cy="50" r="8" fill="#ff5f56"/>
  <circle cx="90" cy="50" r="8" fill="#ffbd2e"/>
  <circle cx="120" cy="50" r="8" fill="#27ca3f"/>

  <!-- Haupttitel -->
  <text x="600" y="130" text-anchor="middle"
        font-family="Monaco, 'Courier New', monospace" font-size="48" font-weight="bold"
        fill="url(#rainbow-grad)" filter="url(#textshadow-filter)">
    NIL DIGITAL EMPIRE
    <animate attributeName="opacity" values="1;0.7;1" dur="1.5s" repeatCount="indefinite"/>
  </text>

  <!-- Untertitel -->
  <text x="600" y="180" text-anchor="middle"
        font-family="Monaco, 'Courier New', monospace" font-size="24"
        fill="#00ff00" filter="url(#glow-filter)">
    🏳️‍🌈 PRIDE EDITION 🏳️‍🌈
  </text>

  <!-- Prompt -->
  <text x="50" y="240"
        font-family="Monaco, 'Courier New', monospace" font-size="18"
        fill="#00ff00">
    sharkBLN@rainbow-terminal:~$
  </text>
  <text x="350" y="240"
        font-family="Monaco, 'Courier New', monospace" font-size="18"
        fill="#ffffff">
    <tspan>whoami</tspan>
    <animate attributeName="opacity" values="0;1;1;0;0" dur="6s" repeatCount="indefinite"/>
  </text>

  <!-- Antwort -->
  <text x="50" y="280"
        font-family="Monaco, 'Courier New', monospace" font-size="16"
        fill="url(#rainbow-grad)">
    🌈 Audio Necromancer | Terminal Wizard | 140 BPM Pride Techno 🌈
    <animate attributeName="opacity" values="0;0;1;1;0" dur="6s" repeatCount="indefinite"/>
  </text>

  <!-- Blinker-Cursor -->
  <rect x="415" y="225" width="12" height="20"
        fill="#00ff00" style="animation: blink 1s infinite;"/>

  <!-- Cyber-Bulldogge -->
  <g transform="translate(80, 300)">
    <ellipse cx="0" cy="0" rx="45" ry="30" fill="url(#rainbow-grad)" opacity="0.8">
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite"/>
    </ellipse>
    <ellipse cx="0" cy="-35" rx="35" ry="25" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="2"/>
    <ellipse cx="0" cy="-25" rx="20" ry="15" fill="#e0e0e0"/>
    <circle cx="-12" cy="-40" r="6" fill="#00ff00" style="filter:url(#glow-filter); animation: eye-glow 1.5s infinite;"/>
    <circle cx="12" cy="-40" r="6" fill="#00ff00" style="filter:url(#glow-filter); animation: eye-glow 1.5s infinite;"/>
    <rect x="-25" y="-45" width="50" height="8" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.7">
      <animate attributeName="opacity" values="0.7;0.3;0.7" dur="1s" repeatCount="indefinite"/>
    </rect>
    <ellipse cx="0" cy="-28" rx="4" ry="3" fill="#333"/>
    <ellipse cx="-25" cy="-50" rx="8" ry="12" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="1"/>
    <ellipse cx="25" cy="-50" rx="8" ry="12" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="1"/>
    <rect x="-30" y="-15" width="60" height="8" fill="url(#rainbow-grad)" rx="4">
      <animate attributeName="fill" values="url(#rainbow-grad);#ff00ff;url(#rainbow-grad)" dur="3s" repeatCount="indefinite"/>
    </rect>
    <circle cx="-20" cy="-11" r="2" fill="#00ffff"/>
    <circle cx="0" cy="-11" r="2" fill="#00ffff"/>
    <circle cx="20" cy="-11" r="2" fill="#00ffff"/>
    <rect x="-35" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
    <rect x="-15" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
    <rect x="5" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
    <rect x="25" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
  </g>

  <!-- Speech-Bubble -->
  <g transform="translate(200, 280)">
    <ellipse cx="0" cy="0" rx="80" ry="30" fill="#1a1a1a" stroke="url(#rainbow-grad)" stroke-width="2" opacity="0.9"/>
    <polygon points="-60,20 -40,40 -40,20" fill="#1a1a1a"/>
    <text x="0" y="-8" text-anchor="middle"
          font-family="Monaco, 'Courier New', monospace" font-size="14"
          fill="url(#rainbow-grad)">
      WOOF! LOVE IS LOVE! 🏳️‍🌈
    </text>
    <text x="0" y="8" text-anchor="middle"
          font-family="Monaco, 'Courier New', monospace" font-size="12"
          fill="#00ff00">
      140 BPM TAIL WAG
    </text>
  </g>

  <!-- Floating Pride-Elemente -->
  <text x="100" y="350" font-size="20" fill="#ff0080" style="animation: float 4s infinite; --dx:50px; --dy:0px;">♦</text>
  <text x="1050" y="350" font-size="20" fill="#00ff80" style="animation: float 3s infinite; --dx:-30px; --dy:0px;">▲</text>
  <text x="150" y="320" font-size="16" fill="#ff0080" style="animation: float 3s infinite; --dx:20px; --dy:-20px;">♥</text>
  <text x="350" y="300" font-size="14" fill="#00ff80" style="animation: float 4s infinite; --dx:-15px; --dy:15px;">🌈</text>

  <!-- ASCII-Ecken -->
  <text x="30" y="100" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">╔═══</text>
  <text x="1130" y="100" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">═══╗</text>
  <text x="30" y="370" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">╚═══</text>
  <text x="1130" y="370" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">═══╝</text>
</svg>

</div>

---

<div align="center">

<!-- ==================== 2) ASCII-Banner ==================== -->
<pre style="background:#1a1a1a; padding:1em; border-radius:8px; color:#00ff00; overflow-x:auto; max-width:90%; margin:auto;">
╔════════════════════════════════════════════════════════════════════╗
║ 🏳️‍🌈♪♫♪ NIL DIGITAL EMPIRE - PRIDE EDITION ♪♫♪🏳️‍🌈               ║
║ ▸═══► LOVE IS LOVE • ONE HUMAN RACE • EQUALITY FOR ALL ◄═══◂    ║
║ 🌈▲▼▲ BERLIN • TERMINAL WIZARD • 140 BPM TECHNO ▲▼▲🌈          ║
║ ♦♦♦ AUDIO NECROMANCER • CYBERPUNK AESTHETICS ♦♦♦               ║
║ ≋≋≋ SPREADING RAINBOW VIBES ACROSS THE DIGITAL REALM ≋≋≋      ║
║ ★☆★ HAPPY PRIDE! EVERY HUMAN DESERVES LOVE & RESPECT ★☆★      ║
╚════════════════════════════════════════════════════════════════════╝
</pre>

</div>

---

<div align="center">

<!-- ==================== 3) Love-Is-Love-SVG ==================== -->
<svg viewBox="0 0 800 60" xmlns="http://www.w3.org/2000/svg" aria-label="💖 LOVE IS LOVE • ONE HUMAN RACE 💖" width="80%">
  <defs>
    <!-- Pride-Gradient -->
    <linearGradient id="prideGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#e40303"/>
      <stop offset="16.66%" style="stop-color:#ff8c00"/>
      <stop offset="33.33%" style="stop-color:#ffed00"/>
      <stop offset="50%" style="stop-color:#008c26"/>
      <stop offset="66.66%" style="stop-color:#004cff"/>
      <stop offset="83.33%" style="stop-color:#732982"/>
      <stop offset="100%" style="stop-color:#e40303"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 100 0; 0 0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
    <!-- Heart-Glow-Filter -->
    <filter id="heartGlow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Hintergrund -->
  <rect width="800" height="60" fill="#0a0a0a" rx="8"/>
  <!-- Pride-Stripes -->
  <rect x="4" y="4" width="792" height="52" fill="url(#prideGradient)" opacity="0.3" rx="6"/>
  <!-- Haupt-Message -->
  <text x="400" y="38" text-anchor="middle"
        font-family="Monaco, 'Courier New', monospace" font-size="24" font-weight="bold"
        fill="url(#prideGradient)" filter="url(#heartGlow)">
    💖 LOVE IS LOVE • ONE HUMAN RACE 💖
    <animate attributeName="opacity" values="1;0.8;1" dur="2s" repeatCount="indefinite"/>
  </text>
  <!-- Floating Herzen -->
  <g>
    <text x="50" y="35" font-size="16" fill="#ff0080">💕</text>
    <animateTransform attributeName="transform" type="translate" values="0,0; 20,-10; 0,0" dur="3s" repeatCount="indefinite"/>
  </g>
  <g>
    <text x="720" y="40" font-size="16" fill="#ff0080">💕</text>
    <animateTransform attributeName="transform" type="translate" values="0,0; -15,5; 0,0" dur="4s" repeatCount="indefinite"/>
  </g>
  <!-- Terminal-Cursor -->
  <rect x="780" y="25" width="3" height="12" fill="#00ff00" style="animation: blink 1s infinite;"/>
</svg>

</div>

---

<div align="center">

<!-- ==================== 4) Kontakt-Badges ==================== -->
[![SoundCloud](https://img.shields.io/badge/SoundCloud-FF3300?style=for-the-badge&logo=soundcloud&logoColor=white)](https://soundcloud.com/nil-official)
[![Beatport](https://img.shields.io/badge/Beatport-FF6900?style=for-the-badge&logo=beatport&logoColor=white)](https://beatport.com/artist/nil)
[![Email](https://img.shields.io/badge/Music-music@n--il.de-F20544?style=for-the-badge&logo=gmail&logoColor=white)](mailto:music@n-il.de)
[![Website](https://img.shields.io/badge/Portal-happening.today-0078d4?style=for-the-badge&logo=github-pages&logoColor=white)](https://happening.today)

</div>

---

<div align="center">

<!-- ==================== 5) Now Playing-SVG ==================== -->
<svg viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg" aria-label="🎵 Now Playing: NIL – Berlin Underground Pride Techno (140 BPM)" width="70%">
  <defs>
    <!-- Rainbow-Gradient -->
    <linearGradient id="nowPlayingGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#e40303">
        <animate attributeName="stop-color" values="
          #e40303;#ff8c00;#ffed00;#008c26;#004cff;#732982;#e40303
        " dur="2s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" style="stop-color:#008c26">
        <animate attributeName="stop-color" values="
          #008c26;#004cff;#732982;#e40303;#ff8c00;#ffed00;#008c26
        " dur="2s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#732982">
        <animate attributeName="stop-color" values="
          #732982;#e40303;#ff8c00;#ffed00;#008c26;#004cff;#732982
        " dur="2s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <!-- Glow-Filter -->
    <filter id="musicGlow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Hintergrund -->
  <rect width="600" height="80" fill="#0a0a0a" rx="10"/>
  <!-- Rahmen -->
  <rect x="2" y="2" width="596" height="76" fill="none" stroke="url(#nowPlayingGradient)" stroke-width="2" rx="8"/>
  <!-- NOW PLAYING -->
  <text x="20" y="30" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#00ff00" filter="url(#musicGlow)">
    ♪ NOW PLAYING
  </text>
  <!-- Track-Info -->
  <text x="20" y="50" font-family="Monaco, 'Courier New', monospace" font-size="12" fill="url(#nowPlayingGradient)">
    NIL – Berlin Underground Pride Techno (140 BPM)
  </text>
  <!-- Equalizer-Balken -->
  <g transform="translate(450, 20)">
    <rect x="0" y="20" width="6" height="20" fill="#00ff00">
      <animate attributeName="height" values="20;5;30;10;20" dur="0.5s" repeatCount="indefinite"/>
      <animate attributeName="y" values="20;35;10;30;20" dur="0.5s" repeatCount="indefinite"/>
    </rect>
    <rect x="10" y="15" width="6" height="25" fill="#00ffff">
      <animate attributeName="height" values="25;10;35;15;25" dur="0.7s" repeatCount="indefinite"/>
      <animate attributeName="y" values="15;30;5;25;15" dur="0.7s" repeatCount="indefinite"/>
    </rect>
    <rect x="20" y="10" width="6" height="30" fill="#ff00ff">
      <animate attributeName="height" values="30;15;40;20;30" dur="0.3s" repeatCount="indefinite"/>
      <animate attributeName="y" values="10;25;0;20;10" dur="0.3s" repeatCount="indefinite"/>
    </rect>
    <rect x="30" y="25" width="6" height="15" fill="#ffff00">
      <animate attributeName="height" values="15;5;25;10;15" dur="0.8s" repeatCount="indefinite"/>
      <animate attributeName="y" values="25;35;15;30;25" dur="0.8s" repeatCount="indefinite"/>
    </rect>
    <rect x="40" y="18" width="6" height="22" fill="#ff8000">
      <animate attributeName="height" values="22;8;32;12;22" dur="0.4s" repeatCount="indefinite"/>
      <animate attributeName="y" values="18;32;8;28;18" dur="0.4s" repeatCount="indefinite"/>
    </rect>
  </g>
  <!-- Pulsing Pride-Herz -->
  <text x="520" y="35" font-size="20" fill="url(#nowPlayingGradient)">🏳️‍🌈</text>
  <!-- BPM-Indikator -->
  <circle cx="560" cy="25" r="8" fill="none" stroke="#00ff00" stroke-width="2">
    <animate attributeName="r" values="8;12;8" dur="0.428s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.3;1" dur="0.428s" repeatCount="indefinite"/>
  </circle>
  <text x="560" y="29" font-family="Monaco, 'Courier New', monospace" font-size="8" text-anchor="middle" fill="#00ff00">140</text>
</svg>

</div>

---

<div align="center">

<!-- ==================== 6) Pride Wave-SVG ==================== -->
<svg viewBox="0 0 1200 200" xmlns="http://www.w3.org/2000/svg" aria-label="🏳️‍🌈 PRIDE WAVE PROTOCOL" width="100%">
  <defs>
    <!-- Wave-Gradient -->
    <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#e40303"/>
      <stop offset="16.66%" style="stop-color:#ff8c00"/>
      <stop offset="33.33%" style="stop-color:#ffed00"/>
      <stop offset="50%" style="stop-color:#008c26"/>
      <stop offset="66.66%" style="stop-color:#004cff"/>
      <stop offset="83.33%" style="stop-color:#722f37"/>
      <stop offset="100%" style="stop-color:#e40303"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 100 0; 0 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <!-- Animated Rainbow -->
    <linearGradient id="animatedRainbow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#e40303">
        <animate attributeName="stop-color" values="#e40303;#ff8c00;#ffed00;#008c26;#004cff;#722f37;#e40303" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="20%" style="stop-color:#ff8c00">
        <animate attributeName="stop-color" values="#ff8c00;#ffed00;#008c26;#004cff;#722f37;#e40303;#ff8c00" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="40%" style="stop-color:#ffed00">
        <animate attributeName="stop-color" values="#ffed00;#008c26;#004cff;#722f37;#e40303;#ff8c00;#ffed00" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="60%" style="stop-color:#008c26">
        <animate attributeName="stop-color" values="#008c26;#004cff;#722f37;#e40303;#ff8c00;#ffed00;#008c26" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="80%" style="stop-color:#004cff">
        <animate attributeName="stop-color" values="#004cff;#722f37;#e40303;#ff8c00;#ffed00;#008c26;#004cff" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" style="stop-color:#722f37">
        <animate attributeName="stop-color" values="#722f37;#e40303;#ff8c00;#ffed00;#008c26;#004cff;#722f37" dur="3s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <!-- Wave-Glow -->
    <filter id="waveGlow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- Cyber-Glow -->
    <filter id="cyberGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Hintergrund -->
  <rect width="1200" height="200" fill="#0a0a0a"/>

  <!-- Wave 1 (unten) -->
  <path d="M0,150 Q150,100 300,150 T600,150 T900,150 T1200,150 L1200,200 L0,200 Z"
        fill="url(#animatedRainbow)" opacity="0.6" filter="url(#waveGlow)" style="animation: wave1 8s infinite;"/>

  <!-- Wave 2 (mittel) -->
  <path d="M0,130 Q200,80 400,130 T800,130 T1200,130 L1200,200 L0,200 Z"
        fill="url(#waveGradient)" opacity="0.7" filter="url(#waveGlow)" style="animation: wave2 6s infinite;"/>

  <!-- Wave 3 (oben) -->
  <path d="M0,110 Q100,60 200,110 T400,110 T600,110 T800,110 T1000,110 T1200,110 L1200,200 L0,200 Z"
        fill="url(#animatedRainbow)" opacity="0.8" filter="url(#cyberGlow)" style="animation: wave3 4s infinite;"/>

  <!-- Overlay-Text -->
  <text x="600" y="50" text-anchor="middle"
        font-family="Monaco, 'Courier New', monospace" font-size="28" font-weight="bold"
        fill="#00ff00" filter="url(#cyberGlow)">
    🏳️‍🌈 PRIDE WAVE PROTOCOL 🏳️‍🌈
    <animate attributeName="opacity" values="1;0.7;1" dur="2s" repeatCount="indefinite"/>
  </text>

  <!-- Mini-Bulldogge auf Welle -->
  <g transform="translate(900,130)" style="animation: float 5s infinite;">
    <ellipse cx="0" cy="0" rx="15" ry="10" fill="url(#animatedRainbow)" opacity="0.9">
      <animate attributeName="opacity" values="0.9;1;0.9" dur="1s" repeatCount="indefinite"/>
    </ellipse>
    <circle cx="-5" cy="-3" r="2" fill="#00ffff" filter="url(#cyberGlow)"/>
    <circle cx="5" cy="-3" r="2" fill="#00ffff" filter="url(#cyberGlow)"/>
    <animateTransform attributeName="transform" type="translate" values="900,130;850,125;900,130" dur="5s" repeatCount="indefinite"/>
  </g>

  <!-- Floating Code-Element -->
  <text x="50" y="80" font-family="Monaco, 'Courier New', monospace" font-size="12" fill="#00ffff" opacity="0.6">
    export PRIDE=true
    <animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite"/>
  </text>
  <text x="950" y="90" font-family="Monaco, 'Courier New', monospace" font-size="12" fill="#ff00ff" opacity="0.6">
    systemctl enable love.service
    <animate attributeName="opacity" values="1;0;1" dur="3s" repeatCount="indefinite"/>
  </text>

  <!-- Cyber-Text -->
  <text x="400" y="75" font-family="Monaco, 'Courier New', monospace" font-size="10" fill="#ffff00" opacity="0.5">
    🐕‍🦺 CYBER BULLDOGGE ENGAGED
    <animate attributeName="opacity" values="0;1;0" dur="6s" repeatCount="indefinite"/>
  </text>

  <!-- Digital Rain -->
  <text x="200" y="40" font-family="Monaco, 'Courier New', monospace" font-size="10" fill="#00ff00" opacity="0.3">
    01001100 01001111 01010110 01000101
    <animateTransform attributeName="transform" type="translate" values="0,-20; 0,200" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="800" y="30" font-family="Monaco, 'Courier New', monospace" font-size="10" fill="#ff0080" opacity="0.3">
    🌈▲▼▲ BERLIN ▲▼▲🌈
    <animateTransform attributeName="transform" type="translate" values="0,-30; 0,220" dur="4s" repeatCount="indefinite"/>
  </text>

  <!-- Tatzen -->
  <text x="150" y="100" font-size="12" fill="#ff00ff" opacity="0.4">
    🐾
    <animateTransform attributeName="transform" type="translate" values="0,0; 30,-10; 0,0" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="1000" y="120" font-size="12" fill="#00ffff" opacity="0.4">
    🐾
    <animateTransform attributeName="transform" type="translate" values="0,0; -25,15; 0,0" dur="4s" repeatCount="indefinite"/>
  </text>

  <!-- Partikel -->
  <circle cx="300" cy="70" r="2" fill="#00ffff">
    <animate attributeName="cy" values="70;170;70" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="60" r="3" fill="#ff00ff">
    <animate attributeName="cy" values="60;180;60" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1000" cy="80" r="2" fill="#ffff00">
    <animate attributeName="cy" values="80;170;80" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- Surfender Cursor -->
  <g transform="translate(500,140)">
    <rect x="0" y="0" width="3" height="8" fill="#00ff00" filter="url(#cyberGlow)">
      <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
    </rect>
    <animateTransform attributeName="transform" type="translate" values="500,140; 400,135; 500,140" dur="7s" repeatCount="indefinite"/>
  </g>
</svg>

</div>

---

<div align="center" style="margin:2em 0;">

<!-- ==================== 7) ONE HUMAN RACE – Bash-Skript ==================== -->
<h3>💖 ONE HUMAN RACE 💖</h3>
<pre style="background:#1a1a1a; padding:1em; border-radius:8px; color:#00ff00; overflow-x:auto; max-width:90%; margin:auto;">
#!/bin/bash
# Pride Protocol v2025.06 – MAXIMUM RAINBOW EDITION

echo "🏳️‍🌈 LOVE IS LOVE, ALWAYS AND FOREVER 🏳️‍🌈"
echo "There is only ONE beautiful, diverse human race on Earth"
echo "Every person deserves love, respect, and equal treatment"
echo "Your identity is valid, your love is valid, YOU are valid"

export HUMAN_VALUE="infinite"
export LOVE_STATUS="universal"
export EQUALITY_LEVEL="100%"

export PRIDE_MODE="always_active"
export RAINBOW_VIBES="maximum"

systemctl enable love.service
systemctl enable respect.service
systemctl enable equality.service
systemctl enable pride.service

echo "🌈 Spreading rainbow love across the digital realm 🌈"
</pre>

</div>

---

<div align="center">

<!-- ==================== 8) Current Status (Terminal-Box) ==================== -->
<h2>🚀 Current Status</h2>
<pre style="background:#1a1a1a; color:#00ff00; font-family:Monaco, 'Courier New', monospace; padding:1em; border-radius:8px; overflow-x:auto; max-width:90%; margin:auto;">
sharkBLN@rainbow-terminal:~$ whoami
🌈 Rainbow Audio Necromancer | Terminal Pride Wizard | Digital Equality Champion

sharkBLN@rainbow-terminal:~$ cat /proc/pride-status
┌───────────────────────────────────────────────────────────────┐
│ 🏳️‍🌈 Pride Mode: MAXIMUM RAINBOW ACTIVATED                      │
│ 🎵 Currently Playing: 140 BPM Pride Techno Frequencies      │
│ 🌊 Streaming: Berlin Underground Pride Scene                │
│ 💻 Coding: Rainbow Terminal-Aesthetic Web Portals           │
│ 🏳️‍🌈 Advocating: One Human Race, Love is Love                 │
│ ⚡ Status: Reality.exe running with rainbow.dll loaded      │
│ 🎯 Location: Berlin, Germany (Pride Capital)               │
│ 🌈 Rainbow Level: OVER 9000                                │
└───────────────────────────────────────────────────────────────┘

sharkBLN@rainbow-terminal:~$ echo $MISSION
"Creating digital art that combines underground techno culture
with authentic terminal aesthetics while promoting equality,
spreading rainbow love, and celebrating the beautiful diversity
of humanity across the digital realm. 🌈✨"

sharkBLN@rainbow-terminal:~$ sudo systemctl status pride-empire.service
● pride-empire.service - NIL Digital Rainbow Empire
   Loaded: loaded (/etc/systemd/system/pride-empire.service; enabled)
   Active: active (transmitting rainbow vibes) since 1990
   Main PID: 140 (BPM)
   Tasks: ∞ (spreading love)
   Memory: 808 MB (beats per minute)
   CPU: 100% (of my rainbow soul)
   Status: "Spreading love, beats, equality, and rainbow vibes"
   Rainbow-Level: MAXIMUM 🌈
</pre>

</div>

---

<div align="center">

<!-- ==================== 9) Rainbow Digital Portals (Markdown-Tabelle) ==================== -->
## 🌈 Rainbow Digital Portals

| Portal                                               | Theme                  | Status                       | Pride Level | Beschreibung                                      |
|:-----------------------------------------------------:|:----------------------:|:----------------------------:|:-----------:|:-------------------------------------------------:|
| 🎵 [**Audio Necromancer**](https://happening.today/music.html)       | `Pride Pink Fire`      | 🌈 **RAINBOW STREAMING**     | 🏳️‍🌈 MAX   | Underground Techno mit Pride‐Beats, 140 BPM         |
| 🧪 [**Digital Alchemy Lab**](https://happening.today/alchemy.html)    | `Rainbow Matrix Green` | 🌈 **PRIDE EXPERIMENTING**   | 🏳️‍🌈 HIGH  | Code‐Experimente mit Regenbogen‐Algorithmen          |
| 💻 [**Development Portfolio**](https://happening.today/projects.html) | `Pride Ice Blue`       | 🌈 **RAINBOW SHOWCASING**    | 🏳️‍🌈 HIGH  | Kunden‐Projekte mit Pride‐Ästhetik                  |
| 🔬 [**Experimental Lab**](https://happening.today/lab.html)           | `Rainbow Fire Orange`  | 🌈 **PRIDE MAINTENANCE**     | 🏳️‍🌈 MEDIUM| Kreative Regenbogen‐Chaos‐Experimente                |
| 👑 [**Central Dashboard**](https://happening.today/dashboard.html)    | `Full Rainbow Spectrum`| 🌈 **RAINBOW COMMAND**       | 🏳️‍🌈 MAXIMUM| Admin‐Center mit allen Pride‐Farben                  |
| 🏳️‍🌈 [**Pride Portal**](https://happening.today/pride.html)          | `PURE RAINBOW`         | 🌈 **SPREADING MAXIMUM LOVE**| 🏳️‍🌈 ∞     | Gleichheit, Vielfalt, ONE HUMAN RACE HQ             |

</div>

---

<div align="center">

<!-- ==================== 10) Rainbow Tech Stack & Pride Arsenal ==================== -->
## ⚡ Rainbow Tech Stack & Pride Arsenal

<p align="center">
  <strong>
    🌈 Frontend Rainbow Wizardry  –   🎵 Audio Production with Pride  –   💻 Terminal & Rainbow Development
  </strong>
</p>
<div style="display:flex; flex-wrap:wrap; gap:2em; justify-content:center; margin:1em 0;">
  <div style="max-width:300px; text-align:center;">
    <h4>🌈 Frontend Rainbow Wizardry</h4>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5" alt="HTML5"/><br/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3" alt="CSS3"/><br/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/><br/>
    <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js" alt="Three.js"/><br/>
    <img src="https://img.shields.io/badge/Pride-Code-FF69B4?style=for-the-badge&logo=heart" alt="Pride Code"/>
  </div>
  <div style="max-width:300px; text-align:center;">
    <h4>🎵 Audio Production with Pride</h4>
    <img src="https://img.shields.io/badge/Logic_Pro-000000?style=for-the-badge&logo=apple" alt="Logic Pro"/><br/>
    <img src="https://img.shields.io/badge/Ableton_Live-000000?style=for-the-badge&logo=ableton-live" alt="Ableton Live"/><br/>
    <img src="https://img.shields.io/badge/SoundCloud-FF3300?style=for-the-badge&logo=soundcloud" alt="SoundCloud"/><br/>
    <img src="https://img.shields.io/badge/Pride_Beats-140_BPM-FF1493?style=for-the-badge&logo=music" alt="Pride Beats"/>
  </div>
  <div style="max-width:300px; text-align:center;">
    <h4>💻 Terminal & Rainbow Development</h4>
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git" alt="Git"/><br/>
    <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code" alt="VS Code"/><br/>
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github" alt="GitHub"/><br/>
    <img src="https://img.shields.io/badge/Rainbow_Terminal-4D4D4D?style=for-the-badge&logo=gnome-terminal" alt="Rainbow Terminal"/>
  </div>
</div>

</div>

---

<div align="center">

<!-- ==================== 11) Rainbow GitHub Pride Statistics ==================== -->
## 📊 Rainbow GitHub Pride Statistics

<p align="center">
  <a href="https://github.com/sharkBLN">
    <img src="https://github-readme-stats.vercel.app/api?username=sharkBLN&show_icons=true&theme=radical&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=e40303&text_color=F0F1F2&icon_color=ff8c00" height="180" alt="GitHub Stats"/>
  </a>
  <a href="https://github.com/sharkBLN">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sharkBLN&layout=compact&langs_count=7&theme=radical&bg_color=0d1117&title_color=ffed00&text_color=F0F1F2" height="180" alt="Top Languages"/>
  </a>
</p>
<p align="center">
  <a href="https://github.com/sharkBLN">
    <img src="https://streak-stats.demolab.com/?user=sharkBLN&theme=radical&background=0d1117&stroke=e40303&ring=ff8c00&fire=ffed00&currStreakNum=F0F1F2&sideNums=F0F1F2&currStreakLabel=008018&sideLabels=0078d4&dates=732982" alt="GitHub Streak" />
  </a>
</p>

</div>

---

<div align="center">

<!-- ==================== 12) Connect to the Rainbow Digital Empire ==================== -->
## 🔗 Connect to the Rainbow Digital Empire

<table>
  <tr>
    <td align="center">
      <h4><span style="color:#e40303">🏳️‍🌈</span> Pride Music & Audio</h4>
      [![SoundCloud](https://img.shields.io/badge/SoundCloud-Pride_Sets-FF3300?style=for-the-badge&logo=soundcloud)](https://soundcloud.com/nil-official)  
      [![Beatport](https://img.shields.io/badge/Beatport-Rainbow_Releases-FF6900?style=for-the-badge&logo=beatport)](https://beatport.com/artist/nil)  
      [![Booking](https://img.shields.io/badge/Booking-music@n--il.de-F20544?style=for-the-badge&logo=gmail)](mailto:music@n-il.de)
    </td>
    <td align="center">
      <h4><span style="color:#e40303">💻</span> Rainbow Development & Code</h4>
      [![Website](https://img.shields.io/badge/Portal-happening.today-0078d4?style=for-the-badge&logo=github-pages)](https://happening.today)  
      [![Dashboard](https://img.shields.io/badge/Rainbow-Central_Command-732982?style=for-the-badge&logo=terminal)](https://happening.today/dashboard.html)
    </td>
    <td align="center">
      <h4><span style="color:#e40303">🌈</span> Pride & Community</h4>
      [![Pride Portal](https://img.shields.io/badge/Pride-Love_Is_Love-e40303?style=for-the-badge&logo=heart)](https://happening.today/pride.html)  
      [![Equality](https://img.shields.io/badge/Human_Race-One_&_Equal-008018?style=for-the-badge&logo=rainbow)](https://happening.today/pride.html)
    </td>
  </tr>
</table>

</div>

---

<div align="center">

<!-- ==================== 13) Current Projects & Pride Experiments ==================== -->
## 🎯 Current Projects & Pride Experiments

| Projekt                       | Status         | Pride Faktor     | Technologie              | Beschreibung                               |
|:-----------------------------:|:--------------:|:----------------:|:------------------------:|:------------------------------------------:|
| 🌈 **Cyber Pride Bulldogge**         | `COMPLETED`    | 🏳️‍🌈 **MAX**      | `SVG + CSS Animations`   | Animierte Pride Bulldogge für Terminal-Banner   |
| 🎵 **140 BPM Pride Matrix**          | `STREAMING`    | 🏳️‍🌈 **HIGH**     | `Three.js + Web Audio`   | Realtime Audio-Visualisierung in Pride-Farben |
| 💻 **Rainbow Terminal Emulator**     | `ACTIVE DEV`   | 🏳️‍🌈 **HIGH**     | `JavaScript + Canvas`    | Pride-Themed Web-Terminal mit 140 BPM-Animationen |
| 🌊 **Pride Wave Generator**          | `PRODUCTION`   | 🏳️‍🌈 **MAX**      | `SVG + CSS Grid`         | Animierte Regenbogen-Wellen-Banner für GitHub |
| 🔮 **Digital Alchemy Pride**         | `EXPERIMENTING`| 🏳️‍🌈 **MEDIUM**   | `React + WebGL`          | Pride-Power-Tools zur Code-Transformation   |
| 🏃‍♂️ **Escape the Heteronorm**        | `PROTOTYPE`    | 🏳️‍🌈 **HIGH**     | `Phaser.js`              | Retro Pride-Arcade-Game-Prototype           |

</div>

---

<div align="center">

<!-- ==================== 14) Rainbow Philosophy & Digital Manifesto ==================== -->
## 💫 Rainbow Philosophy & Digital Manifesto

> „In der digitalen Welt gibt es keine Grenzen, keine Vorurteile, nur das wunderschöne Spektrum menschlicher Kreativität,  
>    das durch faseroptische Regenbögen fließt. Code ist Poesie, Musik ist Mathematik,  
>    und Liebe ist der ultimative Algorithmus, der jedes Mal perfekt kompiliert.“  
>    — <strong><span style="color:#e40303">s</span><span style="color:#ff8c00">h</span><span style="color:#ffed00">a</span><span style="color:#008018">r</span><span style="color:#0078d4">k</span><span style="color:#732982">B</span><span style="color:#e40303">L</span><span style="color:#ff8c00">N</span></strong>, Terminal Poet & Digital Pride Warrior 🌈

```text
# /etc/pride-manifesto.conf
# NIL Digital Empire Pride Manifesto v2025.06
# „Code with Pride, Create with Love, Debug with Empathy“

[CORE_VALUES]
diversity=infinite_spectrum
equality=non_negotiable
love=universal_constant
respect=default_mode
creativity=rainbow_powered

[DIGITAL_PHILOSOPHY]
# Every commit is an act of love
# Every pull request spreads understanding
# Every merge brings us closer together
# Every deploy macht die Welt bunter

[TERMINAL_WISDOM]
"sudo rm -rf /hatred"
"chmod 777 /love /respect /equality"
"export PRIDE_MODE=always_on"
"while true; do spread_rainbow_vibes; done"

[BERLIN_UNDERGROUND_TECHNO_CODE]
bpm=140
frequency=love
amplitude=maximum_pride
echo "🌈 Berlin never sleeps, and neither does equality 🌈"
</div>
<div align="center"> <!-- ==================== 15) About SharkBLN & NIL ==================== -->
🦈 About SharkBLN & NIL
Von den Underground-Techno-Clubs Berlins bis in den unendlichen digitalen Kosmos:

NIL steht für die Fusion authentischen menschlichen Ausdrucks mit modernster Technologie.
Jeder Beat, jede Codezeile und jeder Regenbogen-Pixel ist bewusst gestaltet,
um einen digitalen Raum zu erschaffen, in dem jede*r dazugehört,
Kreativität keine Grenzen kennt und Liebe die stärkste Kraft im Universum ist.

🌈 Gemeinsam coden wir eine bessere Zukunft 🌈

<em>Fun Fact: Der Name „NIL“ steht für den Null-Zustand – den Anfang unendlicher Möglichkeiten,
während „sharkBLN“ die scharfe, entschlossene Energie des Berliner
Kreativgeistes symbolisiert, der durch digitale Gewässer surft.</em> 🦈

bash
Copy
Edit
sharkBLN@rainbow-terminal:~$ echo "HAPPY PRIDE MONTH AND BEYOND! 🏳️‍🌈✨"
HAPPY PRIDE MONTH AND BEYOND! 🏳️‍🌈✨

sharkBLN@rainbow-terminal:~$ sudo systemctl restart love.service
[  OK  ] Started Love is Love Service – Universal Edition
[  OK  ] Started Equality for All Service – Human Race v1.0
[  OK  ] Started Rainbow Vibes Service – Maximum Pride Mode
[  OK  ] Started Berlin Underground Pride Techno Service – 140 BPM

sharkBLN@rainbow-terminal:~$ while true; do echo "🌈"; sleep 0.14; done
🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈
<p align="center"> <strong> 🌈 Maximum Pride Mode: ALWAYS ACTIVATED 🌈<br/> 🎵 140 BPM Berlin Underground Pride Techno 🎵<br/> 🏳️‍🌈 Love is Love, Code is Art, Equality is Non-Negotiable 🏳️‍🌈 </strong> </p> </div> <!-- ================================================================================= -->
