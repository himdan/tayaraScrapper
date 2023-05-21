from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import re


def main(driver):
    driver.maximize_window()
    driver.get("https://www.tayara.tn/search/?category=Immobilier")
    _X_PATH = '//*[@id="__next"]'
    _CSS_SELECTOR = 'article.mx-auto'
    _COUNT_CSS_SELECTOR = '#__next > div.flex.flex-col.xl:flex-row.h-fit.w-full.mt-36.lg:mt-20 > main > div.mt-3.mx-2.lg:ml-0.lg:mr-4.lg:mt-12.relative.z-10 > div.flex.flex-col.gap-3.lg:flex-row > div.flex.lg:flex-row.flex-col.items-center.gap-2 > data'
    _COUNT_X_PATH = '//*[@id="__next"]/div[3]/main/div[2]/div[2]/div[1]/data'
    time.sleep(10)
    element = driver.find_element(By.XPATH, _X_PATH)
    element.click()
    _counter_element = driver.find_element(By.XPATH, _COUNT_X_PATH)
    _full_text = _counter_element.text
    print(_full_text)
    _regex = r'\d+'
    _match = re.search(_regex, _full_text)
    _adverts_count = int(_match.group()) if _match else False
    print(_adverts_count)
    while _adverts_count:
        time.sleep(3)
        _targets = driver.find_elements(By.CSS_SELECTOR, _CSS_SELECTOR)
        _current_length = len(_targets)
        print(f'current queue length {_current_length}')
        _target = _targets[-1]
        _batch = _targets[-30:]
        for _x_element in _batch:
            print('---------------------')
            print(_x_element.text)
        if _current_length == _adverts_count:
            break
        scroll_origin = ScrollOrigin.from_element(_target)
        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 400) \
            .perform()


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    options.add_argument('--disable-notifications')
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )
    try:
        main(driver)
        print('-------------------')
    except TimeoutException as e:
        pass
    except ElementNotVisibleException:
        pass
    except NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print('CTRL+C PRESSED')
    finally:
        driver.quit()
