def get_coordinate(record):
   return record[1]

    


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    #l1=str(coordinate[0])
    #l2=str(coordinate[1])

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return azara_record[1] == "".join(rui_record[1])



def create_record(azara_record, rui_record):
    treasure, azara_coordinate = azara_record
    location, rui_coordinate, quadrant = rui_record

    # Convert Rui coordinate tuple into string
    rui_coordinate_str = "".join(rui_coordinate)

    if azara_coordinate == rui_coordinate_str:
        return (treasure, azara_coordinate, location, rui_coordinate, quadrant)
    else:
        return "not a match"

   


def clean_up(combined_record_group):
   
    cleaned = []

    for record in combined_record_group:
        treasure = record[0]
        location = record[2]
        coordinate_tuple = record[3]
        quadrant = record[4]

        cleaned_record = (treasure, location, coordinate_tuple, quadrant)
        cleaned.append(str(cleaned_record))

    return "\n".join(cleaned) + "\n"
  
