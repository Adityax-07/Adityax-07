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

```aura width=860 height=140
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', alignItems: 'center', justifyContent: 'space-around',
  fontFamily: 'Inter', position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)'
}}>
  <style>{`
    @keyframes float-slow   { 0%,100%{ transform:translateX(0px); opacity:0.7; } 50%{ transform:translateX(200px); opacity:1.0; } }
    @keyframes float-medium { 0%,100%{ transform:translateX(0px); opacity:0.6; } 50%{ transform:translateX(-180px); opacity:0.9; } }
    #st-g1 { animation: float-slow   10s ease-in-out infinite; }
    #st-g2 { animation: float-medium 13s ease-in-out infinite; }
    #st-g3 { animation: float-slow    9s ease-in-out infinite reverse; }
    #st-g4 { animation: float-medium 11s ease-in-out infinite reverse; }
  `}</style>
  <svg width="860" height="140" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="st-g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,20,210,0.55)"/><stop offset="70%" stopColor="rgba(110,20,210,0)"/></radialGradient>
      <radialGradient id="st-g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(40,60,255,0.50)"/><stop offset="70%" stopColor="rgba(40,60,255,0)"/></radialGradient>
      <radialGradient id="st-g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(160,30,255,0.45)"/><stop offset="70%" stopColor="rgba(160,30,255,0)"/></radialGradient>
      <radialGradient id="st-g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(0,130,255,0.40)"/><stop offset="70%" stopColor="rgba(0,130,255,0)"/></radialGradient>
    </defs>
    <ellipse id="st-g1" cx="80"  cy="120" rx="200" ry="140" fill="url(#st-g1)" />
    <ellipse id="st-g2" cx="780" cy="30"  rx="180" ry="130" fill="url(#st-g2)" />
    <ellipse id="st-g3" cx="430" cy="140" rx="170" ry="120" fill="url(#st-g3)" />
    <ellipse id="st-g4" cx="430" cy="0"   rx="160" ry="110" fill="url(#st-g4)" />
    <line x1="286" y1="28" x2="286" y2="112" stroke="rgba(110,80,220,0.22)" strokeWidth="1" />
    <line x1="573" y1="28" x2="573" y2="112" stroke="rgba(110,80,220,0.22)" strokeWidth="1" />
  </svg>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6, position: 'relative' }}>
    <div style={{ display: 'flex', fontSize: 40, fontWeight: 800, color: 'rgba(170,130,255,1)', letterSpacing: -1 }}>
      {(github && github.stats && github.stats.repos) || github.user.publicRepos || '28'}
    </div>
    <div style={{ display: 'flex', fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>repos</div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6, position: 'relative' }}>
    <div style={{ display: 'flex', fontSize: 40, fontWeight: 800, color: 'rgba(80,160,255,1)', letterSpacing: -1 }}>
      {(github && github.stats && github.stats.stars) || '0'}
    </div>
    <div style={{ display: 'flex', fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>stars</div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6, position: 'relative' }}>
    <div style={{ display: 'flex', fontSize: 40, fontWeight: 800, color: 'rgba(255,200,80,1)', letterSpacing: -1 }}>
      {(github && github.stats && github.stats.commits) || '0'}
    </div>
    <div style={{ display: 'flex', fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>commits</div>
  </div>
</div>
```

```aura width=860 height=168
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', flexDirection: 'column', justifyContent: 'center',
  fontFamily: 'Inter', position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)', paddingLeft: 36, paddingRight: 36, rowGap: 20
}}>
  <style>{`
    @keyframes float-slow   { 0%,100%{ transform:translateX(0px); opacity:0.6; } 50%{ transform:translateX(250px); opacity:0.9; } }
    @keyframes float-medium { 0%,100%{ transform:translateX(0px); opacity:0.5; } 50%{ transform:translateX(-200px); opacity:0.8; } }
    #tk-g1 { animation: float-slow   11s ease-in-out infinite; }
    #tk-g2 { animation: float-medium 13s ease-in-out infinite; }
    #tk-g3 { animation: float-slow   10s ease-in-out infinite reverse; }
    #tk-g4 { animation: float-medium 12s ease-in-out infinite reverse; }
  `}</style>
  <svg width="860" height="168" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="tk-g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,20,210,0.45)"/><stop offset="70%" stopColor="rgba(110,20,210,0)"/></radialGradient>
      <radialGradient id="tk-g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(40,60,255,0.40)"/><stop offset="70%" stopColor="rgba(40,60,255,0)"/></radialGradient>
      <radialGradient id="tk-g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(160,30,255,0.38)"/><stop offset="70%" stopColor="rgba(160,30,255,0)"/></radialGradient>
      <radialGradient id="tk-g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(0,130,255,0.35)"/><stop offset="70%" stopColor="rgba(0,130,255,0)"/></radialGradient>
    </defs>
    <ellipse id="tk-g1" cx="80"  cy="140" rx="210" ry="150" fill="url(#tk-g1)" />
    <ellipse id="tk-g2" cx="800" cy="40"  rx="190" ry="140" fill="url(#tk-g2)" />
    <ellipse id="tk-g3" cx="520" cy="168" rx="170" ry="130" fill="url(#tk-g3)" />
    <ellipse id="tk-g4" cx="340" cy="0"   rx="160" ry="120" fill="url(#tk-g4)" />
  </svg>

  <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', columnGap: 14, position: 'relative' }}>
    <div style={{ display: 'flex', fontSize: 10, color: 'rgba(255,255,255,0.30)', letterSpacing: 3, textTransform: 'uppercase', width: 90, flexShrink: 0 }}>languages</div>
    <div style={{ display: 'flex', flexDirection: 'row', columnGap: 8, flexWrap: 'wrap' }}>
      {['Python', 'JavaScript', 'TypeScript', 'C++', 'Java'].map(function(lang) {
        return (
          <div key={lang} style={{
            display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 16, paddingRight: 16,
            background: 'rgba(80,40,220,0.14)', color: 'rgba(185,170,255,0.85)',
            borderRadius: 100, fontSize: 12, border: '1px solid rgba(100,70,240,0.25)', letterSpacing: 0.3
          }}>{lang}</div>
        );
      })}
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', columnGap: 14, position: 'relative' }}>
    <div style={{ display: 'flex', fontSize: 10, color: 'rgba(255,255,255,0.30)', letterSpacing: 3, textTransform: 'uppercase', width: 90, flexShrink: 0 }}>frameworks</div>
    <div style={{ display: 'flex', flexDirection: 'row', columnGap: 8, flexWrap: 'wrap' }}>
      {['LangChain', 'LangGraph', 'FastAPI', 'PyTorch', 'React'].map(function(fw) {
        return (
          <div key={fw} style={{
            display: 'flex', paddingTop: 5, paddingBottom: 5, paddingLeft: 16, paddingRight: 16,
            background: 'rgba(20,60,220,0.14)', color: 'rgba(140,180,255,0.85)',
            borderRadius: 100, fontSize: 12, border: '1px solid rgba(40,80,240,0.25)', letterSpacing: 0.3
          }}>{fw}</div>
        );
      })}
    </div>
  </div>
</div>
```

