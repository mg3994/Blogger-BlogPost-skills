import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Set viewport size
    page.set_viewport_size({"width": 1280, "height": 1000})

    # Go to the local static HTML file
    filepath = "/app/posts/say-goodbye-to-raw-xml-introducing-antinna-blogger-theme.html"
    page.goto(f"file://{filepath}")
    page.wait_for_timeout(2000) # Give Prism.js time to load and highlight

    # 1. Take a screenshot of the top (Banner Image)
    page.screenshot(path="/home/jules/verification/screenshots/verification_banner.png")
    page.wait_for_timeout(1000)

    # 2. Scroll to Step 5 (types/blogger-theme.d.ts block)
    step5_header = page.locator("#section-5")
    if step5_header.is_visible():
        step5_header.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="/home/jules/verification/screenshots/verification_step5.png")

    # 3. Scroll to Step 6 (components/BlogHeader.tsx)
    step6_header = page.locator("#section-6")
    if step6_header.is_visible():
        step6_header.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="/home/jules/verification/screenshots/verification_step6.png")

    # 4. Scroll to Step 8 (client/App.jsx)
    step8_header = page.locator("#section-8")
    if step8_header.is_visible():
        step8_header.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="/home/jules/verification/screenshots/verification_step8.png")

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    os.makedirs("/home/jules/verification/videos", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
    print("Verification script finished successfully!")
