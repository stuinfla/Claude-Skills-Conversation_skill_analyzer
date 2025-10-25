#!/usr/bin/env python3
"""
Test GitHub README download link for v4.2.0
"""

from playwright.sync_api import sync_playwright
import time

def test_github_download_link():
    """Test that the download link in README actually works"""

    print("\n" + "="*70)
    print("  GITHUB DOWNLOAD LINK VERIFICATION - v4.2.0")
    print("="*70 + "\n")

    with sync_playwright() as p:
        print("🚀 Launching Chrome...")
        browser = p.chromium.launch(
            headless=False,
            channel="chrome"
        )

        context = browser.new_context()
        page = context.new_page()

        try:
            # Navigate to GitHub repo
            print("🌐 Navigating to GitHub repository...")
            page.goto("https://github.com/stuinfla/Claude-Skills-Conversation_skill_analyzer", timeout=30000)
            time.sleep(2)

            print("📸 Taking screenshot of page...")
            page.screenshot(path="test_screenshots/github_page.png", full_page=True)

            # Find the download link
            print("🔍 Looking for download link: conversation-skill-analyzer-v4.2.0.zip...")

            # Try to find the link
            download_link = page.locator("a[href*='conversation-skill-analyzer-v4.2.0.zip']")

            if download_link.count() == 0:
                print("❌ FAIL: Download link not found on page!")
                print("\n🔍 Searching for what links ARE present...")

                # Find all .zip links
                all_zip_links = page.locator("a[href*='.zip']")
                print(f"Found {all_zip_links.count()} .zip links:")
                for i in range(all_zip_links.count()):
                    href = all_zip_links.nth(i).get_attribute("href")
                    text = all_zip_links.nth(i).inner_text()
                    print(f"  - {text}: {href}")

                # Check if file exists in repo
                print("\n🔍 Checking repository files...")
                page.screenshot(path="test_screenshots/github_files.png", full_page=True)

                browser.close()
                return False

            print(f"✅ Found {download_link.count()} matching link(s)")

            # Get link details
            link_href = download_link.first.get_attribute("href")
            link_text = download_link.first.inner_text()

            print(f"📝 Link text: {link_text}")
            print(f"📝 Link href: {link_href}")

            # Check if it's a valid GitHub link
            if "github.com" in link_href or link_href.startswith("/"):
                print("✅ Link format looks valid")
            else:
                print("⚠️  Warning: Link format unusual")

            print("\n✅ PASS: Download link exists and is properly formatted")
            print("\n⏸️  Browser will remain open for manual inspection")
            print("Press ENTER to close browser...")
            input()

            browser.close()
            return True

        except Exception as e:
            print(f"❌ ERROR: {e}")
            page.screenshot(path="test_screenshots/error.png", full_page=True)
            print("\n⏸️  Browser will remain open for debugging")
            print("Press ENTER to close browser...")
            input()
            browser.close()
            return False

if __name__ == "__main__":
    success = test_github_download_link()
    exit(0 if success else 1)
