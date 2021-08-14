import pyppeteer
import asyncio
from typing import List

UA_SITE = "https://developers.whatismybrowser.com/useragents/explore/software_name"
UA_DEFAULT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
TABLE_XPATH = '//*[@id="content-base"]/section[2]/div/div/table/tbody'
UA_JS = """
table => {  
    let ua = [];
    for (let i = 0;  i < table.rows.length;  i++){
        ua.push(table.rows[i].cells[0].textContent);
    };
    return ua;    
}"""


async def main() -> None:
    browser = await pyppeteer.launch(headless=True)  # args=["--no-sandbox"])
    for browser_name in ("chrome", "firefox", "safari"):
        data = await asyncio.gather(
            *map(lambda x: scrap_page(browser, browser_name, x), range(1, 6))
        )  # 5 pages
        with open(f"{browser_name}.txt", "w") as f:
            f.write("\n".join([i for x in data for i in x]))
        await asyncio.sleep(2)
    await browser.close()


async def scrap_page(browser, browser_name: str, pg: int) -> List[str]:
    page = await browser.newPage()
    await page.setUserAgent(UA_DEFAULT)
    await page.goto("/".join((UA_SITE, browser_name, str(pg))))
    table = (await page.xpath(TABLE_XPATH))[0]
    return await page.evaluate(UA_JS, table)


asyncio.run(main())
