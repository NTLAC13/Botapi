import requests

class ApiClient:
    @staticmethod
    def bio():
        try:
            response = requests.get("https://api.codebazan.ir/bio", timeout=10)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            return f"خطا در دریافت بیو: {e}"

    @staticmethod
    def jok():
        try:
            response = requests.get("https://api.codebazan.ir/jok", timeout=10)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            return f"خطا در دریافت جوک: {e}"

    @staticmethod
    def dan():
        try:
            response = requests.get("https://api.codebazan.ir/danestani", timeout=10)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            return f"خطا در دریافت دانستنی: {e}"


def bio():
    return ApiClient.bio()

def jok():
    return ApiClient.jok()

def dans():
    return ApiClient.dan()
