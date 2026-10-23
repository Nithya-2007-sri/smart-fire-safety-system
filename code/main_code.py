# SMART FIRE-SAFETY MONITORING SYSTEM
# Python Simulation

def fire_safety_system():
    print("=" * 45)
    print("   SMART FIRE-SAFETY MONITORING SYSTEM")
    print("=" * 45)

    # Automatic simulated sensor readings
    flame_detected = True
    smoke_detected = True
    temperature = 75.0

    print("\n--- SENSOR STATUS ---")
    print("Flame Sensor  :", "DANGER" if flame_detected else "SAFE")
    print("Smoke Sensor  :", "DANGER" if smoke_detected else "SAFE")
    print("Temperature   :", temperature, "C")

    # Fire verification
    danger_count = sum([
        flame_detected,
        smoke_detected,
        temperature >= 60
    ])

    print("\n--- SYSTEM RESPONSE ---")

    if danger_count >= 2:
        print("FIRE ALERT: VERIFIED")
        print("Electrical isolation: Simulated")
        print("Emergency alarm: Activated (simulation)")
        print("Emergency door release: Requested")
        print("LED evacuation path: Activated (simulation)")
        print("Gas suppression: Not activated")
    elif danger_count == 1:
        print("WARNING: Possible fire detected")
        print("Further inspection required")
    else:
        print("STATUS: SAFE")
        print("No simulated danger detected")

    print("\n" + "=" * 45)
    print("Simulation completed successfully.")
    print("This program does not control real equipment.")
    print("=" * 45)


if __name__ == "__main__":
    fire_safety_system()
