import asyncio
import random
import time


async def fetch_flights():
    print("✈ Fetching flight details...")
    await asyncio.sleep(random.randint(2, 4))
    return {
        "airline": "Air India",
        "price": 6500
    }


async def fetch_hotels():
    print("🏨 Fetching hotel details...")
    await asyncio.sleep(random.randint(2, 4))
    return {
        "hotel": "Taj Hotel",
        "price": 4500
    }


async def fetch_cabs():
    print("🚕 Fetching cab availability...")
    await asyncio.sleep(random.randint(2, 4))
    return {
        "cab": "Uber",
        "fare": 850
    }


async def fetch_weather():
    print("🌤 Fetching weather forecast...")
    await asyncio.sleep(random.randint(2, 4))
    return {
        "temperature": "28°C",
        "condition": "Sunny"
    }


async def plan_trip():

    print("=" * 50)
    print("Planning your trip...")
    print("=" * 50)

    start = time.perf_counter()

    # Run all API calls concurrently
    flight, hotel, cab, weather = await asyncio.gather(
        fetch_flights(),
        fetch_hotels(),
        fetch_cabs(),
        fetch_weather()
    )

    end = time.perf_counter()

    print("\n=========== Trip Summary ===========")

    print(f"Flight : {flight['airline']} (₹{flight['price']})")
    print(f"Hotel  : {hotel['hotel']} (₹{hotel['price']})")
    print(f"Cab    : {cab['cab']} (₹{cab['fare']})")
    print(f"Weather: {weather['temperature']} - {weather['condition']}")

    print("\nTotal Time Taken : {:.2f} seconds".format(end - start))


if __name__ == "__main__":
    asyncio.run(plan_trip())