```aura width=860 height=200
<div style={{ position: 'relative', display: 'flex', flexDirection: 'row', alignItems: 'center', width: '100%', height: '100%', background: '#08080c', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', paddingLeft: 36, paddingRight: 36, columnGap: 28 }}>
  <style>{`
    @keyframes float-slow     { 0%,100%{ transform:translate(0,0);       opacity:0.60;} 50%{ transform:translate(20px,-16px); opacity:0.85;} }
    @keyframes float-medium   { 0%,100%{ transform:translate(0,0);       opacity:0.50;} 50%{ transform:translate(-16px,12px); opacity:0.75;} }
    @keyframes float-fast     { 0%,100%{ transform:translate(0,0);       opacity:0.40;} 50%{ transform:translate(12px,-20px);  opacity:0.65;} }
    @keyframes float-diagonal { 0%,100%{ transform:translate(0,0);       opacity:0.35;} 50%{ transform:translate(-20px,-16px);opacity:0.60;} }
    #pg-o1{ animation: float-slow       9s ease-in-out infinite;       }
    #pg-o2{ animation: float-medium    11s ease-in-out infinite  0.8s; }
    #pg-o3{ animation: float-fast       8s ease-in-out infinite  2.0s; }
    #pg-o4{ animation: float-diagonal  10s ease-in-out infinite  1.5s; }
    #pg-o5{ animation: float-slow      12s ease-in-out infinite  3.0s; }
    #pg-o6{ animation: float-medium     9s ease-in-out infinite  0.5s; }
    #pg-o7{ animation: float-fast      11s ease-in-out infinite  4.0s; }
    #pg-o8{ animation: float-diagonal   8s ease-in-out infinite  2.5s; }
  `}</style>
  <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="pg-g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,60,220,0.55)"/><stop offset="100%" stopColor="rgba(110,60,220,0)"/></radialGradient>
      <radialGradient id="pg-g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,100,220,0.50)"/><stop offset="100%" stopColor="rgba(60,100,220,0)"/></radialGradient>
      <radialGradient id="pg-g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(180,80,255,0.40)"/><stop offset="100%" stopColor="rgba(180,80,255,0)"/></radialGradient>
      <radialGradient id="pg-g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(80,160,255,0.35)"/><stop offset="100%" stopColor="rgba(80,160,255,0)"/></radialGradient>
      <radialGradient id="pg-g5" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(40,200,180,0.30)"/><stop offset="100%" stopColor="rgba(40,200,180,0)"/></radialGradient>
      <radialGradient id="pg-g6" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(150,50,200,0.40)"/><stop offset="100%" stopColor="rgba(150,50,200,0)"/></radialGradient>
      <radialGradient id="pg-g7" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,80,200,0.35)"/><stop offset="100%" stopColor="rgba(60,80,200,0)"/></radialGradient>
      <radialGradient id="pg-g8" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(200,100,255,0.30)"/><stop offset="100%" stopColor="rgba(200,100,255,0)"/></radialGradient>
    </defs>
    <ellipse id="pg-o1" cx="100" cy="180" rx="220" ry="170" fill="url(#pg-g1)" />
    <ellipse id="pg-o2" cx="800" cy="40"  rx="200" ry="160" fill="url(#pg-g2)" />
    <ellipse id="pg-o3" cx="680" cy="190" rx="180" ry="140" fill="url(#pg-g3)" />
    <ellipse id="pg-o4" cx="220" cy="30"  rx="170" ry="130" fill="url(#pg-g4)" />
    <ellipse id="pg-o5" cx="430" cy="200" rx="160" ry="120" fill="url(#pg-g5)" />
    <ellipse id="pg-o6" cx="560" cy="20"  rx="150" ry="110" fill="url(#pg-g6)" />
    <ellipse id="pg-o7" cx="350" cy="10"  rx="140" ry="100" fill="url(#pg-g7)" />
    <ellipse id="pg-o8" cx="750" cy="180" rx="130" ry="100" fill="url(#pg-g8)" />
    <circle cx="430" cy="100" r="60" fill="none" stroke="rgba(110,80,220,0.12)" strokeWidth="1" />
    <circle cx="430" cy="100" r="90" fill="none" stroke="rgba(110,80,220,0.08)" strokeWidth="1" />
  </svg>

  <div style={{ display: 'flex', flexShrink: 0, position: 'relative' }}>
    <div style={{ width: 90, height: 90, borderRadius: '50%', background: 'linear-gradient(135deg, rgba(110,60,220,0.9), rgba(60,100,220,0.9))', padding: 2.5, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <img src={(github && github.user && github.user.avatar_url) || 'https://github.com/Adityax-07.png'} width={85} height={85} style={{ borderRadius: '50%', objectFit: 'cover' }} />
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', flex: 1, position: 'relative' }}>
    <span style={{ fontSize: 34, fontWeight: 700, color: '#ffffff', letterSpacing: -1, lineHeight: 1 }}>
      {(github && github.user && (github.user.name || github.user.login)) || 'Aditya Bisht'}
    </span>
    <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.50)', marginTop: 8, lineHeight: 1.4 }}>
      AI/ML Engineer | RAG Systems, LLM Fine-tuning &amp; Agentic AI
    </span>
    <div style={{ display: 'flex', flexDirection: 'row', columnGap: 8, marginTop: 16, flexWrap: 'wrap' }}>
      {['Python', 'LangChain', 'LangGraph', 'PyTorch'].map((tag, i) => (
        <span key={i} style={{ paddingTop: 4, paddingBottom: 4, paddingLeft: 14, paddingRight: 14, background: 'rgba(110,80,220,0.12)', color: 'rgba(180,160,255,0.85)', borderRadius: 100, fontSize: 11, border: '1px solid rgba(110,80,220,0.28)', letterSpacing: 0.5 }}>{tag}</span>
      ))}
    </div>
  </div>
</div>
```

