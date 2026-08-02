#!/usr/bin/env python3
"""Render all banner HTML files to PNG with headless Chromium, in parallel."""
import asyncio, glob, os, re, sys
from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
VERSIONS = sys.argv[1:] if len(sys.argv) > 1 else ["v1","v2","v3","v4","v6","v7","chosen"]
CONCURRENCY = 6

async def render_file(browser, f, sem):
    async with sem:
        m = re.search(r'width:(\d+)px; height:(\d+)px', open(f).read())
        w, h = int(m.group(1)), int(m.group(2))
        page = await browser.new_page(viewport={"width": w, "height": h})
        try:
            await page.goto(f"file://{f}", wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(300)
            await page.screenshot(path=f.replace(".html", ".png"))
            print("rendered", os.path.basename(f))
        finally:
            await page.close()

async def main():
    files = []
    for v in VERSIONS:
        files += sorted(glob.glob(f"{ROOT}/banners/{v}/*.html"))
    print(f"{len(files)} files to render")
    sem = asyncio.Semaphore(CONCURRENCY)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        await asyncio.gather(*[render_file(browser, f, sem) for f in files])
        await browser.close()

asyncio.run(main())
