import allure
from allure_commons.types import Severity

from qa_guru_diplom_tests.model.pages.web.general_page import general_page
from qa_guru_diplom_tests.model.pages.web.header import header


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.epic("UI")
@allure.feature('Search')
@allure.issue('https://jira.autotests.cloud/browse/HOMEWORK-1259')
@allure.title('Выполнить поиск по контенту')
@allure.id("32845")
def test_search_by_content(setup_browser):
    general_page.open()
    header.click_search_button()
    header.type_content_to_search('Оппенгеймер')
    header.should_search_content('Оппенгеймер')
