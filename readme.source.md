```aura width=860 height=200
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', alignItems: 'center', fontFamily: 'Inter',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)'
}}>
  <style>{`
    @keyframes float-slow {
      0%, 100% { transform: translateX(0px); opacity: 0.8; }
      50% { transform: translateX(350px); opacity: 1.2; }
    }
    @keyframes float-medium {
      0%, 100% { transform: translateX(0px); opacity: 0.7; }
      50% { transform: translateX(-250px); opacity: 1.1; }
    }
    @keyframes float-fast {
      0%, 100% { transform: translateX(0px); opacity: 0.9; }
      50% { transform: translateX(200px); opacity: 0.6; }
    }
    @keyframes float-diagonal {
      0%, 100% { transform: translateX(0px); opacity: 0.75; }
      50% { transform: translateX(300px); opacity: 1.0; }
    }
    @keyframes float-wave {
      0%, 100% { transform: translateX(0px); opacity: 0.65; }
      33% { transform: translateX(-160px); opacity: 0.9; }
      66% { transform: translateX(80px); opacity: 1.0; }
    }
    @keyframes float-pulse {
      0%, 100% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.3); opacity: 0.4; }
    }
    #glow-1 { animation: float-slow 8s ease-in-out infinite; }
    #glow-2 { animation: float-medium 12s ease-in-out infinite; }
    #glow-3 { animation: float-fast 9s ease-in-out infinite; }
    #glow-4 { animation: float-slow 11s ease-in-out infinite reverse; }
    #glow-5 { animation: float-medium 14s ease-in-out infinite reverse; }
    #glow-6 { animation: float-diagonal 10s ease-in-out infinite; }
    #glow-7 { animation: float-wave 13s ease-in-out infinite; }
    #glow-8 { animation: float-pulse 7s ease-in-out infinite; }
  `}</style>

  <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.72)" />
        <stop offset="40%" stopColor="rgba(90,15,180,0.35)" />
        <stop offset="70%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
      <radialGradient id="g2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,60,255,0.6)" />
        <stop offset="45%" stopColor="rgba(30,50,200,0.25)" />
        <stop offset="70%" stopColor="rgba(30,50,200,0)" />
      </radialGradient>
      <radialGradient id="g3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,130,255,0.45)" />
        <stop offset="50%" stopColor="rgba(0,100,220,0.18)" />
        <stop offset="70%" stopColor="rgba(0,100,220,0)" />
      </radialGradient>
      <radialGradient id="g4" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,190,230,0.32)" />
        <stop offset="70%" stopColor="rgba(0,190,230,0)" />
      </radialGradient>
      <radialGradient id="g5" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(90,30,200,0.38)" />
        <stop offset="70%" stopColor="rgba(90,30,200,0)" />
      </radialGradient>
      <radialGradient id="g6" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(160,30,255,0.55)" />
        <stop offset="45%" stopColor="rgba(130,20,220,0.22)" />
        <stop offset="70%" stopColor="rgba(130,20,220,0)" />
      </radialGradient>
      <radialGradient id="g7" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(20,60,255,0.42)" />
        <stop offset="50%" stopColor="rgba(10,40,200,0.16)" />
        <stop offset="70%" stopColor="rgba(10,40,200,0)" />
      </radialGradient>
      <radialGradient id="g8" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,170,255,0.40)" />
        <stop offset="50%" stopColor="rgba(0,130,220,0.15)" />
        <stop offset="70%" stopColor="rgba(0,130,220,0)" />
      </radialGradient>
    </defs>
    <ellipse id="glow-1" cx="180" cy="230" rx="260" ry="190" fill="url(#g1)" />
    <ellipse id="glow-2" cx="300" cy="240" rx="220" ry="160" fill="url(#g2)" />
    <ellipse id="glow-3" cx="420" cy="240" rx="180" ry="140" fill="url(#g3)" />
    <ellipse id="glow-4" cx="550" cy="250" rx="150" ry="120" fill="url(#g4)" />
    <ellipse id="glow-5" cx="750" cy="250" rx="130" ry="110" fill="url(#g5)" />
    <ellipse id="glow-6" cx="300" cy="240" rx="180" ry="140" fill="url(#g6)" />
    <ellipse id="glow-7" cx="490" cy="230" rx="220" ry="170" fill="url(#g7)" />
    <ellipse id="glow-8" cx="590" cy="250" rx="150" ry="130" fill="url(#g8)" />
  </svg>

  <div style={{
    position: 'absolute', left: 48, top: 52, width: 96, height: 96,
    borderRadius: 48, background: 'linear-gradient(135deg, #6622ee, #0088ff)',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
  }}>
    <img src={github.user.avatarUrl || 'https://github.com/Adityax-07.png'} width={88} height={88} style={{ borderRadius: 44 }} />
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', marginLeft: 168, gap: 8 }}>
    <div style={{ display: 'flex', fontSize: 38, fontWeight: 800, color: '#ffffff', letterSpacing: '-1px', lineHeight: 1 }}>
      {github.user.name || github.user.login || 'Aditya Bisht'}
    </div>
    <div style={{ display: 'flex', fontSize: 15, color: 'rgba(180,165,255,0.8)', fontWeight: 400, letterSpacing: '0.3px' }}>
      {github.user.bio || 'AI & ML Engineer · RAG Systems · LLM Fine-tuning · Agentic AI'}
    </div>
    <div style={{ display: 'flex', gap: 8, marginTop: 6 }}>
      {['Python', 'LangChain', 'LangGraph', 'PyTorch'].map(function(tag) {
        return (
          <div key={tag} style={{
            display: 'flex', paddingTop: 4, paddingBottom: 4, paddingLeft: 12, paddingRight: 12, borderRadius: 20,
            background: 'rgba(80,40,220,0.18)', border: '1px solid rgba(100,70,240,0.32)',
            color: 'rgba(205,195,255,0.85)', fontSize: 12, fontWeight: 600,
          }}>{tag}</div>
        );
      })}
    </div>
  </div>
</div>
```

