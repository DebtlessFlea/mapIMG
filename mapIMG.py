import os
import webbrowser
from geopy.geocoders import Nominatim
import folium
from folium import DivIcon

def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="FLocation")
    location = geolocator.geocode(place_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def create_map(coords, place_name, filename):
    fmap = folium.Map(location=coords, zoom_start=13)

    folium.Marker(
        location=coords,
        icon=DivIcon(
            icon_size=(20, 20),
            icon_anchor=(10, 10),
            html="""
                <div style="
                    background-color: red;
                    width: 16px;
                    height: 16px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    <div style="
                        background-color: white;
                        width: 6px;
                        height: 6px;
                        border-radius: 50%;
                    "></div>
                </div>
            """
        )
    ).add_to(fmap)

    fmap.save(filename)

def main():
    place_name = input("Enter the name of a place: ")
    coords = get_coordinates(place_name)

    if coords:
        script_path = os.path.dirname(os.path.abspath(__file__))
        map_path = os.path.join(script_path, "location.html")
        create_map(coords, place_name, map_path)
        print(f"Map created successfully at: {map_path}")

        webbrowser.open(f"file://{map_path}")
    else:
        print("Location not found. Please try another place name.")

if __name__ == "__main__":
    main()
