def calculate_distance(pickup, dropoff):
    """
    Temporary distance calculator.

    Abhi demo ke liye address length ke basis par
    distance estimate kar rahe hain.
    """

    distance = abs(len(pickup) - len(dropoff)) * 5

    if distance < 10:
        distance = 10

    return distance


def calculate_quote(distance):

    base_charge = 200

    distance_charge = distance * 2

    total = base_charge + distance_charge

    if total < 500:
        total = 500

    return total