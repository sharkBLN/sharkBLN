[Uploading UNDER CONSTRUCTIO
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UNDER CONSTRUCTION • itshappening.today</title>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            background: #151616;
            color: #F0F1F2;
            font-family: 'JetBrains Mono', monospace;
            min-height: 100vh;
            margin: 0;
            overflow-x: hidden;
        }
        .arcade-border {
            pointer-events:none;
            position:fixed;top:0;left:0;width:100vw;height:100vh;
            border:6px solid #00ff41;
            box-shadow:0 0 20px 6px #00ff41aa, 0 0 80px 10px #ff00c8aa inset;
            border-radius:24px;
            z-index:99;
            animation: border-glitch 1.9s infinite alternate;
        }
        @keyframes border-glitch {
            0% { box-shadow:0 0 20px 6px #00ff41aa, 0 0 80px 10px #ff00c8aa inset;}
            10% { box-shadow:0 0 40px 12px #ff00c8aa, 0 0 120px 24px #00fff7bb inset;}
            40% { box-shadow:0 0 16px 5px #00ff41dd, 0 0 96px 12px #ffed00bb inset;}
            60% { box-shadow:0 0 50px 14px #ffed00cc, 0 0 48px 7px #00ff41cc inset;}
            100% { box-shadow:0 0 20px 6px #00ff41aa, 0 0 80px 10px #ff00c8aa inset;}
        }
        .arcade-invaders {
            text-align:center;
            margin-top:28px;
            font-size:42px;
            letter-spacing: 10px;
            animation: invader-float 1.7s infinite alternate;
        }
        .arcade-invaders span {
            filter: drop-shadow(0 0 7px #ff00c8) drop-shadow(0 0 3px #00ff41);
            animation: invader-blink 2.7s infinite;
            display: inline-block;
        }
        .arcade-invaders span:nth-child(2) { animation-delay: 0.33s;}
        .arcade-invaders span:nth-child(3) { animation-delay: 0.66s;}
        .arcade-invaders span:nth-child(4) { animation-delay: 1s;}
        .arcade-invaders span:nth-child(5) { animation-delay: 1.33s;}
        @keyframes invader-float {
            0%{transform:translateY(0);} 100%{transform:translateY(-12px);}
        }
        @keyframes invader-blink {
            0%,80%,100% {opacity:1;filter:drop-shadow(0 0 7px #ff00c8) drop-shadow(0 0 3px #00ff41);}
            60% {opacity:.5;filter:drop-shadow(0 0 20px #ffed00) drop-shadow(0 0 7px #ff00c8);}
        }
        .arcade-header {
            font-family: 'Press Start 2P', 'JetBrains Mono', monospace;
            font-size: 52px;
            text-align: center;
            margin: 60px auto 18px auto;
            color: #ffed00;
            text-shadow:0 0 28px #ff00c8, 0 0 8px #00ff41;
            letter-spacing:2px;
            position:relative;
            animation: glitch-pulse 1.2s infinite alternate, header-glitch 1.1s infinite alternate;
            z-index:1;
        }
        .glitch {
            position: relative;
        }
        .glitch::before, .glitch::after {
            content: attr(data-text);
            position: absolute;
            left: 0; width: 100%;
        }
        .glitch::before {
            color: #ff00c8; top: -3px; left: 3px; opacity: .67;
            clip-path: polygon(0 0,100% 0,100% 50%,0 50%);
            animation: glitch-top 1.2s infinite linear alternate;
        }
        .glitch::after {
            color: #00fff7; top: 3px; left: -3px; opacity: .62;
            clip-path: polygon(0 50%,100% 50%,100% 100%,0 100%);
            animation: glitch-bot 1.6s infinite linear alternate;
        }
        @keyframes glitch-top { 0%{left:3px;} 100%{left:0px;}}
        @keyframes glitch-bot { 0%{left:-3px;} 100%{left:2px;}}
        @keyframes header-glitch {
            0%{color:#ffed00;}
            50%{color:#ff00c8;}
            100%{color:#00ff41;}
        }
        @keyframes glitch-pulse {0%{filter:brightness(1);} 100%{filter:brightness(2.0) drop-shadow(0 0 36px #ff00c8);}}
        .arcade-icons {
            text-align: center;
            font-size: 64px;
            margin-bottom: 24px;
        }
        .arcade-icons span {
            display: inline-block;
            margin: 0 16px;
            animation: icon-bounce 1.4s infinite cubic-bezier(.36,.07,.19,.97);
        }
        .arcade-icons span:nth-child(2){animation-delay:0.15s;}
        .arcade-icons span:nth-child(3){animation-delay:0.30s;}
        .arcade-icons span:nth-child(4){animation-delay:0.45s;}
        .arcade-icons span:nth-child(5){animation-delay:0.60s;}
        .arcade-icons span:nth-child(6){animation-delay:0.75s;}
        @keyframes icon-bounce {
            0%,100%{transform:translateY(0);}
            45%{transform:translateY(-24px) scale(1.18);}
            60%{transform:translateY(-11px) scale(1.04);}
        }
        .arcade-coin {
            font-family: 'Press Start 2P', 'JetBrains Mono', monospace;
            text-align: center;
            margin: 48px 0 38px 0;
            font-size: 28px;
            color: #ffed00;
            text-shadow: 0 0 20px #ff00c8,0 0 2px #00ff41;
            overflow: hidden;
            white-space: nowrap;
            position: relative;
            animation: insertcoin-glow 1.2s infinite alternate;
            border: 2px solid #ff00c8;
            border-radius: 11px;
            background: rgba(0,0,0,0.19);
            box-shadow: 0 0 12px #ffed00, 0 0 17px #00ff41 inset;
            max-width: max-content;
            margin-left: auto; margin-right: auto;
            padding: 18px 38px;
        }
        #insert-coin {
            display: inline-block;
            animation: coin-marquee 5s linear infinite;
            position: relative;
        }
        @keyframes insertcoin-glow {
            0% { box-shadow: 0 0 12px #ffed00, 0 0 17px #00ff41 inset;}
            100% { box-shadow: 0 0 28px #ff00c8, 0 0 28px #00fff7 inset;}
        }
        @keyframes coin-marquee {
            0% { transform: translateX(100%); opacity:1;}
            50% { opacity: 0.84;}
            100% { transform: translateX(-100%); opacity:1;}
        }
        .arcade-highscore {
            font-family: 'Press Start 2P', 'JetBrains Mono', monospace;
            color: #fff;
            background: rgba(0,0,0,0.42);
            border: 4px dashed #ffed00;
            width: 370px;
            margin: 50px auto 16px auto;
            border-radius: 17px;
            font-size: 22px;
            text-align: left;
            padding: 21px 38px 12px 38px;
            box-shadow: 0 0 38px #00ff41b4, 0 0 20px #ff00c8 inset;
            letter-spacing:2px;
            animation: highscore-glow 2s infinite alternate;
        }
        @keyframes highscore-glow {
            0% { box-shadow: 0 0 18px #ff00c8b4, 0 0 20px #ffed0088 inset; border-color: #ffed00;}
            100% { box-shadow: 0 0 46px #00ff41cc, 0 0 30px #00ff4188 inset; border-color: #00ff41;}
        }
        .arcade-highscore strong {
            letter-spacing:3px;
            display:block;
            margin-bottom:8px;
            color:#ffed00;
            text-shadow:0 0 10px #ff00c8;
        }
        .arcade-highscore table {
            width: 100%;
            font-family: 'Press Start 2P', 'JetBrains Mono', monospace;
            color: #fff;
            border-collapse: separate;
            border-spacing: 0 10px;
            font-size: 1em;
        }
        .arcade-highscore td {
            padding: 0 3px;
            text-align: left;
            font-size:1em;
            vertical-align:middle;
        }
        .arcade-highscore td:last-child {
            text-align: right;
            letter-spacing: 5px;
            font-size:1.09em;
            color:#00ff41;
            text-shadow:0 0 11px #ffed00;
            animation: score-pulse 1.6s infinite alternate;
        }
        @keyframes score-pulse {
            0%{filter:brightness(1);}
            100%{filter:brightness(1.8) drop-shadow(0 0 6px #ffed00);}
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin: 60px 0 10px 0;
            opacity: 0.77;
            font-family: 'JetBrains Mono', monospace;
        }
        .music-credit {
            font-size:15px;
            color:#ffed00;
            text-shadow: 0 0 7px #00ff41,0 0 1px #ff00c8;
            margin-top:12px;
            margin-bottom: 16px;
        }
        .music-credit a {
            color: #00ff41;
            text-decoration: underline;
            transition: color .2s;
        }
        .music-credit a:hover {
            color: #ff00c8;
        }
        @media (max-width: 900px) {
            .arcade-header { font-size: 27px; margin:32px 2px 11px 2px;}
            .arcade-icons {font-size:19px;}
            .arcade-invaders {font-size:18px; margin-top:10px;}
            .arcade-coin {font-size: 13px;padding:7px 8px; margin:21px auto 13px auto;max-width:99vw;}
            .arcade-highscore {font-size:10px;width:147px;padding:7px 8px 5px 8px;}
            .footer {font-size: 10px;}
            .music-credit {font-size:10px;}
        }
    </style>
</head>
<body>
    <audio id="construction-audio" autoplay loop>
        <source src="lady-of-the-80x27s-128379.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <script>
      window.addEventListener('DOMContentLoaded', function() {
        const audio = document.getElementById('construction-audio');
        if (audio) {
          const playBtn = document.createElement('button');
          playBtn.innerText = "🔊 PRESS SPACE TO PLAY SOUND";
          playBtn.style = "position:fixed;bottom:20px;right:20px;padding:16px 28px;background:#151616dd;color:#ffed00;font-weight:bold;border:2px solid #00ff41;border-radius:12px;z-index:9999;cursor:pointer;box-shadow:0 0 15px #00ff4160;font-family:'Press Start 2P',monospace;font-size:20px;";
          playBtn.onclick = function() { audio.play(); playBtn.remove(); };
          setTimeout(function() {
            if (audio.paused) document.body.appendChild(playBtn);
          }, 700);
          // SPACE = Play
          document.addEventListener('keydown', function(e){
            if((e.code==="Space"||e.keyCode===32)&&audio.paused){audio.play(); playBtn.remove();}
          });
        }
      });
    </script>
    <div class="arcade-border"></div>
    <div class="arcade-invaders">
        <span>👾</span><span>👾</span><span>👾</span><span>👾</span><span>👾</span>
    </div>
    <div class="arcade-header glitch" data-text="👾 UNDER CONSTRUCTION 👾">
      <span>👾 UNDER CONSTRUCTION 👾</span>
    </div>
    <div class="arcade-icons">
      <span>🕹️</span> <span>💾</span> <span>🎮</span> <span>🪙</span> <span>🚧</span> <span>🎰</span>
    </div>
    <div class="arcade-coin">
      <span id="insert-coin">INSERT COIN TO CONTINUE...</span>
    </div>
    <div class="arcade-highscore">
      <strong>HIGH SCORE</strong>
      <table>
        <tr><td>NIL</td>    <td>888888</td></tr>
        <tr><td>PICCO</td>  <td>777777</td></tr>
        <tr><td>ANUBIS</td> <td>666666</td></tr>
      </table>
    </div>
    <div class="footer">
        &copy; 2025 nil underground collective // techno rituals & digital mischief
        <div class="music-credit">
            Music by <a href="https://pixabay.com/users/zenmann-25339457/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379" target="_blank" rel="noopener">ZenMan</a>
            from <a href="https://pixabay.com/music//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379" target="_blank" rel="noopener">Pixabay</a>
        </div>
    </div>
</body>
</html>
N • itshappening.today.html…]()

<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">“Oh, I heard there are actually people who don’t like rainbows? Solution: more rainbows—everywhere!” 🌈</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">l🟥o🟧v🟨e🟩i🟪s🟥l🟧o🟨v🟩e</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">I wish you all a wonderful and self-confident Pride Summer.</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">#BerlinerCSD #NeverSilentAgain</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">Ich wünsche euch allen einen wunderbaren und selbstbewussten Pride Summer.</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">#BerlinerCSD #NieWiederStill</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">l🟥o🟧v🟨e🟩i🟪s🟥l🟧o🟨v🟩e</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>




<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">“Oh, I heard there are actually people who don’t like rainbows? Solution: more rainbows—everywhere!” 🌈</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">l🟥o🟧v🟨e🟩i🟪s🟥l🟧o🟨v🟩e</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">I wish you all a wonderful and self-confident Pride Summer.</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">#BerlinerCSD #NeverSilentAgain</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">Ich wünsche euch allen einen wunderbaren und selbstbewussten Pride Summer.</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">#BerlinerCSD #NieWiederStill</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟦🟪</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">l🟥o🟧v🟨e🟩i🟪s🟥l🟧o🟨v🟩e</text>
</svg>
<svg width="100%" height="60" viewBox="0 0 400 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rainbow-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff0000;stop-opacity:1" />
      <stop offset="9.090909090909092%" style="stop-color:#ff8000;stop-opacity:1" />
      <stop offset="18.181818181818183%" style="stop-color:#ffff00;stop-opacity:1" />
      <stop offset="27.27272727272727%" style="stop-color:#80ff00;stop-opacity:1" />
      <stop offset="36.36363636363637%" style="stop-color:#00ff00;stop-opacity:1" />
      <stop offset="45.45454545454545%" style="stop-color:#00ff80;stop-opacity:1" />
      <stop offset="54.54545454545454%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="63.63636363636363%" style="stop-color:#0080ff;stop-opacity:1" />
      <stop offset="72.72727272727273%" style="stop-color:#0000ff;stop-opacity:1" />
      <stop offset="81.81818181818183%" style="stop-color:#8000ff;stop-opacity:1" />
      <stop offset="90.9090909090909%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff0080;stop-opacity:1" />
      <animateTransform attributeName="gradientTransform" attributeType="XML" type="translate" values="0,0;100,0;0,0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <text x="0" y="35" fill="url(#rainbow-gradient)" font-family="JetBrains Mono, monospace" font-size="24" font-weight="bold">🟥🟧🟨🟩🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨🟩🟦🟪🟥🟧🟨</text>
</svg>


