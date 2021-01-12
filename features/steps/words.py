from behave import *

use_step_matcher("re")

@given("two words")
def step_impl(context):
    context.words = context.text.split(",")

@given("one word")
def step_impl(context):
    context.err = ValueError

@given("zero words")
def step_impl(context):
    context.err = ValueError

@when("they are the same")
def step_impl(context):
    context.return_value = True

@when("first includes second")
def step_impl(context):
    context.return_value = True

@when("they are different")
def step_impl(context):
    context.return_value = False

@when("second includes first")
def step_impl(context):
    context.return_value = False

@then("returns True")
def step_impl(context):
    test = context.words[0] == context.words[1] or context.words[1] in context.words[0]
    assert context.return_value == test

@then("returns False")
def step_impl(context):
    test = context.words[0] == context.words[1] or context.words[1] in context.words[0]
    assert context.return_value == test

@then("you have to type two words")
def step_impl(context):
    assert ValueError == context.err