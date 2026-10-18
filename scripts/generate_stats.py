#!/usr/bin/env python3
"""Generate light and dark profile statistics SVGs from the GitHub API."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import urllib.request
from xml.sax.saxutils import escape


USERNAME = "Adityax-07"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"


@dataclass(frozen=True)
class Metrics:
    public_repos: int
    source_repos: int
    top_language: str
    top_language_count: int
    as_of: str

    @property
    def source_ratio(self) -> int:
        if not self.public_repos:
            return 0
        return round(self.source_repos / self.public_repos * 100)


def api_json(path: str, token: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Adityax-07-profile-stats",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_metrics(token: str) -> Metrics:
    user = api_json(f"/users/{USERNAME}", token)
    repos = api_json(
        f"/users/{USERNAME}/repos?per_page=100&type=owner&sort=full_name", token
    )
    if not isinstance(user, dict) or not isinstance(repos, list):
        raise RuntimeError("Unexpected GitHub API response")

    source_repos = [repo for repo in repos if not repo.get("fork", False)]
    languages = Counter(
        repo["language"] for repo in source_repos if repo.get("language")
    )
    top_language, top_count = languages.most_common(1)[0] if languages else ("—", 0)
    return Metrics(
        public_repos=int(user["public_repos"]),
        source_repos=len(source_repos),
        top_language=top_language,
        top_language_count=top_count,
        as_of=datetime.now(timezone.utc).strftime("%d %b %Y").upper(),
    )


def render(metrics: Metrics, dark: bool) -> str:
    if dark:
        background, border, primary, secondary = "#0D1117", "#30363D", "#F0F6FC", "#9198A1"
        blue, mint, amber = "#58A6FF", "#2CE8A0", "#F2B84B"
        blue_bg, mint_bg, amber_bg = "#111C2F", "#0E251D", "#2A2110"
    else:
        background, border, primary, secondary = "#FFFFFF", "#D0D7DE", "#1F2328", "#59636E"
        blue, mint, amber = "#2877F5", "#19A974", "#B67800"
        blue_bg, mint_bg, amber_bg = "#EFF6FF", "#EAFBF4", "#FFF7E6"

    language = escape(metrics.top_language)
    panels = (
        ("PUBLIC REPOS", str(metrics.public_repos), blue, blue_bg),
        ("ORIGINAL BUILDS", str(metrics.source_repos), mint, mint_bg),
        (f"{language.upper()} REPOS", str(metrics.top_language_count), amber, amber_bg),
        ("SOURCE RATIO", f"{metrics.source_ratio}%", blue, blue_bg),
    )
    panel_svg = []
    for index, (label, value, accent, panel_bg) in enumerate(panels):
        x = 24 + index * 172
        panel_svg.append(
            f'''<g transform="translate({x} 50)">
  <rect width="156" height="78" rx="10" fill="{panel_bg}" stroke="{border}"/>
  <text x="14" y="25" class="m" font-size="11" font-weight="700" letter-spacing="1" fill="{secondary}">{label}</text>
  <text x="14" y="61" class="s" font-size="30" font-weight="750" fill="{accent}">{value}</text>
</g>'''
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="174" viewBox="0 0 720 174" role="img" aria-labelledby="title desc">
  <title id="title">Open-source snapshot for {USERNAME}</title>
  <desc id="desc">{metrics.public_repos} public repositories, {metrics.source_repos} original builds, {metrics.top_language_count} {language} repositories, and a {metrics.source_ratio} percent source ratio.</desc>
  <style>.m{{font-family:ui-monospace,SFMono-Regular,Consolas,"Liberation Mono",monospace}}.s{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}</style>
  <rect x="1" y="1" width="718" height="172" rx="14" fill="{background}" stroke="{border}" stroke-width="2"/>
  <circle cx="26" cy="26" r="4" fill="{mint}"/>
  <text x="40" y="31" class="m" font-size="13" font-weight="700" letter-spacing="1.3" fill="{primary}">OPEN-SOURCE SNAPSHOT</text>
  <text x="696" y="31" text-anchor="end" class="m" font-size="11" fill="{secondary}">{escape(metrics.as_of)} · UTC</text>
  {''.join(panel_svg)}
  <path d="M24 145h672" stroke="{border}"/>
  <text x="24" y="162" class="m" font-size="10" letter-spacing=".7" fill="{secondary}">SOURCE REPOS ONLY FOR LANGUAGE COUNTS · UPDATED WEEKLY VIA GITHUB ACTIONS</text>
</svg>
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-repos", type=int)
    parser.add_argument("--source-repos", type=int)
    parser.add_argument("--top-language")
    parser.add_argument("--top-language-count", type=int)
    parser.add_argument("--as-of")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    overrides = (
        args.public_repos,
        args.source_repos,
        args.top_language,
        args.top_language_count,
    )
    if any(value is not None for value in overrides):
        if not all(value is not None for value in overrides):
            raise SystemExit("Provide all four metric override arguments or none of them")
        metrics = Metrics(
            public_repos=args.public_repos,
            source_repos=args.source_repos,
            top_language=args.top_language,
            top_language_count=args.top_language_count,
            as_of=args.as_of or datetime.now(timezone.utc).strftime("%d %b %Y").upper(),
        )
    else:
        metrics = fetch_metrics(os.environ.get("GITHUB_TOKEN", ""))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "stats-light.svg").write_text(render(metrics, dark=False), encoding="utf-8")
    (OUTPUT_DIR / "stats-dark.svg").write_text(render(metrics, dark=True), encoding="utf-8")


if __name__ == "__main__":
    main()
