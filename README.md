<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NIL Digital Empire – Pride Edition</title>
  <style>
    :root {
      --red:    #e40303;
      --orange: #ff8c00;
      --yellow: #ffed00;
      --green:  #008018;
      --cyan:   #00ffff;
      --blue:   #0078d4;
      --indigo: #732982;
      --pink:   #ff00ff;
      --bg:     #0a0a0a;
      --text:   #00ff00;
    }
    body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Monaco, 'Courier New', monospace;
    }
    svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 1em auto;
    }
    /* Gemeinsamer Regenbogen-Gradient-Shift */
    @keyframes rainbow-shift {
      0%   { stop-color: var(--red); }
      14%  { stop-color: var(--orange); }
      28%  { stop-color: var(--yellow); }
      42%  { stop-color: var(--green); }
      56%  { stop-color: var(--blue); }
      70%  { stop-color: var(--indigo); }
      84%  { stop-color: var(--pink); }
      100% { stop-color: var(--red); }
    }
    .rainbow-stop {
      animation: rainbow-shift 3s infinite;
    }
    /* Glow- und Text-Schatten-Effekte */
    .glow { filter: url(#glow-filter); }
    .text-shadow { filter: url(#textshadow-filter); }
    /* Blinking Cursor */
    @keyframes blink { 0%,50%,100% { opacity:1 } 25%,75% { opacity:0 } }
    .cursor { animation: blink 1s infinite; }
    /* Cyber-Augen-Puls */
    @keyframes eye-glow { 0%,100% { fill: var(--text) } 50% { fill: var(--cyan) } }
    .cyber-eye { animation: eye-glow 1.5s infinite; }
    /* Wave-Bewegungen */
    @keyframes wave1 { 0%,100% { transform: translateX(0) } 50% { transform: translateX(-300px) } }
    @keyframes wave2 { 0%,100% { transform: translateX(0) } 50% { transform: translateX(200px)  } }
    @keyframes wave3 { 0%,100% { transform: translateX(0) } 50% { transform: translateX(-150px) } }
    .wave1 { animation: wave1 8s infinite; }
    .wave2 { animation: wave2 6s infinite; }
    .wave3 { animation: wave3 4s infinite; }
    /* Floating-Elemente */
    @keyframes float { 0%,100% { transform: translate(0,0) } 50% { transform: translate(var(--dx), var(--dy)) } }
    .float1 { --dx:50px; --dy:0px; animation: float 4s infinite; }
    .float2 { --dx:-30px; --dy:0px; animation: float 3s infinite; }
    .float3 { --dx:20px; --dy:-20px; animation: float 3s infinite; }
    .float4 { --dx:-15px; --dy:15px; animation: float 4s infinite; }
    /* Pre-Box für ASCII-Banner */
    pre.ascii-banner {
      background: #1a1a1a;
      padding: 1em;
      border-radius: 8px;
      color: var(--text);
      overflow-x: auto;
      margin: 1em auto;
      max-width: 90%;
    }
    table {
      border-collapse: collapse;
      margin: 1em auto;
      width: 90%;
      max-width: 1200px;
    }
    th, td {
      border: 1px solid #444;
      padding: 0.5em;
      text-align: center;
    }
    th {
      background: #222;
      color: var(--text);
    }
    td {
      background: #111;
      color: var(--text);
    }
    a img {
      vertical-align: middle;
    }
    hr {
      border: none;
      border-top: 1px solid #444;
      margin: 2em auto;
      width: 90%;
      max-width: 1200px;
    }
    h2, h3 {
      margin: 1.5em 0 0.5em;
      color: var(--text);
    }
  </style>
</head>
<body>

  <!-- 1) Haupt-Banner (komplett überarbeitet) -->
  <svg aria-label="NIL Digital Empire Pride Edition Banner" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400">
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
      <!-- Konsolidierter Regenbogen-Gradient -->
      <linearGradient id="rainbow-grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   class="rainbow-stop"/>
        <stop offset="16%"  class="rainbow-stop"/>
        <stop offset="33%"  class="rainbow-stop"/>
        <stop offset="50%"  class="rainbow-stop"/>
        <stop offset="66%"  class="rainbow-stop"/>
        <stop offset="83%"  class="rainbow-stop"/>
        <stop offset="100%" class="rainbow-stop"/>
      </linearGradient>
      <!-- Wellen-Gradient -->
      <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   style="stop-color: var(--red)"/>
        <stop offset="16%"  style="stop-color: var(--orange)"/>
        <stop offset="33%"  style="stop-color: var(--yellow)"/>
        <stop offset="50%"  style="stop-color: var(--green)"/>
        <stop offset="66%"  style="stop-color: var(--blue)"/>
        <stop offset="83%"  style="stop-color: var(--indigo)"/>
        <stop offset="100%" style="stop-color: var(--red)"/>
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
    <rect width="1200" height="400" fill="var(--bg)"/>

    <!-- Regenbogen-Rahmen -->
    <rect x="10" y="10" width="1180" height="380" rx="15"
          fill="none" stroke="url(#rainbow-grad)" stroke-width="6" class="glow">
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
          fill="url(#rainbow-grad)" class="text-shadow">
      NIL DIGITAL EMPIRE
      <animate attributeName="opacity" values="1;0.7;1" dur="1.5s" repeatCount="indefinite"/>
    </text>

    <!-- Untertitel -->
    <text x="600" y="180" text-anchor="middle"
          font-family="Monaco, 'Courier New', monospace" font-size="24"
          fill="var(--green)" class="glow">
      🏳️‍🌈 PRIDE EDITION 🏳️‍🌈
    </text>

    <!-- Prompt -->
    <text x="50" y="240"
          font-family="Monaco, 'Courier New', monospace" font-size="18"
          fill="var(--green)">
      sharkBLN@rainbow-terminal:~$
    </text>
    <text x="350" y="240"
          font-family="Monaco, 'Courier New', monospace" font-size="18"
          fill="#fff">
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
          fill="var(--green)" class="cursor"/>

    <!-- Cyber-Bulldogge -->
    <g transform="translate(80, 300)">
      <ellipse cx="0" cy="0" rx="45" ry="30" fill="url(#rainbow-grad)" opacity="0.8">
        <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="0" cy="-35" rx="35" ry="25" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="2"/>
      <ellipse cx="0" cy="-25" rx="20" ry="15" fill="#e0e0e0"/>
      <circle cx="-12" cy="-40" r="6" class="cyber-eye"/>
      <circle cx="12" cy="-40" r="6" class="cyber-eye"/>
      <rect x="-25" y="-45" width="50" height="8" fill="none" stroke="var(--cyan)" stroke-width="2" opacity="0.7">
        <animate attributeName="opacity" values="0.7;0.3;0.7" dur="1s" repeatCount="indefinite"/>
      </rect>
      <ellipse cx="0" cy="-28" rx="4" ry="3" fill="#333"/>
      <ellipse cx="-25" cy="-50" rx="8" ry="12" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="1"/>
      <ellipse cx="25" cy="-50" rx="8" ry="12" fill="#f0f0f0" stroke="url(#rainbow-grad)" stroke-width="1"/>
      <rect x="-30" y="-15" width="60" height="8" fill="url(#rainbow-grad)" rx="4">
        <animate attributeName="fill" values="url(#rainbow-grad);#ff00ff;url(#rainbow-grad)" dur="3s" repeatCount="indefinite"/>
      </rect>
      <circle cx="-20" cy="-11" r="2" fill="var(--cyan)"/>
      <circle cx="0" cy="-11"   r="2" fill="var(--cyan)"/>
      <circle cx="20" cy="-11"  r="2" fill="var(--cyan)"/>
      <rect x="-35" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
      <rect x="-15" y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
      <rect x="5"   y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
      <rect x="25"  y="20" width="12" height="20" fill="#f0f0f0" rx="6"/>
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
            fill="var(--green)">
        140 BPM TAIL WAG
      </text>
    </g>

    <!-- Floating Pride-Elemente -->
    <text x="100" y="350" font-size="20" fill="#ff0080" class="float1">♦</text>
    <text x="1050" y="350" font-size="20" fill="#00ff80" class="float2">▲</text>
    <text x="150" y="320" font-size="16" fill="#ff0080" class="float3">♥</text>
    <text x="350" y="300" font-size="14" fill="#00ff80" class="float4">🌈</text>

    <!-- ASCII-Ecken -->
    <text x="30"   y="100" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">╔═══</text>
    <text x="1130" y="100" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">═══╗</text>
    <text x="30"   y="370" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">╚═══</text>
    <text x="1130" y="370" font-family="Monaco, 'Courier New', monospace" font-size="14" fill="#666">═══╝</text>
  </svg>

  <!-- 2) Kompakte ASCII-Banner -->
  <pre class="ascii-banner">
╔════════════════════════════════════════════════════════════════════╗
║ 🏳️‍🌈♪♫♪ NIL DIGITAL EMPIRE - PRIDE EDITION ♪♫♪🏳️‍🌈               ║
║ ▸═══► LOVE IS LOVE • ONE HUMAN RACE • EQUALITY FOR ALL ◄═══◂    ║
║ 🌈▲▼▲ BERLIN • TERMINAL WIZARD • 140 BPM TECHNO ▲▼▲🌈          ║
║ ♦♦♦ AUDIO NECROMANCER • CYBERPUNK AESTHETICS ♦♦♦               ║
║ ≋≋≋ SPREADING RAINBOW VIBES ACROSS THE DIGITAL REALM ≋≋≋      ║
║ ★☆★ HAPPY PRIDE! EVERY HUMAN DESERVES LOVE & RESPECT ★☆★      ║
╚════════════════════════════════════════════════════════════════════╝
  </pre>

  <!-- 3) Love-Is-Love-SVG (neue Sektion) -->
  <svg viewBox="0 0 800 60" xmlns="http://www.w3.org/2000/svg" aria-label="Love Is Love Banner">
    <defs>
      <!-- Pride-Gradient -->
      <linearGradient id="prideGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   style="stop-color:#e40303"/>
        <stop offset="16.66%" style="stop-color:#ff8c00"/>
        <stop offset="33.33%" style="stop-color:#ffed00"/>
        <stop offset="50%"  style="stop-color:#008c26"/>
        <stop offset="66.66%" style="stop-color:#004cff"/>
        <stop offset="83.33%" style="stop-color:#732982"/>
        <stop offset="100%"  style="stop-color:#e40303"/>
        <animateTransform attributeName="gradientTransform" type="translate"
                          values="0 0; 100 0; 0 0" dur="3s" repeatCount="indefinite"/>
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
    <rect x="780" y="25" width="3" height="12" fill="#00ff00" class="cursor"/>
  </svg>

  <hr/>

  <!-- Kontakt-Links -->
  <div style="text-align:center; margin:1em 0;">
    <a href="https://soundcloud.com/nil-official" style="margin: 0 0.5em;">
      <img src="https://img.shields.io/badge/SoundCloud-FF3300?style=for-the-badge&logo=soundcloud&logoColor=white" alt="SoundCloud"/>
    </a>
    <a href="https://beatport.com/artist/nil" style="margin: 0 0.5em;">
      <img src="https://img.shields.io/badge/Beatport-FF6900?style=for-the-badge&logo=beatport&logoColor=white" alt="Beatport"/>
    </a>
    <a href="mailto:music@n-il.de" style="margin: 0 0.5em;">
      <img src="https://img.shields.io/badge/Music-music@n--il.de-F20544?style=for-the-badge&logo=gmail&logoColor=white" alt="E-Mail"/>
    </a>
    <a href="https://happening.today" style="margin: 0 0.5em;">
      <img src="https://img.shields.io/badge/Portal-happening.today-0078d4?style=for-the-badge&logo=github-pages&logoColor=white" alt="Website"/>
    </a>
  </div>

  <hr/>

  <!-- 4) Now Playing SVG (neue Sektion) -->
  <svg aria-label="Now Playing NIL – Berlin Underground Pride Techno (140 BPM)" viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Regenbogen-Gradient für Now Playing -->
      <linearGradient id="nowPlayingGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#e40303">
          <animate attributeName="stop-color" values="#e40303;#ff8c00;#ffed00;#008c26;#004cff;#732982;#e40303" dur="2s" repeatCount="indefinite"/>
        </stop>
        <stop offset="50%" style="stop-color:#008c26">
          <animate attributeName="stop-color" values="#008c26;#004cff;#732982;#e40303;#ff8c00;#ffed00;#008c26" dur="2s" repeatCount="indefinite"/>
        </stop>
        <stop offset="100%" style="stop-color:#732982">
          <animate attributeName="stop-color" values="#732982;#e40303;#ff8c00;#ffed00;#008c26;#004cff;#732982" dur="2s" repeatCount="indefinite"/>
        </stop>
      </linearGradient>
      <!-- Glow-Filter für Text -->
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
      NIL - Berlin Underground Pride Techno (140 BPM)
    </text>
    <!-- Equalizer-Balken -->
    <g transform="translate(450, 20)">
      <rect x="0"  y="20" width="6" height="20" fill="#00ff00">
        <animate attributeName="height" values="20;5;30;10;20" dur="0.5s" repeatCount="indefinite"/>
        <animate attributeName="y"      values="20;35;10;30;20" dur="0.5s" repeatCount="indefinite"/>
      </rect>
      <rect x="10" y="15" width="6" height="25" fill="#00ffff">
        <animate attributeName="height" values="25;10;35;15;25" dur="0.7s" repeatCount="indefinite"/>
        <animate attributeName="y"      values="15;30;5;25;15" dur="0.7s" repeatCount="indefinite"/>
      </rect>
      <rect x="20" y="10" width="6" height="30" fill="#ff00ff">
        <animate attributeName="height" values="30;15;40;20;30" dur="0.3s" repeatCount="indefinite"/>
        <animate attributeName="y"      values="10;25;0;20;10" dur="0.3s" repeatCount="indefinite"/>
      </rect>
      <rect x="30" y="25" width="6" height="15" fill="#ffff00">
        <animate attributeName="height" values="15;5;25;10;15" dur="0.8s" repeatCount="indefinite"/>
        <animate attributeName="y"      values="25;35;15;30;25" dur="0.8s" repeatCount="indefinite"/>
      </rect>
      <rect x="40" y="18" width="6" height="22" fill="#ff8000">
        <animate attributeName="height" values="22;8;32;12;22" dur="0.4s" repeatCount="indefinite"/>
        <animate attributeName="y"      values="18;32;8;28;18" dur="0.4s" repeatCount="indefinite"/>
      </rect>
    </g>
    <!-- Pulsing Pride-Herz -->
    <text x="520" y="35" font-size="20" fill="url(#nowPlayingGradient)">🏳️‍🌈</text>
    <!-- BPM-Indikator -->
    <circle cx="560" cy="25" r="8" fill="none" stroke="#00ff00" stroke-width="2">
      <animate attributeName="r"      values="8;12;8" dur="0.428s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.3;1" dur="0.428s" repeatCount="indefinite"/>
    </circle>
    <text x="560" y="29" font-family="Monaco, 'Courier New', monospace" font-size="8" text-anchor="middle" fill="#00ff00">140</text>
  </svg>

  <hr/>

  <!-- 5) Pride Wave SVG (neue Sektion) -->
  <svg aria-label="Pride Wave Protocol Banner" viewBox="0 0 1200 200" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Wave-Gradient -->
      <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   style="stop-color:#e40303"/>
        <stop offset="16.66%" style="stop-color:#ff8c00"/>
        <stop offset="33.33%" style="stop-color:#ffed00"/>
        <stop offset="50%"  style="stop-color:#008c26"/>
        <stop offset="66.66%" style="stop-color:#004cff"/>
        <stop offset="83.33%" style="stop-color:#722f37"/>
        <stop offset="100%"   style="stop-color:#e40303"/>
        <animateTransform attributeName="gradientTransform" type="translate"
                          values="0 0; 100 0; 0 0" dur="4s" repeatCount="indefinite"/>
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
          fill="url(#animatedRainbow)" opacity="0.6" filter="url(#waveGlow)" class="wave1"/>

    <!-- Wave 2 (mittel) -->
    <path d="M0,130 Q200,80 400,130 T800,130 T1200,130 L1200,200 L0,200 Z"
          fill="url(#waveGradient)" opacity="0.7" filter="url(#waveGlow)" class="wave2"/>

    <!-- Wave 3 (oben) -->
    <path d="M0,110 Q100,60 200,110 T400,110 T600,110 T800,110 T1000,110 T1200,110 L1200,200 L0,200 Z"
          fill="url(#animatedRainbow)" opacity="0.8" filter="url(#cyberGlow)" class="wave3"/>

    <!-- Overlay-Text -->
    <text x="600" y="50" text-anchor="middle"
          font-family="Monaco, 'Courier New', monospace" font-size="28" font-weight="bold"
          fill="var(--text)" filter="url(#cyberGlow)">
      🏳️‍🌈 PRIDE WAVE PROTOCOL 🏳️‍🌈
      <animate attributeName="opacity" values="1;0.7;1" dur="2s" repeatCount="indefinite"/>
    </text>

    <!-- Mini-Bulldogge auf Welle -->
    <g transform="translate(900,130)">
      <ellipse cx="0" cy="0" rx="15" ry="10" fill="url(#animatedRainbow)" opacity="0.9">
        <animate attributeName="opacity" values="0.9;1;0.9" dur="1s" repeatCount="indefinite"/>
      </ellipse>
      <circle cx="-5" cy="-3" r="2" fill="#00ffff" filter="url(#cyberGlow)"/>
      <circle cx="5" cy="-3" r="2" fill="#00ffff" filter="url(#cyberGlow)"/>
      <animateTransform attributeName="transform" type="translate"
                        values="900,130;850,125;900,130" dur="5s" repeatCount="indefinite"/>
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
      <animateTransform attributeName="transform" type="translate" values="0,0; -100,-5; 0,0" dur="7s" repeatCount="indefinite"/>
    </g>
  </svg>

  <hr/>

  <!-- 6) Love Is Love Bash-Skript (als Pre-Code Box) -->
  <h3 align="center">
    <span style="color: var(--red)">💖 O</span><span style="color: var(--orange)">N</span>
    <span style="color: var(--yellow)">E</span> 
    <span style="color: var(--green)">H</span><span style="color: var(--blue)">U</span>
    <span style="color: var(--indigo)">M</span><span style="color: var(--red)">A</span>
    <span style="color: var(--orange)">N</span> 
    <span style="color: var(--yellow)">R</span><span style="color: var(--green)">A</span>
    <span style="color: var(--blue)">C</span><span style="color: var(--indigo)">E</span> 💖
  </h3>
  <div style="text-align:center;">
    <pre class="ascii-banner">
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

  <div style="text-align:center; margin-bottom:2em; font-size:1.1em;">
    <strong>
      Ob du straight, gay, lesbian, bi, trans, pan, ace, non-binär oder irgendwo dazwischen bist – 
      du bist geliebt, du bist valide, und du verdienst Gleichberechtigung.<br>
      Das ist keine Politik, das ist MENSCHENRECHT. 💖✨
    </strong>
  </div>

  <hr/>

  <!-- 7) Current Status (als Terminal-Box) -->
  <h2 align="center">🚀 Current Status</h2>
  <div style="background:#1a1a1a; color:var(--text); font-family:Monaco, 'Courier New', monospace; padding:1em; border-radius:8px; margin:1em auto; max-width:90%;">
