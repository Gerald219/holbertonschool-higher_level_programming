#!/usr/bin/python3
"""simple invite generator for server side rendering project"""


def generate_invitations(template, attendees):
    """build invite files from a text template and a list of people"""
    # check template type
    if not isinstance(template, str):
        print(
            f"Invalid input: template should be a string, "
            f"got {type(template).__name__}."
        )
        return

    # check that attendees is a list of dicts
    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Invalid input: attendees should be a list of dictionaries.")
        return

    # empty template -> nothing to do
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # no people -> nothing to write
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # keys we expect
    keys = ("name", "event_title", "event_date", "event_location")

    # loop over each person and write one file per person
    for index, attendee in enumerate(attendees, start=1):
        values = {}
        for key in keys:
            raw_value = attendee.get(key)
            # missing or None -> use N/A
            if raw_value is None or raw_value == "":
                values[key] = "N/A"
            else:
                values[key] = str(raw_value)

        content = template
        # plain string replace for each placeholder
        for key, value in values.items():
            content = content.replace("{" + key + "}", value)

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError:
            # failed write for this file only
            print(f"Error: could not write file {filename}.")
