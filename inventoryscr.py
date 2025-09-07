import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Launch Chromium
        browser = await p.chromium.launch(headless=False)  # headless=True runs without UI
        page = await browser.new_page()

        # Go to demo inventory site
        await page.goto("https://books.toscrape.com/")

        # Select all products
        products = await page.query_selector_all(".product_pod")

        print("\n📦 Inventory (first 5 items):\n")

        for product in products[:5]:  # just 5 items for demo
            title = await (await product.query_selector("h3 a")).get_attribute("title")
            price = await (await product.query_selector(".price_color")).inner_text()
            print(f"- {title} → {price}")

        await browser.close()

# Run
asyncio.run(main())