```aura width=800 height=210
<div style={{ position: 'relative', display: 'flex', alignItems: 'center', width: '100%', height: '100%', background: '#0d0e1a', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', padding: '0 32px' }}>
  <style>{`
    @keyframes h-orb-a { 0%, 100% { transform: translate(0,0); opacity: 0.55; } 50% { transform: translate(22px,-18px); opacity: 0.85; } }
    @keyframes h-orb-b { 0%, 100% { transform: translate(0,0); opacity: 0.45; } 50% { transform: translate(-18px,14px); opacity: 0.75; } }
    #h-o1 { animation: h-orb-a 9s ease-in-out infinite; }
    #h-o2 { animation: h-orb-b 11s ease-in-out infinite 1s; }
    #h-o3 { animation: h-orb-a 8s ease-in-out infinite 2.2s; }
    #h-o4 { animation: h-orb-b 13s ease-in-out infinite 0.5s; }
  `}</style>
  <svg width="800" height="210" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="hg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,180,216,0.45)" />
        <stop offset="100%" stopColor="rgba(0,180,216,0)" />
      </radialGradient>
      <radialGradient id="hg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(123,47,190,0.55)" />
        <stop offset="100%" stopColor="rgba(123,47,190,0)" />
      </radialGradient>
    </defs>
    <ellipse id="h-o1" cx="700" cy="35"  rx="210" ry="160" fill="url(#hg2)" />
    <ellipse id="h-o2" cx="90"  cy="190" rx="190" ry="145" fill="url(#hg1)" />
    <ellipse id="h-o3" cx="590" cy="205" rx="165" ry="125" fill="url(#hg1)" />
    <ellipse id="h-o4" cx="190" cy="25"  rx="155" ry="125" fill="url(#hg2)" />
  </svg>
  <div style={{ display: 'flex', alignItems: 'center', zIndex: 10, width: '100%' }}>
    <div style={{ width: 94, height: 94, borderRadius: 999, background: 'linear-gradient(135deg, rgba(0,180,216,0.7), rgba(123,47,190,0.7))', padding: 2, flexShrink: 0 }}>
      <div style={{ width: 90, height: 90, borderRadius: 999, overflow: 'hidden' }}>
        <img src={(github && github.user && github.user.avatar_url) || 'https://github.com/Adityax-07.png'} width={90} height={90} style={{ objectFit: 'cover' }} />
      </div>
    </div>
    <div style={{ display: 'flex', flexDirection: 'column', marginLeft: 26 }}>
      <span style={{ fontSize: 30, fontWeight: 700, color: '#ffffff', lineHeight: 1 }}>
        {(github && github.user && (github.user.name || github.user.login)) || 'Aditya Bisht'}
      </span>
      <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.42)', marginTop: 9 }}>
        {'AI & ML Engineer | LLMs, RAG Systems & Agentic AI'}
      </span>
      <div style={{ display: 'flex', gap: 8, marginTop: 14 }}>
        {['Python', 'LangChain', 'PyTorch', 'FastAPI'].map((tech, i) => (
          <span key={i} style={{ padding: '4px 14px', background: 'rgba(0,180,216,0.08)', color: '#00B4D8', borderRadius: 100, fontSize: 12, border: '1px solid rgba(0,180,216,0.28)' }}>{tech}</span>
        ))}
      </div>
    </div>
  </div>
</div>
```

