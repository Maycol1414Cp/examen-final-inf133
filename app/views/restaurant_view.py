def render_restaurant_list(restaurants):
    return [render_restaurant(restaurants) for restaurant in restaurants]
def render_restaurant(reservation):
    return {
        "id": reservation.id,
        "name": reservation.name,
        "description": reservation.description,
        "price": reservation.price,
        "stock": reservation.stock,
    }