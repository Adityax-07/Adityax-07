```aura width=860 height=200
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', alignItems: 'center', fontFamily: 'Inter',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)'
}}>
  <style>{`
    @keyframes orb-a {
      0%   { transform:translate(0px,0px);   opacity:0.75; }
      25%  { transform:translate(110px,55px); opacity:1.0;  }
      50%  { transform:translate(65px,110px); opacity:0.82; }
      75%  { transform:translate(-25px,65px); opacity:0.95; }
      100% { transform:translate(0px,0px);   opacity:0.75; }
    }
    @keyframes orb-b {
      0%   { transform:translate(0px,0px);    opacity:0.70; }
      25%  { transform:translate(-100px,50px); opacity:0.92; }
      50%  { transform:translate(-55px,105px); opacity:0.78; }
      75%  { transform:translate(20px,60px);  opacity:1.0;  }
      100% { transform:translate(0px,0px);    opacity:0.70; }
    }
    @keyframes orb-c {
      0%   { transform:translate(0px,0px);   opacity:0.68; }
      30%  { transform:translate(50px,95px);  opacity:0.90; }
      65%  { transform:translate(-45px,75px); opacity:0.95; }
      100% { transform:translate(0px,0px);   opacity:0.68; }
    }
    @keyframes orb-d {
      0%   { transform:translate(0px,0px);   opacity:0.72; }
      35%  { transform:translate(90px,35px);  opacity:0.95; }
      70%  { transform:translate(55px,-40px); opacity:0.80; }
      100% { transform:translate(0px,0px);   opacity:0.72; }
    }
    #glow-1 { animation: orb-a 9s  ease-in-out infinite; }
    #glow-2 { animation: orb-b 11s ease-in-out infinite; }
    #glow-3 { animation: orb-b 10s ease-in-out infinite reverse; }
    #glow-4 { animation: orb-a 12s ease-in-out infinite reverse; }
    #glow-5 { animation: orb-c 8s  ease-in-out infinite; }
    #glow-6 { animation: orb-c 13s ease-in-out infinite reverse; }
    #glow-7 { animation: orb-d 14s ease-in-out infinite; }
    #glow-8 { animation: orb-d 10s ease-in-out infinite reverse; }
  `}</style>

  <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.72)" />
        <stop offset="40%" stopColor="rgba(90,15,180,0.35)" />
        <stop offset="70%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
      <radialGradient id="g2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,60,255,0.60)" />
        <stop offset="45%" stopColor="rgba(30,50,200,0.25)" />
        <stop offset="70%" stopColor="rgba(30,50,200,0)" />
      </radialGradient>
      <radialGradient id="g3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,130,255,0.48)" />
        <stop offset="50%" stopColor="rgba(0,100,220,0.18)" />
        <stop offset="70%" stopColor="rgba(0,100,220,0)" />
      </radialGradient>
      <radialGradient id="g4" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,190,230,0.38)" />
        <stop offset="60%" stopColor="rgba(0,160,210,0.12)" />
        <stop offset="100%" stopColor="rgba(0,160,210,0)" />
      </radialGradient>
      <radialGradient id="g5" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(160,30,255,0.55)" />
        <stop offset="45%" stopColor="rgba(130,20,220,0.20)" />
        <stop offset="70%" stopColor="rgba(130,20,220,0)" />
      </radialGradient>
      <radialGradient id="g6" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(20,60,255,0.45)" />
        <stop offset="50%" stopColor="rgba(10,40,200,0.16)" />
        <stop offset="70%" stopColor="rgba(10,40,200,0)" />
      </radialGradient>
      <radialGradient id="g7" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(90,30,200,0.40)" />
        <stop offset="60%" stopColor="rgba(70,20,180,0.14)" />
        <stop offset="100%" stopColor="rgba(70,20,180,0)" />
      </radialGradient>
      <radialGradient id="g8" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,170,255,0.38)" />
        <stop offset="50%" stopColor="rgba(0,130,220,0.13)" />
        <stop offset="70%" stopColor="rgba(0,130,220,0)" />
      </radialGradient>
    </defs>
    <ellipse id="glow-1" cx="50"  cy="22"  rx="200" ry="150" fill="url(#g1)" />
    <ellipse id="glow-2" cx="810" cy="18"  rx="190" ry="148" fill="url(#g2)" />
    <ellipse id="glow-3" cx="55"  cy="178" rx="185" ry="140" fill="url(#g3)" />
    <ellipse id="glow-4" cx="805" cy="182" rx="180" ry="138" fill="url(#g4)" />
    <ellipse id="glow-5" cx="430" cy="-8"  rx="230" ry="130" fill="url(#g5)" />
    <ellipse id="glow-6" cx="430" cy="208" rx="240" ry="132" fill="url(#g6)" />
    <ellipse id="glow-7" cx="-12" cy="100" rx="155" ry="118" fill="url(#g7)" />
    <ellipse id="glow-8" cx="872" cy="100" rx="155" ry="118" fill="url(#g8)" />
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



```aura width=860 height=340
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', flexDirection: 'column', fontFamily: 'Inter',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.28)',
  paddingTop: 28, paddingLeft: 42, paddingRight: 42
}}>
  <style>{`
    @keyframes stack-drift-a {
      0%,100% { transform:translate(0px,0px); opacity:0.78; }
      50% { transform:translate(110px,55px); opacity:1; }
    }
    @keyframes stack-drift-b {
      0%,100% { transform:translate(0px,0px); opacity:0.72; }
      50% { transform:translate(-115px,65px); opacity:1; }
    }
    @keyframes stack-drift-c {
      0%,100% { transform:translate(0px,0px); opacity:0.72; }
      50% { transform:translate(75px,-50px); opacity:0.96; }
    }
    #stack-glow-1 { animation:stack-drift-a 12s ease-in-out infinite; }
    #stack-glow-2 { animation:stack-drift-b 14s ease-in-out infinite; }
    #stack-glow-3 { animation:stack-drift-c 10s ease-in-out infinite; }
    #stack-glow-4 { animation:stack-drift-b 17s ease-in-out infinite reverse; }
    @media (prefers-reduced-motion: reduce) {
      #stack-glow-1, #stack-glow-2, #stack-glow-3, #stack-glow-4 { animation:none; }
    }
  `}</style>

  <svg width="860" height="340" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="stack-purple" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(130,25,230,0.68)" />
        <stop offset="48%" stopColor="rgba(90,15,180,0.28)" />
        <stop offset="100%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
      <radialGradient id="stack-blue" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,70,255,0.58)" />
        <stop offset="48%" stopColor="rgba(25,55,190,0.25)" />
        <stop offset="100%" stopColor="rgba(25,55,190,0)" />
      </radialGradient>
      <radialGradient id="stack-cyan" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,175,225,0.46)" />
        <stop offset="50%" stopColor="rgba(0,120,210,0.17)" />
        <stop offset="100%" stopColor="rgba(0,120,210,0)" />
      </radialGradient>
    </defs>
    <ellipse id="stack-glow-1" cx="120" cy="75" rx="260" ry="195" fill="url(#stack-purple)" />
    <ellipse id="stack-glow-2" cx="740" cy="65" rx="245" ry="185" fill="url(#stack-blue)" />
    <ellipse id="stack-glow-3" cx="270" cy="305" rx="280" ry="175" fill="url(#stack-cyan)" />
    <ellipse id="stack-glow-4" cx="725" cy="315" rx="250" ry="170" fill="url(#stack-purple)" />
  </svg>

  <div style={{ display: 'flex', fontSize: 12, fontWeight: 700, color: '#c7b5ef', letterSpacing: '2.5px', marginBottom: 16 }}>
    TECH STACK
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 9 }}>
    {[
      {label:'LANGUAGES', color:'#c99cff', items:['Python','TypeScript','JavaScript']},
      {label:'AI / ML', color:'#aa9aff', items:['PyTorch','TensorFlow','Hugging Face','scikit-learn']},
      {label:'LLM / AGENTS', color:'#78baff', items:['LangChain','LangGraph','FAISS','vLLM']},
      {label:'BUILD / SHIP', color:'#73d7e9', items:['FastAPI','Streamlit','Docker','Git']}
    ].map(function(group) {
      return (
        <div key={group.label} style={{
          display:'flex', alignItems:'center', height:55, paddingLeft:15, paddingRight:12,
          borderRadius:10, background:'rgba(8,8,16,0.62)',
          border:'1px solid rgba(190,165,255,0.18)'
        }}>
          <div style={{ display:'flex', alignItems:'center', gap:9, width:145, flexShrink:0 }}>
            <div style={{ width:7, height:7, borderRadius:4, background:group.color }} />
            <div style={{ fontSize:13, fontWeight:700, letterSpacing:'1px', color:group.color }}>{group.label}</div>
          </div>
          <div style={{ display:'flex', alignItems:'center', gap:8 }}>
            {group.items.map(function(t) {
              return (
                <div key={t} style={{
                  display:'flex', paddingTop:7, paddingBottom:7, paddingLeft:13, paddingRight:13,
                  borderRadius:7, background:'rgba(8,8,12,0.82)',
                  border:'1px solid rgba(205,190,255,0.26)',
                  color:'#f4f1ff', fontSize:19, fontWeight:600
                }}>{t}</div>
              );
            })}
          </div>
        </div>
      );
    })}
  </div>
