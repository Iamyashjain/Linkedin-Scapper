from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import time

EMAIL = "yashjain200502@gmail.com"
PASSWORD = "Gunjan$1"
TARGET = "soham-sharma"   # linkedin.com/in/<this>

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.linkedin.com/login")
time.sleep(3)
driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(6)

profile_url = f"https://www.linkedin.com/in/{TARGET}/"
driver.get(profile_url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

def get_text(sel):
    try:
        return soup.select_one(sel).get_text(strip=True)
    except:
        return "NA"

name = get_text("h1")
headline = get_text("div.text-body-medium")
location = get_text("span.text-body-small.inline.t-black--light")
about = get_text("div.full-width.t-14.t-normal.t-black.display-flex.align-items-center")


followers = "NA"
connections = "NA"
stats = soup.find_all("span", class_="t-bold")
if len(stats) >= 2:
    connections = stats[0].text
    followers = stats[1].text

# --- Recent Post Count ---
driver.get(profile_url + "recent-activity/shares/")
time.sleep(5)
post_soup = BeautifulSoup(driver.page_source, "html.parser")
posts = post_soup.find_all("div", class_="feed-shared-update-v2")
post_count = len(posts)

print("\n------ LINKEDIN SUMMARY ------\n")
print("Name:", name)
print("Headline:", headline)
print("About:", about)
print("Location:", location)
print("Followers:", followers)
print("Connections:", connections)
print("Recent Posts:", post_count)

# --- PDF Export ---
styles = getSampleStyleSheet()
doc = SimpleDocTemplate("linkedin_summary.pdf")

story = []
story.append(Paragraph(f"<b>Name:</b> {name}", styles["BodyText"]))
story.append(Spacer(1, 6))
story.append(Paragraph(f"<b>Headline:</b> {headline}", styles["BodyText"]))
story.append(Spacer(1, 6))
story.append(Paragraph(f"<b>Location:</b> {location}", styles["BodyText"]))
story.append(Spacer(1, 6))
story.append(Paragraph(f"<b>Followers:</b> {followers}", styles["BodyText"]))
story.append(Spacer(1, 6))
story.append(Paragraph(f"<b>Connections:</b> {connections}", styles["BodyText"]))
story.append(Spacer(1, 6))
story.append(Paragraph(f"<b>Recent Posts:</b> {post_count}", styles["BodyText"]))

doc.build(story)

print("\nPDF Generated → linkedin_summary.pdf")

driver.quit()
