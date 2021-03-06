import datetime
import logging
import time
from optparse import OptionParser

from django.contrib.sessions.models import Session
from django.core.management.base import CommandError, LabelCommand

import maintenance.api as api

logger = logging.getLogger("maintenance")


class Command(LabelCommand):
    opts = ("on", "off", "check", "list", "activate", "deactivate", "status")

    options_parser = OptionParser()
    options_parser.add_option(
        "--force",
        action="store_true",
        dest="ignore_session",
        default=False,
        help="Do not wait for active session. Brutally disconnect users",
    )
    options_parser.add_option(
        "--timeout",
        action="store",
        dest="timeout",
        default=60,
        help="Time to wait for pending sessions",
    )

    args = "|".join(opts)
    label = "command"
    help = """ """

    def handle_default_options(self):
        pass

    def handle_label(self, cmd, **options):
        verbosity = options.get("verbosity")
        timeout = options.get("timeout")
        ignore_session = options.get("ignore_session")
        ret, msg = 0, "Unknow error"
        if cmd not in Command.args:
            raise CommandError(f"Allowed options are: {self.args}")

        if cmd in ("check", "status"):
            ret, msg = api.check()
            print(msg)
        elif cmd in ("on", "activate"):
            ret, msg = api.start(ignore_session, timeout, verbosity)
            if verbosity >= 1:
                print(msg)
        elif cmd in ("off", "deactivate"):
            ret, msg = api.stop()
            if verbosity >= 1:
                print(msg)
        elif cmd in ("list",):
            now = datetime.datetime.now()
            for s in Session.objects.filter(expire_date__gte=now):
                offset = time.mktime(s.expire_date.timetuple()) - time.mktime(
                    now.timetuple()
                )
                print(s.pk, s.expire_date, offset)
        if ret:
            raise CommandError(msg)