```aura width=860 height=130
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', alignItems: 'center', justifyContent: 'space-around',
  fontFamily: 'Inter', position: 'relative', overflow: 'hidden',
  borderRadius: 16, border: '1px solid rgba(110,80,220,0.18)'
}}>
  <style>{`
    @keyframes sdrift { 0%,100%{transform:translateX(0px);opacity:0.5;} 50%{transform:translateX(-180px);opacity:0.85;} }
    @keyframes spulse { 0%,100%{transform:scale(1);opacity:0.55;} 50%{transform:scale(1.4);opacity:0.9;} }
    #se1{animation:sdrift 14s ease-in-out infinite;}
    #se2{animation:spulse 10s ease-in-out infinite;}
    #se3{animation:sdrift 12s ease-in-out infinite reverse;}
  `}</style>

  <svg width="860" height="130" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="grad-s1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,60,255,0.55)" />
        <stop offset="50%" stopColor="rgba(30,50,200,0.20)" />
        <stop offset="100%" stopColor="rgba(30,50,200,0)" />
      </radialGradient>
      <radialGradient id="grad-s2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,130,255,0.38)" />
        <stop offset="60%" stopColor="rgba(0,100,220,0.12)" />
        <stop offset="100%" stopColor="rgba(0,100,220,0)" />
      </radialGradient>
      <radialGradient id="grad-s3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.35)" />
        <stop offset="60%" stopColor="rgba(90,15,180,0.10)" />
        <stop offset="100%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
    </defs>
    <ellipse id="se1" cx="430" cy="160" rx="320" ry="120" fill="url(#grad-s1)" />
    <ellipse id="se2" cx="430" cy="150" rx="200" ry="100" fill="url(#grad-s2)" />
    <ellipse id="se3" cx="200" cy="160" rx="180" ry="100" fill="url(#grad-s3)" />
    <line x1="287" y1="28" x2="287" y2="102" stroke="rgba(110,80,220,0.22)" strokeWidth="1" />
    <line x1="573" y1="28" x2="573" y2="102" stroke="rgba(110,80,220,0.22)" strokeWidth="1" />
  </svg>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
    <div style={{ display: 'flex', fontSize: 42, fontWeight: 800, color: 'rgba(170,150,255,0.95)', letterSpacing: '-1px', lineHeight: 1 }}>
      {String(github.user.publicRepos || '28')}
    </div>
    <div style={{ display: 'flex', fontSize: 11, fontWeight: 600, color: 'rgba(140,130,170,0.7)', letterSpacing: '2px' }}>
      REPOS
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
    <div style={{ display: 'flex', fontSize: 42, fontWeight: 800, color: 'rgba(80,140,255,0.95)', letterSpacing: '-1px', lineHeight: 1 }}>
      {String(github.stars || github.stats && github.stats.stars || '0')}
    </div>
    <div style={{ display: 'flex', fontSize: 11, fontWeight: 600, color: 'rgba(140,130,170,0.7)', letterSpacing: '2px' }}>
      STARS
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
    <div style={{ display: 'flex', fontSize: 42, fontWeight: 800, color: 'rgba(255,180,60,0.95)', letterSpacing: '-1px', lineHeight: 1 }}>
      {String(github.commits || github.contributions || github.stats && github.stats.commits || '500+')}
    </div>
    <div style={{ display: 'flex', fontSize: 11, fontWeight: 600, color: 'rgba(140,130,170,0.7)', letterSpacing: '2px' }}>
      COMMITS
    </div>
  </div>
</div>
```


