# pylint:disable=line-too-long
"""
The tool to check the availability or syntax of domains, IPv4 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This submodule will test PyFunceble.check.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.readthedocs.io/en/dev/special-thanks.html

Contributors:
    http://pyfunceble.readthedocs.io/en/dev/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/dev/

Project homepage:
    https://funilrys.github.io/PyFunceble/

License:
::


    MIT License

    Copyright (c) 2017, 2018, 2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
# pylint: enable=line-too-long
# pylint: disable=import-error

from unittest import TestCase
from unittest import main as launch_tests

import PyFunceble
from PyFunceble.check import Check


class TestCheck(TestCase):
    """
    Test PyFunceble.check.Check().
    """

    def setUp(self):
        """
        Setup what we need for the tests.
        """

        PyFunceble.load_config(generate_directory_structure=False)

        self.valid_domain = [
            "_hello_.abuse.co.za.",
            "_hello_.abuse.co.za",
            "_hello_world_.abuse.co.za.",
            "_hello_world_.abuse.co.za",
            "_hello_world_.hello.eu.com.",
            "_hello_world_.hello.eu.com",
            "_hello-beautiful-world_.wold.eu.com.",
            "_hello-beautiful-world_.wold.eu.com",
            "_hello-world.abuse.co.za.",
            "_hello-world.abuse.co.za",
            "_hello._world.abuse.co.za.",
            "_hello._world.abuse.co.za",
            "_hello.abuse.co.za.",
            "_hello.abuse.co.za",
            "_world_.hello.eu.com.",
            "_world_.hello.eu.com",
            "_world.hello.eu.com.",
            "_world.hello.eu.com",
            "hello_.world.eu.com.",
            "hello_.world.eu.com",
            "hello_world.abuse.co.za.",
            "hello_world.abuse.co.za",
            "hello_world.world.com.",
            "hello_world.world.com",
            "hello_world.world.hello.com.",
            "hello_world.world.hello.com",
            "hello---world.com.",
            "hello---world.com",
            "hello-.abuse.co.za.",
            "hello-.abuse.co.za",
            "hello-world.com.",
            "hello-world.com",
            "hello.world_hello.world.com.",
            "hello.world_hello.world.com",
            "hello.world.com.",
            "hello.world.com",
            "hello.world.hello.com.",
            "hello.world.hello.com",
            "pogotowie-komputerowe-warszawa.com.pl",
            "xn--bittr-fsa6124c.com.",
            "xn--bittr-fsa6124c.com",
            "xn--bllogram-g80d.com.",
            "xn--bllogram-g80d.com",
            "xn--coinbse-30c.com.",
            "xn--coinbse-30c.com",
            "xn--cryptopi-ux0d.com.",
            "xn--cryptopi-ux0d.com",
            "xn--cyptopia-4e0d.com.",
            "xn--cyptopia-4e0d.com",
        ]

        self.not_valid_domain = [
            "_world._hello.eu.com",
            "_world.hello_.eu.com",
            "-hello-.abuse.co.za",
            "-hello-world_.abuse.co.za",
            "-hello-world_all-mine_.hello.eu.com",
            "-hello.abuse.co.za",
            "-hello.world",
            "-world.hello",
            "..",
            ".",
            "bịllogram.com",
            "bittréẋ.com",
            "coinbȧse.com",
            "cryptopiạ.com",
            "cṙyptopia.com",
            "hello_world_.com",
            "hello_world.com",
            "hello-.world",
            "hello-world",
            "hello.-hello-world_.abuse.co.za",
            "hello.com:443",
            "hello@world.com",
            "httpWd",
            "test.-hello-world_all-mine_.abuse.co.za",
            "world_hello.com",
            "world-.hello",
            "world-hello",
            "world.hello:80",
            "world@hello.com",
        ]

    def test_is_url(self):
        """
        Test Check.is_url() for the case that the URL is valid.
        """

        expected = True

        for domain in self.valid_domain:
            to_test = "http://{0}/helloworld".format(domain)

            actual = Check(to_test).is_url()

            self.assertEqual(expected, actual)

    def test_is_url_not_valid(self):
        """
        Test Check.is_url() for the case that the URL is not valid.
        """

        expected = False

        for domain in self.not_valid_domain:
            to_check = "https://{0}/hello_world".format(domain)
            actual = Check(to_check).is_url()

            self.assertEqual(expected, actual)

    def test_is_url_protocol_not_supported(self):
        """
        Test Check.is_url() for the case that the
        URL protocol is not supported nor given.
        """

        expected = False

        for domain in self.not_valid_domain:
            to_check = "{0}/hello_world".format(domain)
            actual = Check(to_check).is_url()

            self.assertEqual(expected, actual)

    def test_is_url_get_base(self):
        """
        Test Check.is_url() for the case that we want to
        extract the url base.
        """

        for domain in self.valid_domain:
            to_check = "http://{0}/hello_world".format(domain)
            expected = domain

            actual = Check(to_check).is_url(return_base=True)

            self.assertEqual(expected, actual)

    def test_is_url_get_not_base(self):
        """
        Test Check.is_url() for the case that we want to
        extract the url base for invalid domains.
        """

        expected = False
        PyFunceble.CONFIGURATION["idna_conversion"] = False

        for domain in self.not_valid_domain:
            to_check = "http://{0}/hello_world".format(domain)

            actual = Check(to_check).is_url(return_base=True)

            self.assertEqual(expected, actual)

    def test_is_url_convert_idna(self):
        """
        Test Check().is_url() for the case that
        we have to convert to IDNA.
        """

        PyFunceble.CONFIGURATION["idna_conversion"] = True

        domains_to_test = {
            "bittréẋ.com": "xn--bittr-fsa6124c.com",
            "hello-world.com": "hello-world.com",
            "coinbȧse.com": "xn--coinbse-30c.com",
            "cryptopiạ.com": "xn--cryptopi-ux0d.com",
            "cṙyptopia.com": "xn--cyptopia-4e0d.com",
        }

        for domain, expected_after_conversion in domains_to_test.items():
            expected = "http://{0}/hello_world".format(expected_after_conversion)
            to_check = "http://{0}/hello_world".format(domain)

            actual = Check(to_check).is_url(return_formatted=True)

            self.assertEqual(expected, actual)

    def test_is_url_not_convert_idna(self):
        """
        Test Check().is_url() for the case that
        we do not have to convert to IDNA.
        """

        PyFunceble.CONFIGURATION["idna_conversion"] = False

        domains_to_test = [
            "bittréẋ.com",
            "hello-world.com",
            "coinbȧse.com",
            "cryptopiạ.com",
            "cṙyptopia.com",
        ]

        for domain in domains_to_test:
            to_check = "http://{0}/hello_world".format(domain)
            expected = to_check

            actual = Check(to_check).is_url(return_formatted=True)

            self.assertEqual(expected, actual)

    def test_is_domain(self):
        """
        Test Check().is_domain() for the case that domains
        are valid.
        """

        expected = True

        for domain in self.valid_domain:
            to_check = domain
            actual = Check(to_check).is_domain()

            self.assertEqual(expected, actual, msg="%s is invalid." % domain)

    def test_is_domain_not_valid(self):
        """
        Test Check().is_domain() for the case that
        we meet invalid domains.
        """

        expected = False

        for domain in self.not_valid_domain:
            to_check = domain
            actual = Check(to_check).is_domain()

            self.assertEqual(expected, actual, msg="%s is valid." % domain)

    def test_is_subdomain(self):
        """
        Test Check().is_subdomain() for the case subdomains
        are valid.
        """

        valid = [
            "hello_world.world.com",
            "hello_world.world.hello.com",
            "hello.world_hello.world.com",
            "hello.world.hello.com",
            "hello_.world.eu.com",
            "_world.hello.eu.com",
            "_world_.hello.eu.com",
            "_hello-beautiful-world_.wold.eu.com",
            "_hello_world_.hello.eu.com",
            "_hello.abuse.co.za",
            "_hello_.abuse.co.za",
            "_hello._world.abuse.co.za",
            "_hello-world.abuse.co.za",
            "_hello_world_.abuse.co.za",
            "hello_world.abuse.co.za",
            "hello-.abuse.co.za",
        ]

        expected = True

        for domain in valid:
            to_check = domain
            actual = Check(to_check).is_subdomain()

            self.assertEqual(expected, actual, msg="%s is not a subdomain." % domain)

    def test_is_subdomain_not_valid(self):
        """
        Test Check().is_subdomain() for the case subdomains
        are not valid.
        """

        not_valid = [
            "-hello.world",
            "bịllogram.com",
            "bittréẋ.com",
            "coinbȧse.com",
            "cryptopiạ.com",
            "cṙyptopia.com",
            "google.com",
            "hello_world_.com",
            "hello_world.com",
            "hello-.world",
            "hello-world",
            "pogotowie-komputerowe-warszawa.com.pl",
        ]

        expected = False

        for domain in not_valid:
            to_check = domain
            actual = Check(to_check).is_subdomain()

            self.assertEqual(expected, actual, msg="%s is a subdomain." % domain)

    def test_is_ipv4(self):
        """
        Test Check().is_ipv4() for the case that the IP is valid.
        """

        expected = True
        valid = ["15.47.85.65", "45.66.255.240"]

        for given_ip in valid:
            to_check = given_ip
            actual = Check(to_check).is_ipv4()

            self.assertEqual(expected, actual, msg="%s is invalid." % given_ip)

    def test_is_ipv4_not_valid(self):
        """
        Test Check().is_ipv4() for the case that the IP
        is not valid.
        """

        expected = False
        invalid = ["google.com", "287.468.45.26", "245.85.69.17:8081"]

        for given_ip in invalid:
            to_check = given_ip
            actual = Check(to_check).is_ipv4()

            self.assertEqual(expected, actual, msg="%s is valid." % given_ip)

    def test_is_ipv4_range(self):
        """
        Test Check().is_ipv4_range() for the case that the IP is a range.
        """

        expected = True
        valid = ["255.45.65.0/24", "255.45.65.6/18"]

        for given_ip in valid:
            to_check = given_ip
            actual = Check(to_check).is_ipv4_range()

            self.assertEqual(expected, actual, msg="%s is not an IP range." % given_ip)

    def test_is_ipv4_range_not_valid(self):
        """
        Test Check().is_ip_range() for the case that the IP is not a range.
        """

        expected = False
        valid = ["15.47.85.65", "45.66.255.240", "github.com"]

        for given_ip in valid:
            to_check = given_ip
            actual = Check(to_check).is_ipv4_range()

            self.assertEqual(expected, actual, msg="%s is an IP range." % given_ip)

    def test_is_reserved_ipv4(self):
        """
        Test Check().is_reserved_ipv4().
        """

        reserved = [
            "0.45.23.59",
            "10.39.93.13",
            "100.64.35.85",
            "127.57.91.13",
            "169.254.98.65",
            "172.16.17.200",
            "192.0.0.145",
            "192.0.2.39",
            "192.168.21.99",
            "192.175.48.25",
            "192.31.196.176",
            "192.52.193.245",
            "192.88.99.30",
            "198.18.145.234",
            "198.51.100.212",
            "203.0.113.103",
            "224.134.13.24",
            "240.214.30.11",
            "255.255.255.255",
        ]
        not_reserved = ["hello.world", "::1", "45.34.29.15"]

        for subject in reserved:
            expected = True
            actual = Check(subject).is_reserved_ipv4()

            self.assertEqual(
                expected, actual, "{0} is not reserved.".format(repr(subject))
            )

        for subject in not_reserved:
            expected = False
            actual = Check(subject).is_reserved_ipv4()

            self.assertEqual(expected, actual, "{0} is reserved.".format(repr(subject)))


if __name__ == "__main__":
    launch_tests()
