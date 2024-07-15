from utils.http_methods import Http_methods

base_url = "https://rahulshettyacademy.com"
key = "key=qaclick123"

class Google_maps_api():

    @staticmethod
    def create_place():
        """Создание локации"""
        json_for_create_place = {
            "location": {
            "lat": -52.007007,
            "lng": 52.000052
            }, "accuracy": 10,
            "name": "Default buiding",
            "phone_number": "+79527812000",
            "address": "52, Nevsky avenue, Russia",
            "types": [
            "House",
            "Shoes market", 
            "Bakery"
            ],
            "website": "http://google.com",
            "language": "Russian-RU"
        }
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + "?" + key
        result_post = Http_methods.post(post_url, json_for_create_place)
        return result_post
    
    @staticmethod
    def get_place(place_id):
        """Получение информации о локации"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + "?" + key + "&place_id=" + place_id
        result_get = Http_methods.get(get_url)
        return result_get    

    @staticmethod
    def change_place(place_id):
        """Метод изменения локации"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + "?" + key
        json_for_update = { "place_id": place_id,"address":"101, Gagarina avenue, Russia", "key":"qaclick123"}
        result_put= Http_methods.put(put_url, json_for_update)
        return result_put
    
    @staticmethod
    def delete_place(place_id):
        """Метод удаления локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + "?" + key
        json_for_delete = {"place_id":place_id}
        result_delete = Http_methods.delete(delete_url, json_for_delete)
        return result_delete