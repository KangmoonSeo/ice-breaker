import os
import requests


def scrape_linked_profile(linkedin_profile_url: str):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile.
    """
    proxycurl_api_key = os.environ.get("PROXYCURL_API_KEY")

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer {proxycurl_api_key}"}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()

    # 데이터 정리
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