```aura width=168 height=44 link="https://linkedin.com/in/aditya-bisht" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/linkedin/0A66C2"
  text="LinkedIn"
  backgroundColor="#060f1a"
  width={168}
  height={44}
  gradientStops={[
    { offset: '0%',   color: '#ffffff' },
    { offset: '10%',  color: '#0a1929' },
    { offset: '50%',  color: '#eeeeee' },
    { offset: '60%',  color: '#0A66C2' },
    { offset: '80%',  color: '#0a1929' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

```aura width=140 height=44 link="https://github.com/Adityax-07" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/github/ffffff"
  text="GitHub"
  backgroundColor="#141414"
  width={140}
  height={44}
  gradientStops={[
    { offset: '0%',   color: '#ffffff' },
    { offset: '10%',  color: '#111111' },
    { offset: '50%',  color: '#eeeeee' },
    { offset: '60%',  color: '#ffffff' },
    { offset: '80%',  color: '#111111' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

```aura width=120 height=44 link="mailto:aaditya85677@gmail.com" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/gmail/EA4335"
  text="Email"
  backgroundColor="#1a0606"
  width={120}
  height={44}
  gradientStops={[
    { offset: '0%',   color: '#ffffff' },
    { offset: '10%',  color: '#1a0606' },
    { offset: '50%',  color: '#eeeeee' },
    { offset: '60%',  color: '#EA4335' },
    { offset: '80%',  color: '#1a0606' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

```aura width=148 height=44 link="https://leetcode.com/u/Adityax-07/" inline align=center
<SocialMediaButton
  icon="https://cdn.simpleicons.org/leetcode/FFA116"
  text="LeetCode"
  backgroundColor="#141000"
  width={148}
  height={44}
  gradientStops={[
    { offset: '0%',   color: '#ffffff' },
    { offset: '10%',  color: '#141000' },
    { offset: '50%',  color: '#eeeeee' },
    { offset: '60%',  color: '#FFA116' },
    { offset: '80%',  color: '#141000' },
    { offset: '100%', color: '#555555' },
  ]}
/>
```

---

## 🚀 Featured Projects

| Project | Description | Stack | Link |
|---------|-------------|-------|------|
| **RAG Systems Eval Suite** | Benchmarked 7 RAG strategies across 3,500 pairs. Advanced RAG achieved 0.881 faithfulness. Dual-provider LLM-as-judge with checkpoint/resume. | Python · FAISS · LangChain · Groq · Streamlit | [GitHub](https://github.com/Adityax-07) |
| **CodeSage** | Fine-tuned Qwen2.5-1.5B with LoRA to 85.3% accuracy at $0.0002/query — outperforming RAG and baseline LLM across all quality metrics. | Python · HuggingFace PEFT · LoRA · Groq · Streamlit | [GitHub](https://github.com/Adityax-07) |
| **Autonomous MLOps Agent** | UPI fraud detection agent using LangGraph + XGBoost. Reduced incident response from days to <60 seconds. ROC-AUC 0.99 post-retrain. | FastAPI · XGBoost · LangGraph · Evidently AI · MLflow · Docker | [GitHub](https://github.com/Adityax-07) |

---

## 🏆 Highlights

- Benchmarked **7 RAG strategies** across **3,500 evaluation pairs** — Advanced RAG at 0.881 faithfulness
- Fine-tuned **Qwen2.5-1.5B** → **85.3% accuracy** at **$0.0002/query** using LoRA
- MLOps agent reducing incident response from **days → <60 seconds**, zero human intervention
- **Oracle Generative AI Professional** & **Oracle AI Vector Search Professional** certified
- B.Tech IT, MAIT GGSIPU — CGPA **8.0**

---

## 🐍 Contribution Graph

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Adityax-07/Adityax-07/output/github-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Adityax-07/Adityax-07/output/github-snake.svg"/>
    <img alt="github contribution snake" src="https://raw.githubusercontent.com/Adityax-07/Adityax-07/output/github-snake.svg"/>
  </picture>
</div>

---

<div align="center">
  <sub>powered by <a href="https://github.com/collectioneur/readme-aura">readme-aura</a></sub>
</div>
