# Log Analyzer

## Overview

This project is a Python-based log analyzer that detects failed login attempts and identifies suspicious IP addresses.

## Features

* Reads and parses log files
* Counts failed login attempts
* Tracks failed logins by IP address
* Detects suspicious IPs using a configurable threshold
* Identifies the IP with the highest number of failed login attempts
* Generates a security report

## Technologies Used

* Python
* File Handling
* Dictionaries
* Loops and Conditional Statements

## Example Log Format

LOGIN_FAILED user=admin ip=192.168.1.10

LOGIN_SUCCESS user=admin ip=192.168.1.10

LOGIN_FAILED user=root ip=10.0.0.5

## Output

The program generates:

* Console alerts
* report.txt containing the security analysis results

## Skills Demonstrated

* Log parsing
* Basic cybersecurity monitoring
* Data analysis using Python
* Rule-based alert generation