<code>
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
</code>
  </div>

  <hr/>

  <!-- 8) Rainbow Digital Portals -->
  <h2 align="center">🌈 Rainbow Digital Portals</h2>
  <table>
    <tr>
      <th>Portal</th><th>Theme</th><th>Status</th><th>Pride Level</th><th>Beschreibung</th>
    </tr>
    <tr>
      <td>🎵 <a href="https://happening.today/music.html" style="color: var(--orange); text-decoration: none;"><strong>Audio Necromancer</strong></a></td>
      <td><code>Pride Pink Fire</code></td>
      <td>🌈 <strong>RAINBOW STREAMING</strong></td>
      <td>🏳️‍🌈 MAX</td>
      <td>Underground Techno mit Pride-Beats, 140 BPM</td>
    </tr>
    <tr>
      <td>🧪 <a href="https://happening.today/alchemy.html" style="color: var(--green); text-decoration: none;"><strong>Digital Alchemy Lab</strong></a></td>
      <td><code>Rainbow Matrix Green</code></td>
      <td>🌈 <strong>PRIDE EXPERIMENTING</strong></td>
      <td>🏳️‍🌈 HIGH</td>
      <td>Code-Experimente mit Regenbogen-Algorithmen</td>
    </tr>
    <tr>
      <td>💻 <a href="https://happening.today/projects.html" style="color: var(--blue); text-decoration: none;"><strong>Development Portfolio</strong></a></td>
      <td><code>Pride Ice Blue</code></td>
      <td>🌈 <strong>RAINBOW SHOWCASING</strong></td>
      <td>🏳️‍🌈 HIGH</td>
      <td>Kunden-Projekte mit Pride-Ästhetik</td>
    </tr>
    <tr>
      <td>🔬 <a href="https://happening.today/lab.html" style="color: var(--indigo); text-decoration: none;"><strong>Experimental Lab</strong></a></td>
      <td><code>Rainbow Fire Orange</code></td>
      <td>🌈 <strong>PRIDE MAINTENANCE</strong></td>
      <td>🏳️‍🌈 MEDIUM</td>
      <td>Kreative Regenbogen-Chaos-Experimente</td>
    </tr>
    <tr>
      <td>👑 <a href="https://happening.today/dashboard.html" style="color: var(--pink); text-decoration: none;"><strong>Central Dashboard</strong></a></td>
      <td><code>Full Rainbow Spectrum</code></td>
      <td>🌈 <strong>RAINBOW COMMAND</strong></td>
      <td>🏳️‍🌈 MAXIMUM</td>
      <td>Admin-Center mit allen Pride-Farben</td>
    </tr>
    <tr>
      <td>🏳️‍🌈 <a href="https://happening.today/pride.html" style="color: var(--red); text-decoration: none;"><strong>Pride Portal</strong></a></td>
      <td><code>PURE RAINBOW</code></td>
      <td>🌈 <strong>SPREADING MAXIMUM LOVE</strong></td>
      <td>🏳️‍🌈 ∞</td>
      <td>Gleichheit, Vielfalt, ONE HUMAN RACE HQ</td>
    </tr>
  </table>

  <hr/>

  <!-- 9) Rainbow Tech Stack & Pride Arsenal -->
  <h2 align="center">⚡ Rainbow Tech Stack & Pride Arsenal</h2>
  <div style="display:flex; justify-content:center; flex-wrap:wrap; gap:2em; margin:2em 0;">
    <div style="max-width:300px;">
      <h3 style="margin-bottom:0.5em; text-align:center;">
        <span style="color: var(--red)">🌈</span>
        <span style="color: var(--orange)">F</span><span style="color: var(--yellow)">r</span><span style="color: var(--green)">o</span>
        <span style="color: var(--blue)">n</span><span style="color: var(--indigo)">t</span><span style="color: var(--red)">e</span>
        <span style="color: var(--orange)">n</span><span style="color: var(--yellow)">d</span> 
        <span style="color: var(--green)">R</span><span style="color: var(--blue)">a</span>
        <span style="color: var(--indigo)">i</span><span style="color: var(--red)">n</span>
        <span style="color: var(--orange)">b</span><span style="color: var(--yellow)">o</span>
        <span style="color: var(--green)">w</span> <span style="color: var(--blue)">W</span>
        <span style="color: var(--indigo)">i</span><span style="color: var(--red)">z</span>
        <span style="color: var(--orange)">a</span><span style="color: var(--yellow)">r</span>
        <span style="color: var(--green)">d</span><span style="color: var(--blue)">r</span>
        <span style="color: var(--indigo)">y</span>
      </h3>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5" alt="HTML5"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3" alt="CSS3"/>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
      <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js" alt="Three.js"/>
      <img src="https://img.shields.io/badge/Pride-Code-FF69B4?style=for-the-badge&logo=heart" alt="Pride Code"/>
    </div>
    <div style="max-width:300px;">
      <h3 style="margin-bottom:0.5em; text-align:center;">
        <span style="color: var(--red)">🎵</span>
        <span style="color: var(--orange)">A</span><span style="color: var(--yellow)">u</span>
        <span style="color: var(--green)">d</span><span style="color: var(--blue)">i</span>
        <span style="color: var(--indigo)">o</span> 
        <span style="color: var(--red)">P</span><span style="color: var(--orange)">r</span>
        <span style="color: var(--yellow)">o</span><span style="color: var(--green)">d</span>
        <span style="color: var(--blue)">u</span><span style="color: var(--indigo)">c</span>
        <span style="color: var(--red)">t</span><span style="color: var(--orange)">i</span>
        <span style="color: var(--yellow)">o</span><span style="color: var(--green)">n</span> 
        <span style="color: var(--blue)">w</span><span style="color: var(--indigo)">i</span>
        <span style="color: var(--red)">t</span><span style="color: var(--orange)">h</span> 
        <span style="color: var(--yellow)">P</span><span style="color: var(--green)">r</span>
        <span style="color: var(--blue)">i</span><span style="color: var(--indigo)">d</span>
        <span style="color: var(--red)">e</span>
      </h3>
      <img src="https://img.shields.io/badge/Logic_Pro-000000?style=for-the-badge&logo=apple" alt="Logic Pro"/>
      <img src="https://img.shields.io/badge/Ableton_Live-000000?style=for-the-badge&logo=ableton-live" alt="Ableton Live"/>
      <img src="https://img.shields.io/badge/SoundCloud-FF3300?style=for-the-badge&logo=soundcloud" alt="SoundCloud"/>
      <img src="https://img.shields.io/badge/Pride_Beats-140_BPM-FF1493?style=for-the-badge&logo=music" alt="Pride Beats"/>
    </div>
    <div style="max-width:300px;">
      <h3 style="margin-bottom:0.5em; text-align:center;">
        <span style="color: var(--red)">💻</span> 
        <span style="color: var(--orange)">T</span><span style="color: var(--yellow)">e</span>
        <span style="color: var(--green)">r</span><span style="color: var(--blue)">m</span>
        <span style="color: var(--indigo)">i</span><span style="color: var(--red)">n</span>
        <span style="color: var(--orange)">a</span><span style="color: var(--yellow)">l</span> 
        <span style="color: var(--green)">&</span> 
        <span style="color: var(--blue)">R</span><span style="color: var(--indigo)">a</span>
        <span style="color: var(--red)">i</span><span style="color: var(--orange)">n</span>
        <span style="color: var(--yellow)">b</span><span style="color: var(--green)">o</span>
        <span style="color: var(--blue)">w</span> 
        <span style="color: var(--indigo)">D</span><span style="color: var(--red)">e</span>
        <span style="color: var(--orange)">v</span><span style="color: var(--yellow)">e</span>
        <span style="color: var(--green)">l</span><span style="color: var(--blue)">o</span>
        <span style="color: var(--indigo)">p</span><span style="color: var(--red)">m</span>
        <span style="color: var(--orange)">e</span><span style="color: var(--yellow)">n</span>
        <span style="color: var(--green)">t</span>
      </h3>
      <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git" alt="Git"/>
      <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code" alt="VS Code"/>
      <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github" alt="GitHub"/>
      <img src="https://img.shields.io/badge/Rainbow_Terminal-4D4D4D?style=for-the-badge&logo=gnome-terminal" alt="Rainbow Terminal"/>
    </div>
  </div>

  <hr/>

  <!-- 10) Rainbow GitHub Pride Statistics -->
  <h2 align="center">📊 Rainbow GitHub Pride Statistics</h2>
  <div style="display: flex; gap: 1em; justify-content: center; flex-wrap: wrap; margin:1em 0;">
    <a href="https://github.com/sharkBLN">
      <img src="https://github-readme-stats.vercel.app/api?username=sharkBLN&show_icons=true&theme=radical&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=e40303&text_color=F0F1F2&icon_color=ff8c00" height="180" alt="GitHub Stats"/>
    </a>
    <a href="https://github.com/sharkBLN">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sharkBLN&layout=compact&langs_count=7&theme=radical&bg_color=0d1117&title_color=ffed00&text_color=F0F1F2" height="180" alt="Top Languages"/>
    </a>
  </div>
  <div style="text-align:center; margin-top:1em;">
    <a href="https://github.com/sharkBLN">
      <img src="https://streak-stats.demolab.com/?user=sharkBLN&theme=radical&background=0d1117&stroke=e40303&ring=ff8c00&fire=ffed00&currStreakNum=F0F1F2&sideNums=F0F1F2&currStreakLabel=008018&sideLabels=0078d4&dates=732982" alt="GitHub Streak" />
    </a>
  </div>

  <hr/>

  <!-- 11) Pride Audio Frequencies & Rainbow Beats (extra Now Playing ist oben integriert) -->

  <!-- 12) Connect to Rainbow Digital Empire -->
  <h2 align="center">🔗 Connect to the Rainbow Digital Empire</h2>
  <table>
    <tr>
      <td align="center">
        <h3><span style="color: var(--red)">🏳️‍🌈</span>
          <span style="color: var(--orange)">P</span><span style="color: var(--yellow)">r</span>
          <span style="color: var(--green)">i</span><span style="color: var(--blue)">d</span>
          <span style="color: var(--indigo)">e</span> 
          <span style="color: var(--red)">M</span><span style="color: var(--orange)">u</span>
          <span style="color: var(--yellow)">s</span><span style="color: var(--green)">i</span>
          <span style="color: var(--blue)">c</span> & 
          <span style="color: var(--pink)">A</span><span style="color: var(--red)">u</span>
          <span style="color: var(--orange)">d</span><span style="color: var(--yellow)">i</span>
          <span style="color: var(--green)">o</span>
        </h3>
        <a href="https://soundcloud.com/nil-official" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/SoundCloud-Pride_Sets-FF3300?style=for-the-badge&logo=soundcloud" alt="SoundCloud Pride Sets"/>
        </a>
        <a href="https://beatport.com/artist/nil" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Beatport-Rainbow_Releases-FF6900?style=for-the-badge&logo=beatport" alt="Beatport Rainbow Releases"/>
        </a>
        <a href="mailto:music@n-il.de" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Booking-music@n--il.de-F20544?style=for-the-badge&logo=gmail" alt="Booking E-Mail"/>
        </a>
      </td>
      <td align="center">
        <h3><span style="color: var(--red)">💻</span>
          <span style="color: var(--orange)">R</span><span style="color: var(--yellow)">a</span>
          <span style="color: var(--green)">i</span><span style="color: var(--blue)">n</span>
          <span style="color: var(--indigo)">b</span><span style="color: var(--red)">o</span>
          <span style="color: var(--orange)">w</span> 
          <span style="color: var(--yellow)">D</span><span style="color: var(--green)">e</span>
          <span style="color: var(--blue)">v</span><span style="color: var(--indigo)">e</span>
          <span style="color: var(--red)">l</span><span style="color: var(--orange)">o</span>
          <span style="color: var(--yellow)">p</span><span style="color: var(--green)">m</span>
          <span style="color: var(--blue)">e</span><span style="color: var(--indigo)">n</span>
          <span style="color: var(--red)">t</span> & 
          <span style="color: var(--orange)">C</span><span style="color: var(--yellow)">o</span>
          <span style="color: var(--green)">d</span><span style="color: var(--blue)">e</span>
        </h3>
        <a href="https://happening.today" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Portal-happening.today-0078d4?style=for-the-badge&logo=github-pages" alt="Website"/>
        </a>
        <a href="https://happening.today/dashboard.html" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Rainbow-Central_Command-732982?style=for-the-badge&logo=terminal" alt="Central Command Dashboard"/>
        </a>
      </td>
      <td align="center">
        <h3><span style="color: var(--red)">🌈</span>
          <span style="color: var(--orange)">P</span><span style="color: var(--yellow)">r</span>
          <span style="color: var(--green)">i</span><span style="color: var(--blue)">d</span>
          <span style="color: var(--indigo)">e</span> & 
          <span style="color: var(--red)">C</span><span style="color: var(--orange)">o</span>
          <span style="color: var(--yellow)">m</span><span style="color: var(--green)">m</span>
          <span style="color: var(--blue)">u</span><span style="color: var(--indigo)">n</span>
          <span style="color: var(--red)">i</span><span style="color: var(--orange)">t</span>
          <span style="color: var(--yellow)">y</span>
        </h3>
        <a href="https://happening.today/pride.html" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Pride-Love_Is_Love-e40303?style=for-the-badge&logo=heart" alt="Pride Love Is Love"/>
        </a>
        <a href="https://happening.today/pride.html" style="margin:0 0.5em;">
          <img src="https://img.shields.io/badge/Human_Race-One_&_Equal-008018?style=for-the-badge&logo=rainbow" alt="One & Equal"/>
        </a>
      </td>
    </tr>
  </table>

  <hr/>

  <!-- 13) Current Projects & Pride Experiments -->
  <h2 align="center">🎯 Current Projects & Pride Experiments</h2>
  <table>
    <tr>
      <th>Projekt</th><th>Status</th><th>Pride Faktor</th><th>Technologie</th><th>Beschreibung</th>
    </tr>
    <tr>
      <td>🌈 <strong>Cyber Pride Bulldogge</strong></td>
      <td><code>COMPLETED</code></td>
      <td>🏳️‍🌈 <strong>MAX</strong></td>
      <td><code>SVG + CSS Animations</code></td>
      <td>Animierte Pride Bulldogge für Terminal-Banner</td>
    </tr>
    <tr>
      <td>🎵 <strong>140 BPM Pride Matrix</strong></td>
      <td><code>STREAMING</code></td>
      <td>🏳️‍🌈 HIGH</td>
      <td><code>Three.js + Web Audio</code></td>
      <td>Realtime Audio-Visualisierung in Pride-Farben</td>
    </tr>
    <tr>
      <td>💻 <strong>Rainbow Terminal Emulator</strong></td>
      <td><code>ACTIVE DEV</code></td>
      <td>🏳️‍🌈 HIGH</td>
      <td><code>JavaScript + Canvas</code></td>
      <td>Pride-Themed Web-Terminal mit 140 BPM-Animationen</td>
    </tr>
    <tr>
      <td>🌊 <strong>Pride Wave Generator</strong></td>
      <td><code>PRODUCTION</code></td>
      <td>🏳️‍🌈 MAX</td>
      <td><code>SVG + CSS Grid</code></td>
      <td>Animierte Regenbogen-Wellen-Banner für GitHub</td>
    </tr>
    <tr>
      <td>🔮 <strong>Digital Alchemy Pride</strong></td>
      <td><code>EXPERIMENTING</code></td>
      <td>🏳️‍🌈 MEDIUM</td>
      <td><code>React + WebGL</code></td>
      <td>Pride-Power-Tools zur Code-Transformation</td>
    </tr>
    <tr>
      <td>🏃‍♂️ <strong>Escape the Heteronorm</strong></td>
      <td><code>PROTOTYPE</code></td>
      <td>🏳️‍🌈 HIGH</td>
      <td><code>Phaser.js</code></td>
      <td>Retro Pride-Arcade-Game-Prototype</td>
    </tr>
  </table>

  <hr/>

  <!-- 14) Rainbow Philosophy & Digital Manifesto -->
  <h2 align="center">💫 Rainbow Philosophy & Digital Manifesto</h2>
  <div style="text-align:center; font-style:italic; color:#ccc; margin:1em auto; max-width:800px;">
    „In der digitalen Welt gibt es keine Grenzen, keine Vorurteile, nur das wunderschöne Spektrum menschlicher Kreativität,
    das durch faseroptische Regenbögen fließt. Code ist Poesie, Musik ist Mathematik, und Liebe ist der ultimative Algorithmus,
    der jedes Mal perfekt kompiliert.“
    <br>— <strong>
      <span style="color: var(--red)">s</span><span style="color: var(--orange)">h</span>
      <span style="color: var(--yellow)">a</span><span style="color: var(--green)">r</span>
      <span style="color: var(--blue)">k</span><span style="color: var(--indigo)">B</span>
      <span style="color: var(--red)">L</span><span style="color: var(--orange)">N</span>
    </strong>, Terminal Poet & Digital Pride Warrior 🌈
  </div>

  <div style="background:#1a1a1a; color:var(--text); font-family:Monaco, 'Courier New', monospace; padding:1em; border-radius:8px; margin:1em auto; max-width:90%;">
