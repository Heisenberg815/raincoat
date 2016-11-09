try:
    import xmlrpc.client as xmlrpc_client
except ImportError:
    # Python2
    import xmlrpclib

from raincoat.match import Checker, NotMatching
from raincoat.match import Match


class DjangoChecker(Checker):

    @staticmethod
    def ticket_key(match):
        return match.ticket

    def check(matches):
        for ticket, matches in groupby(
                sorted(matches, key=ticket_key), ticket_key):
            pass


class DjangoMatch(Match):
    checker = DjangoChecker
    match_type = "django"

    def __init__(self, filename, lineno, ticket):
        super(DjangoMatch, self).__init__(filename, lineno)
        try:
            self.ticket = int(ticket.strip())
        except TypeError:
            raise NotMatching

    def __str__(self):
        return (
            "Match Django ticket #{match.ticket} "
            "{match._str_partial}".format(match=self))
