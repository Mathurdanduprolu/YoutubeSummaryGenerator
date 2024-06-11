import os
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.dirname(__file__))

try:
    from django.core.wsgi import get_wsgi_application
except Exception as e:
    logging.error("WSGI Import Error: %s", e)
    raise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_transcript_GPT_summary.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    logging.error("WSGI Application Error: %s", e)
    raise
