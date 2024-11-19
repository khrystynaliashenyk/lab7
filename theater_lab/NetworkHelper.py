import requests

class NetworkHelper:
    BASE_URL = "http://127.0.0.1:8000/theater/"

    @staticmethod
    def get_list(endpoint):
        """Отримує список об'єктів з REST API."""
        response = requests.get(f"{NetworkHelper.BASE_URL}{endpoint}/")
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                print("Error: Response is not valid JSON.")
                return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    @staticmethod
    def get_item(endpoint, item_id):
        """Отримує один елемент за його ID з REST API."""
        response = requests.get(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/")
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def delete_item(endpoint, item_id):
        """Видаляє елемент за його ID з REST API."""
        response = requests.delete(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/")
        return response.status_code == 204

    @staticmethod
    def create_item(endpoint, data):
        """Створює новий елемент в REST API."""
        response = requests.post(f"{NetworkHelper.BASE_URL}{endpoint}/", data=data)
        return response.status_code == 201

    @staticmethod
    def update_item(endpoint, item_id, data):
        """Оновлює елемент за його ID в REST API."""
        response = requests.put(f"{NetworkHelper.BASE_URL}{endpoint}/{item_id}/", data=data)
        return response.status_code == 200

