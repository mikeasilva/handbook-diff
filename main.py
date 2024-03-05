import requests
from markdownify import markdownify as md
from bs4 import BeautifulSoup

urls = [
    "https://www.churchofjesuschrist.org/study/manual/general-handbook?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/1-work-of-salvation-and-exaltation?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/2-supporting-individuals-and-families?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/3-priesthood-principles?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/4-leadership-in-the-church-of-jesus-christ?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/5-general-and-area-leadership?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/6-stake-leadership?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/7?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/8-elders-quorum?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/9-relief-society?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/10-aaronic-priesthood?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/11-young-women?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/12-primary?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/13-sunday-school?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/14-single-members?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/15-seminaries-and-institutes?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/16-living-the-gospel?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/17-teaching-the-gospel?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/18-priesthood-ordinances-and-blessings?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/19-music?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/20-activities?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/21-ministering?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/22-providing-for-temporal-needs?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/23?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/24?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/25-temple-and-family-history-work?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/26-temple-recommends?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/27-temple-ordinances-for-the-living?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/28?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/29-meetings-in-the-church?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/30-callings-in-the-church?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/31?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/32-repentance-and-membership-councils?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/33-records-and-reports?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/34-finances-and-audits?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/35?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/36-creating-changing-and-naming-new-units?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/37-specialized-stakes-wards-and-branches?lang=eng",
    "https://www.churchofjesuschrist.org/study/manual/general-handbook/38-church-policies-and-guidelines?lang=eng",
]


for url in urls:
    print(url)
    # Pull the url
    response = requests.get(url)
    # Parse the content
    soup = BeautifulSoup(response.content, "html.parser")
    # Select the page
    page = soup.find(attrs={"id": "page"})
    # Select text in the article tag
    article = page.find("article")
    # Convert html to markdown
    text = md(str(article))
    # Strip out extra new lines and white space
    clean_text = "\n".join([s for s in text.strip().splitlines(True) if s.strip()])
    # Get the file name from the url
    file_name = url.split("/")[-1].split("?")[0]
    # Save the markdown text
    with open(f"./markdown/{file_name}.md", "w", encoding="utf-8") as f:
        f.write(clean_text)
