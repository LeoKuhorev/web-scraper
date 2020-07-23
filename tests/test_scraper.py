import pytest

from web_scraper.scraper import (get_citations_needed_count,
                                 get_citations_needed_report)


class TestScraper:
    report_1 = """Citation needed for Uładzimier Niaklajeŭ was a member of the Union of Creative and Scientific Youth under the Central Committee of Belarus Komsomol and a member of Belarusian Theatrical Association. 
Citation needed for According to Niaklajeŭ’s words, after having been appointed to the position of the chairman of the Association of Writers, he had to deal with the president of Belarus Alaksandar Łukašenka who treated Niaklajeŭ as "the boss over the writers". At the same time an agreement creating Belarus and Russia Union State was signed, which was not approved by the writers of Belarus, protesting against this decision in public. It was the beginning of the conflict between Łukašenka and Niaklajeŭ and as a result, Uładzimier Niaklajeŭ had to leave the country. 
Citation needed for According to Niaklajeŭ’s words, after having been appointed to the position of the chairman of the Association of Writers, he had to deal with the president of Belarus Alaksandar Łukašenka who treated Niaklajeŭ as "the boss over the writers". At the same time an agreement creating Belarus and Russia Union State was signed, which was not approved by the writers of Belarus, protesting against this decision in public. It was the beginning of the conflict between Łukašenka and Niaklajeŭ and as a result, Uładzimier Niaklajeŭ had to leave the country. 
Citation needed for In 2005, V. Niaklajeŭ was elected as the head of Belarusian PEN Center, and on 10 April, he voluntarily left that position. Andrej Chadanvič became the next head of the Center. 
"""

    report_2 = """Citation needed for Confusion over the state of Washington and the city of Washington, D.C., led to renaming proposals during the statehood process for Washington in 1889, including David Dudley Field II's suggestion to name the new state "Tacoma". These proposals failed to garner support.[10] Washington, D.C.'s, own statehood movement in the 21st century includes a proposal to use the name "State of Washington, Douglass Commonwealth", which would conflict with the current state of Washington.[11] Residents of Washington (known as "Washingtonians") and the Pacific Northwest simply refer to the state as "Washington", and the nation's capital "Washington, D.C.", "the other Washington",[12] or simply "D.C." 
Citation needed for Washington state has the 18th highest per capita effective tax rate in the United States, as of 2017. Their tax policy differs from neighboring Oregon's, which levies no sales tax, but does levy a personal income tax. This leads to border economic anomalies in the Portland-Vancouver metropolitan area.[112] Additional border economies exist with neighboring British Columbia and Idaho. 
Citation needed for Washington state has the 18th highest per capita effective tax rate in the United States, as of 2017. Their tax policy differs from neighboring Oregon's, which levies no sales tax, but does levy a personal income tax. This leads to border economic anomalies in the Portland-Vancouver metropolitan area.[112] Additional border economies exist with neighboring British Columbia and Idaho. 
Citation needed for There are extensive waterways around Washington's largest cities, including Seattle, Bellevue, Tacoma and Olympia. The state highways incorporate an extensive network of bridges and the largest ferry system in the United States to serve transportation needs in the Puget Sound area. Washington's marine highway constitutes a fleet of twenty-eight ferries that navigate Puget Sound and its inland waterways to 20 different ports of call, completing close to 147,000 sailings each year. Washington is home to four of the five longest floating bridges in the world: the Evergreen Point Floating Bridge, Lacey V. Murrow Memorial Bridge and Homer M. Hadley Memorial Bridge over Lake Washington, and the Hood Canal Bridge which connects the Olympic Peninsula and Kitsap Peninsula. Among its most famous bridges is the Tacoma Narrows Bridge, which collapsed in 1940 and was rebuilt. Washington has a number of seaports on the Pacific Ocean, including Seattle, Tacoma, Kalama, Anacortes, Vancouver, Longview, Grays Harbor, Olympia, and Port Angeles. 
Citation needed for The Cascade Mountain Range also impedes transportation. Washington operates and maintains roads over seven[vague] major mountain passes and eight minor passes. During winter months some of these passes are plowed, sanded, and kept safe with avalanche control. Not all stay open through the winter. The North Cascades Highway, State Route 20, closes every year due to snowfall and avalanches in the area of Washington Pass. The Cayuse and Chinook passes east of Mount Rainier also close in winter. 
Citation needed for Washington is crossed by a number of freight railroads, and Amtrak's passenger Cascade route between Eugene, Oregon and Vancouver, BC is the eighth busiest Amtrak service in the U.S. Seattle's King Street Station, the busiest station in Washington, and 15th busiest in the U.S.,[125] serves as the terminus for the two long distance Amtrak routes in Washington, the Empire Builder to Chicago and the Coast Starlight to Los Angeles. The Sounder commuter rail service operates in Seattle and its surrounding cities, between Everett and Lakewood. The intercity network includes the Cascade Tunnel, the longest railroad tunnel in the United States, which is part of the Stevens Pass route on the BNSF Northern Transcom. 
Citation needed for Sound Transit Link light rail currently operates in the Seattle area at a length of 20 miles (32 km), and in Tacoma at a length of 1.6 miles (2.6 km). The entire system has a funded expansion plan that will expand light rail to a total of 116 miles by 2041. Seattle also has a 3.8-mile (6.1 km) streetcar network with two lines and plans to expand further by 2025. Bus systems exist across the state, the busiest being King County Metro, located in Seattle and King County, with just above 122 million riders in 2017.[126] Residents of Vancouver have resisted proposals to extend Portland's mass transit system into Washington. 
"""

    test_count = (
        ('https://en.wikipedia.org/wiki/Uladzimir_Nyaklyayew', 4),
        ('https://en.wikipedia.org/wiki/Washington_(state)', 7)
    )

    test_report = (
        ('https://en.wikipedia.org/wiki/Uladzimir_Nyaklyayew', report_1),
        ('https://en.wikipedia.org/wiki/Washington_(state)', report_2),
    )

    def test_proof_of_life(self):
        assert get_citations_needed_count
        assert get_citations_needed_report

    @pytest.mark.parametrize('url, _count', test_count)
    def test_citations_count(self, url, _count):
        """Test if the function returns correct number of citations
        """
        assert get_citations_needed_count(url) == _count

    @pytest.mark.parametrize('url, report', test_report)
    def test_citations_report(self, url, report):
        """Test if the function returns correct citation report
        """
        assert get_citations_needed_report(url) == report
