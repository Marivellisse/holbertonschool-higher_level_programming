def generate_invitations(template, attendees):
    """
    Generates personalized invitation files based on a string template and a list of attendee dictionaries.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Returns:
        None
    """

    # Input validation
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generate output for each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Copy the original template
        invitation = template

        # Replace placeholders with actual values or "N/A"
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))

        # Write to file
        try:
            with open(f"output_{index}.txt", "w", encoding="utf-8") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Failed to write output_{index}.txt: {e}")