```aura width=860 height=200
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', flexDirection: 'column', justifyContent: 'center',
  fontFamily: 'Inter', position: 'relative', overflow: 'hidden',
  borderRadius: 16, border: '1px solid rgba(110,80,220,0.18)',
  paddingLeft: 48, paddingRight: 48
}}>
  <style>{`
    @keyframes tdrift { 0%,100%{transform:translateX(0px);opacity:0.45;} 50%{transform:translateX(220px);opacity:0.75;} }
    @keyframes tpulse { 0%,100%{transform:scale(1);opacity:0.5;} 50%{transform:scale(1.35);opacity:0.8;} }
    #te1{animation:tdrift 16s ease-in-out infinite;}
    #te2{animation:tpulse 11s ease-in-out infinite;}
    #te3{animation:tdrift 13s ease-in-out infinite reverse;}
  `}</style>

  <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="grad-t1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.5)" />
        <stop offset="50%" stopColor="rgba(90,15,180,0.18)" />
        <stop offset="100%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
      <radialGradient id="grad-t2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,60,255,0.45)" />
        <stop offset="50%" stopColor="rgba(30,50,200,0.15)" />
        <stop offset="100%" stopColor="rgba(30,50,200,0)" />
      </radialGradient>
      <radialGradient id="grad-t3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,130,255,0.32)" />
        <stop offset="60%" stopColor="rgba(0,100,220,0.10)" />
        <stop offset="100%" stopColor="rgba(0,100,220,0)" />
      </radialGradient>
    </defs>
    <ellipse id="te1" cx="100" cy="220" rx="280" ry="160" fill="url(#grad-t1)" />
    <ellipse id="te2" cx="600" cy="210" rx="300" ry="160" fill="url(#grad-t2)" />
    <ellipse id="te3" cx="860" cy="220" rx="200" ry="140" fill="url(#grad-t3)" />
  </svg>

  <div style={{ display: 'flex', fontSize: 11, fontWeight: 700, color: 'rgba(140,130,170,0.6)', letterSpacing: '2.5px', marginBottom: 16 }}>
    TECH STACK
  </div>

  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginBottom: 10 }}>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(255,212,59,0.10)', border: '1px solid rgba(255,212,59,0.30)', color: 'rgba(255,220,80,0.90)', fontSize: 13, fontWeight: 600 }}>Python</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(238,76,44,0.10)', border: '1px solid rgba(238,76,44,0.30)', color: 'rgba(255,110,80,0.90)', fontSize: 13, fontWeight: 600 }}>PyTorch</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(255,111,0,0.10)', border: '1px solid rgba(255,111,0,0.30)', color: 'rgba(255,150,60,0.90)', fontSize: 13, fontWeight: 600 }}>TensorFlow</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(255,210,30,0.10)', border: '1px solid rgba(255,210,30,0.28)', color: 'rgba(255,220,70,0.88)', fontSize: 13, fontWeight: 600 }}>Hugging Face</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(247,147,30,0.10)', border: '1px solid rgba(247,147,30,0.28)', color: 'rgba(255,170,70,0.88)', fontSize: 13, fontWeight: 600 }}>scikit-learn</div>
  </div>

  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(28,198,180,0.10)', border: '1px solid rgba(28,198,180,0.28)', color: 'rgba(60,220,200,0.88)', fontSize: 13, fontWeight: 600 }}>LangChain</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(40,180,100,0.10)', border: '1px solid rgba(40,180,100,0.28)', color: 'rgba(70,210,130,0.88)', fontSize: 13, fontWeight: 600 }}>LangGraph</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(0,150,136,0.10)', border: '1px solid rgba(0,150,136,0.28)', color: 'rgba(0,200,180,0.88)', fontSize: 13, fontWeight: 600 }}>FastAPI</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(255,75,75,0.10)', border: '1px solid rgba(255,75,75,0.28)', color: 'rgba(255,110,110,0.88)', fontSize: 13, fontWeight: 600 }}>Streamlit</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(36,150,237,0.10)', border: '1px solid rgba(36,150,237,0.28)', color: 'rgba(80,180,255,0.88)', fontSize: 13, fontWeight: 600 }}>Docker</div>
    <div style={{ display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 14, paddingRight: 14, borderRadius: 8, background: 'rgba(240,80,50,0.10)', border: '1px solid rgba(240,80,50,0.28)', color: 'rgba(255,120,90,0.88)', fontSize: 13, fontWeight: 600 }}>Git</div>
  </div>
</div>
```