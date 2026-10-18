# Design notes

Research and repository audit completed 18 October 2026. The live GitHub profile, public repository listing, pinned repositories, benchmark artifacts, and 20 reference profile READMEs were inspected before design work began.

## Research sample

Curated/high-star profiles: [abhisheknaiidu](https://github.com/abhisheknaiidu), [simonw](https://github.com/simonw), [anuraghazra](https://github.com/anuraghazra), [DenverCoder1](https://github.com/DenverCoder1), [MartinHeinz](https://github.com/MartinHeinz), [rafnixg](https://github.com/rafnixg), [natemoo-re](https://github.com/natemoo-re), [sindresorhus](https://github.com/sindresorhus), [antfu](https://github.com/antfu), [cassidoo](https://github.com/cassidoo), [addyosmani](https://github.com/addyosmani), [b0o](https://github.com/b0o), [gautamkrishnar](https://github.com/gautamkrishnar), [mokkapps](https://github.com/mokkapps), [athul](https://github.com/athul), [blackcater](https://github.com/blackcater), [thewhiteh4t](https://github.com/thewhiteh4t), [iampavangandhi](https://github.com/iampavangandhi), [rahul-jha98](https://github.com/rahul-jha98), and [caneco](https://github.com/caneco). GitHub's current [Trending developers](https://github.com/trending/developers) page was also checked to compare profile-first and repository-first presentation.

| Technique | Example profile/tool | Why it works | Risk | Decision |
|---|---|---|---|---|
| Project-first proof | anuraghazra, rafnixg | Leads with outcomes and gives recruiters a short path to code | Claims can age | Adopt; every featured metric is tied to a repository artifact |
| Self-owned SVG identity | caneco, thewhiteh4t | Strong identity with no runtime service | Text can become unreadable on mobile | Adopt with 720–800 px viewBoxes, large type, and image alt text |
| Action-generated content | simonw, abhisheknaiidu | Keeps a profile current without a hosted widget | Token permissions and scheduled-workflow inactivity | Adopt for one small weekly stats asset |
| Theme-aware `<picture>` | [Platane/snk](https://github.com/Platane/snk), [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) | Native light/dark selection; no client JavaScript | More assets to maintain | Adopt for every visual |
| Dynamic stats service | anuraghazra, DenverCoder1 | Immediate social/activity context | Public endpoint rate limits and outages; the original service now recommends Actions/self-hosting | Replace with repository-owned generation |
| WakaTime block | abhisheknaiidu, [waka-readme](https://github.com/athul/waka-readme) | Shows recent practice | Requires editor telemetry and a secret; can expose project names and add noise | Skip |
| Contribution snake | DenverCoder1, [Platane/snk](https://github.com/Platane/snk) | Memorable and automatically current | Large motion surface; weak relevance to applied-AI work | Skip |
| Generated capsule header | [capsule-render](https://github.com/kyechan99/capsule-render), MartinHeinz-style banners | Fast visual polish | Third-party render dependency and familiar/template-like look | Replace with hand-authored local SVG |
| Dense badge/icon wall | DenverCoder1, gautamkrishnar, rahul-jha98 | Fast technology scan | High request count, weak hierarchy, visual noise | Skip; use one self-hosted grouped stack asset |
| Minimal text narrative | antfu, cassidoo, addyosmani, natemoo-re | Fast, credible, and accessible | Can under-show proof | Adopt for bio, current focus, and contact |

## GitHub rendering constraints

- GitHub's rendering pipeline aggressively sanitizes HTML, removing dangerous elements such as scripts as well as inline styles/classes; JavaScript-driven UI is therefore out. Source: [github/markup](https://github.com/github/markup).
- The sanitizer removes iframe contents, so embeds are represented as normal links. Source: [Selma sanitizer](https://github.com/gjtorikian/selma).
- Externally hosted images are rewritten through GitHub's Camo proxy. Private/authenticated images will not render. Source: [GitHub Docs — anonymized URLs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls).
- GitHub supports `<picture>` plus `prefers-color-scheme` for theme-aware images; the pattern is documented in the github-readme-stats and Platane/snk READMEs.
- A profile README requires a public repository named exactly like the account with a non-empty root `README.md`. Source: [GitHub Docs — profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).
- GitHub provides no repository-README JavaScript or reliable custom page CSS. Responsive behavior must come from GitHub's image scaling, compact prose, and avoiding wide tables.

## Chosen concept

**Benchmark dashboard / terminal-grade minimalism.**<br>
The terminal language fits CLI skills and self-hosted inference without becoming a costume.<br>
Every decorative surface carries evidence: focus, measured work, stack, or live repository counts.<br>
The restrained system makes the line “I benchmark, not just build.” the organizing idea rather than a slogan pasted onto a generic profile.

### Visual system

- Palette: blue `#2877F5` / `#58A6FF`, mint `#19A974` / `#2CE8A0`, amber `#F2B84B`; neutral GitHub-compatible light and dark surfaces.
- Type: native UI sans for reading; native monospace for labels, metrics, and terminal syntax. No web-font request.
- Spacing: 8 px base rhythm; major sections use 24–32 px visual gaps.
- Icons: one custom 2 px rounded line style. No mixed emoji or logo packs.
- Hierarchy: hero → positioning → current focus → four measured projects → grouped stack → one stats widget → contact.
- Motion: one cursor blink in the hero, disabled by `prefers-reduced-motion`.

## Content provenance

| Repository | Audited artifact | Profile claim used |
|---|---|---|
| [RAG-Systems-eval-suite](https://github.com/Adityax-07/RAG-Systems-eval-suite) | `data/benchmark_results.json`, `data/rag_dataset.json`, commit `0d76995` | 8 systems × 50 questions × 10 metrics; advanced RAG average 0.770 |
| [AgentBench](https://github.com/Adityax-07/AgentBench) | `bench_results.json`, commit `944321c` | 50 queries; hallucination 24% single-agent vs 4% multi-agent |
| [LLM-vs-RAG-vs-Fine-Tuning-](https://github.com/Adityax-07/LLM-vs-RAG-vs-Fine-Tuning-) | `data/benchmark_cache.json`, commit `e8cc55d` | 3 systems × 50 questions × 8 metrics; top answer accuracy 85.3% |
| [RAG_SECURITY_DEMO](https://github.com/Adityax-07/RAG_SECURITY_DEMO) | `test_queries.py`, commit `d4f2656` | 100 labeled queries across 8 security categories |

The public repository listing showed 31 repositories, 23 non-forks, and Python as the primary language of 10 non-fork repositories on the audit date. The checked-in stats assets start from that snapshot; the weekly workflow replaces it with authenticated API data.

Contact provenance: LinkedIn was matched by MAIT, GGSIPU, applied-LLM focus, and Oracle certifications; the email address is the public author email on the latest commits in three featured repositories. “Project portfolio” intentionally links to the GitHub repository index because no separate portfolio URL is published on the GitHub account.

## Performance and dependency decisions

- No GIFs, remote badges, remote fonts, iframe embeds, or runtime JavaScript.
- All displayed images are local SVGs. The SVG set is small, text remains selectable in the README fallback/alt path, and the card width scales below 375 px.
- The only workflow dependency is `actions/checkout`, pinned to commit `11bd71901bbe5b1630ceea73d27597364c9af683` (v4.2.2).
- Remaining network dependencies: GitHub image delivery when the README renders; GitHub's REST API during the scheduled workflow; ordinary outbound contact/project links. No third-party image host remains.

## Setup

The special repository already exists at `Adityax-07/Adityax-07`. This delivery was integrated into a clone of its `main` branch in `existing-profile/`. To publish from that directory:

```bash
cd existing-profile
git add README.md DESIGN_NOTES.md assets scripts screenshots .github/workflows
git commit -m "feat: redesign profile README"
git push origin main
```

The previous `readme-aura` and snake workflows were removed from the integrated checkout because the former rewrote `README.md` on every push and the latter only generated an unused output-branch asset. Their prior source files and graphics remain in the repository, and Git history preserves the workflow definitions. The new workflow generates only the local stats SVGs.

If the special repository is ever removed, recreate it as public and with the exact username:

```bash
gh repo create Adityax-07/Adityax-07 --public --clone
```

Then open **Settings → Actions → General → Workflow permissions**, select **Read and write permissions**, save, and run **Actions → Update profile stats → Run workflow** once. The workflow then refreshes the two stats SVGs every Sunday at 00:17 UTC.

## Verification record

Verified on 18 October 2026:

- Rendered the full Markdown in GitHub-like light and dark frames at 900 px and captured both results in `screenshots/`. Each page is 2,028 px tall in a 900 px viewport: 1.25 viewport-lengths of scrolling after the initial screen, within the two-scroll target.
- Emulated a 375 × 812 px mobile viewport. Reported `clientWidth = 375` and `scrollWidth = 375`, so there is no horizontal overflow. The first pass exposed rigid status-line wrapping; the `Currently` block was changed to normal Markdown lines and re-rendered.
- Parsed all 14 SVGs as XML. The complete displayed SVG set is 24,853 bytes; there are no GIFs, external image requests, scripts, or iframes.
- Resolved all 14 local light/dark image paths and confirmed 7/7 rendered images have descriptive `alt` text and 7/7 visuals have dark-mode sources.
- All five GitHub destinations returned HTTP 200. LinkedIn rejects automated requests with its anti-bot HTTP 999 response, but the exact public profile was independently matched in indexed results. The `mailto:` target is syntactically valid and matches the public commit identity used by three featured repositories.
- Compiled `scripts/generate_stats.py`, exercised its deterministic override path, and confirmed the workflow references only a full-length pinned action commit.
- Checked representative foreground/background pairs for WCAG contrast. The lowest text pair is mint-on-light at 5.31:1; primary text reaches 15.80:1 light and 17.39:1 dark.

### Self-critique

| Criterion | Score | Evidence |
|---|---:|---|
| Clarity | 9/10 | One-line position, three-line bio, explicit current work, then measurable proof |
| Visual polish | 9/10 | Cohesive local SVG system, aligned geometry, complete light/dark treatment |
| Originality | 9/10 | Benchmark-console language is specific to the work; no template banner or badge wall |
| Load speed | 10/10 | 24.3 KiB of SVG in total, one visual per section, zero third-party image hosts |
| Mobile layout | 9/10 | Verified at 375 px with zero overflow; prose remains available when images are disabled |
| Credibility | 9/10 | Every project number traces to an audited repository artifact and commit; live repository totals refresh weekly |

No category remained below 8 after the mobile status-block fix.