<code>
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
</code>
  </div>

  <hr/>

  <!-- 15) About SharkBLN & NIL -->
  <h2 align="center">🦈 About SharkBLN & NIL</h2>
  <div style="text-align:center; color:#ddd; max-width:800px; margin:1em auto;">
    <p><strong>Von den Underground-Techno-Clubs Berlins bis in den unendlichen digitalen Kosmos:</strong><br>
    NIL steht für die Fusion authentischen menschlichen Ausdrucks mit modernster Technologie. Jeder Beat, jede Codezeile und jeder Regenbogen-Pixel ist bewusst gestaltet,
    um einen digitalen Raum zu erschaffen, in dem jede*r dazugehört, Kreativität keine Grenzen kennt und Liebe die stärkste Kraft im Universum ist.</p>
    <p>🌈 Gemeinsam coden wir eine bessere Zukunft 🌈</p>
    <p><em>Fun Fact: Der Name „NIL“ steht für den Null-Zustand – den Anfang unendlicher Möglichkeiten, während „sharkBLN“ die scharfe, entschlossene Energie
       des Berliner Kreativgeistes symbolisiert, der durch digitale Gewässer surft.</em> 🦈</p>
  </div>

  <div style="text-align:center; margin:1em 0;">
<code>
sharkBLN@rainbow-terminal:~$ echo "HAPPY PRIDE MONTH AND BEYOND! 🏳️‍🌈✨"
HAPPY PRIDE MONTH AND BEYOND! 🏳️‍🌈✨

