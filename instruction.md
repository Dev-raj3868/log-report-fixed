# Task

Analyze the Apache access log in the working directory and generate a JSON summary of the traffic.

## Input

- Input file: `access.log`
- Location: `./access.log`
- Format: Apache HTTP access log containing one HTTP request per line.

## Output

- Output file: `report.json`
- Location: `.app/report.json`
- Output format: JSON
- The JSON object must contain the following fields:
  - `total_requests` (integer): Total number of HTTP requests.
  - `clients` (array): Unique client IP addresses that made requests.
  - `popular_pages` (array): Pages ordered by request count in descending order. Each element must contain:
    - `page` (string): Requested page path.
    - `request_count` (integer): Number of requests for that page.

## Success Criteria

1. Read `./access.log` successfully.
2. Analyze every request in the log.
3. Produce `./report.json`.
4. Include all required JSON fields.
5. Compute all values from the input log.
6. Produce valid JSON.

## Constraints

- Do not modify `access.log`.
- Do not require network access.
- Only create `report.json`.