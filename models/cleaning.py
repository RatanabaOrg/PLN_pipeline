import re
from bs4 import BeautifulSoup
from .web_scrapping import scrap

def get_rid_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe','script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]','\n',stripped_text)
    reviews = stripped_text[stripped_text.find("Top reviews from United Kingdom"):]
    review_beginning = reviews.find("Verified Purchase")+17
    review_ending = reviews.find("Read more")
    review = reviews[review_beginning:review_ending]
    return review

# url = "https://www.amazon.co.uk/dp/B0CGVTJ583/ref=sspa_dk_detail_4?pd_rd_i=B0CGVTJ583&pd_rd_w=j8DH0&content-id=amzn1.sym.6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_p=6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_r=TD9BS15D1F72TTW87YB5&pd_rd_wg=aOTnF&pd_rd_r=1d4023ee-f894-487e-a3a7-2fbc25172bd0&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1"
# review = get_rid_html_tags(scrap(url))
# print(review)

# https://www.amazon.co.uk/dp/B0CGVTJ583/ref=sspa_dk_detail_4?pd_rd_i=B0CGVTJ583&pd_rd_w=j8DH0&content-id=amzn1.sym.6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_p=6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_r=TD9BS15D1F72TTW87YB5&pd_rd_wg=aOTnF&pd_rd_r=1d4023ee-f894-487e-a3a7-2fbc25172bd0&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1