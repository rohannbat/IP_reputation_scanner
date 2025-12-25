# IP Check

A Python tool to check IP address reputation using the AbuseIPDB API. This script helps you quickly determine if an IP address has been reported for malicious activity.

## Features

- Check IP reputation against AbuseIPDB database
- **Single IP mode**: Check individual IP addresses
- **Bulk mode**: Check multiple IP addresses from a text file
- View detailed information including ISP, country, and abuse confidence score
- Check last 120 days of history
- Simple command-line interface
- Secure API key management using environment variables

## Prerequisites

- Python 3.6 or higher
- An AbuseIPDB API key ([Get one here](https://www.abuseipdb.com/pricing))

## Installation

1. Clone or download this repository:
   ```bash
   cd IP_check
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirments.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory:
   ```bash
   touch .env
   ```

2. Add your AbuseIPDB API key to the `.env` file:
   ```
   API_KEY=your_api_key_here
   ```

   **Note:** Make sure `.env` is in your `.gitignore` file to keep your API key secure.

## Usage

The script supports two modes: **Single IP mode** and **Bulk mode**.

### Single IP Mode

Check a single IP address by passing it as an argument:

```bash
python ip_check.py <IP_ADDRESS>
```

**Example:**
```bash
python ip_check.py 192.168.1.1
```

### Bulk Mode

Check multiple IP addresses by providing a text file containing one IP address per line:

```bash
python ip_check.py <FILENAME.txt>
```

**Example:**
```bash
python ip_check.py ip_list.txt
```

**File Format:**
Create a text file with one IP address per line:
```
192.168.1.1
10.0.0.1
172.16.0.1
```

Empty lines in the file will be automatically skipped.

### Output

The script will display:
- IP Address
- ISP (Internet Service Provider)
- Country
- Total Reports
- Risk Score (0-100)
- Security status (CLEAN or ALERT)

**Single IP Mode Output:**
```
[*] Single Mode: Checking 192.168.1.1...
[*] Checking IP reputation for 192.168.1.1...

========================================
Report for: 192.168.1.1
========================================
ISP: Example ISP
Country: United States
Total Reports: 0
Risk Score: 0
----------------------------------------
[+] CLEAN: No malicious activity reported.
========================================
```

**Bulk Mode Output:**
```
[*] Bulk Mode: Reading from ip_list.txt...
======================================================================

[*] Checking IP reputation for 192.168.1.1...
========================================
Report for: 192.168.1.1
========================================
...

[*] Checking IP reputation for 10.0.0.1...
========================================
Report for: 10.0.0.1
========================================
...

======================================================================
[*] Scan Complete.
```

## Dependencies

- `requests` - For making HTTP requests to the AbuseIPDB API
- `python-dotenv` - For loading environment variables from `.env` file

## Error Handling

The script handles various error scenarios:
- Missing API key
- Authentication failures (401)
- Rate limiting (429)
- Network errors
- Invalid API responses

## API Information

This tool uses the [AbuseIPDB API v2](https://www.abuseipdb.com/api). The check looks at the last 120 days of history and provides a confidence score from 0-100, where:
- **0**: No reports (clean)
- **1-100**: Confidence level that the IP is malicious (higher = more confident)

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key secure and private
- Be aware of API rate limits based on your AbuseIPDB plan

## License

This project is open source and available for personal use.

