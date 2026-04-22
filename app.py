"""Vercel entrypoint.

This module exposes the Flask app object for serverless runtimes.
"""

from main import app

# Some runtimes look for `handler` by convention.
handler = app
