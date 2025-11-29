from pprint import pprint
import os
import xmltodict
import json

def micros_to_laptime(micros):
    total_seconds = float(micros)/1_000_000
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:06.3f}" #MM:SS.mmm racing lap format

def trim_xml_dict(xml_dict):

    layers = xml_dict["LDXFile"]["Layers"] 

    details = layers["Details"]["String"] #works!(must keep string)
    session_info = {
        item["@Id"]: item["@Value"]
        for item in details
    }
    
    layer_list = layers["Layer"]["MarkerBlock"]["MarkerGroup"]["Marker"]
    layer_list_sorted = sorted(
        layer_list, 
        key=lambda x: int(x["@Name"].split(".")[1])
    )

    lap_data = []
    previous_time = 0
    for item in layer_list_sorted:
        current_time = float(item["@Time"])
        lap_delta = current_time - previous_time
        previous_time = current_time
        lap_data.append({
            "lap_name": item["@Name"], 
            "lap_time": micros_to_laptime(lap_delta)
        })
    return {
        "session_info": session_info, 
        "lap_data": lap_data
    }


with open(os.path.dirname(__file__) + '/XMLTestData/data.xml') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
parsed_data = trim_xml_dict(data_dict)
pprint(parsed_data)
print("done without errors?")

