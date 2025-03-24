import psutil
import time

def monitor_resources(interval=5):
    """Monitors CPU and memory usage every `interval` seconds."""
    print("📊 Monitoring CPU and Memory usage... (Press Ctrl+C to stop)\n")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent

            print(f"🖥️ CPU Usage: {cpu_usage}% | 🧠 Memory Usage: {memory_usage}%")
            time.sleep(interval - 1)  # Adjust for the CPU check time

    except KeyboardInterrupt:
        print("\n❌ Monitoring stopped.")

# Run the monitoring function
monitor_resources()