</div>
```

```aura width=148 height=44
<div style={{ width:'100%', height:'100%', background:'#08080c', display:'flex', alignItems:'center', justifyContent:'center', borderRadius:22, border:'1px solid rgba(10,102,194,0.45)', gap:8, fontFamily:'Inter' }}>
  <div style={{ display:'flex', width:8, height:8, borderRadius:4, background:'rgba(10,102,194,0.95)' }} />
  <div style={{ display:'flex', fontSize:13, fontWeight:700, color:'rgba(100,160,255,0.95)' }}>LinkedIn</div>
</div>
```

```aura width=128 height=44
<div style={{ width:'100%', height:'100%', background:'#08080c', display:'flex', alignItems:'center', justifyContent:'center', borderRadius:22, border:'1px solid rgba(200,200,200,0.25)', gap:8, fontFamily:'Inter' }}>
  <div style={{ display:'flex', width:8, height:8, borderRadius:4, background:'rgba(220,220,220,0.85)' }} />
  <div style={{ display:'flex', fontSize:13, fontWeight:700, color:'rgba(220,220,220,0.92)' }}>GitHub</div>
</div>
```

```aura width=158 height=44
<div style={{ width:'100%', height:'100%', background:'#08080c', display:'flex', alignItems:'center', justifyContent:'center', borderRadius:22, border:'1px solid rgba(255,210,30,0.35)', gap:8, fontFamily:'Inter' }}>
  <div style={{ display:'flex', width:8, height:8, borderRadius:4, background:'rgba(255,220,60,0.90)' }} />
  <div style={{ display:'flex', fontSize:13, fontWeight:700, color:'rgba(255,220,70,0.92)' }}>Hugging Face</div>