```aura width=800 height=110
<div style={{ position: 'relative', display: 'flex', alignItems: 'center', justifyContent: 'space-around', width: '100%', height: '100%', background: '#0d0e1a', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif' }}>
  <style>{`
    @keyframes s-pulse { 0%, 100% { opacity: 0.38; } 50% { opacity: 0.65; } }
    #s-o1 { animation: s-pulse 8s ease-in-out infinite; }
    #s-o2 { animation: s-pulse 10s ease-in-out infinite 1.2s; }
    #s-o3 { animation: s-pulse 9s ease-in-out infinite 2.4s; }
  `}</style>
  <svg width="800" height="110" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="sg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,180,216,0.32)" />
        <stop offset="100%" stopColor="rgba(0,180,216,0)" />
      </radialGradient>
      <radialGradient id="sg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(155,114,207,0.32)" />
        <stop offset="100%" stopColor="rgba(155,114,207,0)" />
      </radialGradient>
      <radialGradient id="sg3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(240,192,64,0.28)" />
        <stop offset="100%" stopColor="rgba(240,192,64,0)" />
      </radialGradient>
    </defs>
    <ellipse id="s-o1" cx="133" cy="55" rx="110" ry="85" fill="url(#sg1)" />
    <ellipse id="s-o2" cx="400" cy="55" rx="110" ry="85" fill="url(#sg2)" />
    <ellipse id="s-o3" cx="667" cy="55" rx="110" ry="85" fill="url(#sg3)" />
  </svg>
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 10 }}>
    <span style={{ fontSize: 38, fontWeight: 700, color: '#00B4D8', lineHeight: 1 }}>
      {(github && github.user && github.user.public_repos) || '0'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.32)', letterSpacing: 3, textTransform: 'uppercase', marginTop: 7 }}>repos</span>
  </div>
  <div style={{ width: 1, height: 36, background: 'rgba(255,255,255,0.07)' }} />
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 10 }}>
    <span style={{ fontSize: 38, fontWeight: 700, color: '#9B72CF', lineHeight: 1 }}>
      {(github && github.stars) || '0'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.32)', letterSpacing: 3, textTransform: 'uppercase', marginTop: 7 }}>stars</span>
  </div>
  <div style={{ width: 1, height: 36, background: 'rgba(255,255,255,0.07)' }} />
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 10 }}>
    <span style={{ fontSize: 38, fontWeight: 700, color: '#F0C040', lineHeight: 1 }}>
      {(github && github.commits) || '0'}
    </span>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.32)', letterSpacing: 3, textTransform: 'uppercase', marginTop: 7 }}>commits</span>
  </div>
</div>
```

```aura width=800 height=175
<div style={{ position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'center', width: '100%', height: '100%', background: '#0d0e1a', borderRadius: 20, overflow: 'hidden', fontFamily: 'Inter, sans-serif', padding: '0 32px' }}>
  <style>{`
    @keyframes ts-orb { 0%, 100% { opacity: 0.32; } 50% { opacity: 0.58; } }
    #ts-o1 { animation: ts-orb 10s ease-in-out infinite; }
    #ts-o2 { animation: ts-orb 12s ease-in-out infinite 2s; }
  `}</style>
  <svg width="800" height="175" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="tg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,180,216,0.28)" />
        <stop offset="100%" stopColor="rgba(0,180,216,0)" />
      </radialGradient>
      <radialGradient id="tg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(123,47,190,0.28)" />
        <stop offset="100%" stopColor="rgba(123,47,190,0)" />
      </radialGradient>
    </defs>
    <ellipse id="ts-o1" cx="720" cy="145" rx="190" ry="140" fill="url(#tg2)" />
    <ellipse id="ts-o2" cx="75"  cy="28"  rx="170" ry="125" fill="url(#tg1)" />
  </svg>
  <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.28)', letterSpacing: 4, textTransform: 'uppercase', marginBottom: 20, zIndex: 10 }}>tech stack</span>
  <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 12, zIndex: 10 }}>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.22)', letterSpacing: 2, textTransform: 'uppercase', width: 88, flexShrink: 0 }}>languages</span>
    <div style={{ display: 'flex', gap: 8 }}>
      {['Python', 'JavaScript', 'TypeScript', 'C++', 'Java'].map((l, i) => (
        <span key={i} style={{ padding: '5px 14px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.65)', borderRadius: 8, fontSize: 12, border: '1px solid rgba(255,255,255,0.07)' }}>{l}</span>
      ))}
    </div>
  </div>
  <div style={{ display: 'flex', alignItems: 'center', gap: 12, zIndex: 10 }}>
    <span style={{ fontSize: 10, color: 'rgba(255,255,255,0.22)', letterSpacing: 2, textTransform: 'uppercase', width: 88, flexShrink: 0 }}>frameworks</span>
    <div style={{ display: 'flex', gap: 8 }}>
      {['LangChain', 'FastAPI', 'PyTorch', 'React', 'Streamlit'].map((f, i) => (
        <span key={i} style={{ padding: '5px 14px', background: 'rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.65)', borderRadius: 8, fontSize: 12, border: '1px solid rgba(255,255,255,0.07)' }}>{f}</span>
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
