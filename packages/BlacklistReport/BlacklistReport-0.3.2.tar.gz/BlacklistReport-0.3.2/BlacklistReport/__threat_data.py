import requests
import logging
from greynoise import GreyNoise


class ThreatData:
    __OPSWAT_KEY = None
    __OPSWAT_URL = "https://api.metadefender.com/v4/ip/"
    __GREYNOISE_KEY = None

    @staticmethod
    def set_opswat_key(opswat_key: str):
        ThreatData.__OPSWAT_KEY = opswat_key

    @staticmethod
    def set_greynoise_key(greynoise_key: str):
        ThreatData.__GREYNOISE_KEY = greynoise_key

    @staticmethod
    def fetch_country(ip: str):
        url = ThreatData.__OPSWAT_URL + ip
        headers = dict(apikey=ThreatData.__OPSWAT_KEY)
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            res = res.json()
            geo_info = res.get('geo_info', {})
            country = geo_info.get('country', {})
            country = country.get('name')
        else:
            country = None
        return country

    @staticmethod
    def fetch_OPSWAT_summary(ip: str) -> str:
        url = ThreatData.__OPSWAT_URL + ip
        headers = {'apikey': ThreatData.__OPSWAT_KEY}
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            res = res.json()
            res = res.get('lookup_results', {})
            detected = res.get('detected_by', 0)
            sources = res.get('sources', [])
            source_labels = []
            for source in sources:
                if source['status'] not in [0, 5]:
                    source_labels.append(source['assessment'])
            summary = f"{detected}/{len(sources)} Score"
            if len(source_labels) > 0:
                summary += " - " + (', '.join(source_labels)).title()
        else:
            logging.warning('Failed to fetch OPSWAT summary for ip {}'.format(ip))
            summary = None
        return summary

    @staticmethod
    def fetch_TALOS_summary(ip: str) -> str:
        url = 'https://talosintelligence.com/sb_api/query_lookup'
        headers = {
            'referer': 'https://talosintelligence.com/reputation_center/lookup?search=%s' % ip,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        params = {
            'query': '/api/v2/details/ip/',
            'query_entry': ip
        }
        res = requests.get(url=url, headers=headers, params=params)
        if res.status_code == 201:
            res_json = res.json()
            email_rep: str = res_json.get('email_score_name', 'Missing')
            web_rep: str = res_json.get('web_score_name', 'Missing')
            summary = f"Email Reputation - {email_rep.upper()}, Web Reputation - {web_rep.upper()}"
        else:
            logging.warning('Failed to fetch Talos summary for ip {}'.format(ip))
            summary = None
        return summary

    @staticmethod
    def fetch_GREYNOISE_summary(ip: str) -> str:
        gn_api_key = GreyNoise(api_key=ThreatData.__GREYNOISE_KEY, timeout=30)
        gn_ip_data = gn_api_key.ip(ip)

        org, classification, tags = '', '', ''
        gn_summary = "No data found"

        if gn_ip_data.get('metadata', {}).get('organization'):
            org = f"Organization - {gn_ip_data['metadata']['organization']}, "
        if gn_ip_data.get('classification') and gn_ip_data['classification'] != 'unknown':
            classification = f"Classification - {gn_ip_data['classification'].upper()}, "
        if gn_ip_data.get('tags'):
            tags = f"Tags - {gn_ip_data['tags']}"
        if gn_ip_data.get('seen', False):
            gn_summary = f"{org}{classification}{tags}"
        return gn_summary