</div>
```

```aura width=110 height=44
<div style={{ width:'100%', height:'100%', background:'#08080c', display:'flex', alignItems:'center', justifyContent:'center', borderRadius:22, border:'1px solid rgba(234,67,53,0.38)', gap:8, fontFamily:'Inter' }}>
  <div style={{ display:'flex', width:8, height:8, borderRadius:4, background:'rgba(234,100,90,0.90)' }} />
  <div style={{ display:'flex', fontSize:13, fontWeight:700, color:'rgba(255,120,110,0.92)' }}>Email</div>
</div>
```

## Proof of work

I benchmark, not just build.

- [RAG-Systems-eval-suite](https://github.com/Adityax-07/RAG-Systems-eval-suite) — 8 RAG systems evaluated on 50 questions and 10 metrics; advanced RAG scored 0.770 overall.
- [AgentBench](https://github.com/Adityax-07/AgentBench) — 50-query evaluation measured 4% hallucination for the multi-agent system versus 24% for a single agent.
- [LLM-vs-RAG-vs-Fine-Tuning-](https://github.com/Adityax-07/LLM-vs-RAG-vs-Fine-Tuning-) — compared 3 systems across 50 questions and 8 metrics.
- [RAG_SECURITY_DEMO](https://github.com/Adityax-07/RAG_SECURITY_DEMO) — tested a secure RAG pipeline with 100 labeled queries across 8 categories.

## Currently

- Building CLI-native agent skills and repeatable orchestration.
- Learning vLLM serving and self-hosted inference.
- Benchmarking RAG and agent trade-offs across accuracy, latency, cost, and safety.

## Background

B.Tech IT at MAIT, GGSIPU (2023–27) · Applied AI / Prompt Engineering intern<br>
Oracle Generative AI Professional · Oracle AI Vector Search Professional

[Projects](https://github.com/Adityax-07?tab=repositories) · [LinkedIn](https://www.linkedin.com/in/aditya-bisht-82211b327/) · [Email](mailto:aaditya85677@gmail.com)
