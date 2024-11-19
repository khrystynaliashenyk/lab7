from theater_lab.models import Seat

class SeatRepository:
    def get_all(self):
        return Seat.objects.all()

    def get_by_id(self, seat_id):
        return Seat.objects.get(id=seat_id)

    def create(self, seat_number, hall):
        seat = Seat(seat_number=seat_number, hall=hall)
        seat.save()
        return seat