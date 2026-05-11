def traffic_light_controller(current_signal: str, is_emergency_vehicle_approaching: bool) -> str:
    """
    Controls traffic light output based on current signal and emergency status.

    Args:
        current_signal (str): The current traffic signal - "RED", "YELLOW", or "GREEN".
        is_emergency_vehicle_approaching (bool): True if an emergency vehicle is approaching.

    Returns:
        str: The appropriate traffic instruction.
    """
    if is_emergency_vehicle_approaching:
        return "IMMEDIATE GREEN"

    match current_signal:
        case "RED":
            return "STOP"
        case "YELLOW":
            return "PREPARE TO STOP"
        case "GREEN":
            return "GO"
        case _:
            return "INVALID SIGNAL"


# --- Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("RED",    False),
        ("YELLOW", False),
        ("GREEN",  False),
        ("RED",    True),
        ("YELLOW", True),
        ("GREEN",  True),
        ("BLUE",   False),
        ("",       False),
    ]

    print("=" * 60)
    print("       SMART TRAFFIC LIGHT SYSTEM - TEST RESULTS")
    print("=" * 60)

    for signal, emergency in test_cases:
        result = traffic_light_controller(signal, emergency)
        print(f"Signal: {signal!r:8} | Emergency: {str(emergency):5} | Output: {result}")

    print("=" * 60)
