
from playwright.sync_api import sync_playwright

def test_drag_slider_to_95():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.lambdatest.com/selenium-playground")
        
        # Click the "Drag & Drop Sliders" link
        page.click("text=Drag & Drop Sliders")
        
        # Select the slider "Default value 15"
        slider_locator = page.locator("input.range-slider__range").nth(0)
        
        # Drag the slider to 95
        slider_locator.drag_to(slider_locator, source_position={"x":0, "y":0}, target_position={"x":460, "y":0})
        
        # Validate if the range shows 95
        range_value = page.input_value("#rangeSuccess")
        assert range_value == "95", f"Expected range value to be 95, but got {range_value}"
        
        browser.close()

test_drag_slider_to_95()