sharkBLN@rainbow-terminal:~$ sudo systemctl restart love.service
[  OK  ] Started Love is Love Service – Universal Edition
[  OK  ] Started Equality for All Service – Human Race v1.0
[  OK  ] Started Rainbow Vibes Service – Maximum Pride Mode
[  OK  ] Started Berlin Underground Pride Techno Service – 140 BPM

sharkBLN@rainbow-terminal:~$ while true; do echo "🌈"; sleep 0.14; done
🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈
</code>
  </div>

  <h3 align="center">
    <span style="color: var(--red)">🏳️‍🌈</span>
    <span style="color: var(--orange)">Spread Rainbow Love Across the Digital Realm</span>
    <span style="color: var(--yellow)">🏳️‍🌈</span>
  </h3>

  <div style="text-align:center; margin:2em 0;">
    <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2FsharkBLN">
      <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FsharkBLN&labelColor=%23e40303&countColor=%23ff8c00&style=flat&labelStyle=upper" alt="Visitors"/>
    </a>
  </div>

  <div style="text-align:center; margin-bottom:2em;">
    <strong>
      🌈 Maximum Pride Mode: ALWAYS ACTIVATED 🌈<br>
      🎵 140 BPM Berlin Underground Pride Techno 🎵<br>
      🏳️‍🌈 Love is Love, Code is Art, Equality is Non-Negotiable 🏳️‍🌈
    </strong>
  </div>
</body>
</html>
