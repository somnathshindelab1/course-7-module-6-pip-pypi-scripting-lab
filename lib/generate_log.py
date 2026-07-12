from datetime import datetime


def generate_log(data):
    """Write log entries to a dated text file and return the filename."""
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    return filename


def fetch_data(url="https://jsonplaceholder.typicode.com/posts/1"):
    """Fetch a sample post from a public API using requests."""
    import requests

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    """Generate a local log file and optionally fetch API data."""
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(log_data)
    print(f"Log written to {filename}")

    try:
        post = fetch_data()
        print("Fetched Post Title:", post.get("title", "No title found"))
    except Exception as exc:
        print(f"Could not fetch API data: {exc}")


if __name__ == "__main__":
    main()
