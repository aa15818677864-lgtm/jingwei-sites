"""Render the October 24 20-story batch using the established site template."""
from __future__ import annotations
import publish_daily_20261023 as publisher

ROOT = publisher.ROOT
publisher.DRAFTS = ROOT / 'content-drafts' / 'daily-20261024'
publisher.DATE = '2026-10-23'  # Actual first publication; batch directory is an identifier.
publisher.OUT = ROOT / 'content-system' / 'daily-publication-log-20261024.json'

if __name__ == '__main__':
    publisher.main()
