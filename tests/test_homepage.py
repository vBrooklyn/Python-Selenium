import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        for indx in range(12):
            homepage_nav.get_nav_links()[indx].click()


