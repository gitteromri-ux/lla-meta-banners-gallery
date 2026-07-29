#!/usr/bin/env python3
"""Render chosen banner HTML files to PNG with headless Chromium."""
import asyncio, glob, os, re
from playwright.async_api import async_playwright

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banners", "chosen")

async def main():
    files = sorted(glob.glob(f"{DIR}/*.html"))
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for f in files:
            m = re.search(r'width:(\d+)px; height:(\d+)px', open(f).read())
            w, h = int(m.group(1)), int(m.group(2))
            page = await browser.new_page(viewport={"width": w, "height": h})
            await page.goto(f"file://{f}", wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(400)
            await page.screenshot(path=f.replace(".html", ".png"))
            await page.close()
            print("rendered", os.path.basename(f), w, h)
        await browser.close()

asyncio.run(main())
