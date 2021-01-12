from behave import *
from src.roman import roman

# 4 13 29 233 959 1527 999

use_step_matcher("re")

#

@given("decimal number equal to 1")
def step_impl(context):
    context.num = 1

@when("roman symbol I is taken from set")
def step_impl(context):
    context.roman = "I"

@then("roman number should be I")
def step_impl(context):
    assert context.roman == roman(context.num)

#

@given("decimal number equal to 4")
def step_impl(context):
    context.num = 4

@when("roman symbols I and V are taken from set")
def step_impl(context):
    context.roman = "IV"

@then("roman number should be IV")
def step_impl(context):
    assert context.roman == roman(context.num)

#

@given("decimal number equal to 29")
def step_impl(context):
    context.num = 29

@when("roman symbols three X and I are taken from set")
def step_impl(context):
    context.roman = "XXIX"

@then("roman number should be XXIX")
def step_impl(context):
    assert context.roman == roman(context.num)

#

@given("decimal number equal to 233")
def step_impl(context):
    context.num = 233

@when("roman symbols two C three X and three I are taken from set")
def step_impl(context):
    context.roman = "CCXXXIII"

@then("roman number should be CCXXXIII")
def step_impl(context):
    assert context.roman == roman(context.num)

#

@given("decimal number equal to 959")
def step_impl(context):
    context.num = 959

@when("roman symbols C, M, L, I and X are taken from set")
def step_impl(context):
    context.roman = "CMLIX"

@then("roman number should be CMLIX")
def step_impl(context):
    assert context.roman == roman(context.num)

#


@given("decimal number equal to 1527")
def step_impl(context):
    context.num = 1527

@when("roman symbols M, D, two X, V and two I are taken from set")
def step_impl(context):
    context.roman = "MDXXVII"

@then("roman number should be MDXXVII")
def step_impl(context):
    assert context.roman == roman(context.num)

#

@given("decimal number equal to 999")
def step_impl(context):
    context.num = 999

@when("roman symbols two C, M, two X and I are taken from set")
def step_impl(context):
    context.roman = "CMXCIX"

@then("roman number should be CMXCIX")
def step_impl(context):
    assert context.roman == roman(context.num)

#