```aura width=860 height=140
<div style={{ position: 'relative', display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'space-around', width: '100%', height: '100%', background: '#08080c', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif' }}>
  <style>{`
    @keyframes float-slow   { 0%,100%{ transform:translate(0,0);    opacity:0.50;} 50%{ transform:translate(16px,-12px); opacity:0.75;} }
    @keyframes float-medium { 0%,100%{ transform:translate(0,0);    opacity:0.40;} 50%{ transform:translate(-12px,10px);opacity:0.65;} }
    #st-o1{ animation: float-slow   10s ease-in-out infinite;      }
    #st-o2{ animation: float-medium 12s ease-in-out infinite 1.0s; }
    #st-o3{ animation: float-slow    9s ease-in-out infinite 2.0s; }
    #st-o4{ animation: float-medium 11s ease-in-out infinite 0.5s; }
  `}</style>
  <svg width="860" height="140" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="st-g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,60,220,0.45)"/><stop offset="100%" stopColor="rgba(110,60,220,0)"/></radialGradient>
      <radialGradient id="st-g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,100,220,0.40)"/><stop offset="100%" stopColor="rgba(60,100,220,0)"/></radialGradient>
      <radialGradient id="st-g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(180,80,255,0.35)"/><stop offset="100%" stopColor="rgba(180,80,255,0)"/></radialGradient>
      <radialGradient id="st-g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(80,160,255,0.30)"/><stop offset="100%" stopColor="rgba(80,160,255,0)"/></radialGradient>
    </defs>
    <ellipse id="st-o1" cx="80"  cy="120" rx="180" ry="130" fill="url(#st-g1)" />
    <ellipse id="st-o2" cx="780" cy="30"  rx="170" ry="120" fill="url(#st-g2)" />
    <ellipse id="st-o3" cx="430" cy="140" rx="160" ry="110" fill="url(#st-g3)" />
    <ellipse id="st-o4" cx="430" cy="0"   rx="150" ry="100" fill="url(#st-g4)" />
    <line x1="286" y1="28" x2="286" y2="112" stroke="rgba(110,80,220,0.18)" strokeWidth="1" />
    <line x1="573" y1="28" x2="573" y2="112" stroke="rgba(110,80,220,0.18)" strokeWidth="1" />
  </svg>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6 }}>
    <span style={{ fontSize: 40, fontWeight: 700, color: 'rgba(160,120,255,1)', letterSpacing: -1 }}>
      {(github && github.user && github.user.public_repos) || '28'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>repos</span>
  </div>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6 }}>
    <span style={{ fontSize: 40, fontWeight: 700, color: 'rgba(100,170,255,1)', letterSpacing: -1 }}>
      {(github && github.stars) || '0'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>stars</span>
  </div>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', rowGap: 6 }}>
    <span style={{ fontSize: 40, fontWeight: 700, color: 'rgba(255,200,80,1)', letterSpacing: -1 }}>
      {(github && github.commits) || '200+'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.35)', letterSpacing: 3, textTransform: 'uppercase' }}>commits</span>
  </div>
</div>
```

