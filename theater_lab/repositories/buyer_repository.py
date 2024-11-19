from theater_lab.models import Buyer

class BuyerRepository:
    def get_all(self):
        return Buyer.objects.all()

    def get_by_id(self, buyer_id):
        return Buyer.objects.get(id=buyer_id)

    def create(self, first_name, last_name, email):
        buyer = Buyer(first_name=first_name, last_name=last_name, email=email)
        buyer.save()
        return buyer