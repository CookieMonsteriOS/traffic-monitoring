# IP Address and Traffic Monitoring Script

This Python script is designed to monitor incoming network traffic, extract source IP addresses, and log them to a SQLite database. It utilizes the `pcapy` library for packet capturing and `sqlite3` for database operations.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.x
- pcapy library (`pip install pcapy`)
- SQLite3 library (should come pre-installed with Python)

## Usage

1. Clone or download the repository to your local machine.
2. Modify the script (`traffic_monitor.py`) to replace `'eth0'` with your actual network interface.
3. Run the script using the following command:


## Configuration

- To change the network interface being monitored, modify the `'eth0'` parameter in the `main()` function of `traffic_monitor.py`.
- The script captures only IP packets. If you need to capture other types of packets, adjust the packet filter accordingly (`cap.setfilter('ip')`).
- By default, captured IP addresses are logged to a SQLite database named `traffic_log.db`. You can modify the database name or path in the script if needed.

## Database Schema

The database schema consists of a single table `traffic_log` with the following columns:

1. `id` (INTEGER): Primary key for each log entry.
2. `ip_address` (TEXT): Source IP address of the captured packet.
3. `timestamp` (TIMESTAMP): Timestamp when the packet was captured.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script is based on the `pcapy` library for packet capturing and `sqlite3` for database operations.

