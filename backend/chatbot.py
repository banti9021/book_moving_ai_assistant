from backend.database import save_booking
from backend.quote import calculate_distance, calculate_quote


sessions = {}


def create_session(session_id):

    sessions[session_id] = {
        "step": "pickup",

        "pickup_address": None,

        "dropoff_address": None,

        "moving_date": None,

        "moving_time": None,

        "name": None,

        "phone": None,

        "email": None,

        "distance": None,

        "quote": None
    }


def get_bot_response(session_id, message):

    message = message.strip()

    # New user
    if session_id not in sessions:

        create_session(session_id)


    session = sessions[session_id]


    # -------------------------
    # CHANGE ADDRESS
    # -------------------------

    if message.lower().startswith("change pickup"):

        session["step"] = "change_pickup"

        return "Sure 👍 Please provide the new pickup address."


    if message.lower().startswith("change dropoff"):

        session["step"] = "change_dropoff"

        return "Sure 👍 Please provide the new drop-off address."


    # -------------------------
    # CHANGE PICKUP
    # -------------------------

    if session["step"] == "change_pickup":

        session["pickup_address"] = message

        # Recalculate distance

        if session["dropoff_address"]:

            distance = calculate_distance(
                session["pickup_address"],
                session["dropoff_address"]
            )

            quote = calculate_quote(distance)

            session["distance"] = distance

            session["quote"] = quote

            session["step"] = "complete"

            return (
                "Pickup address updated successfully. ✅\n\n"
                f"New estimated quote: ${quote}"
            )

        session["step"] = "dropoff"

        return "Great! What is your drop-off address?"


    # -------------------------
    # CHANGE DROPOFF
    # -------------------------

    if session["step"] == "change_dropoff":

        session["dropoff_address"] = message

        if session["pickup_address"]:

            distance = calculate_distance(
                session["pickup_address"],
                session["dropoff_address"]
            )

            quote = calculate_quote(distance)

            session["distance"] = distance

            session["quote"] = quote

            session["step"] = "complete"

            return (
                "Drop-off address updated successfully. ✅\n\n"
                f"New estimated quote: ${quote}"
            )

        session["step"] = "date"

        return "Perfect! 📅 What date would you like to move?"


    # -------------------------
    # PICKUP
    # -------------------------

    if session["step"] == "pickup":

        session["pickup_address"] = message

        session["step"] = "dropoff"

        return "Great! 👍 What is your drop-off address?"


    # -------------------------
    # DROPOFF
    # -------------------------

    if session["step"] == "dropoff":

        session["dropoff_address"] = message

        # Calculate distance

        distance = calculate_distance(
            session["pickup_address"],
            session["dropoff_address"]
        )

        # Calculate quote

        quote = calculate_quote(distance)

        session["distance"] = distance

        session["quote"] = quote

        session["step"] = "date"

        return (
            f"Perfect! 📍\n\n"
            f"Estimated distance: {distance} miles\n"
            f"Current estimated quote: ${quote}\n\n"
            f"📅 What date would you like to move?"
        )


    # -------------------------
    # DATE
    # -------------------------

    if session["step"] == "date":

        session["moving_date"] = message

        session["step"] = "time"

        return "What time would you prefer for the move?"


    # -------------------------
    # TIME
    # -------------------------

    if session["step"] == "time":

        session["moving_time"] = message

        session["step"] = "name"

        return "Great! What is your name?"


    # -------------------------
    # NAME
    # -------------------------

    if session["step"] == "name":

        session["name"] = message

        session["step"] = "phone"

        return "Thanks! 📱 What is your phone number?"


    # -------------------------
    # PHONE
    # -------------------------

    if session["step"] == "phone":

        session["phone"] = message

        session["step"] = "email"

        return "Almost done! 📧 What is your email address?"


    # -------------------------
    # EMAIL
    # -------------------------

    if session["step"] == "email":

        session["email"] = message

        booking_id = save_booking(
            name=session["name"],
            phone=session["phone"],
            email=session["email"],
            pickup_address=session["pickup_address"],
            dropoff_address=session["dropoff_address"],
            moving_date=session["moving_date"],
            moving_time=session["moving_time"],
            quote=session["quote"]
        )

        session["step"] = "complete"

        return (
            f"Thank you, {session['name']}! 🎉\n\n"
            f"Estimated moving distance: "
            f"{session['distance']} miles\n\n"
            f"Your instant quote: "
            f"${session['quote']}\n\n"
            f"Booking ID: {booking_id}\n\n"
            f"Status: Pending Confirmation."
        )


    # -------------------------
    # COMPLETE
    # -------------------------

    if session["step"] == "complete":

        return (
            "Your booking has already been submitted. "
            "Our team will confirm it shortly. 😊"
        )


    return "Sorry, I didn't understand that."