```aura width=860 height=168
<div style={{ position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'center', width: '100%', height: '100%', background: '#08080c', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', paddingLeft: 36, paddingRight: 36, rowGap: 20 }}>
  <style>{`
    @keyframes float-slow   { 0%,100%{ transform:translate(0,0);    opacity:0.45;} 50%{ transform:translate(18px,-14px); opacity:0.70;} }
    @keyframes float-medium { 0%,100%{ transform:translate(0,0);    opacity:0.38;} 50%{ transform:translate(-14px,10px);opacity:0.62;} }
    #tk-o1{ animation: float-slow   11s ease-in-out infinite;      }
    #tk-o2{ animation: float-medium 13s ease-in-out infinite 1.0s; }
    #tk-o3{ animation: float-slow   10s ease-in-out infinite 2.5s; }
    #tk-o4{ animation: float-medium 12s ease-in-out infinite 0.5s; }
  `}</style>
  <svg width="860" height="168" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="tk-g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,60,220,0.40)"/><stop offset="100%" stopColor="rgba(110,60,220,0)"/></radialGradient>
      <radialGradient id="tk-g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,100,220,0.35)"/><stop offset="100%" stopColor="rgba(60,100,220,0)"/></radialGradient>
      <radialGradient id="tk-g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(180,80,255,0.30)"/><stop offset="100%" stopColor="rgba(180,80,255,0)"/></radialGradient>
      <radialGradient id="tk-g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(80,160,255,0.28)"/><stop offset="100%" stopColor="rgba(80,160,255,0)"/></radialGradient>
    </defs>
    <ellipse id="tk-o1" cx="80"  cy="140" rx="200" ry="140" fill="url(#tk-g1)" />
    <ellipse id="tk-o2" cx="800" cy="40"  rx="180" ry="130" fill="url(#tk-g2)" />
    <ellipse id="tk-o3" cx="520" cy="168" rx="160" ry="120" fill="url(#tk-g3)" />
    <ellipse id="tk-o4" cx="340" cy="0"   rx="150" ry="110" fill="url(#tk-g4)" />
  </svg>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'row', alignItems: 'center', columnGap: 14 }}>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.30)', letterSpacing: 3, textTransform: 'uppercase', width: 90, flexShrink: 0 }}>languages</span>
    <div style={{ display: 'flex', flexDirection: 'row', columnGap: 8, flexWrap: 'wrap' }}>
      {['Python', 'JavaScript', 'TypeScript', 'C++', 'Java'].map((lang, i) => (
        <span key={i} style={{ paddingTop: 5, paddingBottom: 5, paddingLeft: 16, paddingRight: 16, background: 'rgba(110,80,220,0.10)', color: 'rgba(180,160,255,0.80)', borderRadius: 100, fontSize: 12, border: '1px solid rgba(110,80,220,0.22)', letterSpacing: 0.3 }}>{lang}</span>
      ))}
    </div>
  </div>

  <div style={{ position: 'relative', display: 'flex', flexDirection: 'row', alignItems: 'center', columnGap: 14 }}>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.30)', letterSpacing: 3, textTransform: 'uppercase', width: 90, flexShrink: 0 }}>frameworks</span>
    <div style={{ display: 'flex', flexDirection: 'row', columnGap: 8, flexWrap: 'wrap' }}>
      {['LangChain', 'LangGraph', 'FastAPI', 'PyTorch', 'React'].map((fw, i) => (
        <span key={i} style={{ paddingTop: 5, paddingBottom: 5, paddingLeft: 16, paddingRight: 16, background: 'rgba(60,100,220,0.10)', color: 'rgba(130,170,255,0.80)', borderRadius: 100, fontSize: 12, border: '1px solid rgba(60,100,220,0.22)', letterSpacing: 0.3 }}>{fw}</span>
      ))}
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
