from behave import *
from src.user import User

use_step_matcher("re")

u = User()

@given("password parameter equal to abc")
def step_impl(context):
    context.password = context.text
@when("checks if abc is valid")
def setp_impl(context):
    context.boo = False
@then("password abc should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to Abc")
def step_impl(context):
    context.password = context.text
@when("checks if Abc is valid")
def setp_impl(context):
    context.boo = False
@then("password Abc should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to Abc1")
def step_impl(context):
    context.password = context.text
@when("checks if Abc1 is valid")
def setp_impl(context):
    context.boo = False
@then("password Abc1 should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given(u"password parameter equal to Abc1&")
def step_impl(context):
    context.password = context.text
@when("checks if Abc1& is valid")
def setp_impl(context):
    context.boo = False
@then("password Abc1& should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to Abc&")
def step_impl(context):
    context.password = context.text
@when("checks if Abc& is valid")
def setp_impl(context):
    context.boo = False
@then("password Abc& should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to Abcdebfiewbfi1")
def step_impl(context):
    context.password = context.text
@when("checks if Abcdebfiewbfi1 is valid")
def setp_impl(context):
    context.boo = False
@then("password Abcdebfiewbfi1 should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to njenvjewovoew&")
def step_impl(context):
    context.password = context.text
@when("checks if njenvjewovoew& is valid")
def setp_impl(context):
    context.boo = False
@then("password njenvjewovoew& should not be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)

@given("password parameter equal to Abcvewjvewvwevev&1")
def step_impl(context):
    context.password = context.text
@when("checks if Abcvewjvewvwevev&1 is valid")
def setp_impl(context):
    context.boo = True
@then("password Abcvewjvewvwevev&1 should be valid")
def step_impl(context):
    assert context.boo == u.valid_password(context.password)