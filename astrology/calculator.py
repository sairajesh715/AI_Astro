"""
Astrology calculator using Kerykeion (Swiss Ephemeris based).
No external API keys required.
"""
from kerykeion import AstrologicalSubject, KerykeionChartSVG
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import pytz
from datetime import datetime
import re


ZODIAC_EMOJIS = {
    "Ari": "♈", "Tau": "♉", "Gem": "♊", "Can": "♋",
    "Leo": "♌", "Vir": "♍", "Lib": "♎", "Sco": "♏",
    "Sag": "♐", "Cap": "♑", "Aqu": "♒", "Pis": "♓"
}

ZODIAC_FULL = {
    "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
    "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
    "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
}

PLANET_EMOJIS = {
    "Sun": "☀️", "Moon": "🌙", "Mercury": "☿", "Venus": "♀",
    "Mars": "♂", "Jupiter": "♃", "Saturn": "♄", "Uranus": "⛢",
    "Neptune": "♆", "Pluto": "♇", "True_Node": "☊", "Chiron": "⚷"
}

PLANET_NAMES = {
    "Sun": "Sun", "Moon": "Moon", "Mercury": "Mercury", "Venus": "Venus",
    "Mars": "Mars", "Jupiter": "Jupiter", "Saturn": "Saturn",
    "Uranus": "Uranus", "Neptune": "Neptune", "Pluto": "Pluto",
    "True_Node": "North Node", "Chiron": "Chiron"
}

ELEMENTS = {
    "Ari": "Fire", "Leo": "Fire", "Sag": "Fire",
    "Tau": "Earth", "Vir": "Earth", "Cap": "Earth",
    "Gem": "Air", "Lib": "Air", "Aqu": "Air",
    "Can": "Water", "Sco": "Water", "Pis": "Water"
}

MODALITIES = {
    "Ari": "Cardinal", "Can": "Cardinal", "Lib": "Cardinal", "Cap": "Cardinal",
    "Tau": "Fixed", "Leo": "Fixed", "Sco": "Fixed", "Aqu": "Fixed",
    "Gem": "Mutable", "Vir": "Mutable", "Sag": "Mutable", "Pis": "Mutable"
}


def geocode_location(place_name: str) -> dict | None:
    """Geocode a place name to latitude, longitude, and timezone."""
    try:
        geolocator = Nominatim(user_agent="astrology_app_v1", timeout=10)
        location = geolocator.geocode(place_name, exactly_one=True, language="en")
        if not location:
            return None

        lat = location.latitude
        lon = location.longitude

        # Determine timezone from coordinates using timezonefinder if available
        try:
            from timezonefinder import TimezoneFinder
            tf = TimezoneFinder()
            tz_name = tf.timezone_at(lat=lat, lng=lon)
        except ImportError:
            # Fallback: rough timezone from longitude
            offset_hours = round(lon / 15)
            tz_name = f"Etc/GMT{-offset_hours:+d}" if offset_hours != 0 else "UTC"

        return {
            "name": location.address,
            "lat": lat,
            "lon": lon,
            "timezone": tz_name or "UTC"
        }
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        return None


def calculate_chart(name: str, dob: str, birth_time: str, birth_place: str) -> dict:
    """
    Calculate astrological chart from birth data.

    Args:
        name: Full name of the person
        dob: Date of birth as 'YYYY-MM-DD'
        birth_time: Time of birth as 'HH:MM'
        birth_place: City/place of birth

    Returns:
        Dictionary with chart data or error info
    """
    # Geocode birth place
    location_data = geocode_location(birth_place)
    if not location_data:
        return {"error": f"Could not find location: '{birth_place}'. Please try a more specific city name."}

    try:
        # Parse date and time
        date_parts = dob.split("-")
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])

        time_parts = birth_time.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1])

        lat = location_data["lat"]
        lon = location_data["lon"]
        tz_name = location_data["timezone"]

        # Create astrological subject
        subject = AstrologicalSubject(
            name=name,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            city=birth_place,
            lat=lat,
            lng=lon,
            tz_str=tz_name,
            zodiac_type="Tropic",
            online=False
        )

        # Extract planetary data
        planets = {}
        planet_keys = ["sun", "moon", "mercury", "venus", "mars",
                       "jupiter", "saturn", "uranus", "neptune", "pluto",
                       "true_node", "chiron"]

        for key in planet_keys:
            try:
                planet = getattr(subject, key)
                sign_short = planet.sign
                display_name = PLANET_NAMES.get(planet.name, planet.name)
                planets[display_name] = {
                    "sign": ZODIAC_FULL.get(sign_short, sign_short),
                    "sign_short": sign_short,
                    "degree": round(planet.position, 2),
                    "house": planet.house_name if hasattr(planet, 'house_name') else "",
                    "emoji": PLANET_EMOJIS.get(planet.name, "★"),
                    "element": ELEMENTS.get(sign_short, ""),
                    "modality": MODALITIES.get(sign_short, ""),
                    "retrograde": planet.retrograde if hasattr(planet, 'retrograde') else False
                }
            except Exception:
                continue

        # Extract house data
        houses = {}
        house_attrs = [f"first_house", "second_house", "third_house", "fourth_house",
                       "fifth_house", "sixth_house", "seventh_house", "eighth_house",
                       "ninth_house", "tenth_house", "eleventh_house", "twelfth_house"]
        house_nums = ["1st", "2nd", "3rd", "4th", "5th", "6th",
                      "7th", "8th", "9th", "10th", "11th", "12th"]

        for i, attr in enumerate(house_attrs):
            try:
                house = getattr(subject, attr)
                sign_short = house.sign
                houses[house_nums[i]] = {
                    "sign": ZODIAC_FULL.get(sign_short, sign_short),
                    "sign_short": sign_short,
                    "degree": round(house.position, 2),
                    "emoji": ZODIAC_EMOJIS.get(sign_short, ""),
                }
            except Exception:
                continue

        # Get key placements
        sun_sign_short = planets.get("Sun", {}).get("sign_short", "")
        moon_sign_short = planets.get("Moon", {}).get("sign_short", "")
        rising_sign_short = houses.get("1st", {}).get("sign_short", "")

        return {
            "success": True,
            "name": name,
            "dob": dob,
            "birth_time": birth_time,
            "birth_place": birth_place,
            "location_resolved": location_data["name"],
            "lat": lat,
            "lon": lon,
            "timezone": tz_name,
            "sun_sign": ZODIAC_FULL.get(sun_sign_short, ""),
            "moon_sign": ZODIAC_FULL.get(moon_sign_short, ""),
            "rising_sign": ZODIAC_FULL.get(rising_sign_short, ""),
            "sun_sign_short": sun_sign_short,
            "moon_sign_short": moon_sign_short,
            "rising_sign_short": rising_sign_short,
            "planets": planets,
            "houses": houses,
        }

    except Exception as e:
        return {"error": f"Chart calculation failed: {str(e)}"}
