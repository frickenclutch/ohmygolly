import base64
import platform
from datetime import datetime

def print_banner():
    print("🔐 Booting Codex Protocol...")
    print(f"🕰️  Timestamp: {datetime.utcnow().isoformat()}Z")
    print("🧬 Codex Base64 Ping:", base64.b64encode(b"DEEP_FV_READY").decode())

def decode_value():
    encoded = "RGVlcCBGdWNraW5nIFZhbHVlIGlzIHJlYWwu"  # Base64 for "Deep Fucking Value is real."
    decoded = base64.b64decode(encoded).decode()
    print("📜 Codex Message:", decoded)

def system_check():
    print("\n🔍 System Diagnostics:")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Python Version:", platform.python_version())

def launch_payload():
    print("\n🚀 Executing DFV Modules...")
    bags = ["GME", "BTC", "Your Soul"]
    for b in bags:
        print(f"[📦 Holding Bag] {b.upper()}")
    print("\n🧾 Codex Ritual Complete.")

if __name__ == "__main__":
    print_banner()
    decode_value()
    system_check()
    launch_payload()
