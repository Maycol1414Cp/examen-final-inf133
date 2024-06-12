def render_reservation_list(reservations):
    return [render_reservation(reservations) for reservation in reservations]
def render_reservation(product):
    return {
        "id": product.id,
        "user_id": product.user_id,
        "restaurant_id": product.restaurant_id,
        "reservation_date": product.reservation_date,
        "num_guests": product.num_guests,
        "special_requests": product.special_requests,
        "status": product.status
    }



