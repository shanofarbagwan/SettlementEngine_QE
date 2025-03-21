# features/steps/data_quality_steps.py
from behave import given, when, then
from features.pages.data_quality_page import DataQualityPage

@given('the user navigates to the Data Quality Assignment page')
def step_impl(context):
    context.dq_page = DataQualityPage(context.page.driver)
    context.dq_page.navigate_to_data_quality_assignment_page()

@then('the Data Quality Assignment header should be displayed')
def step_impl(context):
    assert context.dq_page.is_data_quality_header_displayed(), "Data Quality Assignment header not displayed"

@then('the Data Quality form should be visible')
def step_impl(context):
    assert context.dq_page.is_data_quality_form_displayed(), "Data Quality form not displayed"

@then('the Applied Data Quality table should contain data')
def step_impl(context):
    assert context.dq_page.is_applied_data_quality_table_displayed(), "Applied Data Quality table not displayed"

@when('the user fills in the Data Quality Assignment form')
def step_impl(context):
    context.dq_page.fill_data_quality_form("Tallyman", "Transaction Amt.", "Comparison", "01/01/2024", "01/02/2024")

@when('the user leaves required fields empty')
def step_impl(context):
    context.dq_page.fill_data_quality_form("", "", "", "", "")

@when('clicks the Save button')
def step_impl(context):
    context.dq_page.click_save()

@then('the new Data Quality Assignment should be added successfully')
def step_impl(context):
    assert context.dq_page.is_applied_data_quality_table_displayed(), "New Data Quality Assignment not added"

@then('an error message should be displayed')
def step_impl(context):
    assert context.dq_page.is_error_message_displayed(), "Error message not displayed"

@then('the Download button should be visible')
def step_impl(context):
    assert context.dq_page.is_download_button_visible(), "Download button not visible"
